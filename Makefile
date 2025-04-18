.SHELLFLAGS := -xc
SHELL := /bin/bash
.PHONY: py_118 py_119 py_120 py_21_v3 py_21_v4 download release

# Common variables
SPEC_DIR = spec
CONFIG = $(SPEC_DIR)/gen_config.yaml
YAML_118 = $(SPEC_DIR)/rest_v2_sql_gateway_1_18.yml
YAML_119 = $(SPEC_DIR)/rest_v2_sql_gateway_1_19.yml
YAML_120 = $(SPEC_DIR)/rest_v3_sql_gateway_1_20.yml
YAML_21_v3 = $(SPEC_DIR)/rest_v3_sql_gateway_2_1.yml
YAML_21_v4 = $(SPEC_DIR)/rest_v4_sql_gateway_2_1.yml

# Get today's date in YYYYMMDD format
TODAY_DATE := $(shell date '+%Y%m%d')

# Define YAML files as targets that depend on the download action
$(YAML_118) $(YAML_119) $(YAML_120) $(YAML_21_v3) $(YAML_21_v4):
	cd $(SPEC_DIR) && bash fetch_and_patch.sh && cd ..

# Download target depends on the YAML files
download: $(YAML_119) $(YAML_120) $(YAML_21_v3) $(YAML_21_v4)

py_118: download
	openapi-python-client generate \
		--path $(YAML_118) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 1.18.a$(TODAY_DATE)
	pushd flink-sql-gateway-client && pytest tests && popd

py_119: download
	openapi-python-client generate \
		--path $(YAML_119) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 1.19.a$(TODAY_DATE)
	pushd flink-sql-gateway-client && pytest tests && popd

py_120: download
	openapi-python-client generate \
		--path $(YAML_120) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 1.20.a$(TODAY_DATE)
	pushd flink-sql-gateway-client && pytest tests && popd

py_21_v3: download
	openapi-python-client generate \
		--path $(YAML_21_v3) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 2.1.3a$(TODAY_DATE)
	pushd flink-sql-gateway-client && pytest tests && popd

py_21_v4: download
	openapi-python-client generate \
		--path $(YAML_21_v4) \
		--overwrite \
		--config $(CONFIG)
	cp -v README.md flink-sql-gateway-client/
	cp -rv spec/py/* flink-sql-gateway-client/
	poetry -C flink-sql-gateway-client/ version 2.1.4a$(TODAY_DATE)
	pushd flink-sql-gateway-client && pytest tests && popd

release:
	cd $$(git rev-parse --show-toplevel)/flink-sql-gateway-client && pytest tests
	@if [ $$? -ne 0 ]; then \
		echo "Tests failed. Release aborted."; \
		exit 1; \
	fi
	cd $$(git rev-parse --show-toplevel)
	@echo "Current version:"
	@cat flink-sql-gateway-client/pyproject.toml | grep version
	@version=$$(cat flink-sql-gateway-client/pyproject.toml | grep version | cut -d '"' -f2); \
	release_tag="release-$$version"; \
	echo "Tagging and releasing version $$version"; \
	cd $$(git rev-parse --show-toplevel); \
	git add -u; \
	git commit -m "Release version $$version"; \
	git tag -d $$release_tag || true; \
	git tag "$$release_tag"; \
	git push origin "$$release_tag"

