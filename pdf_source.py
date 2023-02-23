from dataclasses import dataclass
from typing import Optional
import arxiv


@dataclass
class AbstractSource:
    title: Optional[str] = None
    year: Optional[str] = None


@dataclass
class GenericSource(AbstractSource):
    pass


@dataclass
class ArxivSource(AbstractSource):
    """
    for papers obtained through arXiv
    """
    arxiv_id: Optional[str] = None

    def __post_init__(self):
        self.extract_info_from_arxiv()

    def extract_info_from_arxiv(self):
        search_result = next(arxiv.Search(id_list=[self.arxiv_id]).results())
        self.title = search_result.title
        self.year = search_result.published.year
