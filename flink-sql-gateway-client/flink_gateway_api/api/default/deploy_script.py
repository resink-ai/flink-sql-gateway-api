from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deploy_script_request_body import DeployScriptRequestBody
from ...models.deploy_script_response_body import DeployScriptResponseBody
from ...types import Response


def _get_kwargs(
    session_handle: str,
    *,
    body: DeployScriptRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/sessions/{session_handle}/scripts",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeployScriptResponseBody]:
    if response.status_code == 200:
        response_200 = DeployScriptResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeployScriptResponseBody]:
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
    body: DeployScriptRequestBody,
) -> Response[DeployScriptResponseBody]:
    """Deploy the script in application mode

    Args:
        session_handle (str):
        body (DeployScriptRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeployScriptResponseBody]
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
    body: DeployScriptRequestBody,
) -> Optional[DeployScriptResponseBody]:
    """Deploy the script in application mode

    Args:
        session_handle (str):
        body (DeployScriptRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeployScriptResponseBody
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
    body: DeployScriptRequestBody,
) -> Response[DeployScriptResponseBody]:
    """Deploy the script in application mode

    Args:
        session_handle (str):
        body (DeployScriptRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeployScriptResponseBody]
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
    body: DeployScriptRequestBody,
) -> Optional[DeployScriptResponseBody]:
    """Deploy the script in application mode

    Args:
        session_handle (str):
        body (DeployScriptRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeployScriptResponseBody
    """

    return (
        await asyncio_detailed(
            session_handle=session_handle,
            client=client,
            body=body,
        )
    ).parsed
