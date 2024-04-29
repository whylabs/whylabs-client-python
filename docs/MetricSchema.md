# MetricSchema

Schema for user-defined metrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | User-friendly label for the metric. | 
**column** | **str** | Entity column to extract the metric from | 
**default_metric** | **str** | whylogs metric to extract when this schema is applied. Should match the values of the SimpleColumnMetric enum within the monitor config schema. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


