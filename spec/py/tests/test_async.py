import json
import time
import unittest
import asyncio

from flink_gateway_api import Client
from flink_gateway_api.api.default import (
    get_api_version,
    get_info,
    open_session,
    close_session,
    execute_statement,
    fetch_results,
)
from flink_gateway_api.models import (
    OpenSessionRequestBody,
    ExecuteStatementResponseBody,
    RowFormat,
)


class TestAsyncCalls(unittest.IsolatedAsyncioTestCase):
    async def test_api_version(self):
        async with Client('http://localhost:8083') as client:
            response = await get_api_version.asyncio(client=client)
            self.assertEqual(response.versions, ["V1", "V2"])
            print(response.to_dict())

    async def test_info(self):
        async with Client('http://localhost:8083') as client:
            response = await get_info.asyncio(client=client)
            self.assertIsNotNone(response.to_dict())
            print(f"info response: {response.to_dict()}")

    async def test_execute(self):
        async with Client('http://localhost:8083') as client:
            responses = await open_session.asyncio(client=client, body=OpenSessionRequestBody.from_dict({
                "properties": {
                    "idle-timeout": "10s"
                },
                "sessionName": "test_session"
            }))
            print(f"Open session response: {responses}")

            select_result = await execute_statement.asyncio(responses.session_handle, client=client,
                                                            body=ExecuteStatementResponseBody.from_dict({
                                                                "statement": "SELECT 23 as age, 'Alice Liddel' as name;",
                                                            }))

            print(f"Select result: {select_result}")
            await asyncio.sleep(1)
            fetch_return = await fetch_results.asyncio(
                responses.session_handle,
                select_result.operation_handle,
                0,
                client=client,
                row_format=RowFormat.JSON,
            )
            print(f"Fetch return: {json.dumps(fetch_return.to_dict())}")

            await close_session.asyncio(responses.session_handle, client=client)
            print(f"Session closed")