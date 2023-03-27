# ColumnSchema

Column schema for a given column

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifier** | **str, none_type** | We can classify these columns into various grouping. Currently we only support &#39;input&#39; and &#39;output&#39; | 
**data_type** | **str, none_type** | The data type of the columns. Setting this field affects the default grouping (i.e integral columns) | 
**discreteness** | **str, none_type** | Whether a column should be discrete or continuous. Changing this column will change the default grouping (discrete columns vs. continuous columns | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


