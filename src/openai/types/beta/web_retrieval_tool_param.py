# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebRetrievalToolParam"]


class WebRetrievalToolParam(TypedDict, total=False):
    type: Required[Literal["web_retrieval"]]
    """The type of tool being defined: `web_retrieval`"""
