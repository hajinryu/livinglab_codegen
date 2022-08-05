# openapi_client.NiceApiControllerApi

All URIs are relative to *http://poultryheatstress.co.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nice_token_using_post**](NiceApiControllerApi.md#get_nice_token_using_post) | **POST** /api/niceCryptoToken | getNiceToken


# **get_nice_token_using_post**
> str get_nice_token_using_post()

getNiceToken

### Example


```python
import time
import openapi_client
from openapi_client.api import nice_api_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://poultryheatstress.co.kr
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://poultryheatstress.co.kr"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nice_api_controller_api.NiceApiControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # getNiceToken
        api_response = api_instance.get_nice_token_using_post()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NiceApiControllerApi->get_nice_token_using_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

