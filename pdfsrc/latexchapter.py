from .settings import *
from .styles import *
from .latexfile import *

from typing import List

# Month order mapping for sorting by month name in filenames
MONTH_ORDER = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

class LatexChapter:
    def __init__(self, config: Settings, basefile: str, style: Styles, chapterFilename: str) -> None:
        self.files: List[LatexFile] = []
        self.config: Settings = config
        self.chapter = ''
        self.style = style
        self.compiledfile = chapterFilename
        self.base = ''

        if basefile is not None:
            with open(basefile) as f:
                self.base = f.read()

    # Append a file
    def add_file(self, file: LatexFile):
        self.files.append(file)

    # Combine all code and make chapter file
    def compile(self):
        # Sort files by year, month, shift, then question
        def sort_key(file: LatexFile):
            # Split filename into parts based on expected structure
            parts = file.filename.split('/')
            year = int(parts[0])                    # Extract year as integer
            month = MONTH_ORDER.get(parts[1], 0)    # Convert month name to its order
            shift = parts[2]                        # Use shift as is for lexicographical sorting
            question = parts[3]                     # Use question name within shift
            return (year, month, shift, question)

        self.files.sort(key=sort_key)

        chapter_code = self.base

        if self.config.useSections:
            section_codes = {}
            for file in self.files:
                if file.section not in section_codes:
                    section_codes[file.section] = ''
                section_codes[file.section] += file.getFileRepr()
            for section_alias, section_code in section_codes.items():
                chapter_code += self.style.applySectionStyle(section_alias, section_code)
        else:
            for file in self.files:
                chapter_code += file.getFileRepr()
        
        with open(self.compiledfile, 'w') as f:
            f.write(self.style.applyChapterStyle(chapter_code))

