from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.result_kind import ResultKind
from ..models.result_type import ResultType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_info import ResultInfo


T = TypeVar("T", bound="FetchResultsResponseBody")


@_attrs_define
class FetchResultsResponseBody:
    """
    Attributes:
        job_id (Union[Unset, str]):
        next_result_uri (Union[Unset, str]):
        query_result (Union[Unset, bool]):
        result_kind (Union[Unset, ResultKind]):
        result_type (Union[Unset, ResultType]):
        results (Union[Unset, ResultInfo]):
    """

    job_id: Union[Unset, str] = UNSET
    next_result_uri: Union[Unset, str] = UNSET
    query_result: Union[Unset, bool] = UNSET
    result_kind: Union[Unset, ResultKind] = UNSET
    result_type: Union[Unset, ResultType] = UNSET
    results: Union[Unset, "ResultInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        next_result_uri = self.next_result_uri

        query_result = self.query_result

        result_kind: Union[Unset, str] = UNSET
        if not isinstance(self.result_kind, Unset):
            result_kind = self.result_kind.value

        result_type: Union[Unset, str] = UNSET
        if not isinstance(self.result_type, Unset):
            result_type = self.result_type.value

        results: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobID"] = job_id
        if next_result_uri is not UNSET:
            field_dict["nextResultUri"] = next_result_uri
        if query_result is not UNSET:
            field_dict["queryResult"] = query_result
        if result_kind is not UNSET:
            field_dict["resultKind"] = result_kind
        if result_type is not UNSET:
            field_dict["resultType"] = result_type
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.result_info import ResultInfo

        d = src_dict.copy()
        job_id = d.pop("jobID", UNSET)

        next_result_uri = d.pop("nextResultUri", UNSET)

        query_result = d.pop("queryResult", UNSET)

        _result_kind = d.pop("resultKind", UNSET)
        result_kind: Union[Unset, ResultKind]
        if isinstance(_result_kind, Unset):
            result_kind = UNSET
        else:
            result_kind = ResultKind(_result_kind)

        _result_type = d.pop("resultType", UNSET)
        result_type: Union[Unset, ResultType]
        if isinstance(_result_type, Unset):
            result_type = UNSET
        else:
            result_type = ResultType(_result_type)

        _results = d.pop("results", UNSET)
        results: Union[Unset, ResultInfo]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = ResultInfo.from_dict(_results)

        fetch_results_response_body = cls(
            job_id=job_id,
            next_result_uri=next_result_uri,
            query_result=query_result,
            result_kind=result_kind,
            result_type=result_type,
            results=results,
        )

        fetch_results_response_body.additional_properties = d
        return fetch_results_response_body

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
