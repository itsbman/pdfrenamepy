import arxiv

from dataclasses import dataclass
from typing import Optional


@dataclass
class AbstractPDF:
    """
    Abstract PDF class
    """

    title: Optional[str] = None
    year: Optional[str] = None


@dataclass
class GenericPDF(AbstractPDF):
    """
    For publications with complete information
    """

    pass


@dataclass
class ArxivPDF(AbstractPDF):
    """
    Publications obtained through arXiv
    """

    arxiv_id: Optional[str] = None

    def __post_init__(self):
        self.extract_info_from_arxiv()

    def extract_info_from_arxiv(self) -> None:
        """
        Search for missing info by querying arxiv
        """
        search_result = next(arxiv.Search(id_list=[self.arxiv_id]).results())
        self.title = search_result.title
        self.year = search_result.published.year
