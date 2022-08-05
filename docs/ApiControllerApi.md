# openapi_client.ApiControllerApi

All URIs are relative to *http://poultryheatstress.co.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_livestock_list_api_response_using_get**](ApiControllerApi.md#get_livestock_list_api_response_using_get) | **GET** /api/livestockList | livestockList 요청
[**get_seamless_forecast_api_test_response_using_get**](ApiControllerApi.md#get_seamless_forecast_api_test_response_using_get) | **GET** /api/ShortTermLiveData | ShortTermLiveData 기상청 초단기실황 데이터 요청
[**get_seamless_forecast_api_test_response_using_get1**](ApiControllerApi.md#get_seamless_forecast_api_test_response_using_get1) | **GET** /api/seamlessForecast | SeamlessForecast 요청


# **get_livestock_list_api_response_using_get**
> LivestockApiResponseVO get_livestock_list_api_response_using_get(user_name)

livestockList 요청

livestock 축사데이터를 조회합니다

### Example


```python
import time
import openapi_client
from openapi_client.api import api_controller_api
from openapi_client.model.livestock_api_response_vo import LivestockApiResponseVO
from pprint import pprint
# Defining the host is optional and defaults to http://poultryheatstress.co.kr
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://poultryheatstress.co.kr"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_controller_api.ApiControllerApi(api_client)
    user_name = "userName_example" # str | 에스이랩

    # example passing only required values which don't have defaults set
    try:
        # livestockList 요청
        api_response = api_instance.get_livestock_list_api_response_using_get(user_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApiControllerApi->get_livestock_list_api_response_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| 에스이랩 |

### Return type

[**LivestockApiResponseVO**](LivestockApiResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 조회 성공! |  -  |
**400** | 잘못된 접근 |  -  |
**401** | 권한 없음 |  -  |
**403** | 허용되지 않은 요청 |  -  |
**404** | 찾을 수 없음 |  -  |
**500** | 서버 에러 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seamless_forecast_api_test_response_using_get**
> ShortTermLiveApiResponseVO get_seamless_forecast_api_test_response_using_get(base_time, end_date, latitude, longitude, start_date)

ShortTermLiveData 기상청 초단기실황 데이터 요청

초단기실황 데이터를 조회합니다(22년 2월 9일 - )

### Example


```python
import time
import openapi_client
from openapi_client.api import api_controller_api
from openapi_client.model.short_term_live_api_response_vo import ShortTermLiveApiResponseVO
from pprint import pprint
# Defining the host is optional and defaults to http://poultryheatstress.co.kr
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://poultryheatstress.co.kr"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_controller_api.ApiControllerApi(api_client)
    base_time = "baseTime_example" # str | 발표시각:0900
    end_date = "endDate_example" # str | 종료날짜:2022-02-10
    latitude = "latitude_example" # str | 위도:35.82053888888889
    longitude = "longitude_example" # str | 경도:127.14271111111111
    start_date = "startDate_example" # str | 시작날짜:2022-02-09

    # example passing only required values which don't have defaults set
    try:
        # ShortTermLiveData 기상청 초단기실황 데이터 요청
        api_response = api_instance.get_seamless_forecast_api_test_response_using_get(base_time, end_date, latitude, longitude, start_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApiControllerApi->get_seamless_forecast_api_test_response_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_time** | **str**| 발표시각:0900 |
 **end_date** | **str**| 종료날짜:2022-02-10 |
 **latitude** | **str**| 위도:35.82053888888889 |
 **longitude** | **str**| 경도:127.14271111111111 |
 **start_date** | **str**| 시작날짜:2022-02-09 |

### Return type

[**ShortTermLiveApiResponseVO**](ShortTermLiveApiResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 조회 성공! |  -  |
**400** | 잘못된 접근 |  -  |
**401** | 권한 없음 |  -  |
**403** | 허용되지 않은 요청 |  -  |
**404** | 찾을 수 없음 |  -  |
**500** | 서버 에러 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seamless_forecast_api_test_response_using_get1**
> SeamlessForecastApiResponseVO get_seamless_forecast_api_test_response_using_get1(end_date, latitude, longitude, start_date)

SeamlessForecast 요청

SeamlessForecast 자료를 조회합니다

### Example


```python
import time
import openapi_client
from openapi_client.api import api_controller_api
from openapi_client.model.seamless_forecast_api_response_vo import SeamlessForecastApiResponseVO
from pprint import pprint
# Defining the host is optional and defaults to http://poultryheatstress.co.kr
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://poultryheatstress.co.kr"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_controller_api.ApiControllerApi(api_client)
    end_date = "endDate_example" # str | 종료날짜:2022-01-31
    latitude = "latitude_example" # str | 위도:35.82053888888889
    longitude = "longitude_example" # str | 경도:127.14271111111111
    start_date = "startDate_example" # str | 시작날짜:2022-01-01

    # example passing only required values which don't have defaults set
    try:
        # SeamlessForecast 요청
        api_response = api_instance.get_seamless_forecast_api_test_response_using_get1(end_date, latitude, longitude, start_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApiControllerApi->get_seamless_forecast_api_test_response_using_get1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| 종료날짜:2022-01-31 |
 **latitude** | **str**| 위도:35.82053888888889 |
 **longitude** | **str**| 경도:127.14271111111111 |
 **start_date** | **str**| 시작날짜:2022-01-01 |

### Return type

[**SeamlessForecastApiResponseVO**](SeamlessForecastApiResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 조회 성공! |  -  |
**400** | 잘못된 접근 |  -  |
**401** | 권한 없음 |  -  |
**403** | 허용되지 않은 요청 |  -  |
**404** | 찾을 수 없음 |  -  |
**500** | 서버 에러 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

