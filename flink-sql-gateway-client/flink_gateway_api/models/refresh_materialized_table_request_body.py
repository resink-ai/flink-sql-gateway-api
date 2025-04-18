from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refresh_materialized_table_request_body_dynamic_options import (
        RefreshMaterializedTableRequestBodyDynamicOptions,
    )
    from ..models.refresh_materialized_table_request_body_execution_config import (
        RefreshMaterializedTableRequestBodyExecutionConfig,
    )
    from ..models.refresh_materialized_table_request_body_static_partitions import (
        RefreshMaterializedTableRequestBodyStaticPartitions,
    )


T = TypeVar("T", bound="RefreshMaterializedTableRequestBody")


@_attrs_define
class RefreshMaterializedTableRequestBody:
    """
    Attributes:
        dynamic_options (Union[Unset, RefreshMaterializedTableRequestBodyDynamicOptions]):
        execution_config (Union[Unset, RefreshMaterializedTableRequestBodyExecutionConfig]):
        is_periodic (Union[Unset, bool]):
        periodic (Union[Unset, bool]):
        schedule_time (Union[Unset, str]):
        static_partitions (Union[Unset, RefreshMaterializedTableRequestBodyStaticPartitions]):
    """

    dynamic_options: Union[Unset, "RefreshMaterializedTableRequestBodyDynamicOptions"] = UNSET
    execution_config: Union[Unset, "RefreshMaterializedTableRequestBodyExecutionConfig"] = UNSET
    is_periodic: Union[Unset, bool] = UNSET
    periodic: Union[Unset, bool] = UNSET
    schedule_time: Union[Unset, str] = UNSET
    static_partitions: Union[Unset, "RefreshMaterializedTableRequestBodyStaticPartitions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dynamic_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dynamic_options, Unset):
            dynamic_options = self.dynamic_options.to_dict()

        execution_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.execution_config, Unset):
            execution_config = self.execution_config.to_dict()

        is_periodic = self.is_periodic

        periodic = self.periodic

        schedule_time = self.schedule_time

        static_partitions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_partitions, Unset):
            static_partitions = self.static_partitions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dynamic_options is not UNSET:
            field_dict["dynamicOptions"] = dynamic_options
        if execution_config is not UNSET:
            field_dict["executionConfig"] = execution_config
        if is_periodic is not UNSET:
            field_dict["isPeriodic"] = is_periodic
        if periodic is not UNSET:
            field_dict["periodic"] = periodic
        if schedule_time is not UNSET:
            field_dict["scheduleTime"] = schedule_time
        if static_partitions is not UNSET:
            field_dict["staticPartitions"] = static_partitions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.refresh_materialized_table_request_body_dynamic_options import (
            RefreshMaterializedTableRequestBodyDynamicOptions,
        )
        from ..models.refresh_materialized_table_request_body_execution_config import (
            RefreshMaterializedTableRequestBodyExecutionConfig,
        )
        from ..models.refresh_materialized_table_request_body_static_partitions import (
            RefreshMaterializedTableRequestBodyStaticPartitions,
        )

        d = src_dict.copy()
        _dynamic_options = d.pop("dynamicOptions", UNSET)
        dynamic_options: Union[Unset, RefreshMaterializedTableRequestBodyDynamicOptions]
        if isinstance(_dynamic_options, Unset):
            dynamic_options = UNSET
        else:
            dynamic_options = RefreshMaterializedTableRequestBodyDynamicOptions.from_dict(_dynamic_options)

        _execution_config = d.pop("executionConfig", UNSET)
        execution_config: Union[Unset, RefreshMaterializedTableRequestBodyExecutionConfig]
        if isinstance(_execution_config, Unset):
            execution_config = UNSET
        else:
            execution_config = RefreshMaterializedTableRequestBodyExecutionConfig.from_dict(_execution_config)

        is_periodic = d.pop("isPeriodic", UNSET)

        periodic = d.pop("periodic", UNSET)

        schedule_time = d.pop("scheduleTime", UNSET)

        _static_partitions = d.pop("staticPartitions", UNSET)
        static_partitions: Union[Unset, RefreshMaterializedTableRequestBodyStaticPartitions]
        if isinstance(_static_partitions, Unset):
            static_partitions = UNSET
        else:
            static_partitions = RefreshMaterializedTableRequestBodyStaticPartitions.from_dict(_static_partitions)

        refresh_materialized_table_request_body = cls(
            dynamic_options=dynamic_options,
            execution_config=execution_config,
            is_periodic=is_periodic,
            periodic=periodic,
            schedule_time=schedule_time,
            static_partitions=static_partitions,
        )

        refresh_materialized_table_request_body.additional_properties = d
        return refresh_materialized_table_request_body

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
