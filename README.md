# open-audio-controller

------------------------------------------------------------------------------------------------------
# Coding Standard

Readable code should be prioritised over comments.  

Where necesary block comments in the form:  
![Block comment image](/images/example_comment.jpg)  
  
Variable names to be relevant to their intended purpose and named in the form:  
![Image variables in the form this_is_an_example_variable, __this_is_an_example_private_variable, THIS_IS_AN_EXAMPLE_CONSTANT](/images/example_variables.jpg)  

function names to follow same convention as variables:  
![Image of a function named in the format example_function with a linebreak following each parameters comma](/images/example_function.jpg)  

When defining lists or passing many parameters to functions,  
place individual parameters on separate lines for readability and  
in general try to adhere to Python's recommended maximum line length.  

Lists should be formatted as shown below:  
![Image of list with a linebreak following each items comma](/images/example_list.jpg)  

Console output should be performed through the logging python package as opposed to print(x).  
All unused variables and all unnecesary logging to be removed **BEFORE** commiting to git unless specifically required.  

Full code coverage tests to be added as soon as possible following function completion, all unreachable code must be removed. For proper format see tests\test_example_name.py  
Test files should be placed in the test directory and names should be preffixed with test_ as shown here:  
![Image of two files named test_valid.py and invalid_test.py](/images/example_test_file.jpg)  

Running open_audio_controller_test.py will automatically import and run all tests in the test directory providing code coverage at the bottom:  
![Image of a make test run with code coverage shown at the bottom](/images/example_make_test.jpg)  

------------------------------------------------------------------------------------------------------


