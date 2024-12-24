from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.row_format import RowFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_info import ColumnInfo
    from ..models.field_getter import FieldGetter
    from ..models.resolved_schema import ResolvedSchema
    from ..models.row_data import RowData


T = TypeVar("T", bound="ResultInfo")


@_attrs_define
class ResultInfo:
    """
    Attributes:
        column_infos (Union[Unset, list['ColumnInfo']]):
        data (Union[Unset, list['RowData']]):
        field_getters (Union[Unset, list['FieldGetter']]):
        result_schema (Union[Unset, ResolvedSchema]):
        row_format (Union[Unset, RowFormat]):
    """

    column_infos: Union[Unset, list["ColumnInfo"]] = UNSET
    data: Union[Unset, list["RowData"]] = UNSET
    field_getters: Union[Unset, list["FieldGetter"]] = UNSET
    result_schema: Union[Unset, "ResolvedSchema"] = UNSET
    row_format: Union[Unset, RowFormat] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_infos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.column_infos, Unset):
            column_infos = []
            for column_infos_item_data in self.column_infos:
                column_infos_item = column_infos_item_data.to_dict()
                column_infos.append(column_infos_item)

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_getters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.field_getters, Unset):
            field_getters = []
            for field_getters_item_data in self.field_getters:
                field_getters_item = field_getters_item_data.to_dict()
                field_getters.append(field_getters_item)

        result_schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.result_schema, Unset):
            result_schema = self.result_schema.to_dict()

        row_format: Union[Unset, str] = UNSET
        if not isinstance(self.row_format, Unset):
            row_format = self.row_format.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if column_infos is not UNSET:
            field_dict["columnInfos"] = column_infos
        if data is not UNSET:
            field_dict["data"] = data
        if field_getters is not UNSET:
            field_dict["fieldGetters"] = field_getters
        if result_schema is not UNSET:
            field_dict["resultSchema"] = result_schema
        if row_format is not UNSET:
            field_dict["rowFormat"] = row_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.column_info import ColumnInfo
        from ..models.field_getter import FieldGetter
        from ..models.resolved_schema import ResolvedSchema
        from ..models.row_data import RowData

        d = src_dict.copy()
        column_infos = []
        _column_infos = d.pop("columnInfos", UNSET)
        for column_infos_item_data in _column_infos or []:
            column_infos_item = ColumnInfo.from_dict(column_infos_item_data)

            column_infos.append(column_infos_item)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = RowData.from_dict(data_item_data)

            data.append(data_item)

        field_getters = []
        _field_getters = d.pop("fieldGetters", UNSET)
        for field_getters_item_data in _field_getters or []:
            field_getters_item = FieldGetter.from_dict(field_getters_item_data)

            field_getters.append(field_getters_item)

        _result_schema = d.pop("resultSchema", UNSET)
        result_schema: Union[Unset, ResolvedSchema]
        if isinstance(_result_schema, Unset):
            result_schema = UNSET
        else:
            result_schema = ResolvedSchema.from_dict(_result_schema)

        _row_format = d.pop("rowFormat", UNSET)
        row_format: Union[Unset, RowFormat]
        if isinstance(_row_format, Unset):
            row_format = UNSET
        else:
            row_format = RowFormat(_row_format)

        result_info = cls(
            column_infos=column_infos,
            data=data,
            field_getters=field_getters,
            result_schema=result_schema,
            row_format=row_format,
        )

        result_info.additional_properties = d
        return result_info

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
