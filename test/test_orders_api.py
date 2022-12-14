"""
    SeadataNet API

    A detailed description of the operation.  # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Contact: info@maris.nl
    Generated by: https://openapi-generator.tech
"""


import unittest

import cdi_sdn_py
from cdi_sdn_py.api.orders_api import OrdersApi  # noqa: E501


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self):
        self.api = OrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_order_download_csv_order_number_restriction_get(self):
        """Test case for order_download_csv_order_number_restriction_get

        Download metadata CSV for this order  # noqa: E501
        """
        pass

    def test_order_order_number_get(self):
        """Test case for order_order_number_get

        Find order by Ordernumber  # noqa: E501
        """
        pass

    def test_order_query_post(self):
        """Test case for order_query_post

        Make an order by query  # noqa: E501
        """
        pass

    def test_orderlist_get(self):
        """Test case for orderlist_get

        Show all your relevant orders from 30 days or less  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
