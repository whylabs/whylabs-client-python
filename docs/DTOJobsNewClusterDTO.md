# DTOJobsNewClusterDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** |  | [optional] 
**runtime_engine** | **str** |  | [optional] 
**num_workers** | **int** |  | [optional] 
**auto_scale** | [**DTOClustersAutoScaleDTO**](DTOClustersAutoScaleDTO.md) |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**spark_version** | **str** |  | [optional] 
**spark_conf** | **{str: (str,)}** |  | [optional] 
**aws_attributes** | [**DTOClustersAwsAttributesDTO**](DTOClustersAwsAttributesDTO.md) |  | [optional] 
**node_type_id** | **str** |  | [optional] 
**driver_node_type_id** | **str** |  | [optional] 
**ssh_public_keys** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**custom_tags** | **{str: (str,)}** |  | [optional] 
**cluster_log_conf** | [**DTOClustersClusterLogConfDTO**](DTOClustersClusterLogConfDTO.md) |  | [optional] 
**init_scripts** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**spark_env_vars** | **{str: (str,)}** |  | [optional] 
**enable_elastic_disk** | **bool** |  | [optional] 
**instance_pool_id** | **str** |  | [optional] 
**data_security_mode** | [**DTOJobsDataSecurityModeDTO**](DTOJobsDataSecurityModeDTO.md) |  | [optional] 
**auto_termination_minutes** | **int** |  | [optional] 
**artifact_paths** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


