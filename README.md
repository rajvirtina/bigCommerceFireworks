
# Firework Shared Automation Library for OMS Integrations

This library provides a shared automation framework for integrating Order Management Systems (OMS) automation test suites using Selenium with Python. The library contains pre-defined functions and methods to automate various example / reference tests on OMS Integrations processes such as business creation, test widget creation and configuration, embed business portal, product import, thereby reducing the time and effort required for OMS testing and integration. 


The test cases are available at the following link:

[Link to test cases](https://docs.google.com/spreadsheets/d/1IS0BytdmsBmJMJFvEk3wP-HVo6kysE9gaLd6OTJDI0U/edit?usp=sharing)

> To use the library, first install the required dependencies using the following command in the command prompt:

 
```` Python -m pip install -U Selenium ````

> After importing the project, select the interpreter and install the following libraries:

Selenium
pytest
pytest-html
pytest-xdist
pytest-order
pytest-ordering
pytest-order-modify
pytest-metadata
openpyxl
allure-pytest
allure-python-commons


> To execute a single test case, use the following command in the terminal:

 
```` pytest -v --browser chrome testCases/specificTestName.py --html=Reports/report.html ```` 

> To execute all test cases at once, use the following command in the terminal:

 
```` pytest -v --browser chrome testCases/ --html=Reports/report.html ````

The library also includes sample test cases for reference, which can be used as a starting point for new OMS integrations.

Overall, this shared automation library aims to streamline the testing process for OMS integrations and improve efficiency for developers working on OMS projects.
