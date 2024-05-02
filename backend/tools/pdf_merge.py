import os
from typing import List, Optional
import fitz  # PyMuPDF
import glob

class PDFMerger:
    def __init__(self, save_dir: Optional[str] = None, input_dir: Optional[str] = None):
        """
        Initializes the PDFMerger with optional directories for saving and input.
        :param save_dir: Directory where merged PDFs will be saved.
        :param input_dir: Directory from where PDFs will be read.
        """
        self.save_dir = save_dir
        self.input_dir = input_dir

    def merge(self, input_files: List[str], output_file_path: str):
        """
        Merges multiple PDF files into a single PDF file.
        :param input_files: List of paths to PDF files to merge.
        :param output_file_path: The output file path for the merged PDF.
        """
        output_file_path = self._ensure_pdf_extension(output_file_path)
        if not os.path.isabs(output_file_path) and self.save_dir:
            output_file_path = os.path.join(self.save_dir, output_file_path)

        doc = fitz.open()
        for filename in input_files:
            full_path = self._resolve_input_path(filename)
            doc.insert_pdf(fitz.open(full_path))
        doc.save(output_file_path)
        print(f"Merged file saved at path {output_file_path}")
        doc.close()

    def merge_specific_files_from_folder(self, input_file_names: List[str], output_file_path: str):
        if not self.input_dir:
            raise ValueError("Input directory not set.")
        
        input_files = [os.path.join(self.input_dir, f"{name}.pdf") for name in input_file_names]
        
        # Check if files exist before merging
        for file_path in input_files:
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

        self.merge(input_files, output_file_path)

    def merge_from_folder(self, output_file_path: str):
        """
        Merges all PDF files from the self.input_dir into a single PDF file.
        """
        if not self.input_dir:
            raise ValueError("Input directory not set.")
        pdf_files = glob.glob(f"{self.input_dir}/*.pdf")
        self.merge(pdf_files, output_file_path)

    def _resolve_input_path(self, filename: str) -> str:
        """
        Resolves the full path of a file using self.input_dir if the file path is not absolute.
        """
        if os.path.isabs(filename):
            return filename
        elif self.input_dir:
            return os.path.join(self.input_dir, filename)
        else:
            raise ValueError("Input directory not set and filename is not an absolute path.")

    def _ensure_pdf_extension(self, filename: str) -> str:
        """
        Ensures the filename ends with '.pdf'. Adds the extension if missing.
        """
        if not filename.lower().endswith('.pdf'):
            filename += '.pdf'
        return filename