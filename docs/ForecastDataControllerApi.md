# openapi_client.ForecastDataControllerApi

All URIs are relative to *http://poultryheatstress.co.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_jupyter_notebook_using_post**](ForecastDataControllerApi.md#access_jupyter_notebook_using_post) | **POST** /api/forecast/mergence | accessJupyterNotebook


# **access_jupyter_notebook_using_post**
> bool access_jupyter_notebook_using_post()

accessJupyterNotebook

### Example


```python
import time
import openapi_client
from openapi_client.api import forecast_data_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://poultryheatstress.co.kr
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://poultryheatstress.co.kr"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = forecast_data_controller_api.ForecastDataControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # accessJupyterNotebook
        api_response = api_instance.access_jupyter_notebook_using_post()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ForecastDataControllerApi->access_jupyter_notebook_using_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

