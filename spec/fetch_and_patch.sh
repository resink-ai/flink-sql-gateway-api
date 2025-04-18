#!/bin/bash

set -euox pipefail
wget https://nightlies.apache.org/flink/flink-docs-release-1.18/generated/rest_v2_sql_gateway.yml -O rest_v2_sql_gateway_1_18.yml
wget https://nightlies.apache.org/flink/flink-docs-release-1.19/generated/rest_v2_sql_gateway.yml -O rest_v2_sql_gateway_1_19.yml
wget https://nightlies.apache.org/flink/flink-docs-release-1.20/generated/rest_v2_sql_gateway.yml -O rest_v2_sql_gateway_1_20.yml
wget https://nightlies.apache.org/flink/flink-docs-release-1.20/generated/rest_v3_sql_gateway.yml -O rest_v3_sql_gateway_1_20.yml
wget https://nightlies.apache.org/flink/flink-docs-master/generated/rest_v4_sql_gateway.yml -O rest_v4_sql_gateway_2_1.yml

## Patching the session handle to be string
for file in rest*sql_gateway*.yml; do
    yq e '
        .components.schemas.SessionHandle = {"type": "string"} |
        .components.schemas.OperationHandle = {"type": "string"}
    ' -i "$file"
done
