import requests
import unittest

class ApiTestFramework(unittest.TestCase):
    BASE_URL = "https://api.test.idnow.de/api/v1/ihrebank"

    @classmethod
    def setUpClass(cls):
        """Setup for the test cases, including base URL."""
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls):
        """Teardown for the test cases."""
        cls.session.close()

    def get(self, url, params=None):
        """Perform a GET request."""
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, url, data=None, json=None):
        """Perform a POST request."""
        response = self.session.post(url, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def put(self, url, data=None, json=None):
        """Perform a PUT request."""
        response = self.session.put(url, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def delete(self, url):
        """Perform a DELETE request."""
        response = self.session.delete(url)
        response.raise_for_status()
        return response.json()

    def test_autoident_browser_support(self):
        """Test to validate the autoident key's browser support matrix."""
        response = self.get(self.BASE_URL)

        autoident = response.get('settings', {}).get('idnow', {}).get('autoident', {})
        self.assertIsNotNone(autoident, "autoident key is missing")
        if not autoident:
            self.fail("The 'autoident' key is missing or empty in the response.")

        browser_support_matrix = autoident.get('web', {}).get('browserSupportMatrix', {})
        self.assertIsNotNone(browser_support_matrix, "browserSupportMatrix key is missing")
        print(type(browser_support_matrix))
        if self.check_min_key_exists(browser_support_matrix):
            print("'min' key exists for every browser.")
        else:
            print("'min' key does not exist for every browser.")

        
    def check_min_key_exists(self, browser_dict):
        def check_min_in_nested_dict(d):
            if isinstance(d, dict):
                for key, value in d.items():
                    if isinstance(value, dict):
                        # Check if 'min' key exists at the current level
                        if 'min' in value:
                            continue
                        # Recursively check deeper levels
                        else:
                            if not check_min_in_nested_dict(value):
                                return False
            return True

        # Start the check from the top level of the browser dictionary
        return check_min_in_nested_dict(browser_dict)       

if __name__ == "__main__":
    unittest.main()
