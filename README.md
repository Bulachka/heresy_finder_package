# Heresy Finder Pipeline
This project processes historical text files to detect and highlight heretical terms using a multi-step Python pipeline.
## ⚠️ Preparation Step
Before running the scripts, make sure that your `.txt` files are **manually cleaned**. You should:
- Remove the **title page**
- Remove the **preface**
- Remove the **table of contents**
- Remove the **index**
Only the **main document content** should remain in the file.
## 💡 What It Does
### 1. Split Text into Paragraphs
- Detects section starts using Roman numerals (e.g., `I.`, `IV.`) or `"Nr."` + Arabic number (e.g., `Nr. 5`)
- Outputs clean paragraph-separated text (`*_paragraphs.txt`)
### 2. Detect Heresy
- Searches for pre-defined heretical terms using regex patterns
- Saves matching paragraphs to a DOCX file (`*_heresy.docx`)
- Automatically replaces old Latin long-s characters (`ſ`) with `s` for accurate matching
### 3. Highlight Heresy
- Highlights individual heretical words in **red**
- Adds a summary table at the end of the DOCX showing how many times each pattern matched
- Also normalizes `ſ` → `s` to ensure historical forms are matched
## 📁 Folder Structure
- 📂 input_txt/                        # Place your manually cleaned TXT files here
- 📂 output/                           # All generated outputs go here
- 📄 paragraph_splitter.py             # Step 1
- 📄 find_heresy_in_paragraphs.py      # Step 2
- 📄 highlight_heresy.py               # Step 3
- 📄 main.py                           # Runs all 3 steps for each file
- 📄 README.md
## 🚀 Run the Script
From the terminal:
```bash
python main.py
```
All processed and highlighted `.docx` files will be saved to the `output/` folder.
## 🧾 Heretical Patterns (Regex)
The following regular expressions are used to identify potentially heretical terms in the documents:
- `chetzer.*`
- `kætzer.*`
- `kätzer.*`
- `keczer.*`
- `keczir.*`
- `keczzer.*`
- `ketzcer.*`
- `ketzcir.*`
- `ketzeer.*`
- `ketzer.*`
- `khetzer.*`
- `ketczer.*`
- `keczczer.*`
- `haeres\w+`
- `haeret.*`
- `heret.*`
- `heres\w+`
- `hæret.*`
- `hæres\w+`
- `huss.*`
## ✅ Additional Features
- Handles historical Latin spelling by automatically converting `ſ` (long-s) to `s`
- Generates a match count table per pattern in the final document
- Fully compatible with large `.txt` files containing many paragraphs
## 💬 Questions?
If you're unsure about input formatting or need help customizing patterns, feel free to reach out or create an issue. Enjoy Heresy Inquisition!
