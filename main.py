import os
import pathlib
import argparse

from utils import get_pdf_info, file_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename publication pdfs")
    parser.add_argument("-f", "--file", type=pathlib.Path)
    args = parser.parse_args()

    file_path = args.file
    file_dir, file_names = file_list(file_path)

    for file_name in file_names:
        pdf_file = file_dir / file_name
        pdf_info = get_pdf_info(pdf_file)
        new_pdf_name = f"{pdf_info.title} ({pdf_info.year}).pdf"
        new_pdf_file = file_dir / new_pdf_name
        os.rename(pdf_file, new_pdf_file)
