from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigureSessionRequestBody")


@_attrs_define
class ConfigureSessionRequestBody:
    """
    Attributes:
        execution_timeout (Union[Unset, int]):
        statement (Union[Unset, str]):
    """

    execution_timeout: Union[Unset, int] = UNSET
    statement: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_timeout = self.execution_timeout

        statement = self.statement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_timeout is not UNSET:
            field_dict["executionTimeout"] = execution_timeout
        if statement is not UNSET:
            field_dict["statement"] = statement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        execution_timeout = d.pop("executionTimeout", UNSET)

        statement = d.pop("statement", UNSET)

        configure_session_request_body = cls(
            execution_timeout=execution_timeout,
            statement=statement,
        )

        configure_session_request_body.additional_properties = d
        return configure_session_request_body

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
