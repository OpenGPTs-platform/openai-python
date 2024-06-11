from typing import List, Optional
from typing_extensions import TypedDict

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
)
from ..._models import BaseModel
from ..._resource import SyncAPIResource
from ..._base_client import (
    make_request_options,
)

__all__ = ["WebRetrieval"]


class WebRetrievalCreate(TypedDict):
    root_urls: List[str]
    constrain_to_root_domain: bool
    max_depth: int
    description: Optional[str]


class CrawlInfo(BaseModel):
    url: str
    error: Optional[str] = None
    content: str
    depth: int


class WebRetrievalResponse(BaseModel):
    message: str
    crawl_infos: List[CrawlInfo]


class DeleteResponse(BaseModel):
    message: str


class WebRetrieval(SyncAPIResource):
    def crawl_and_upsert(
        self,
        root_urls: List[str],
        max_depth: int,
        constrain_to_root_domain: bool = True,
        description: Optional[str] = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebRetrievalResponse:
        """
        Start a web crawl job and upsert data to the collection.

        :param data: WebRetrievalCreate object containing the data.
        :param extra_headers: Optional headers to send with the request.
        :return: The response data.
        """
        extra_headers = {"OpenAI-Beta": "assistants=v2", **(extra_headers or {})}
        return self._post(
            "/ops/web_retrieval",
            body=maybe_transform(
                {
                    "root_urls": root_urls,
                    "constrain_to_root_domain": constrain_to_root_domain,
                    "max_depth": max_depth,
                    "description": description,
                },
                WebRetrievalCreate,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebRetrievalResponse,
        )

    def delete(
        self,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeleteResponse:
        """
        Delete a web retrieval job.

        :param id: The ID of the web retrieval job.
        """
        return self._delete(
            "/ops/web_retrieval",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteResponse,
        )
