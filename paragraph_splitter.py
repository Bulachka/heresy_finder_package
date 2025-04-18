import re
import sys


def is_new_paragraph(line):
    line = line.strip()
    roman_match = re.match(r'^[IVXLCDM]+\.', line)
    nr_match = re.match(r'^Nr\.\s*\d+', line)
    return bool(roman_match or nr_match)

def process_text(text):
    lines = text.split('\n')
    paragraphs = []
    buffer = ''
    in_paragraph = False

    for line in lines:
        stripped = line.strip()
        if is_new_paragraph(stripped):
            if buffer:
                paragraphs.append(buffer.strip())
            buffer = stripped
            in_paragraph = True
        elif in_paragraph:
            if stripped == '':
                continue
            buffer += ' ' + stripped
        else:
            paragraphs.append(stripped)

    if buffer:
        paragraphs.append(buffer.strip())

    return '\n\n'.join(paragraphs)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python paragraph_splitter.py input_file.txt output_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    processed = process_text(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed)

    print(f"✅ Done! Processed file saved to {output_file}")
