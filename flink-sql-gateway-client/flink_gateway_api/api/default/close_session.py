from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.close_session_response_body import CloseSessionResponseBody
from ...types import Response


def _get_kwargs(
    session_handle: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/sessions/{session_handle}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CloseSessionResponseBody]:
    if response.status_code == 200:
        response_200 = CloseSessionResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CloseSessionResponseBody]:
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
) -> Response[CloseSessionResponseBody]:
    """Closes the specific session.

    Args:
        session_handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloseSessionResponseBody]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CloseSessionResponseBody]:
    """Closes the specific session.

    Args:
        session_handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloseSessionResponseBody
    """

    return sync_detailed(
        session_handle=session_handle,
        client=client,
    ).parsed


async def asyncio_detailed(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CloseSessionResponseBody]:
    """Closes the specific session.

    Args:
        session_handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloseSessionResponseBody]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CloseSessionResponseBody]:
    """Closes the specific session.

    Args:
        session_handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloseSessionResponseBody
    """

    return (
        await asyncio_detailed(
            session_handle=session_handle,
            client=client,
        )
    ).parsed
