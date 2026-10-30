"""Build the static site and its PDF from the Markdown source into _site/."""

import html
import re
import shutil
from pathlib import Path
from string import Template

import markdown
from weasyprint import HTML

ROOT = Path(__file__).parent
SOURCE = ROOT / "The Python Architecture Why It Works So Elegantly.md"
ASSETS = ROOT / "site"
OUT = ROOT / "_site"
PDF_NAME = "the-python-architecture.pdf"


def split_front_matter(text):
    """Pull the title, byline and tagline off the top of the document."""
    match = re.match(r"# (.+)\n+(.+)\n+\*(.+)\*\n+", text)
    if not match:
        raise ValueError(f"{SOURCE.name} must start with a title, a byline and an *italic tagline*")
    title, byline, tagline = match.groups()
    return title, byline, tagline, text[match.end():]


def link_section_references(body, sections):
    """Turn every "Section N" in the prose into a link to that section."""
    anchors = {}
    for section in sections:
        number = re.match(r"\d+", section["name"])
        if number:
            anchors[number.group()] = section["id"]

    def link(match):
        anchor = anchors.get(match.group(1))
        return f'<a href="#{anchor}">{match.group(0)}</a>' if anchor else match.group(0)

    return re.sub(r"\bSection (\d+)\b", link, body)


def toc_items(sections):
    return "\n".join(
        f'<li><a href="#{section["id"]}">{section["name"]}</a></li>' for section in sections
    )


def build_pdf(title, byline, author, tagline, body, sections):
    # Permalinks are noise on paper, and would leak into the running page header.
    body = re.sub(r'<a class="headerlink".*?</a>', "", body)
    page = f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>{title}</title><meta name="author" content="{author}"></head>
<body>
<header class="cover">
  <h1>{title}</h1>
  <p class="tagline">{tagline}</p>
  <p class="byline">{byline}</p>
</header>
<nav class="toc"><h2 class="toc-title">Contents</h2><ol>{toc_items(sections)}</ol></nav>
{body}
</body>
</html>"""
    document = HTML(string=page, base_url=str(ASSETS)).render(
        stylesheets=[ASSETS / "code.css", ASSETS / "pdf.css"]
    )
    document.write_pdf(OUT / PDF_NAME)
    return len(document.pages)


def main():
    title, byline, tagline, source = split_front_matter(SOURCE.read_text(encoding="utf-8"))
    author = html.escape(byline.split("·")[-1].strip().lstrip("@"), quote=True)

    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite", "tables", "toc", "sane_lists", "smarty"],
        extension_configs={
            "codehilite": {"guess_lang": False, "css_class": "highlight"},
            "toc": {"permalink": True, "toc_depth": "2-3"},
        },
    )
    body = md.convert(source)
    # toc_depth 2-3 keeps h3 anchors and permalinks; the contents list shows h2 only.
    sections = md.toc_tokens
    body = link_section_references(body, sections)
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    pages = build_pdf(title, byline, author, tagline, body, sections)
    size_kb = round((OUT / PDF_NAME).stat().st_size / 1024)

    page = Template((ASSETS / "template.html").read_text(encoding="utf-8")).substitute(
        title=title,
        byline=byline,
        author=author,
        tagline=tagline,
        toc=toc_items(sections),
        body=body,
        pdf=PDF_NAME,
        pdf_info=f"{pages} pages, {size_kb} KB",
    )
    (OUT / "index.html").write_text(page, encoding="utf-8")
    for name in ("style.css", "code.css"):
        shutil.copy(ASSETS / name, OUT / name)

    print(f"Built {OUT}/index.html and {PDF_NAME} ({pages} pages, {size_kb} KB)")


if __name__ == "__main__":
    main()
