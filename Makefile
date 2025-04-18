.SHELLFLAGS := -xc
SHELL := /bin/bash
.PHONY: py_118 py_119 py_120 download

# Common variables
SPEC_DIR = spec
CONFIG = $(SPEC_DIR)/gen_config.yaml
YAML_118 = $(SPEC_DIR)/rest_v2_sql_gateway_1_18.yml
YAML_119 = $(SPEC_DIR)/rest_v2_sql_gateway_1_19.yml
YAML_120 = $(SPEC_DIR)/rest_v3_sql_gateway_1_20.yml
YAML_21 = $(SPEC_DIR)/rest_v4_sql_gateway_2_1.yml

# Get today's date in YYYYMMDD format
TODAY_DATE := $(shell date '+%Y%m%d')

# Define YAML files as targets that depend on the download action
$(YAML_118) $(YAML_119) $(YAML_120) $(YAML_21):
	cd $(SPEC_DIR) && bash fetch_and_patch.sh && cd ..

# Download target depends on the YAML files
download: $(YAML_119) $(YAML_120) $(YAML_21)

py_118: download
	openapi-python-client generate \
		--path $(YAML_118) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 1.18.alpha$(TODAY_DATE)

py_119: download
	openapi-python-client generate \
		--path $(YAML_119) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 1.19.alpha$(TODAY_DATE)

py_120: download
	openapi-python-client generate \
		--path $(YAML_120) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 1.20.alpha$(TODAY_DATE)

py_2_1: download
	openapi-python-client generate \
		--path $(YAML_21) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 2.1.alpha$(TODAY_DATE)
