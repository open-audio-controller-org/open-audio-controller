# open-audio-controller

------------------------------------------------------------------------------------------------------
# coding standard

readable code over comments.

where necesary block comments in the form 
"""
    comment
"""

variable names to be relevant to their intended purpose.
variable names in the form: this_is_an_example
constant names in the form: THIS_IS_AN_EXAMPLE
private variables in the form: __this_is_an_example

function names to follow same convention as variables.

When defining lists or passing many parameters to functions,
place individual parameters on separate lines for readability and
in general try to adhere to Python's recommended maximum line length.
some_long_variable = ["One",
                      "Per",
                      "Line",
                      "Instead",
                      "of",
                      "Super",
                      "Long",
                      "List"]

All unused variables and all unnecesary logging to be removed **BEFORE** commiting to git unless specifically required.

Full code coverage tests to be added as soon as possible following function completion, all unreachable code must be removed.
Test files should be placed in the test directory and names should be suffixed with _test.py, running open_audio_controller_test.py will then automatically import and run all present tests.

------------------------------------------------------------------------------------------------------


