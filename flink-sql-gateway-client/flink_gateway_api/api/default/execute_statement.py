from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_statement_request_body import ExecuteStatementRequestBody
from ...models.execute_statement_response_body import ExecuteStatementResponseBody
from ...types import Response


def _get_kwargs(
    session_handle: str,
    *,
    body: ExecuteStatementRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/sessions/{session_handle}/statements",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExecuteStatementResponseBody]:
    if response.status_code == 200:
        response_200 = ExecuteStatementResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExecuteStatementResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExecuteStatementRequestBody,
) -> Response[ExecuteStatementResponseBody]:
    """Execute a statement.

    Args:
        session_handle (str):
        body (ExecuteStatementRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteStatementResponseBody]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExecuteStatementRequestBody,
) -> Optional[ExecuteStatementResponseBody]:
    """Execute a statement.

    Args:
        session_handle (str):
        body (ExecuteStatementRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteStatementResponseBody
    """

    return sync_detailed(
        session_handle=session_handle,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExecuteStatementRequestBody,
) -> Response[ExecuteStatementResponseBody]:
    """Execute a statement.

    Args:
        session_handle (str):
        body (ExecuteStatementRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteStatementResponseBody]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExecuteStatementRequestBody,
) -> Optional[ExecuteStatementResponseBody]:
    """Execute a statement.

    Args:
        session_handle (str):
        body (ExecuteStatementRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteStatementResponseBody
    """

    return (
        await asyncio_detailed(
            session_handle=session_handle,
            client=client,
            body=body,
        )
    ).parsed
