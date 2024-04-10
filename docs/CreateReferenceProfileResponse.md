# CreateReferenceProfileResponse

Response payload for creating a reference profile.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID that identifies the reference profile | 
**alias** | **str** | A human readable name | 
**dataset_id** | **str** | The dataset ID for the upload | 
**segments** | **[str]** | The segments corresponding to the upload URLs | 
**upload_urls** | **[str]** | The URL list to upload the dataset profiles to | 
**upload_timestamp** | **int** | The time when the upload was completed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


