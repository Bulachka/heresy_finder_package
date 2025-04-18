import os
import subprocess

# 📁 Change this if your source .txt files are located elsewhere
input_folder = "input_txt"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

# Script file names (must be in the same directory as this script)
splitter_script = "paragraph_splitter.py"
heresy_finder_script = "find_heresy_in_paragraphs.py"
highlighter_script = "highlight_heresy.py"

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        base_name = os.path.splitext(filename)[0]

        print(f"\n🔁 Processing file: {filename}")

        paragraphs_file = os.path.join(output_folder, f"{base_name}_paragraphs.txt")
        heresy_file = os.path.join(output_folder, f"{base_name}_heresy.docx")
        highlighted_file = os.path.join(output_folder, f"{base_name}_highlighted.docx")

        # Step 1: Split paragraphs
        print("→ Step 1: Splitting paragraphs")
        subprocess.run([
            "python", splitter_script,
            os.path.join(input_folder, filename),
            paragraphs_file
        ])

        # Step 2: Find heresy
        print("→ Step 2: Finding heresy")
        subprocess.run([
            "python", heresy_finder_script,
            paragraphs_file,
            heresy_file
        ])

        # Step 3: Highlight heresy
        print("→ Step 3: Highlighting heresy")
        subprocess.run([
            "python", highlighter_script,
            heresy_file,
            highlighted_file
        ])

print("\n✅ Batch processing complete.")
