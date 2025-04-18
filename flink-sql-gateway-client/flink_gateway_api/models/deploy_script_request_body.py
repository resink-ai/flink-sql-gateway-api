from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deploy_script_request_body_execution_config import DeployScriptRequestBodyExecutionConfig


T = TypeVar("T", bound="DeployScriptRequestBody")


@_attrs_define
class DeployScriptRequestBody:
    """
    Attributes:
        execution_config (Union[Unset, DeployScriptRequestBodyExecutionConfig]):
        script (Union[Unset, str]):
        script_uri (Union[Unset, str]):
    """

    execution_config: Union[Unset, "DeployScriptRequestBodyExecutionConfig"] = UNSET
    script: Union[Unset, str] = UNSET
    script_uri: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.execution_config, Unset):
            execution_config = self.execution_config.to_dict()

        script = self.script

        script_uri = self.script_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_config is not UNSET:
            field_dict["executionConfig"] = execution_config
        if script is not UNSET:
            field_dict["script"] = script
        if script_uri is not UNSET:
            field_dict["scriptUri"] = script_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.deploy_script_request_body_execution_config import DeployScriptRequestBodyExecutionConfig

        d = src_dict.copy()
        _execution_config = d.pop("executionConfig", UNSET)
        execution_config: Union[Unset, DeployScriptRequestBodyExecutionConfig]
        if isinstance(_execution_config, Unset):
            execution_config = UNSET
        else:
            execution_config = DeployScriptRequestBodyExecutionConfig.from_dict(_execution_config)

        script = d.pop("script", UNSET)

        script_uri = d.pop("scriptUri", UNSET)

        deploy_script_request_body = cls(
            execution_config=execution_config,
            script=script,
            script_uri=script_uri,
        )

        deploy_script_request_body.additional_properties = d
        return deploy_script_request_body

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
