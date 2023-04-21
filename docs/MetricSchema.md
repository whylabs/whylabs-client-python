# MetricSchema

Schema for user-defined metrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | User-friendly label for the metric. This should be a unique for the entity. | 
**column** | **str** | Entity column to extract the metric from | 
**default_metric** | **str** | whylogs metric to extract. Note that other metrics may be available for this column as well, this is the one to be used by default. Should match the values of the SimpleColumnMetric enum within the monitor config schema. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


