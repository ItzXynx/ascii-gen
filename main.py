#!/usr/bin/env python3
"""ASCII Art Generator - Convert text to ASCII art using figlet-style rendering."""
import sys

BANNER = {
    'A':'  /\\  \n /  \\ \n/----\\\n/    \\','B':'|--\\ \n|--/ \n|  \\ \n|--/ ','C':' ---\n/   \n\\   \n ---',
    'D':'|--\\ \n|  |\n|  |\n|--/','E':'|---\n|-- \n|   \n|---','F':'|---\n|-- \n|   \n|   ',
    'G':' ---\n/   \n/ --\n \\--','H':'|  |\n|--|\n|  |\n|  |','I':'---\n | \n | \n---',
    'L':'|   \n|   \n|   \n|---','O':' -- \n/  \\\n\\  /\n -- ','R':'|-- \n|--/\n|  \\\n|   ',
    'S':' --\n/  \n --\n  /\n-- ','T':'---\n | \n | \n | ','Y':'\\  /\n -- \n | \n | ',
}

def render(text):
    lines = ["", "", "", ""]
    for char in text.upper():
        art = BANNER.get(char, ["   "]*4)
        rows = art.split("\n") if "\n" in art else [art]*4
        for i in range(min(4, len(rows))):
            lines[i] += rows[i].ljust(6)
    return "\n".join(lines)

def main():
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "HELLO"
    print(f"\n{render(text)}\n")

if __name__ == "__main__": main()
