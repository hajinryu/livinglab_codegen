# openapi_client.JupyterCallBackApiControllerApi

All URIs are relative to *http://poultryheatstress.co.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jupyter_log_using_get**](JupyterCallBackApiControllerApi.md#jupyter_log_using_get) | **GET** /api/jupyterCallBack | jupyterLog


# **jupyter_log_using_get**
> jupyter_log_using_get()

jupyterLog

### Example


```python
import time
import openapi_client
from openapi_client.api import jupyter_call_back_api_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://poultryheatstress.co.kr
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://poultryheatstress.co.kr"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jupyter_call_back_api_controller_api.JupyterCallBackApiControllerApi(api_client)
    broiler_id = "broilerId_example" # str | broilerId (optional)
    path = "path_example" # str | path (optional)
    state = "state_example" # str | state (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # jupyterLog
        api_instance.jupyter_log_using_get(broiler_id=broiler_id, path=path, state=state)
    except openapi_client.ApiException as e:
        print("Exception when calling JupyterCallBackApiControllerApi->jupyter_log_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broiler_id** | **str**| broilerId | [optional]
 **path** | **str**| path | [optional]
 **state** | **str**| state | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

