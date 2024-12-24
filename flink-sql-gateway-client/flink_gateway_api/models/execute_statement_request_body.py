from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_statement_request_body_execution_config import ExecuteStatementRequestBodyExecutionConfig


T = TypeVar("T", bound="ExecuteStatementRequestBody")


@_attrs_define
class ExecuteStatementRequestBody:
    """
    Attributes:
        execution_config (Union[Unset, ExecuteStatementRequestBodyExecutionConfig]):
        execution_timeout (Union[Unset, int]):
        statement (Union[Unset, str]):
    """

    execution_config: Union[Unset, "ExecuteStatementRequestBodyExecutionConfig"] = UNSET
    execution_timeout: Union[Unset, int] = UNSET
    statement: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.execution_config, Unset):
            execution_config = self.execution_config.to_dict()

        execution_timeout = self.execution_timeout

        statement = self.statement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_config is not UNSET:
            field_dict["executionConfig"] = execution_config
        if execution_timeout is not UNSET:
            field_dict["executionTimeout"] = execution_timeout
        if statement is not UNSET:
            field_dict["statement"] = statement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.execute_statement_request_body_execution_config import ExecuteStatementRequestBodyExecutionConfig

        d = src_dict.copy()
        _execution_config = d.pop("executionConfig", UNSET)
        execution_config: Union[Unset, ExecuteStatementRequestBodyExecutionConfig]
        if isinstance(_execution_config, Unset):
            execution_config = UNSET
        else:
            execution_config = ExecuteStatementRequestBodyExecutionConfig.from_dict(_execution_config)

        execution_timeout = d.pop("executionTimeout", UNSET)

        statement = d.pop("statement", UNSET)

        execute_statement_request_body = cls(
            execution_config=execution_config,
            execution_timeout=execution_timeout,
            statement=statement,
        )

        execute_statement_request_body.additional_properties = d
        return execute_statement_request_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
