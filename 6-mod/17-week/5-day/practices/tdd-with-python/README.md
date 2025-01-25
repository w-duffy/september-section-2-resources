# TDD With pytest

In this project, you and your pair will alternate writing unit tests for each
requirement with **pytest**, making each test pass before moving on to the next
feature. This is one of the ways that pair programming is done on professional
software teams.

* Person Purple and Person Tree talk about the feature they're going to write.
* Person Purple writes a test and runs the tests. If the test fails, then the
  process goes on. Otherwise, Person Purple keeps writing tests until one fails.
* Person Tree writes code to make the failing test pass without making any of
  the other tests break.
* Person Purple and Person Tree talk about the feature they're going to write.
* Person Tree writes a test and runs the tests. If the test fails, then the
  process goes on. Otherwise, Person Purple keeps writing tests until one fails.
* Person Purple writes code to make the failing test pass without making any of
  the other tests break.
* Repeat until all the features are done.

This project will have you write a Roman numeral parser, something that
translates Roman numerals ("MCM") to their correspoinding Hindi numeral based
value (1900).

## Rules of Roman numerals

There are only seven base numerals which can be used to create any numeral
sequence or number representation:

| Number | Roman numeral |
|--------|---------------|
| 1      | I             |
| 5      | V             |
| 10     | X             |
| 50     | L             |
| 100    | C             |
| 500    | D             |
| 1000   | M             |

Utilising the base numerals, there are also six special combinations which act
as shortcuts to represent numerals which would otherwise require four or five
individual numerals:

| Number | Roman numeral |
|--------|---------------|
| 4      | IV            |
| 9      | IX            |
| 40     | XL            |
| 90     | XC            |
| 400    | CD            |
| 900    | CM            |

The Roman numeral "MCMXCIII" converts to a Hindi-numeral number like this:

```
MCMXCIXIII
  = M + CM + XC + I + I + I
  = 1000 + 900 + 90 + 1 + 1 + 1
  = 1993
```

Here's another example.

```
MDCXVI
   = M + D + C + X + V + I
   = 1000 + 500 + 100 + 10 + 5 + 1
   = 1661
```

## Getting started

Create a new project directory. In there, initialize a new python project and
install **pytest** all at the same time.

```shell
pipenv install pytest --python 3.9.6
```

Activate your virtual environment.

```shell
pipenv shell
```

Make sure you can run **pytest**.

```shell
pytest
```

You should see something like the following.

```
============== test session starts ==============
platform linux -- Python 3.9.6, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /path/to/your/project
collected 0 items

============= no tests ran in 0.04s =============
```

Open Visual Studio Code from the project directory.

## Test 1

In your pair, decide who will write the test and who will write the code.

### The Test Writer

The Test Writer will now create a directory named **test** in the project
directory . Then, create a file named `__init__.py` in the **test** directory
which will allow **pytest** to load your tests as a module. Then, add a file
named `test_roman_numerals_unittest.py` in the **test** directory. In the new
file, add the following imports:

* **unittest**, and
* from **app.roman_numerals**, import the `parse` function

Then, create a _test case_ class named `TestRomanNumerals`. Declare one method
named `test_i`. In the test method, assert that calling the imported `parse`
method with the argument "I" returns the value 1. The test should look like
this.

```python
class TestRomanNumerals(unittest.TestCase):
    def test_i(self):
        value = parse("I")

        self.assertEqual(value, 1)
```

**Note:** If you plan on running **pytest** from inside the Visual Studio Code
Terminal, make sure that the shell in the Terminal is also properly started.
If you don't see the directory prefix in the prompt, you need to activate the
virtual environment in your Terminal by typing `pipenv shell`.

Run the tests to make sure you have a failing unit test. You run the tests by
just typing `pytest` on the command line. You are only allowed to write code
when you have a failing unit test. Your unit test should fail with a message
like

```
ModuleNotFoundError: No module named 'app'
```

### The Code Writer

The Code Writer will now create a directory named **app** in the project's root
directory as a sibling directory of **test**. Create an `__init__.py` file in
the **app** directory. (Remember, that makes the directory a package. This way,
your tests can import from there.)

Run **pytest** to see what happens. At this point, you should see an error
message that contains

```
ImportError: cannot import name 'parse' from 'app.roman_numerals'
```

