import pathlib
from PyPDF2 import PdfReader
from pdf_source import AbstractSource, GenericSource, ArxivSource


def extract_pdf_metadata(pdf_file_path: str):
    pdf_file = pathlib.Path(pdf_file_path)
    reader = PdfReader(pdf_file)
    pdf_info = get_pdf_source(reader)
    return pdf_info


def get_pdf_source(reader):
    pdf_title = reader.metadata.title
    pdf_year = reader.metadata.creation_date.year

    #TODO: change to is metadata valid function

    # check if information is complete
    if pdf_title and pdf_year:
        pdf_source = GenericSource(title=pdf_title, year=pdf_year)
        return pdf_source

    # check for arxiv information
    pdf_first_page_text = reader.pages[0].extract_text()
    check_arxiv_index = pdf_first_page_text.find('arXiv')
    if check_arxiv_index != -1:
        arxiv_info = pdf_first_page_text[check_arxiv_index:].split(' ')
        arxiv_id = arxiv_info[0][6:]
        pub_date = arxiv_info[-1]
        pdf_source = ArxivSource(year=pub_date, arxiv_id=arxiv_id)
        return pdf_source
