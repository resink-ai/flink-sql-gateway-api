from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_session_request_body_properties import OpenSessionRequestBodyProperties


T = TypeVar("T", bound="OpenSessionRequestBody")


@_attrs_define
class OpenSessionRequestBody:
    """
    Attributes:
        properties (Union[Unset, OpenSessionRequestBodyProperties]):
        session_name (Union[Unset, str]):
    """

    properties: Union[Unset, "OpenSessionRequestBodyProperties"] = UNSET
    session_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        session_name = self.session_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if properties is not UNSET:
            field_dict["properties"] = properties
        if session_name is not UNSET:
            field_dict["sessionName"] = session_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_session_request_body_properties import OpenSessionRequestBodyProperties

        d = src_dict.copy()
        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, OpenSessionRequestBodyProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = OpenSessionRequestBodyProperties.from_dict(_properties)

        session_name = d.pop("sessionName", UNSET)

        open_session_request_body = cls(
            properties=properties,
            session_name=session_name,
        )

        open_session_request_body.additional_properties = d
        return open_session_request_body

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
