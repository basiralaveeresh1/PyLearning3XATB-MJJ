# Python 3x Learning - ATB
https://sdet.live/python0x

Below are the key topics to learn in Python, organized as bullet points for easy reference:

## Python Basics

1. Introduction to Python 
2. Installation and Setup 
3. Running Python Programs 
4. Python Syntax 
5. Variables and Data Types 
6. Basic Operators 
7. Control Flow 
8. If Statements 
9. Loops (For, While)
10. Functions

## Defining Functions
1. Function Arguments
2. Return Statement
3. Lambda Functions
4. Map, Filter, and Reduce Functions
5. Recursion
6. Strings 
7. String Manipulation 
8. String Methods
9. Formatting Strings
10. Regular Expressions
11. Data Structures

## Lists
1. List Methods
2. List Comprehensions
## Tuples
1. Dictionaries
2. Dictionary Methods
## Sets
1. Set Methods
2. Modules and Packages

## Importing Modules
* Standard Library Modules
* Creating and Using Packages
* File Handling

## Reading and Writing Files
* Working with CSV and JSON Files
* Error and Exception Handling

## Try, Except Blocks
* Finally and Else Clauses
* Custom Exceptions

# Object-Oriented Programming (OOP)

* Classes and Objects
* Inheritance
* Polymorphism
* Encapsulation
* Method Overriding
* Testing

## Test Automation with pytest
## Web Development

* Introduction to Web Frameworks (Flask, Django)
* Building Simple Web Applications
* APIs

### Working with APIs
### RESTful Services
### Concurrency

### Multithreading
### Multiprocessing
### Asynchronous Programming (asyncio)
### Version Control with Git

## Basic Git Commands
* Branching and Merging
* Collaborating with GitHub
### How to Work with the PyTest?
* pip install pytest
* File name - test_name.py
* Test name - test_name_of_test():
* Assert - Actual Result == Expected Result.
* How to run the PyTest?
* open cmd ->go the the folder - pytest
* run icon
## PyTest Commands
* pytest -h (If you wanted to know about history )
* To run all the testcases
* pytest
* To run specific testcase
* pytest ex02_July/22072024/test_Lab181.py
* To run specific testcase with pattern
* pytest -k "18"
* To run a specific marked Testcase
* Add a annotation @pytest.mark.regression
* pytest -m "regression" ex02_July/22072024/test_Lab182.py
* How to see the Report of the PyTest Testcases?
* Make sure that allure commandline is installed
* Download the Node JS

## Pytest

python -m pytest is used to run tests using the pytest framework in Python. Let's break down what each part of the command does:

python: This invokes the Python interpreter. It ensures that the subsequent command (-m pytest) is executed within the Python environment.

-m: This option stands for "module". It allows you to run a module as a script. When used with python -m, it tells Python to run the specified module as if it were a standalone script.

pytest: This is the name of the module or package that Python will run. In this case, pytest refers to the pytest testing framework for Python.

When you execute python -m pytest, here's what happens step by step:

Python Interpreter: First, the python command starts the Python interpreter.

-m Option: The -m option tells Python to run a module as a script.

pytest Module: The pytest module is then executed. pytest is a testing framework that will look for test files and functions within the current directory and its subdirectories.

Test Discovery and Execution: pytest will automatically discover files and functions that follow its conventions for test discovery (files named test_*.py or methods named test_*). It will then run these tests and report the results in the console.

Summary:
Purpose: To run tests written using the pytest framework.
Usage: python -m pytest is entered in the command line in the directory where your test files (test_*.py) are located.
Result: pytest will find and execute all test functions within those files, showing the test results (successes, failures, and errors) in the console output.
This command is commonly used in Python projects that utilize pytest for testing because it ensures that pytest runs within the correct Python environment and can find the necessary test files and functions automatically.



* node -v
* npm install -g npm allure-commandline
* Verify that allure -> options
* Run your Pytestcase - pytest ex02_July/22072024/test_Lab183.py --alluredir=allure_result
* allure serve allure_result

  ## Pytest Commands
  --> pytest
