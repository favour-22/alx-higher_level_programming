# 0x07. Python - Test-driven development
## Test-Driven Development (TDD), or Test-First Programming, involves writing automated tests to verify desired functionality before the code that implements this functionality is written. These tests will of course fail initially. The goal is then to quickly write minimalcode to make these tests pass.

### Command to test : python3 -m doctest -v name of python file(script.py)

* EXAMPLE
* """
    Sample test case
  """
def mul(a,b):
    >>> mul(3,4)
    12
    >>> mul(1,4)
    4
    return a * b
* Then run the code above to test.

