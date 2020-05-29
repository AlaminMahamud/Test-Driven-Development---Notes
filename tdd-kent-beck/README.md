# Test Driven Development - Kent Beck

## Table of Contents

- Money Example


## Money Example

### Objectives

- Multi Currency Support for existing Dollar based Payment System

### Workflow

- Quickly add a test
- Run all tests  and see the new one  fail
- Make a Little change
- Run all tests and see them all succeed
- Refactor to remove duplication
 
### Problem

- Report Format

![](assets/report-format.png)
- to make a multi currency report we need to add currencies
![](assets/add-currencies.png)
- also specify exchange rates
![](assets/exchange-reports.png)

```
$5 + 10CHF = $10 if rate is 2:1
$5 * 2 = $10
```

```python
# $5 * 2 = $10
def test_multiply_dollars():
    dollar = Dollar(5)
    dollar.times(2)
    assert dollar.amount == 10
```

^ Problems?

- no Dollar Class
- no times method
- no amount attribute
- integer for Currency

```
Traceback (most recent call last):
  File "test.py", line 6, in <module>
    test_multiply_dollars()
  File "test.py", line 2, in test_multiply_dollars
    dollar = Dollar(5)
NameError: global name 'Dollar' is not defined
```

Let's solve one by one

- first lets create a Dollar Class

```python
class Dollar:
    pass
```

- then another error pops up

```
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    test_multiply_dollars()
  File "test.py", line 5, in test_multiply_dollars
    dollar = Dollar(5)
TypeError: this constructor takes no arguments
```

- lets create constructor with arguments

```python
class Dollar:
    def __init__(self, amount):
        pass
```

- next error about times method

```
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    test_multiply_dollars()
  File "test.py", line 6, in test_multiply_dollars
    dollar.times(2)
AttributeError: Dollar instance has no attribute 'times'

```

- added `times` method

```python
class Dollar:
    def __init__(self, amount):
        pass

    def times(self, multiplier):
        pass
```

- next error - no amount field

```
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    test_multiply_dollars()
  File "test.py", line 7, in test_multiply_dollars
    assert dollar.amount == 10
AttributeError: Dollar instance has no attribute 'amount'
```

- adding amount field

```python
class Dollar:
    def __init__(self, amount):
        self.amount = None

    def times(self, multiplier):
        pass
```

- then we are getting assertion error
```
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    test_multiply_dollars()
  File "test.py", line 7, in test_multiply_dollars
    assert dollar.amount == 10
AssertionError
```
- fixing the logic just enough to pass the test

```python
class Dollar:
    def __init__(self, amount):
        self.amount = None

    def times(self, multiplier):
        self.amount = 5 * 2
```

- and in the end it passed

- now eliminating duplication

> Depenedecy is a key problem, the symptom is duplication

^ Objects are excellent for abstracting away the duplication of logic.

By eliminating dupliation before we go on to the next test, we maximize our chance of being able to get the next test running with one and only one change

```python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount = self.amount * multiplier
```

![](assets/9f184447.png)

Our current workflow

- made a todo list
- snippet explaining our course of action input/output
- made the test compile with stubs
- made the test run by dummy code (horrible sins)
- gradually generalizing the working code replacing consts with vars
- rather than addressing all, tackling them one by one

---

### Possibilities

*Method*: Team needs to have a consistent experience growing the design of the system, little by little so the mechanics of the transformation are well practiced

*Motive* - business importance of  the feature and have the courage to do seemingly impossible task

*Opportunity* - combination of comprehensive, confidence-generated tests, well-factored program makes possible to isolate design decision which helps the team to identify the few potential sources of errors 
 
### Thoughts
- How each test  cover a small increment of functionality
- How small and ugly the changes can be to make the new tests run
- How often the tests are run
- How many teensy-weensy steps make up the refactorings
