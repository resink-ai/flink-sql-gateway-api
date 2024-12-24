from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolved_expression import ResolvedExpression


T = TypeVar("T", bound="WatermarkSpec")


@_attrs_define
class WatermarkSpec:
    """
    Attributes:
        rowtime_attribute (Union[Unset, str]):
        watermark_expression (Union[Unset, ResolvedExpression]):
    """

    rowtime_attribute: Union[Unset, str] = UNSET
    watermark_expression: Union[Unset, "ResolvedExpression"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rowtime_attribute = self.rowtime_attribute

        watermark_expression: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.watermark_expression, Unset):
            watermark_expression = self.watermark_expression.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rowtime_attribute is not UNSET:
            field_dict["rowtimeAttribute"] = rowtime_attribute
        if watermark_expression is not UNSET:
            field_dict["watermarkExpression"] = watermark_expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.resolved_expression import ResolvedExpression

        d = src_dict.copy()
        rowtime_attribute = d.pop("rowtimeAttribute", UNSET)

        _watermark_expression = d.pop("watermarkExpression", UNSET)
        watermark_expression: Union[Unset, ResolvedExpression]
        if isinstance(_watermark_expression, Unset):
            watermark_expression = UNSET
        else:
            watermark_expression = ResolvedExpression.from_dict(_watermark_expression)

        watermark_spec = cls(
            rowtime_attribute=rowtime_attribute,
            watermark_expression=watermark_expression,
        )

        watermark_spec.additional_properties = d
        return watermark_spec

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
