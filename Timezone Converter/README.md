# Timezone Converter Script

This script demonstrates basic usage of an Open API via a Python script.  The script accepts
CLI arguments for source and destination timezone, and the target date/time to convert to 
the destination timezone.

The script will also work interactively, allowing you to request a list of valid timezones
and specify the necessary information through interactive prompts.

This script utilizes the free API from Time API:

https://timeapi.io

https://timeapi.io/swagger/index.html

## Usage

If you run the script without any command line options (`python3 tzconverter.py`, Windows users: `py tzconverter.py`), it will enter an interactive mode where you are prompted for the necessary options via the command line.  A list of valid IANA registered timezone names will be printed out along with index numbers.  You will be prompted to provide the index number of the source and destination timezones, as well as the date/time stamp you would like to convert.

You can also provide these arguments via command line options.  To view the available command line options and a description of their usage by running the command: `python3 tzconverter.py --help`.  The output will look like this:

```bash
usage: tzconverter.py [-h] [-s SOURCE] [-d DEST] [-t TIME]

A simple script that converts time from one timezone to another.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        The source timezone name in IANA format.
  -d DEST, --dest DEST  The destination timezone name in IANA format.
  -t TIME, --time TIME  The date/time stamp you want to convert, in the format: YYYY-MM-DD hh:mm:ss
```

* `-s` or `--source`
    * The source timezone that you want to convert ***from***.  This timezone name must be expressed using a valid IANA registered format.
* `-d` or `--dest`
    * The destination timezone that you want to convert ***to***.  This timezone name must be expressed using a valid IANA registered format.
* `-t` or `--time`
    * The date/time stamp that you want to convert from source timezone to destination timezone.  This date/time stamp must be in the format: YYYY-MM-DD hh:mm:ss

## Package Requirements

This script requires the installation of external Python package(s) from the Python Package
Index (https://pypi.org).  To install those required packages, run this command (or similar):

```
pip install -r requirements.txt
```