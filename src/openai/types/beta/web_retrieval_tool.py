# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebRetrievalTool"]


class WebRetrievalTool(BaseModel):
    type: Literal["web_retrieval"]
    """The type of tool being defined: `web_retrieval`"""
