# UserApiKey

Response when creating an API key successfully

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The key id. Can be used to identify keys for a given user | 
**org_id** | **str** | The organization that the key belongs to | 
**user_id** | **str** | The user that the key represents | 
**creation_time** | **str** | Creation time in human readable format | 
**key** | **str, none_type** | The full value of the key. This is not persisted in the system | [optional] 
**expiration_time** | **str, none_type** | Expiration time in human readable format | [optional] 
**scopes** | **[str], none_type** | Scope of the key | [optional] 
**alias** | **str, none_type** | Human-readable alias for the key | [optional] 
**revoked** | **bool, none_type** | Whether the key has been revoked | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


