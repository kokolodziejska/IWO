import re
import zlib
import markdown2
import weasyprint

BASE_URL = "https://www.plantuml.com/plantuml/png/"

CSS_STRING = """
@page {
    size: A4;    /* or Letter, etc. */
    margin: 1in; /* adjust margins as needed */
}
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto; /* optional: center the image */
}
"""

def plantuml_encode(data):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    encoded = ""
    value = 0
    bits = 0
    for byte in data:
        value = (value << 8) | byte
        bits += 8
        while bits >= 6:
            bits -= 6
            encoded += alphabet[(value >> bits) & 0x3F]
    if bits > 0:
        encoded += alphabet[(value << (6 - bits)) & 0x3F]
    return encoded

def generate_plantuml_url(plantuml_text):
    text_bytes = plantuml_text.encode('utf-8')
    compressed = zlib.compress(text_bytes)[2:-4]
    encoded = plantuml_encode(compressed)
    return BASE_URL + encoded

def replace_uml_blocks(markdown_content):
    pattern = r"```(?:puml|plantuml)\n(.*?)```"  # Capture code in group(1)
    
    def repl(match):
        puml_code = match.group(1).strip()
        url = generate_plantuml_url(puml_code)
        return f"![PlantUML Diagram]({url})"
    
    return re.sub(pattern, repl, markdown_content, flags=re.DOTALL)

def markdown_to_pdf(md_content, output_pdf):
    html_content = markdown2.markdown(md_content)
    css = weasyprint.CSS(string=CSS_STRING)
    weasyprint.HTML(string=html_content).write_pdf(output_pdf, stylesheets=[css])

def process_markdown_to_pdf(input_md_file, output_pdf_file):
    with open(input_md_file, 'r', encoding='utf-8') as f:
        original_md = f.read()
    replaced_md = replace_uml_blocks(original_md)
    markdown_to_pdf(replaced_md, output_pdf_file)
    print(f"PDF generated successfully: {output_pdf_file}")

if __name__ == "__main__":
    input_md = "dokumentacja.md"
    output_pdf = "dokumentacja.pdf"

    process_markdown_to_pdf(input_md, output_pdf)
