from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.constraint_type import ConstraintType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UniqueConstraint")


@_attrs_define
class UniqueConstraint:
    """
    Attributes:
        columns (Union[Unset, list[str]]):
        enforced (Union[Unset, bool]):
        name (Union[Unset, str]):
        type_ (Union[Unset, ConstraintType]):
    """

    columns: Union[Unset, list[str]] = UNSET
    enforced: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, ConstraintType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        enforced = self.enforced

        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if enforced is not UNSET:
            field_dict["enforced"] = enforced
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        columns = cast(list[str], d.pop("columns", UNSET))

        enforced = d.pop("enforced", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ConstraintType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConstraintType(_type_)

        unique_constraint = cls(
            columns=columns,
            enforced=enforced,
            name=name,
            type_=type_,
        )

        unique_constraint.additional_properties = d
        return unique_constraint

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
