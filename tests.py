"""Tests for AJAX exercise server."""


import json
import unittest

import server


class AjaxServerTestCase(unittest.TestCase):
    """Test Flask AJAX exercise server."""

    def test_fortune(self):
        """Test /fortune route."""

        client = server.app.test_client()
        response = client.get("/fortune")
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, server.FORTUNES)

    def test_weather_94110(self):
        """Test /weather with a good zipcode."""

        client = server.app.test_client()
        response = client.get("/weather.json?zipcode=94110")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data, {'forecast': 'Rainy, damp, and rich with hipsters.', 'temp': '60F'})

    def test_weather_missing_zip(self):
        """Test /weather with a zipcode that is missing in dict."""

        client = server.app.test_client()
        response = client.get("/weather.json?zipcode=94114")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data, {'forecast': 'Kind of boring.', 'temp': '68F'})

    def test_order_melons(self):
        """Test order form with good data."""

        client = server.app.test_client()
        response = client.post("/order-melons.json", data={'melon_type': 'Yummy', 'qty': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data, {'code': 'OK', 'msg': 'You have bought 1 Yummy melons'})

    def test_order_melons_too_many(self):
        """Test order form by ordering too many melons."""

        client = server.app.test_client()
        response = client.post("/order-melons.json", data={'melon_type': 'Yummy', 'qty': 11})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data, {'code': "ERROR", 'msg': "You can't buy more than 10 melons"})

    def test_order_melons_too_few(self):
        """Test order form by ordering too few melons."""

        client = server.app.test_client()
        response = client.post("/order-melons.json", data={'melon_type': 'Yummy', 'qty': -1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data, {'code': "ERROR", 'msg': "You want to buy fewer than 1 melons? Huh?"})


if __name__ == '__main__':
    unittest.main(verbosity=2)
