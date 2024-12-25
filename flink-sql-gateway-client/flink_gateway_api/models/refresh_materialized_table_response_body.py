from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefreshMaterializedTableResponseBody")


@_attrs_define
class RefreshMaterializedTableResponseBody:
    """
    Attributes:
        operation_handle (Union[Unset, str]):
    """

    operation_handle: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_handle = self.operation_handle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation_handle is not UNSET:
            field_dict["operationHandle"] = operation_handle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_handle = d.pop("operationHandle", UNSET)

        refresh_materialized_table_response_body = cls(
            operation_handle=operation_handle,
        )

        refresh_materialized_table_response_body.additional_properties = d
        return refresh_materialized_table_response_body

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
