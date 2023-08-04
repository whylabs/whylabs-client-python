# DTOJobsJobSettingsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_cluster_id** | **str** |  | [optional] 
**new_cluster** | [**DTOJobsNewClusterDTO**](DTOJobsNewClusterDTO.md) |  | [optional] 
**notebook_task** | [**DTOJobsNotebookTaskDTO**](DTOJobsNotebookTaskDTO.md) |  | [optional] 
**spark_jar_task** | [**DTOJobsSparkJarTaskDTO**](DTOJobsSparkJarTaskDTO.md) |  | [optional] 
**spark_python_task** | [**DTOJobsSparkPythonTaskDTO**](DTOJobsSparkPythonTaskDTO.md) |  | [optional] 
**spark_submit_task** | [**DTOJobsSparkSubmitTaskDTO**](DTOJobsSparkSubmitTaskDTO.md) |  | [optional] 
**name** | **str** |  | [optional] 
**libraries** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**email_notifications** | [**DTOJobsJobEmailNotificationsDTO**](DTOJobsJobEmailNotificationsDTO.md) |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 
**max_retries** | **int** |  | [optional] 
**min_retry_interval_millis** | **int** |  | [optional] 
**retry_on_timeout** | **bool** |  | [optional] 
**schedule** | [**DTOJobsCronScheduleDTO**](DTOJobsCronScheduleDTO.md) |  | [optional] 
**max_concurrent_runs** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


