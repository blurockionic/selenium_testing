# Marriage Vendors - Selenium Test Automation

A comprehensive test automation suite for the Marriage Vendors website (marriagevendors.com) using Python, Selenium WebDriver, and unittest framework.

## 🎯 Project Overview

This project contains automated tests for various functionalities of the Marriage Vendors platform:

- **User Authentication**: Login, logout, and access control
- **Vendor Authentication**: Vendor-specific login and access
- **User Features**: Checklist management and wedding planning tools
- **Vendor Services**: Service management and vendor operations
- **Homepage**: Navigation and UI functionality testing

## 📁 Project Structure

```
BlueRock/
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── base_test.py                       # Base test class with WebDriver setup
├── utils.py                          # Common utility functions
├── test_1_user_authencation.py       # User authentication tests
├── test_2_vendor_authencation.py     # Vendor authentication tests
├── test_3_user_checklist.py          # User checklist functionality tests
├── test_4_user_wedding_planner.py    # Wedding planner feature tests
├── test_5_vendor_service.py          # Vendor service management tests
├── test_6_homepage.py                # Homepage navigation and UI tests
├── images/                           # Test assets (images for upload tests)
│   └── test.png
├── env/                              # Python virtual environment
└── __pycache__/                      # Python cache files
```

## 🔧 Prerequisites

- **Python**: 3.8 or higher
- **Google Chrome**: Latest version (ChromeDriver is automatically managed)
- **Git**: For version control
- **Internet Connection**: Required for downloading ChromeDriver and accessing the test website

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/blurockionic/selenium_testing.git
cd BlueRock
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv env
.\env\Scripts\activate.bat
```

**Linux/macOS:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
# Copy the example file
cp .env.example .env
```

Edit the `.env` file with your test credentials:

```env
# Test User Credentials
TEST_USER_EMAIL=your_test_user@example.com
TEST_USER_PASSWORD=your_test_password

# Test Vendor Credentials (optional)
TEST_VENDOR_EMAIL=your_vendor@example.com
TEST_VENDOR_PASSWORD=your_vendor_password

# Application URLs
BASE_URL=https://www.marriagevendors.com/
LOGIN_URL=https://www.marriagevendors.com/login

# Test Configuration
EXPLICIT_WAIT=15
HEADLESS=false
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Installation

```bash
python -c "import selenium; print('Selenium version:', selenium.__version__)"
```

## ▶️ Running Tests

### Run All Tests

```bash
# Run all test files
python -m unittest discover -s tests -p "test_*.py" -v
```

### Run Individual Test Files

```bash
# User authentication tests
python tests/test_1_user_authencation.py

# Vendor authentication tests
python tests/test_2_vendor_authencation.py

# User checklist tests
python tests/test_3_user_checklist.py

# Wedding planner tests
python tests/test_4_user_wedding_planner.py

# Vendor service tests
python tests/test_5_vendor_service.py

# Homepage tests
python tests/test_6_homepage.py
```


## 📋 Test Cases Overview

### 🔐 User Authentication (`test_1_user_authencation.py`)
- **test_1_invalid_login**: Validates error handling for invalid credentials
- **test_2_valid_login**: Tests successful user login
- **test_3_authorization**: Verifies access control after login
- **test_4_logout**: Tests user logout functionality

### 🏪 Vendor Authentication (`test_2_vendor_authencation.py`)
- Vendor-specific login and logout scenarios
- Vendor access control validation

### ✅ User Checklist (`test_3_user_checklist.py`)
- Checklist creation and management
- Task completion workflows

### 💒 Wedding Planner (`test_4_user_wedding_planner.py`)
- Wedding planning tool functionality
- Event management features

### 🛠️ Vendor Services (`test_5_vendor_service.py`)
- Service listing and management
- Vendor dashboard operations

### 🏠 Homepage (`test_6_homepage.py`)
- Navigation testing
- UI element validation

## 🛠️ Configuration

### Environment Variables
All configuration is managed through the `.env` file:

- **TEST_USER_EMAIL**: Email for user authentication tests
- **TEST_USER_PASSWORD**: Password for user authentication tests
- **TEST_VENDOR_EMAIL**: Email for vendor authentication tests (optional)
- **TEST_VENDOR_PASSWORD**: Password for vendor authentication tests (optional)
- **BASE_URL**: Base URL of the application
- **LOGIN_URL**: Login page URL
- **EXPLICIT_WAIT**: Wait timeout in seconds (default: 15)
- **HEADLESS**: Run tests in headless mode (true/false)

### Browser Configuration
The tests use Chrome by default. To modify browser settings, edit `base_test.py`:

```python
# Add Chrome options
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
```

### Headless Mode
To run tests in headless mode, set in your `.env` file:

```env
HEADLESS=true
```

### Wait Times
Configure wait times in your `.env` file:

```env
EXPLICIT_WAIT=30
```

### Test Website
The tests run against the URL specified in your `.env` file:

```env
BASE_URL=https://www.marriagevendors.com/
```

## 🔍 Troubleshooting

### Common Issues

**1. ChromeDriver Issues**
```bash
# ChromeDriver is automatically managed by webdriver-manager
# If issues persist, try updating:
pip install --upgrade webdriver-manager
```

**2. Element Not Found Errors**
- Increase wait time in `base_test.py`
- Check if website structure has changed
- Verify element locators in test files

**3. Login Credentials**
- Ensure your `.env` file contains valid test credentials
- Check that `TEST_USER_EMAIL` and `TEST_USER_PASSWORD` are set correctly
- Verify credentials work by manually logging into the website

**4. Environment Variables Not Loading**
```bash
# Ensure python-dotenv is installed
pip install python-dotenv

# Check if .env file exists in project root
ls -la .env  # Linux/macOS
dir .env     # Windows
```

**5. Network Issues**
```bash
# Check internet connection
ping google.com

# Verify website accessibility
curl -I https://www.marriagevendors.com/
```

### Debug Mode

To enable debug output, add print statements or use logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📊 Test Reports

### Generate HTML Reports (Optional)

Install `unittest-xml-reporting`:

```bash
pip install unittest-xml-reporting
```

Run tests with XML output:

```python
import xmlrunner

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the test suite: `python -m unittest discover -v`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## 📝 Best Practices

- **Page Object Model**: Consider implementing POM for better maintainability
- **Data-Driven Testing**: Use external data files for test data
- **Environment Variables**: Use environment variables for sensitive data
- **Logging**: Implement proper logging for better debugging
- **Screenshots**: Capture screenshots on test failures

## 🔗 Dependencies

- **selenium**: Web automation framework
- **webdriver-manager**: Automatic ChromeDriver management
- **unittest**: Python's built-in testing framework

## 📧 Support

For issues and questions:
- Create an issue in the GitHub repository
- Contact: [Your Contact Information]

---

**Happy Testing! 🚀**
