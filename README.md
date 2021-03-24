# open-audio-controller
 
------------------------------------------------------------------------------------------------------
# Coding Standard
 
All comments to be in the form of block comments as seen here:  
![Block comment image](/images/example_comment.jpg)  
  
Variable names to be relevant to their intended purpose and named in the form:  
![Image variables in the form this_is_an_example_variable, __this_is_an_example_private_variable, THIS_IS_AN_EXAMPLE_CONSTANT](/images/example_variables.jpg)  
 
Function names to follow same convention as variables. Block comments making up a Docstring must be placed on the first line of the function. 
Every parameter must be accompanied an expected type in the form \<Param Name\>:\<Expected type\>. 
Following the parameter declarations we use function annotation, ->, to show what our return type will be:  
![Image of a function named in the format example_function with a line break following each parameters comma](/images/example_function.jpg)  
 
When defining lists or passing many parameters to functions, 
place individual parameters on separate lines for readability and 
in general try to adhere to Python's recommended maximum line length:  
![Image of list with a line break following each items comma](/images/example_list.jpg)  
 
Console output should be performed through the logging python package as opposed to using print:  
![Image of a logging example which includes logging.info and logging.basicConfig which allows for info to be displayed rather than simply warnings](/images/example_logging_file.jpg)  
![Image of console output from the above file showing INFO and ERROR output along with timestamps](/images/example_logging_console.jpg)   
If DEBUG was set to False, the first INFO message would not be displayed as the minimum logging level would be WARNING.  
 
All unused variables and all unnecessary logging to be removed **BEFORE** commiting to git unless specifically required.  

------------------------------------------------------------------------------------------------------
# How To Contribute
 
Full code coverage tests to be added as soon as possible following function completion, all unreachable code must be removed. For proper format see tests\test_example_name.py  
Test files should be placed in the test directory and names should be prefixed with "test_" as shown here:  
![Image of two files named test_valid.py and invalid_test.py](/images/example_test_file.jpg)  

Running the command 'make test' will automatically import and run all tests in the test directory providing code coverage at the bottom:  
![Image of a make test run with code coverage shown at the bottom](/images/example_make_test.jpg)  

In order to add python packages, firstly the package must be verified to be open source, secondly the package should be well maintained in order to avoid compatibility issues, and finally the package name must be formatted as shown. Adding new python packages should be done by appending a new line to the requirements.txt and should contain the package name as it appears in the Python Package Index, a version number should also be specified formatting the line as \<Package Name\>==\<Version Number\>, eg. to add the pyaudio package; PyAudio==0.2.11.
 
In the case of additional linux packages being required we follow the same open source and maintenance guidelines as our python packages but rather than add them to the requirements.txt we append the package name to line 3 of the Dockerfile:  
![Image of dockerfile with green box surrounding line 3](/images/example_linux.jpg)  
Alter lines 1,2,4,+ at own risk.  
 
Full documentation is required for all functionality, this is both in the form of the docstring within each function as well as an example_name.txt file in the docs folder:  
![Image of function docstring](/images/example_docstring.jpg)  
![Image of documentation template example](/images/example_documentation.jpg)  
The file example.py will have a corresponding example_doc.txt in the documents folder.  

------------------------------------------------------------------------------------------------------