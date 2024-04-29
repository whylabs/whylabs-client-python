# NamedMetricSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the metric. This should be a unique across the metrics for the dataset and consist of alphanumeric plus _ characters. | 
**label** | **str** | User-friendly label for the metric. | 
**column** | **str** | Entity column to extract the metric from | 
**builtin_metric** | **str** | WhyLabs built-in profile metric to use for this named metric. Note that other metrics may be available for this column as well, this is the one to be used in the named metric. Should match the values of the SimpleColumnMetric enum within the monitor config schema. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


