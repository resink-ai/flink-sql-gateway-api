from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_type import DataType


T = TypeVar("T", bound="Column")


@_attrs_define
class Column:
    """
    Attributes:
        comment (Union[Unset, str]):
        data_type (Union[Unset, DataType]):
        name (Union[Unset, str]):
        persisted (Union[Unset, bool]):
        physical (Union[Unset, bool]):
    """

    comment: Union[Unset, str] = UNSET
    data_type: Union[Unset, "DataType"] = UNSET
    name: Union[Unset, str] = UNSET
    persisted: Union[Unset, bool] = UNSET
    physical: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        data_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.to_dict()

        name = self.name

        persisted = self.persisted

        physical = self.physical

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if name is not UNSET:
            field_dict["name"] = name
        if persisted is not UNSET:
            field_dict["persisted"] = persisted
        if physical is not UNSET:
            field_dict["physical"] = physical

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_type import DataType

        d = src_dict.copy()
        comment = d.pop("comment", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, DataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = DataType.from_dict(_data_type)

        name = d.pop("name", UNSET)

        persisted = d.pop("persisted", UNSET)

        physical = d.pop("physical", UNSET)

        column = cls(
            comment=comment,
            data_type=data_type,
            name=name,
            persisted=persisted,
            physical=physical,
        )

        column.additional_properties = d
        return column

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
