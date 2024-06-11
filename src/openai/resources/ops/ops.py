from openai._compat import cached_property
from openai._resource import SyncAPIResource

from .web_retireval import WebRetrieval

__all__ = ["Ops"]


class Ops(SyncAPIResource):
    @cached_property
    def web_retrieval(self) -> WebRetrieval:
        return WebRetrieval(self._client)
