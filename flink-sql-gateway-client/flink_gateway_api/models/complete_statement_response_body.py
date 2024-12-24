from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompleteStatementResponseBody")


@_attrs_define
class CompleteStatementResponseBody:
    """
    Attributes:
        candidates (Union[Unset, list[str]]):
    """

    candidates: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidates: Union[Unset, list[str]] = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = self.candidates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidates is not UNSET:
            field_dict["candidates"] = candidates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        candidates = cast(list[str], d.pop("candidates", UNSET))

        complete_statement_response_body = cls(
            candidates=candidates,
        )

        complete_statement_response_body.additional_properties = d
        return complete_statement_response_body

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
