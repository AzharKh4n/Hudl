# **AUTOMATED TEST SUITE FOR THE HUDL LOGIN PAGE**

## **INTRODUCTION**
---
Small and basic test automation suite for the Hudl login page. 

Created using a Python hybrid framework with Pytest, Selenium WebDriver, (POM), and HTML reporting.

The Python hybrid framework facilitates the flexibility of using both Data-Driven and Keyword-Driven frameworks.

I have chosen to use this framework as it is very easy to read, manage and maintain test data and the (POM) page objects model design pattern works very well when using selenium for test case automation.The Page Object Model means that each individual webpage has its own class, each containing the methods specific to controls on that page. Thus, each page is independent and separate from the tests, meaning any changes to the page are isolated to only the corresponding page class. This makes for code that is cleaner, easier to read and maintain, and contains less duplication. 

Follow the instructions below to setup and execute the test suite and generate a report of the results.

---

## **PROJECT STRUCTURE**

### **`\Configurations:`** 

`config.ini` file has been used as a source of common data and to replace any hard coded values in test cases.

### **`\Logs:`**

Folder has been created to store any logs when logging has enabled.

### **`\pageObjects:`**

Web pages are represented by a corresponding class and web elements are represented by the variables of the class and all interactions are possible through the methods or say functions of the class.

`LoginPage.py` contains all of the web elements under the `LoginPage` class that makes it very easy to read, write and maintain test cases without having to change numerous test cases if changes are made.

### **`\Reports:`**

HTML reports are stored here, you will find some previously generated reports in the folder and are able to generate future reports in this directory too.

### **`\Screenshots:`**

If a test fails a screenshot will be taken and saved in this folder, each screenshot will be named the test that failed.


### **`\testCases:`**

All test cases and the `conftest.py` are stored here. The `conftest.py` file contains all required fixtures, all setup and teardown requirements are set here. If tests are to be run on a particular browser, cross browser or in parallel can all defined in this file.

`test_login.py` is the suite of tests for the login page, a total of 11 tests.

### **`\TestData:`**

Any files that are used for Data-Driven test automation will be stored here. For instance data could be prepared on an excel sheet and stored in this folder and then a corresponding utilities class would need to be created under the `utilities` package in order to create automated Data-Driven test cases.

*There are no Data-Driven test cases for the login page.*

### **`\utilities:`**

For this project the utilities package is being used to read common values from the `config.ini` file.


---

## **TECH STACK**

* PYTHON (3.7)
* PYTEST FRAMEWORK
* SELENIUM WEB DRIVER 
* POM FRAMEWORK
* HTML REPORTING

---

## **SUPPORTED BROWSERS**

---

The `conftest.py` module uses the Webdriver-Manager dependency to manage the various browser drivers. The browser Pytest fixture returns the relevant WebDriver instance for the chosen browser, at present the suite only supports the Chrome browser.

**NOTE:**
*You will not need to download the chrome driver specifically as I have used the web driver manager that will automatically install the latest driver when executing the test.*

---
## **SETUP INSTRUCTIONS**

---
### **STEP 1**

* **Clone the repository** 

```
git clone https://github.com/AzharKh4n/Hudl.git
```

### **STEP 2**

* **Create and Activate Virtual Environment** 

Once repo has been cloned navigate to the project directory in terminal:

```
cd path/to/hudl
```

**Create a virtual environment:**

```python
virtualenv venv
```

**Activate the environment:**


```
source venv/bin/activate
```

### **STEP 3**

* **Install all of the dependencies**


```
pip install -r requirements.txt
```

### **STEP 4**

* **Update paths in [`readProperties.py`](https://github.com/AzharKh4n/Hudl/blob/3c6d01695d1cc4c73a526e7109b58213ef585d19/utilities/readProperties.py#L4-L7) in the `utilities` folder**


Before running the tests it's important that the two paths shown below are set correctly (depending on where the repo is saved locally on your machine):

```python
../Hudl/utilities/readProperties.py

assert os.path.exists("/Users/khan/PycharmProjects/Hudl/Configurations/config.ini")

config = configparser.RawConfigParser()
config.read("/Users/khan/PycharmProjects/Hudl/Configurations/config.ini")

```

*If the `config parser` is unable to locate the `config.ini` file the tests will not run.*


---

## **RUNNING THE TEST SUITE**

---
Navigate to the project directory in terminal and run:


**RUN SUITE OF TESTS:**

```python
pytest -v -s testCases/test_login.py
```


**RUN SUITE OF TESTS AND GENERATE AN    HTML REPORT**:

```python
pytest -v -s --html=report --self-contained-html testCases/test_login.py
```
This command will execute the suite of tests and then generate and save the HTML report in the main project directory.

![alt text](https://blog.testproject.io/wp-content/uploads/2019/05/pytest-html-report.png)
*sample report*



**RUN SUITE OF TESTS IN PYCHARM:**

Right click on the `test_login.py` file and select `Run 'pytest in test login'` 

![alt text](https://resources.jetbrains.com/help/img/idea/2022.2/py_pytest_run_test.png)

or click on the `run test` icon displayed at the start of each test *(as shown above)* to run a test individually.

---


