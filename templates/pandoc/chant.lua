-- Pandoc Lua filter for the typst (PDF) build: turns the classed divs that
-- scripts/assemble.py writes into calls of the typst functions in
-- templates/typst/book.typ (docs/book-build.md).
--
-- Pandoc's own typst output drops the div classes, wraps each table in a
-- centred figure, and prints the backticked words and tags as monospace raw
-- text. The passes below run in order.

local function raw(s) return pandoc.RawBlock("typst", s) end
local function rawi(s) return pandoc.RawInline("typst", s) end

-- A typst string literal.
local function tstr(s)
  return '"' .. s:gsub('\\', '\\\\'):gsub('"', '\\"') .. '"'
end

local function has_class(el, cls)
  return el.classes and el.classes:includes(cls)
end

-- Div class → typst function.
local FUNC = {
  unit = "unit",
  ["unit-head"] = "unit-head",
  pali = "pali",
  literal = "literal",
  faithful = "faithful",
  ["repeat"] = "repeat-note",
  citation = "citation",
  rubric = "rubric",
  instruction = "instruction",
  variant = "variant",
  gloss = "gloss",
  subtitle = "en-title",
  figure = "figure-block",
  keep = "keep-block",
  resources = "resources",
}

-- Pass 1: inlines.
local inlines = {
  -- `(masc nom sg)` is a tag group; any other backticked text is a word,
  -- which keeps the formatting around it (bold in the word cells).
  Code = function(el)
    if el.text:sub(1, 1) == "(" then
      return { rawi("#tags["), pandoc.Str(el.text), rawi("]") }
    end
    return pandoc.Str(el.text)
  end,

  -- Typst resolves image paths against its --root (the repo root); a leading
  -- "/" makes them absolute there. The assembled Markdown keeps them
  -- relative to the repo root for the EPUB build.
  Image = function(el)
    local src = el.src
    if src:match("^/") or src:match("^%a[%w+.-]*:") then return el end
    el.src = "/" .. src
    return el
  end,

  -- The English title in a chant title: shown in the contents only.
  Header = function(el)
    local out = pandoc.Inlines{}
    for _, il in ipairs(el.content) do
      if il.t == "Span" and has_class(il, "toc-en") then
        if #out > 0 and out[#out].t == "Space" then out:remove(#out) end
        out:insert(rawi("#toc-en["))
        out:extend(il.content)
        out:insert(rawi("]"))
      else
        out:insert(il)
      end
    end
    el.content = out
    return el
  end,
}

-- Pass 2: in a unit, the blocks before the first table form the unit head,
-- which typst keeps on the same page as the start of the table.
local units = {
  Div = function(el)
    if not has_class(el, "unit") then return nil end
    local first_table
    for i, b in ipairs(el.content) do
      if b.t == "Table" then first_table = i; break end
    end
    if not first_table or first_table == 1 then return nil end
    local head = pandoc.Blocks{}
    for i = 1, first_table - 1 do head:insert(el.content[i]) end
    local rest = pandoc.Blocks{ pandoc.Div(head, pandoc.Attr("", { "unit-head" })) }
    for i = first_table, #el.content do rest:insert(el.content[i]) end
    el.content = rest
    return el
  end,
}

-- Typst markup for a table cell.
local function cell_markup(cell)
  local s = pandoc.write(pandoc.Pandoc(cell.contents), "typst")
  return "[" .. s:gsub("%s+$", "") .. "]"
end

-- Pass 3: tables and divs (bottom-up, so inner divs are done first).
local blocks = {
  Table = function(tbl)
    local header = {}
    for _, row in ipairs(tbl.head.rows) do
      for _, cell in ipairs(row.cells) do table.insert(header, cell_markup(cell)) end
    end
    local rows = {}
    for _, body in ipairs(tbl.bodies) do
      for _, row in ipairs(body.body) do
        local word, analysis = row.cells[1], row.cells[2]
        local member = pandoc.utils.stringify(word.contents):sub(1, 3) == "↳"
        table.insert(rows, "(" .. cell_markup(word) .. ", "
          .. (analysis and cell_markup(analysis) or "[]") .. ", "
          .. tostring(member) .. "),")
      end
    end
    return raw("#word-table(\n  header: (" .. table.concat(header, ", ") .. ",),\n"
      .. "  rows: (\n    " .. table.concat(rows, "\n    ") .. "\n  ),\n)")
  end,

  Div = function(el)
    for _, cls in ipairs(el.classes) do
      local f = FUNC[cls]
      if f then
        local out = pandoc.Blocks{ raw("#" .. f .. "[") }
        out:extend(el.content)
        out:insert(raw("]"))
        return out
      end
    end
    return nil
  end,
}

-- Pass 4: the contents page goes after the About text, before the first
-- numbered level-1 heading; and the cover data reaches the template.
local document = {
  Pandoc = function(doc)
    for i, b in ipairs(doc.blocks) do
      if b.t == "Header" and b.level == 1 and not has_class(b, "unnumbered") then
        doc.blocks:insert(i, raw("#contents-page(depth: "
          .. PANDOC_WRITER_OPTIONS.toc_depth .. ")"))
        break
      end
    end
    local meta = doc.meta
    local id = pandoc.utils.stringify(meta["book-id"] or "")
    meta["cover-data-path"] = pandoc.MetaInlines{ rawi(tstr("/build/covers/" .. id .. ".json")) }
    if meta["cover-pdf"] then
      meta["cover-pdf"] = pandoc.MetaInlines{ rawi(tstr("/" .. pandoc.utils.stringify(meta["cover-pdf"]))) }
    end
    return doc
  end,
}

return { inlines, units, blocks, document }
