# QA Automation Assignment

This project contains:

- API Automation using Pytest + Requests
- UI Automation using Playwright + Pytest
- HTML Test Reporting
- GitHub Actions CI/CD Integration

---

# Tech Stack

- Python
- Pytest
- Requests
- Playwright
- JSON Schema Validation

---

# Project Structure

```text
qa-automation-assignment/
│
├── tests/
│   ├── api/
│   │   └── test_cart_flow.py
│   │
│   └── ui/
│       └── test_saucedemo_flow.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── utils/
│   └── config.py
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/ShubhamMirani2/QA-automation-assignment.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Playwright Browsers

```bash
playwright install
```

---

# Environment Variables

Create a `.env` file in project root.

Example:

```env
BASE_URL=https://dummyjson.com
USER_CRED=emilys
PASS_CRED=emilyspass
```

---

# Run API Tests

```bash
pytest tests/api -v
```

---

# Run UI Tests

```bash
pytest tests/ui -v
```

---

# Run UI Tests in Headed Mode

```bash
pytest tests/ui -v --headed
```

---

# Generate HTML Report

## API Report

```bash
pytest tests/api --html=api_report.html
```

## UI Report

```bash
pytest tests/ui --html=ui_report.html
```

---

# Features Implemented

## API Automation

- Authentication API
- Token Extraction
- Dynamic User ID Handling
- Cart Retrieval
- Add Product to Cart
- JSON Schema Validation
- Total Price Validation

## UI Automation

- Login Automation
- Product Sorting Validation
- Add Products to Cart
- Checkout Flow
- Order Confirmation Validation
- Page Object Model Design

---

# CI/CD

GitHub Actions pipeline included for automated execution in headless environment. We have also used GitHub Secrets and HTML reports generation, once test suite is exceuted by GitHub Actions.