import re
import sys
from docx import Document
from collections import defaultdict
from patterns import raw_patterns


# Compile patterns with word boundary at the start
compiled_patterns = [re.compile(pat, re.IGNORECASE) for pat in raw_patterns]
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
    
    doc.save(output_docx)
    # print(f"✅ {matches_found} heretical paragraph(s) saved to {output_docx}")

    if matches_found:
        print(f"✅ {matches_found} heretical paragraph(s) saved to {output_docx}")
    else:
        print(f"⚠️ No heretical paragraphs found in {input_file}")

