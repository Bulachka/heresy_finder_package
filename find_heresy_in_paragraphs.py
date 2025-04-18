import re
import sys
from docx import Document
from collections import defaultdict

# Raw regex patterns (with .* or \w+ preserved)
raw_patterns = [
    r"chetzer.*", r"kætzer.*", r"kätzer.*", r"keczer.*", r"keczir.*", r"keczzer.*",
    r"ketzcer.*", r"ketzcir.*", r"ketzeer.*", r"ketzer.*", r"khetzer.*", r"ketczer.*",
    r"haeres\w+", r"haeret.*", r"heret.*", r"heres\w+",
    r"huss.*"
]

# Compile patterns with word boundary at the start
compiled_patterns = [re.compile(r'\b' + pat, re.IGNORECASE) for pat in raw_patterns]
pattern_stats = defaultdict(int)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python find_heresy_in_paragraphs.py input.txt output.docx")
        sys.exit(1)

    input_file = sys.argv[1]
    output_docx = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    normalized_text = raw_text.replace("ſ", "s")
    paragraphs = normalized_text.split('\n\n')

    doc = Document()
    matches_found = 0

    for para in paragraphs:
        if any(p.search(para) for p in compiled_patterns):
            doc.add_paragraph(para.strip())
            matches_found += 1
            for pattern, raw in zip(compiled_patterns, raw_patterns):
                count = len(pattern.findall(para))
                pattern_stats[raw] += count

    doc.add_paragraph("\nMatch counts by pattern:")
    table = doc.add_table(rows=1, cols=2)
    table.rows[0].cells[0].text = 'Pattern'
    table.rows[0].cells[1].text = 'Count'

    for pattern in raw_patterns:
        row = table.add_row().cells
        row[0].text = pattern
        row[1].text = str(pattern_stats[pattern])

    doc.save(output_docx)
    print(f"✅ {matches_found} heretical paragraph(s) saved to {output_docx}")
