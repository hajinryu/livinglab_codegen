"""
    Api Documentation

    Api Documentation  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.api_controller_api import ApiControllerApi  # noqa: E501


class TestApiControllerApi(unittest.TestCase):
    """ApiControllerApi unit test stubs"""

    def setUp(self):
        self.api = ApiControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_livestock_list_api_response_using_get(self):
        """Test case for get_livestock_list_api_response_using_get

        livestockList 요청  # noqa: E501
        """
        pass

    def test_get_seamless_forecast_api_test_response_using_get(self):
        """Test case for get_seamless_forecast_api_test_response_using_get

        ShortTermLiveData 기상청 초단기실황 데이터 요청  # noqa: E501
        """
        pass

    def test_get_seamless_forecast_api_test_response_using_get1(self):
        """Test case for get_seamless_forecast_api_test_response_using_get1

        SeamlessForecast 요청  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
