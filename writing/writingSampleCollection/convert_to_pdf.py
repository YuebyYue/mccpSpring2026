#!/usr/bin/env python3
"""Convert revisedDraft.md to PDF with academic formatting:
   Font: Times New Roman 12pt, line spacing 1.5, margins 2.54cm
"""

import markdown
from weasyprint import HTML

MD_FILE = "revisedDraft.md"
PDF_FILE = "revisedDraft.pdf"

# Read markdown
with open(MD_FILE, "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert markdown to HTML
html_body = markdown.markdown(md_text, extensions=["extra", "smarty"])

# Full HTML with CSS for academic formatting
html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman');

  @page {{
    size: A4;
    margin: 2.54cm;
  }}

  body {{
    font-family: "Times New Roman", "Nimbus Roman No9 L", "Liberation Serif", Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #000;
    text-align: justify;
  }}

  h1 {{
    font-size: 16pt;
    font-weight: bold;
    text-align: center;
    margin-top: 0.5cm;
    margin-bottom: 0.5cm;
  }}

  h2 {{
    font-size: 14pt;
    font-weight: bold;
    margin-top: 0.8cm;
    margin-bottom: 0.3cm;
  }}

  h3 {{
    font-size: 12pt;
    font-weight: bold;
    margin-top: 0.5cm;
    margin-bottom: 0.2cm;
  }}

  p {{
    margin-top: 0.2cm;
    margin-bottom: 0.2cm;
    text-indent: 0;
  }}

  strong {{
    font-weight: bold;
  }}

  em {{
    font-style: italic;
  }}

  hr {{
    border: none;
    border-top: 1px solid #999;
    margin: 0.5cm 0;
  }}

  ul, ol {{
    margin-left: 1cm;
  }}

  li {{
    margin-bottom: 0.15cm;
  }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

# Generate PDF
HTML(string=html_doc).write_pdf(PDF_FILE)
print(f"PDF generated: {PDF_FILE}")
