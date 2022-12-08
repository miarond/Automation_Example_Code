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
Creating a callable function that will return specific values for each input() function prompt. This will be used when we test the interact() function.
"""
def fake_input(prompt):
    value_dict = {
        'Enter the number of the source timezone: ': '93',
        'Enter the number of the destination timezone: ': '180',
        'Enter the date/time stamp to convert (format: YYYY-MM-DD hh:mm:ss): ': '2022-11-01 10:00:00'
    }
    return value_dict[prompt]


"""
We are using the "requests_mock" package to override the actions of the "requests" package in tzconverter.py. To do this, we add the "@" decorator below which initiates this override. We then pass our "test_json" example API output to this overridden version of the requests package, so that it uses the fake response we provide, rather than making a live API call to the target URL.
"""
@requests_mock.Mocker(kw='mock')
def test_get_timezones(**kwargs):
    kwargs['mock'].get('https://timeapi.io/api/TimeZone/AvailableTimeZones', json=test_json)
    result = tzconverter.get_timezones()
    assert result == test_json


@requests_mock.Mocker(kw='mock')
def test_interact(monkeypatch, **kwargs):
    kwargs['mock'].get('https://timeapi.io/api/TimeZone/AvailableTimeZones', json=test_json)
    monkeypatch.setattr('builtins.input', fake_input)
    result_source, result_dest, result_time = tzconverter.interact()
    assert result_source == 'America/Chicago'
    assert result_dest == 'America/Phoenix'
    assert result_time == '2022-11-01 10:00:00'


def test_get_timezone_calculation():
        result = tzconverter.get_time_calculation(payload)
        assert result == response