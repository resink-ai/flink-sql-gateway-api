from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.row_kind import RowKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="RowData")


@_attrs_define
class RowData:
    """
    Attributes:
        arity (Union[Unset, int]):
        row_kind (Union[Unset, RowKind]):
    """

    arity: Union[Unset, int] = UNSET
    row_kind: Union[Unset, RowKind] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arity = self.arity

        row_kind: Union[Unset, str] = UNSET
        if not isinstance(self.row_kind, Unset):
            row_kind = self.row_kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arity is not UNSET:
            field_dict["arity"] = arity
        if row_kind is not UNSET:
            field_dict["rowKind"] = row_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        arity = d.pop("arity", UNSET)

        _row_kind = d.pop("rowKind", UNSET)
        row_kind: Union[Unset, RowKind]
        if isinstance(_row_kind, Unset):
            row_kind = UNSET
        else:
            row_kind = RowKind(_row_kind)

        row_data = cls(
            arity=arity,
            row_kind=row_kind,
        )

        row_data.additional_properties = d
        return row_data

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
