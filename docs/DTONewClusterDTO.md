# DTONewClusterDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spark_version** | **str** |  | [optional] 
**aws_attributes** | [**DTOAwsAttributesDTO**](DTOAwsAttributesDTO.md) |  | [optional] 
**node_type_id** | **str** |  | [optional] 
**num_workers** | **int** |  | [optional] 
**auto_scale** | [**DTOAutoScaleDTO**](DTOAutoScaleDTO.md) |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**spark_conf** | **{str: (str,)}** |  | [optional] 
**driver_node_type_id** | **str** |  | [optional] 
**ssh_public_keys** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**custom_tags** | **{str: (str,)}** |  | [optional] 
**cluster_log_conf** | [**DTOClusterLogConfDTO**](DTOClusterLogConfDTO.md) |  | [optional] 
**spark_env_vars** | **{str: (str,)}** |  | [optional] 
**auto_termination_minutes** | **int** |  | [optional] 
**enable_elastic_disk** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


