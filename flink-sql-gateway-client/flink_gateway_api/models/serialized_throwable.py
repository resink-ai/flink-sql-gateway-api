from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="SerializedThrowable")


@_attrs_define
class SerializedThrowable:
    """
    Attributes:
        serialized_throwable (Union[Unset, File]):
    """

    serialized_throwable: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        serialized_throwable: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.serialized_throwable, Unset):
            serialized_throwable = self.serialized_throwable.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serialized_throwable is not UNSET:
            field_dict["serialized-throwable"] = serialized_throwable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _serialized_throwable = d.pop("serialized-throwable", UNSET)
        serialized_throwable: Union[Unset, File]
        if isinstance(_serialized_throwable, Unset):
            serialized_throwable = UNSET
        else:
            serialized_throwable = File(payload=BytesIO(_serialized_throwable))

        serialized_throwable = cls(
            serialized_throwable=serialized_throwable,
        )

        serialized_throwable.additional_properties = d
        return serialized_throwable

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
