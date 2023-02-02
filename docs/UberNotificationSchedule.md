# UberNotificationSchedule

 Combination of all possible schedule types, a hacky workaround for bugs in generated clients that use polymorphic types. There are three types of schedules. Weekly, Daily, and Individual. You need to set the right fields for each one.  Weekly:     enabled, cadence=WEEKLY, dayOfWeek, local24HourOfDay, localMinuteOfHour, localTimezone      Daily:     enabled, cadence=DAILY, local24HourOfDay, localMinuteOfHour, localTimezone      Individual:     enabled, cadence=INDIVIDUAL 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**cadence** | [**NotificationSqsMessageCadence**](NotificationSqsMessageCadence.md) |  | 
**day_of_week** | [**NotificationSettingsDay**](NotificationSettingsDay.md) |  | [optional] 
**local24_hour_of_day** | **int, none_type** |  | [optional] 
**local_minute_of_hour** | **int, none_type** |  | [optional] 
**local_timezone** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


