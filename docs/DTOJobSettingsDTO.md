# DTOJobSettingsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**new_cluster** | [**DTONewClusterDTO**](DTONewClusterDTO.md) |  | [optional] 
**existing_cluster_id** | **str** |  | [optional] 
**email_notifications** | [**DTOJobEmailNotificationsDTO**](DTOJobEmailNotificationsDTO.md) |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 
**schedule** | [**DTOCronScheduleDTO**](DTOCronScheduleDTO.md) |  | [optional] 
**notebook_task** | [**DTONotebookTaskDTO**](DTONotebookTaskDTO.md) |  | [optional] 
**spark_jar_task** | [**DTOSparkJarTaskDTO**](DTOSparkJarTaskDTO.md) |  | [optional] 
**spark_python_task** | [**DTOSparkPythonTaskDTO**](DTOSparkPythonTaskDTO.md) |  | [optional] 
**spark_submit_task** | [**DTOSparkSubmitTaskDTO**](DTOSparkSubmitTaskDTO.md) |  | [optional] 
**retry_on_timeout** | **bool** |  | [optional] 
**max_retries** | **int** |  | [optional] 
**min_retry_interval_millis** | **int** |  | [optional] 
**libraries** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**max_concurrent_runs** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


