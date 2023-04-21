# EntitySchema

Entity schema for a dataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**{str: (ColumnSchema,)}**](ColumnSchema.md) | Column schema for a given column | 
**metadata** | [**SchemaMetadata**](SchemaMetadata.md) |  | [optional] 
**metrics** | [**{str: (MetricSchema,)}, none_type**](MetricSchema.md) | Schema for user-defined metrics (map of unique custom metric labels to their definitions) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


