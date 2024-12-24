from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_session_config_response_body_properties import GetSessionConfigResponseBodyProperties


T = TypeVar("T", bound="GetSessionConfigResponseBody")


@_attrs_define
class GetSessionConfigResponseBody:
    """
    Attributes:
        properties (Union[Unset, GetSessionConfigResponseBodyProperties]):
    """

    properties: Union[Unset, "GetSessionConfigResponseBodyProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_session_config_response_body_properties import GetSessionConfigResponseBodyProperties

        d = src_dict.copy()
        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, GetSessionConfigResponseBodyProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = GetSessionConfigResponseBodyProperties.from_dict(_properties)

        get_session_config_response_body = cls(
            properties=properties,
        )

        get_session_config_response_body.additional_properties = d
        return get_session_config_response_body

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
