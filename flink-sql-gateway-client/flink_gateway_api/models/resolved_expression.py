from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_type import DataType
    from ..models.expression import Expression


T = TypeVar("T", bound="ResolvedExpression")


@_attrs_define
class ResolvedExpression:
    """
    Attributes:
        children (Union[Unset, list['Expression']]):
        output_data_type (Union[Unset, DataType]):
        resolved_children (Union[Unset, list['ResolvedExpression']]):
    """

    children: Union[Unset, list["Expression"]] = UNSET
    output_data_type: Union[Unset, "DataType"] = UNSET
    resolved_children: Union[Unset, list["ResolvedExpression"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        output_data_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.output_data_type, Unset):
            output_data_type = self.output_data_type.to_dict()

        resolved_children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resolved_children, Unset):
            resolved_children = []
            for resolved_children_item_data in self.resolved_children:
                resolved_children_item = resolved_children_item_data.to_dict()
                resolved_children.append(resolved_children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if output_data_type is not UNSET:
            field_dict["outputDataType"] = output_data_type
        if resolved_children is not UNSET:
            field_dict["resolvedChildren"] = resolved_children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_type import DataType
        from ..models.expression import Expression

        d = src_dict.copy()
        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = Expression.from_dict(children_item_data)

            children.append(children_item)

        _output_data_type = d.pop("outputDataType", UNSET)
        output_data_type: Union[Unset, DataType]
        if isinstance(_output_data_type, Unset):
            output_data_type = UNSET
        else:
            output_data_type = DataType.from_dict(_output_data_type)

        resolved_children = []
        _resolved_children = d.pop("resolvedChildren", UNSET)
        for resolved_children_item_data in _resolved_children or []:
            resolved_children_item = ResolvedExpression.from_dict(resolved_children_item_data)

            resolved_children.append(resolved_children_item)

        resolved_expression = cls(
            children=children,
            output_data_type=output_data_type,
            resolved_children=resolved_children,
        )

        resolved_expression.additional_properties = d
        return resolved_expression

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
