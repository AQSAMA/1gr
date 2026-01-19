function HorizontalRule(elem)
  if FORMAT:match 'docx' then
    return pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
  else
    return elem
  end
end