That's because the `roman_numerals.py` file is empty and has no `parse` function
in it. Declare the `parse` function and implement it in the _simplest way
possible to make the test pass_. (Yes, that means, just return the value 1.)

Run **pytest** to make sure that the test passes.

## Test 2

Now, the person that was the Code Writer becomes the Test Writer, and the person
that was the Test Writer becomes the code writer.

### The Test Writer

Now, in `test_roman_numerals_unittest.py`, write a new method on the
`TestRomanNumerals` class named `test_ii`. Have it call the `parse` method with
the string "II" and assert that the result equals 2.

Run **pytest** to make sure that you have an unmet expectation.

### The Code Writer

In `roman_numerals.py`, implement the functionality in the `parse` method that
will the test pass. Do this in the _simplest possible manner_. (Yes, that
means just write an `if` statement so that it returns the proper value given
the two inputs you know about: "I" and "II".)

## Tests 3 through 8

Just keep switching back and forth writing tests for the following input
strings, their associated outputs, and the test name for the test.

**Note:** Do not add all the tests at once and make them pass. This is a
_process_. One failing test allows the other person to write code. Many failing
tests is _wrong_.

| Input  | Output | Test name   |
|--------|--------|-------------|
| "III"  | 3      | `test_iii`  |
| "IV"   | 4      | `test_iv`   |
| "V"    | 5      | `test_v`    |
| "VI    | 6      | `test_vi`   |
| "VII"  | 7      | `test_vii`  |
| "VIII" | 8      | `test_viii` |

Keep doing the _simplest thing possible_, which may feel really stupid at first,
but the next step will show you the power of having the tests in place. And,
when you have the instructions _simplest thing possible_, that means just
extending your `if` statement with `elif` statements.

## Refactor the parse method

Now, as a team, figure out how to refactor the code to make it pass for the
values "I" through "VIII". This means, change the code from one big `if`-`elif`
thing into a tidy Roman numeral parser for those values. You get to use loops,
now. `:-D`

Don't forget whose turn it is to next write the tests.

## Test 9

It's now time to switch away from **unittest** and use **pytest** as the testing
framework.

### The Test Writer

Now, try something different, using **pytest**. Create a new file named
`test_roman_numerals_pytest.py`. In there, do the following things.

* Import the `parse` the same way you did in `test_roman_numerals_unittest.py`.
* Create a new function named "test_roman_numeral_parser" that has no
  parameters.
* In `test_roman_numeral_parser`, create a test for the input "IX" and the
  result 9. Refer to _Cookbook For Testing_ to remember how to write assertions
  with **pytest**.

### The Code Writer

Make the test pass in the _simplest_ way possible.

## Test 10

You will now leverage the awesomeness of **pytest** and it ability to
parameterize tests.

### The Test Writer

Refer to _Cookbook for Testing_ to see how to parameterize a test. Parameterize
the existing test in `test_roman_numerals_pytest.py` only for the input "IX" and
the result 9. Run the tests to make sure you parameterized it correctly. Now,
add a new tuple to the arguments list for the input "X" and the result 10. Run
the tests to make sure that one fails.

### The Code Writer

Make the test pass in the simplest way you know how.

## Refactor

Now, as a team, figure out the best way to refactor the `parse` method to
account for the new inputs "IX" and "X".

## The rest of the exercise

Use the following values as test values for the rest of the exercise. This way,
you don't have to do _all_ of the numbers between 0 and 3000. With these new
inputs, the "simplest way possible" should mean that it would correctly parse
any number _less_ than the given input. Use either of the test files to add new
test cases, either as a new method on the `TestRomanNumerals` class, as a new
input/expected value in the parameterized function, or as a new function in the
`test_roman_numerals_pytest.py` file.

| Input       | Output |
|-------------|--------|
| "XI"        | 11     |
| "XIV"       | 14     |
| "XIX"       | 19     |
| "XX"        | 20     |
| "XXXIV"     | 34     |
| "XLI"       | 41     |
| "L"         | 50     |
| "XCIX"      | 99     |
| "C"         | 100    |
| "CCCXXXIII" | 333    |
| "DLV"       | 555    |
| "CDXLIX"    | 449    |
| "MCMLXXII"  | 1972   |
