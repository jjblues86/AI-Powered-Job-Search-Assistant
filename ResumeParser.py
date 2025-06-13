import spacy
import json
from PyPDF2 import PdfReader
import docx

class ResumeParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def parse_resume(self, resume_text):
        # TO DO: Implement resume parsing logic
        pass

    def parse_pdf_resume(self, file_path):
        # TO DO: Implement PDF resume parsing logic
        pass

    def parse_docx_resume(self, file_path):
        # TO DO: Implement DOCX resume parsing logic
        pass