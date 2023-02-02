# RequestMonitorConfig

A configuration for the whylabs monitor for a single model or segment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**num_std_dev** | **float, none_type** |  | [optional] 
**reference** | [**MonitorRequestReference**](MonitorRequestReference.md) |  | [optional] 
**missing_recent_data** | [**MissingRecentDataRequestConfig**](MissingRecentDataRequestConfig.md) |  | [optional] 
**missing_recent_profiles** | [**MissingRecentProfilesRequestConfig**](MissingRecentProfilesRequestConfig.md) |  | [optional] 
**distribution** | [**DistributionMonitorRequestConfig**](DistributionMonitorRequestConfig.md) |  | [optional] 
**missing_values** | [**MissingValuesMonitorRequestConfig**](MissingValuesMonitorRequestConfig.md) |  | [optional] 
**unique_values** | [**UniqueValuesMonitorRequestConfig**](UniqueValuesMonitorRequestConfig.md) |  | [optional] 
**datatype** | [**DatatypeMonitorRequestConfig**](DatatypeMonitorRequestConfig.md) |  | [optional] 
**seasonal_arima** | [**SeasonalARIMARequestConfig**](SeasonalARIMARequestConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


