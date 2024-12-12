# This is an Automation Repository for Mitt Arv Website

This repository Contains Automation Scripts to Test the Mitt Arv Web Application



## Tools

- ***Testing Framework:*** Pytest

- ***Tool/Libraries Used for Web Automation:*** Selenium



## Getting Started



### Prerequisites

- Python(>= 3.10)

- Chrome Browser(Any Latest Version)



### Installation



#### Step 1:

Clone this repository



#### Step 2:

Install the Dependencies(Libraries) from the requirements.txt file. This will install all the required Libraries to start with the project

```sh

pip install -r requirements.txt

```

#### Step 3:

#### Run All tests

Below Command will run all the test cases and will generate a report with Filename as 'report.html'.

```sh

python -m -pytest --html=report.html

```

#### Run Specific Group of tests

Below Command will run all the test cases with markers 'login' and will generate a report with Filename as 'report.html'.

```sh

python -m -pytest -m regression --html=report.html

```

Test case are configured with various markers: regression (in this case I have used only one marker to group all test cases)

## Report
![Report](https://i.imgur.com/ob55M9I.png)