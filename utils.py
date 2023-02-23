import pathlib

from typing import List, Tuple
from PyPDF2 import PdfReader
from pdf import AbstractPDF, GenericPDF, ArxivPDF


def is_pdf_info_complete(title, year) -> bool:
    """
    Check if the title and year information is present.
    :param title: Title of the publication
    :param year: Year of the publication
    :return: Boolean check
    """
    if title and year:
        return True


def file_list(file_path: pathlib.Path) -> Tuple[pathlib.Path, List[str]]:
    """
    Obtain the file(s) to be renamed with the directory.
    :param file_path: directory or file of pdf to be renamed
    :return: directory and list of pdf file names
    """
    if file_path.is_file():
        file_dir = file_path.parent
        file_names = [file_path.name]
    else:
        file_dir = file_path
        file_names = list(x for x in file_path.iterdir() if x.is_file())

    return file_dir, file_names


def get_pdf_info(pdf_file_path: pathlib.Path) -> AbstractPDF:
    """
    Get the year and title of the PDF file
    :param pdf_file_path: path to PDF file
    :return: PDF information
    """
    reader = PdfReader(pdf_file_path)

    title = reader.metadata.title
    year = reader.metadata.creation_date.year

    # check if information is complete
    if is_pdf_info_complete(title, year):
        pdf_info = GenericPDF(title=title, year=year)
        return pdf_info

    # check for arxiv information
    pdf_first_page_text = reader.pages[0].extract_text()
    check_arxiv_index = pdf_first_page_text.find("arXiv")
    if check_arxiv_index != -1:
        arxiv_info = pdf_first_page_text[check_arxiv_index:].split(" ")
        arxiv_id = arxiv_info[0][6:]
        pub_date = arxiv_info[-1]
        pdf_info = ArxivPDF(year=pub_date, arxiv_id=arxiv_id)
        return pdf_info
