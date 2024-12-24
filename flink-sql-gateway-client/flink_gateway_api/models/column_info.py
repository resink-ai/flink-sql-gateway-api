from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_type import LogicalType


T = TypeVar("T", bound="ColumnInfo")


@_attrs_define
class ColumnInfo:
    """
    Attributes:
        comment (Union[Unset, str]):
        logical_type (Union[Unset, LogicalType]):
        name (Union[Unset, str]):
    """

    comment: Union[Unset, str] = UNSET
    logical_type: Union[Unset, "LogicalType"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        logical_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.logical_type, Unset):
            logical_type = self.logical_type.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if logical_type is not UNSET:
            field_dict["logicalType"] = logical_type
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.logical_type import LogicalType

        d = src_dict.copy()
        comment = d.pop("comment", UNSET)

        _logical_type = d.pop("logicalType", UNSET)
        logical_type: Union[Unset, LogicalType]
        if isinstance(_logical_type, Unset):
            logical_type = UNSET
        else:
            logical_type = LogicalType.from_dict(_logical_type)

        name = d.pop("name", UNSET)

        column_info = cls(
            comment=comment,
            logical_type=logical_type,
            name=name,
        )

        column_info.additional_properties = d
        return column_info

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
