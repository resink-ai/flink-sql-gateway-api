from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_type import LogicalType


T = TypeVar("T", bound="DataType")


@_attrs_define
class DataType:
    """
    Attributes:
        children (Union[Unset, list['DataType']]):
        logical_type (Union[Unset, LogicalType]):
    """

    children: Union[Unset, list["DataType"]] = UNSET
    logical_type: Union[Unset, "LogicalType"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        logical_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.logical_type, Unset):
            logical_type = self.logical_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if logical_type is not UNSET:
            field_dict["logicalType"] = logical_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.logical_type import LogicalType

        d = src_dict.copy()
        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = DataType.from_dict(children_item_data)

            children.append(children_item)

        _logical_type = d.pop("logicalType", UNSET)
        logical_type: Union[Unset, LogicalType]
        if isinstance(_logical_type, Unset):
            logical_type = UNSET
        else:
            logical_type = LogicalType.from_dict(_logical_type)

        data_type = cls(
            children=children,
            logical_type=logical_type,
        )

        data_type.additional_properties = d
        return data_type

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
