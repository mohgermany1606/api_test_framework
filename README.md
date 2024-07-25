ApiTestFramework

This project is a Python-based test framework using the unittest module to test API endpoints. It specifically tests the browser support matrix for the autoident key in the API response.

Prerequisites

Python 3.x
requests library
pytest library
jsonschema library
Files

test_api.py: Contains the test cases for the API.
requirements.txt: Lists the dependencies required for the project.
Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/ApiTestFramework.git
cd ApiTestFramework
Create a virtual environment and activate it:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:
Copy code
pip install -r requirements.txt
Usage

To run the tests, execute the following command:

Copy code
python test_api.py
test_api.py

This script contains the ApiTestFramework class that includes methods for making GET, POST, PUT, and DELETE requests to the API. It also includes a test case to validate the autoident key's browser support matrix.

Class Methods
setUpClass(cls): Sets up the test case, including the base URL and a session.
tearDownClass(cls): Tears down the test case, closing the session.
get(self, url, params=None): Performs a GET request.
post(self, url, data=None, json=None): Performs a POST request.
put(self, url, data=None, json=None): Performs a PUT request.
delete(self, url): Performs a DELETE request.
test_autoident_browser_support(self): Test case to validate the autoident key's browser support matrix.
check_min_key_exists(self, browser_dict): Checks whether the 'min' key exists for every browser in the given dictionary.
Example Test Case
The test case test_autoident_browser_support checks if the autoident key exists and verifies that the min key is present for every browser in the browserSupportMatrix.

requirements.txt

This file contains the list of dependencies required for the project:

Copy code
requests
pytest
jsonschema
License

This project is licensed under the MIT License.

Feel free to contribute to this project by creating issues or submitting pull requests. If you encounter any issues, please report them in the issue tracker.

For any questions, please contact [your-email@example.com].





