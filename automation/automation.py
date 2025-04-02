import re
import zlib
import base64
import requests

from markdown_pdf import MarkdownPdf, Section

BASE_URL = "https://www.plantuml.com/plantuml/png/"

CSS_STRING = """
body { 
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif; 
    color: #2d333b; 
    line-height: 1.5; 
    margin: 0 auto; 
    padding: 20px;
}
h1, h2, h3 { 
    font-weight: bold; 
    color: #333; 
}
code, pre {
    background-color: #f5f5f5;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 3px;
    padding: 3px;
}
a { 
    text-decoration: none;
    color: #0366d6; 
}
img {
    max-width: 100%;
    display: block;
    margin: 0 auto;
}
@page {
    size: A4;
    margin: 1in;
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
    text_bytes = plantuml_text.encode("utf-8")
    # Use raw deflate (wbits=-15) to produce the correct output without zlib header and checksum
    compressor = zlib.compressobj(level=9, wbits=-15)
    compressed = compressor.compress(text_bytes) + compressor.flush()
    encoded = plantuml_encode(compressed)
    return BASE_URL + encoded

def replace_uml_blocks(markdown_content):
    pattern = r"```(?:puml|plantuml)\n(.*?)```"

    def repl(match):
        puml_code = match.group(1).strip()
        url = generate_plantuml_url(puml_code)
        # Download the image from the PlantUML server
        response = requests.get(url)
        if response.status_code == 200:
            image_base64 = base64.b64encode(response.content).decode('utf-8')
            # Embed the image as a data URI
            return f"![PlantUML Diagram](data:image/png;base64,{image_base64})"
        else:
            # Fallback to the URL if the download fails
            return f"![PlantUML Diagram]({url})"

    return re.sub(pattern, repl, markdown_content, flags=re.DOTALL)

def process_markdown_to_pdf(input_md_file, output_pdf_file):
    with open(input_md_file, "r", encoding="utf-8") as f:
        original_md = f.read()
    replaced_md = replace_uml_blocks(original_md)

    pdf = MarkdownPdf(toc_level=2)  # Adjust css parameter if needed
    pdf.add_section(Section(replaced_md))
    pdf.save(output_pdf_file)
    print(f"PDF generated successfully: {output_pdf_file}")

if __name__ == "__main__":
    input_md = "dokumentacja.md"
    output_pdf = "dokumentacja.pdf"
    process_markdown_to_pdf(input_md, output_pdf)

