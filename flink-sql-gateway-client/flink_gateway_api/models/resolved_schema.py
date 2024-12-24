from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column import Column
    from ..models.data_type import DataType
    from ..models.unique_constraint import UniqueConstraint
    from ..models.watermark_spec import WatermarkSpec


T = TypeVar("T", bound="ResolvedSchema")


@_attrs_define
class ResolvedSchema:
    """
    Attributes:
        column_count (Union[Unset, int]):
        column_data_types (Union[Unset, list['DataType']]):
        column_names (Union[Unset, list[str]]):
        columns (Union[Unset, list['Column']]):
        primary_key (Union[Unset, UniqueConstraint]):
        primary_key_indexes (Union[Unset, list[int]]):
        watermark_specs (Union[Unset, list['WatermarkSpec']]):
    """

    column_count: Union[Unset, int] = UNSET
    column_data_types: Union[Unset, list["DataType"]] = UNSET
    column_names: Union[Unset, list[str]] = UNSET
    columns: Union[Unset, list["Column"]] = UNSET
    primary_key: Union[Unset, "UniqueConstraint"] = UNSET
    primary_key_indexes: Union[Unset, list[int]] = UNSET
    watermark_specs: Union[Unset, list["WatermarkSpec"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_count = self.column_count

        column_data_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.column_data_types, Unset):
            column_data_types = []
            for column_data_types_item_data in self.column_data_types:
                column_data_types_item = column_data_types_item_data.to_dict()
                column_data_types.append(column_data_types_item)

        column_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.column_names, Unset):
            column_names = self.column_names

        columns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        primary_key: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_key, Unset):
            primary_key = self.primary_key.to_dict()

        primary_key_indexes: Union[Unset, list[int]] = UNSET
        if not isinstance(self.primary_key_indexes, Unset):
            primary_key_indexes = self.primary_key_indexes

        watermark_specs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.watermark_specs, Unset):
            watermark_specs = []
            for watermark_specs_item_data in self.watermark_specs:
                watermark_specs_item = watermark_specs_item_data.to_dict()
                watermark_specs.append(watermark_specs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if column_count is not UNSET:
            field_dict["columnCount"] = column_count
        if column_data_types is not UNSET:
            field_dict["columnDataTypes"] = column_data_types
        if column_names is not UNSET:
            field_dict["columnNames"] = column_names
        if columns is not UNSET:
            field_dict["columns"] = columns
        if primary_key is not UNSET:
            field_dict["primaryKey"] = primary_key
        if primary_key_indexes is not UNSET:
            field_dict["primaryKeyIndexes"] = primary_key_indexes
        if watermark_specs is not UNSET:
            field_dict["watermarkSpecs"] = watermark_specs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.column import Column
        from ..models.data_type import DataType
        from ..models.unique_constraint import UniqueConstraint
        from ..models.watermark_spec import WatermarkSpec

        d = src_dict.copy()
        column_count = d.pop("columnCount", UNSET)

        column_data_types = []
        _column_data_types = d.pop("columnDataTypes", UNSET)
        for column_data_types_item_data in _column_data_types or []:
            column_data_types_item = DataType.from_dict(column_data_types_item_data)

            column_data_types.append(column_data_types_item)

        column_names = cast(list[str], d.pop("columnNames", UNSET))

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = Column.from_dict(columns_item_data)

            columns.append(columns_item)

        _primary_key = d.pop("primaryKey", UNSET)
        primary_key: Union[Unset, UniqueConstraint]
        if isinstance(_primary_key, Unset):
            primary_key = UNSET
        else:
            primary_key = UniqueConstraint.from_dict(_primary_key)

        primary_key_indexes = cast(list[int], d.pop("primaryKeyIndexes", UNSET))

        watermark_specs = []
        _watermark_specs = d.pop("watermarkSpecs", UNSET)
        for watermark_specs_item_data in _watermark_specs or []:
            watermark_specs_item = WatermarkSpec.from_dict(watermark_specs_item_data)

            watermark_specs.append(watermark_specs_item)

        resolved_schema = cls(
            column_count=column_count,
            column_data_types=column_data_types,
            column_names=column_names,
            columns=columns,
            primary_key=primary_key,
            primary_key_indexes=primary_key_indexes,
            watermark_specs=watermark_specs,
        )

        resolved_schema.additional_properties = d
        return resolved_schema

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
