import unittest
import json
import time
import unittest

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


class TestSyncCalls(unittest.TestCase):
    def test_api_version(self):
        with Client('http://localhost:8083') as client:
            response = get_api_version.sync(client=client)
            self.assertEqual(response.versions, ["V1", "V2"])
            print(response.to_dict())

    def test_info(self):
        with Client('http://localhost:8083') as client:
            response = get_info.sync(client=client)
            self.assertIsNotNone(response.version)
            print(f"info response: {response.to_dict()}")

    def test_execute(self):
        with Client('http://localhost:8083') as client:
            responses = open_session.sync(client=client, body=OpenSessionRequestBody.from_dict({
                "properties": {
                    "idle-timeout": "10s"
                },
                "sessionName": "test_session"
            }))
            print(f"Open session response: {responses}")

            select_result = execute_statement.sync(responses.session_handle, client=client,
                                                   body=ExecuteStatementResponseBody.from_dict({
                                                       "statement": "SELECT 23 as age, 'Alice Liddel' as name;",
                                                   }))

            print(f"Select result: {select_result}")
            time.sleep(1)
            fetch_return = fetch_results.sync(
                responses.session_handle,
                select_result.operation_handle,
                0,
                client=client,
                row_format=RowFormat.JSON,
            )
            print(f"[0] Fetch return: {json.dumps(fetch_return.to_dict())}")
            
            fetch_return = fetch_results.sync(
                responses.session_handle,
                select_result.operation_handle,
                1,
                client=client,
                row_format=RowFormat.JSON,
            )
            print(f"[1] Fetch return: {json.dumps(fetch_return.to_dict())}")

            close_session.sync(responses.session_handle, client=client)
            print(f"Session closed")