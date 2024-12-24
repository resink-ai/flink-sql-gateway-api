from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_results_response_body import FetchResultsResponseBody
from ...models.row_format import RowFormat
from ...types import UNSET, Response


def _get_kwargs(
    session_handle: str,
    operation_handle: str,
    token: int,
    *,
    row_format: RowFormat,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_row_format = row_format.value
    params["rowFormat"] = json_row_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sessions/{session_handle}/operations/{operation_handle}/result/{token}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FetchResultsResponseBody]:
    if response.status_code == 200:
        response_200 = FetchResultsResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FetchResultsResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_handle: str,
    operation_handle: str,
    token: int,
    *,
    client: Union[AuthenticatedClient, Client],
    row_format: RowFormat,
) -> Response[FetchResultsResponseBody]:
    """Fetch results of Operation.

    Args:
        session_handle (str):
        operation_handle (str):
        token (int):
        row_format (RowFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchResultsResponseBody]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
        operation_handle=operation_handle,
        token=token,
        row_format=row_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_handle: str,
    operation_handle: str,
    token: int,
    *,
    client: Union[AuthenticatedClient, Client],
    row_format: RowFormat,
) -> Optional[FetchResultsResponseBody]:
    """Fetch results of Operation.

    Args:
        session_handle (str):
        operation_handle (str):
        token (int):
        row_format (RowFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchResultsResponseBody
    """

    return sync_detailed(
        session_handle=session_handle,
        operation_handle=operation_handle,
        token=token,
        client=client,
        row_format=row_format,
    ).parsed


async def asyncio_detailed(
    session_handle: str,
    operation_handle: str,
    token: int,
    *,
    client: Union[AuthenticatedClient, Client],
    row_format: RowFormat,
) -> Response[FetchResultsResponseBody]:
    """Fetch results of Operation.

    Args:
        session_handle (str):
        operation_handle (str):
        token (int):
        row_format (RowFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchResultsResponseBody]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
        operation_handle=operation_handle,
        token=token,
        row_format=row_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_handle: str,
    operation_handle: str,
    token: int,
    *,
    client: Union[AuthenticatedClient, Client],
    row_format: RowFormat,
) -> Optional[FetchResultsResponseBody]:
    """Fetch results of Operation.

    Args:
        session_handle (str):
        operation_handle (str):
        token (int):
        row_format (RowFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchResultsResponseBody
    """

    return (
        await asyncio_detailed(
            session_handle=session_handle,
            operation_handle=operation_handle,
            token=token,
            client=client,
            row_format=row_format,
        )
    ).parsed
