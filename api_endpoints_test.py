
## Imports - enables automated testing and interaction with the main code.
import unittest
from app import app

class TestApiEndpoints(unittest.TestCase): ##Inherits from unittest. 

    def setUp(self): ## Called before each test method is executed.

        self.app = app.test_client()
        self.app.testing = True ## Enables testing mode for the Flask application.
    
    def test_low_stock_levels(self):

        # Test the low stock levels endpoint
        response = self.app.get("api/low_stock_levels")
        # Check the status code of the response is 200.
        self.assertEqual(response.status_code, 200) 

        # Test if the response is in JSON format
        self.assertTrue(response.is_json)

        # Test if the response contains the expected keys
        self.assertTrue("products" in response.json)
        self.assertTrue("quantities" in response.json)

        # Test if the products response is a list
        self.assertIsInstance(response.json["products"], list)

        # Test to see if quantities response is an integer
        self.assertTrue(all(isinstance(x, int) for x in response.json["quantities"]))

if __name__ == '__main__':
    unittest.main()