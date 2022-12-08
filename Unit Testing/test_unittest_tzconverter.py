import unittest
from unittest.mock import patch
import json
import tzconverter
import requests_mock

# Load example JSON output from local test files into Python objects
with open('./tests/test_timezones_response.json') as f:
    test_json = json.load(f)
    f.close()

with open('./tests/test_get_time_calculation_payload.json') as p:
    payload = json.load(p)
    p.close()

with open('./tests/test_get_time_calculation_result.json') as r:
    response = json.load(r)
    r.close()

"""
Instantiate unittest TestCase class, then define test case functions
"""
class TestTzconverter(unittest.TestCase):
    """
    Here we're calling "get_timezones()" which makes an actual API call out to
    timeapi.io and gets a JSON response back. We will use the "requests_mock" package to "mock" this API call (which uses the Requests package), because we can't be sure that the API will always return the same data...or that the API call will actually work. The "requests_mock" package makes this process much easier, and we only need to use the @ decorator below to instantiate the Mocker class, along with a call to the "get" method of this new object. This get method call specifies the destination URL to we want to capture and override, and it allows us to pass in the test response data.
    """
    @requests_mock.Mocker(kw='mock') 
    def test_get_timezones(self, **kwargs):
        kwargs['mock'].get('https://timeapi.io/api/TimeZone/AvailableTimeZones', json=test_json)
        result = tzconverter.get_timezones()
        self.assertEqual(result, test_json)

    """
    Test the "interactive" capabilities of the script. We're using unittest's
    Patch decorator from the "mock" sub-package. This allows us to override
    the "input()" function and pass it specific values, rather than prompting
    the user on the CLI. We are also adding the @requests_mock decorator to override the API call to timeapi.io, because the "interact()" function in tzconverter.py also calls upon the "get_timezone()" function within the script.
    """
    @patch('builtins.input', side_effect=['93', '180', '2022-11-01 10:00:00'])
    @requests_mock.Mocker(kw='mock')
    def test_interactive(self, mock_inputs, **kwargs):
        kwargs['mock'].get('https://timeapi.io/api/TimeZone/AvailableTimeZones', json=test_json)
        result_source, result_dest, result_time = tzconverter.interact()
        self.assertEqual(result_source, 'America/Chicago')
        self.assertEqual(result_dest, 'America/Phoenix')
        self.assertEqual(result_time, '2022-11-01 10:00:00')

    
    """
    Here we're calling the "get_time_calculation()" function and passing it a pre-built example payload, then we're comparing the returned result to an example from our "tests" subdirectory. Again, this function is making an actual API call to timeapi.io and we're trusting that the returned data will be exactly as we predicted. We could mock this returned data but that would not validate that the actual API's calculation returns the expected value, so we're better off allowing this live API call to occur.
    """
    def test_get_timezone_calculation(self):
        result = tzconverter.get_time_calculation(payload)
        self.assertEqual(result, response)


if __name__ == '__main__':
    # We're setting "buffer=True" to prevent print() statements from being
    # printed to the CLI when we run this test script.
    unittest.main(buffer=True)