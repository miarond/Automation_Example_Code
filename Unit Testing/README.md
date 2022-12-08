# Unit Testing Examples

This directory contains example Unit Testing scripts that utilize Python's built-in `unittest` framework, and the more user friendly `pytest` package available from [PyPi](https://pypi.org/project/pytest/).

Unit Testing is a fundamental skill in software development.  The concept of Test-Driven Development revolves around starting a software development project by first building all of the "tests" that the properly written, completed software application should pass.  Some may consider this practice "putting the cart before the horse", but in the world of software development this truly makes sense.  You design your tests first to govern what the application should and should not do, then you write the application to pass those tests.

In these examples we have developed Unit Tests that test the functionality of the Timezone Converter script, which exists in the "Timezone Converter" directory in this repository.

## Initial setup

These example scripts make use of external Python packages that must be downloaded from PyPi.org and installed using the `pip` command.  To install these dependencies, run the following command (optionally after you've set up and activated a Python Virtual Environment):

```bash
pip install -r requirements.txt
```

## Running `test_unittest_tzconverter.py`

To run the `test_unittest_tzconverter.py` script, execute the following command:

```bash
python3 test_unittest_tzconverter.py`
```

Unittest is a built-in Python package that comes preinstalled with Python 3.  This script also uses the `requests-mock` package, which must be installed from PyPi.org.  Running this script will cause the individual unit tests to be auto-discovered and run in sequence, and the output on your command line should look similar to this:

```bash
bash % python3 test_unittest_tzconverter.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.705s

OK
```

## Running `test_pytest_tzconverter.py`

To run the `test_pytest_tzconverter.py` script, simply execute the following command:

```bash
pytest
```

Pytest will auto-discover any scripts whose filenames start with `test_` or end with `_test.py`.  It will then run those scripts, auto-discover the unit test functions contained in them, and display the results on your command line, similar to this:

```bash
bash % pytest
========================== test session starts ===============================
platform darwin -- Python 3.9.12, pytest-7.2.0, pluggy-1.0.0
rootdir: ~/Automation_Example_Code/Unit Testing
plugins: requests-mock-1.10.0
collected 6 items

test_pytest_tzconverter.py ...                                          [ 50%]
test_unittest_tzconverter.py ...                                        [100%]

=========================== 6 passed in 0.84s ================================
```

Note that `pytest` will also auto-discover the `unittest` script and run it as well, because `pytest` is compatible with `unittest` scripts.

## References

* `unittest` documentation: 
    * https://docs.python.org/3/library/unittest.html
* `pytest` documentation: 
    * https://docs.pytest.org/en/latest/
* `requests-mock` documentation:
    * https://requests-mock.readthedocs.io/en/latest/
