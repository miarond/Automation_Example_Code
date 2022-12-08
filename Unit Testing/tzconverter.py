"""
Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Aron Donaldson <ardonald@cisco.com>"
__contributors__ = ""
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
import argparse
import sys

# Packages from PyPi
import requests

def interact():
    """
    Function to get interactive input from the user, if no CLI arguments are provided.

    returns: source (str), dest (str), time (str)
    """
    # Get list of timezones first, then print them with their index numbers
    timezones = get_timezones()
    # For each timezone in the List returned, print the index number and the timezone name
    for tz in timezones:
            print(f'{timezones.index(tz)}: {tz}')
    source = int(input('Enter the number of the source timezone: '))
    dest = int(input('Enter the number of the destination timezone: '))
    time = input('Enter the date/time stamp to convert (format: YYYY-MM-DD hh:mm:ss): ')
    # Use the provided index number to obtain the timezones' names, then return them
    return timezones[source], timezones[dest], time


def get_timezones():
    """
    Function to obtain a list of IANA registered timezones names, accepted by the API

    returns: timezones (list)
    """
    timezones = requests.get('https://timeapi.io/api/TimeZone/AvailableTimeZones', headers={'Content-Type': 'application/json'}).json()
    return timezones


def get_time_calculation(payload):
    """
    Function to calculate the requested time in the destination timezone.

    params: payload (dict) - contains POST method payload for the API call
    returns: result (dict) - JSON formatted response data
    """
    result = requests.post('https://timeapi.io/api/Conversion/ConvertTimeZone', headers={'Content-Type': 'application/json'}, json=payload).json()
    return result


def main(args):
    """
    Main function to control code flow within the script.  Obtains data from arguments, intiates functions to make API calls, and prints returned data.
    """
    # Check if user provided arguments. sys.argv returns a List object containing the name of the script (index 0) and any subsequent arguments given via the CLI command.
    if len(sys.argv) > 1:
        source = args.source
        dest = args.dest
        time = args.time
    else:
        source, dest, time = interact()
    # Create the POST method payload for the upcoming API call
    data_payload = {
            "fromTimeZone": source,
            "dateTime": time,
            "toTimeZone": dest,
            "dstAmbiguity": ""
        }
    result = get_time_calculation(data_payload)
    print(f'\nResults:\n{json.dumps(result, indent=4)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple script that converts time from one timezone to another.')
    parser.add_argument('-s', '--source', help='The source timezone name in IANA format.')
    parser.add_argument('-d', '--dest', help='The destination timezone name in IANA format.')
    parser.add_argument('-t', '--time', help='The date/time stamp you want to convert, in the format: YYYY-MM-DD hh:mm:ss')
    args = parser.parse_args()
    main(args)