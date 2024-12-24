from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.configure_session_request_body import ConfigureSessionRequestBody
from ...types import Response


def _get_kwargs(
    session_handle: str,
    *,
    body: ConfigureSessionRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/sessions/{session_handle}/configure-session",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    body: ConfigureSessionRequestBody,
) -> Response[Any]:
    """Configures the session with the statement which could be:
    CREATE TABLE, DROP TABLE, ALTER TABLE, CREATE DATABASE, DROP DATABASE, ALTER DATABASE, CREATE
    FUNCTION, DROP FUNCTION, ALTER FUNCTION, CREATE CATALOG, DROP CATALOG, USE CATALOG, USE
    [CATALOG.]DATABASE, CREATE VIEW, DROP VIEW, LOAD MODULE, UNLOAD MODULE, USE MODULE, ADD JAR.

    Args:
        session_handle (str):
        body (ConfigureSessionRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    session_handle: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConfigureSessionRequestBody,
) -> Response[Any]:
    """Configures the session with the statement which could be:
    CREATE TABLE, DROP TABLE, ALTER TABLE, CREATE DATABASE, DROP DATABASE, ALTER DATABASE, CREATE
    FUNCTION, DROP FUNCTION, ALTER FUNCTION, CREATE CATALOG, DROP CATALOG, USE CATALOG, USE
    [CATALOG.]DATABASE, CREATE VIEW, DROP VIEW, LOAD MODULE, UNLOAD MODULE, USE MODULE, ADD JAR.

    Args:
        session_handle (str):
        body (ConfigureSessionRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_handle=session_handle,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
