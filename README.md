# Bookbot

Bookbot is a CLI tool written in Python designed to analyze text documents. This tool can provide a report of the total number of words, the most and least used characters, and the frequency of each character in the document.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Overview](#code-overview)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/CN-M/bookbot.git
   cd bookbot
   ```

2. Ensure you have Python installed. Bookbot is compatible with Python 3.x.

## Usage

1. Place the text document you want to analyze in the `text` directory. The default file is `frankenstein.txt`.

2. Run the main script:
   ```sh
   python3 main.py
   ```

3. Bookbot will generate a report in the console with the following information:
   - Total number of words in the document.
   - The most used character and its frequency.
   - The least used character and its frequency.
   - The frequency of each character.

## Project Structure

```
.
├── README.md
├── text
│   └── frankenstein.txt
└── main.py
```

- `README.md`: Project documentation.
- `text`: Directory to store text files for analysis.
- `main.py`: Main script to run the Bookbot CLI tool.

## Code Overview

- `main()`: The entry point of the script. It calls other functions to read the text, analyze it, and print the report.
- `print_report()`: Prints the analysis report.
- `get_book_text()`: Reads and returns the text from the specified file.
- `get_num_words()`: Returns the total number of words in the text.
- `get_string_count()`: Returns a dictionary with the frequency of each character in the text.
- `least_used_char()`: Returns the least used character and its frequency.
- `most_used_char()`: Returns the most used character and its frequency.
