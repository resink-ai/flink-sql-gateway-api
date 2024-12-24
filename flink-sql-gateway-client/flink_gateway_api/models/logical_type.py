from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.logical_type_root import LogicalTypeRoot
from ..types import UNSET, Unset

T = TypeVar("T", bound="LogicalType")


@_attrs_define
class LogicalType:
    """
    Attributes:
        children (Union[Unset, list['LogicalType']]):
        nullable (Union[Unset, bool]):
        type_root (Union[Unset, LogicalTypeRoot]):
    """

    children: Union[Unset, list["LogicalType"]] = UNSET
    nullable: Union[Unset, bool] = UNSET
    type_root: Union[Unset, LogicalTypeRoot] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        nullable = self.nullable

        type_root: Union[Unset, str] = UNSET
        if not isinstance(self.type_root, Unset):
            type_root = self.type_root.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if nullable is not UNSET:
            field_dict["nullable"] = nullable
        if type_root is not UNSET:
            field_dict["typeRoot"] = type_root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = LogicalType.from_dict(children_item_data)

            children.append(children_item)

        nullable = d.pop("nullable", UNSET)

        _type_root = d.pop("typeRoot", UNSET)
        type_root: Union[Unset, LogicalTypeRoot]
        if isinstance(_type_root, Unset):
            type_root = UNSET
        else:
            type_root = LogicalTypeRoot(_type_root)

        logical_type = cls(
            children=children,
            nullable=nullable,
            type_root=type_root,
        )

        logical_type.additional_properties = d
        return logical_type

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
