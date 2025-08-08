# Python + Pytest + Selenium UI Tests

## 📌 Overview
This project contains automated UI tests written in **Python**, using **Pytest** as the test runner and **Selenium WebDriver** for browser automation.  
The tests follow the **Page Object Model (POM)** pattern, where each page is represented by a dedicated Python class in the `pages/` directory.

---

## 📂 Project Structure

```
.
├── pages/                  # Page Object classes
│   ├── AbTestingPage.py
│   ├── AddRemoveElementsPage.py
│   ├── BasePage.py
│   ├── BasicAuthPage.py
│   ├── BrokenImagePage.py
│   ├── CheckboxesPage.py
│   ├── MainPage.py
├── tests/                  # Test files
│   ├── test_selenium.py
│   ├── conftest.py         # Pytest fixtures and WebDriver setup
├── .gitignore
└── README.md
```

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lentyl/pytest-selenium.git
   cd pytest-selenium
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, install manually:
   ```bash
   pip install pytest selenium
   ```

4. **Install a WebDriver**
   - **Chrome**: [Download ChromeDriver](https://chromedriver.chromium.org/downloads)  
   - **Firefox**: [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)  

   Make sure the driver is in your system PATH.

---

## 🚀 Running Tests

Run all tests:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run a specific test file:
```bash
pytest tests/test_selenium.py
```

Run a specific test function:
```bash
pytest tests/test_selenium.py::test_example
```

---

## ⚙️ WebDriver Configuration

The WebDriver is configured in `tests/conftest.py`.  
Example setup:
```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Optional: run without UI
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
```

To change browser settings, modify the fixture in `conftest.py`.

---

## 🧪 Test Design

- **Page Object Model**:  
  Each page is represented by a class in the `pages/` folder, encapsulating locators and actions.
- **Tests** import these page classes to perform UI interactions and assertions.

Example test:
```python
from pages.MainPage import MainPage

def test_example(driver):
    page = MainPage(driver)
    page.open()
    assert page.get_title() == "Expected Title"
```

---

## 📊 Optional: HTML Reports

Install:
```bash
pip install pytest-html
```

Run with report:
```bash
pytest --html=report.html --self-contained-html
```

---

## ✅ Summary

This project is ready to:
- Launch a browser via Selenium
- Navigate and interact with web pages using POM
- Run tests with Pytest
- Optionally generate test reports
