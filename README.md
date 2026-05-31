# OrangeHRM Automation Testing

Dự án Automation Testing cho hệ thống **OrangeHRM** sử dụng Python + Selenium WebDriver.

## Mục tiêu
- Áp dụng Page Object Model (POM) chuẩn
- Tích hợp PyTest + Allure Report
- Kiểm tra Database (MySQL)
- Testing API (Auth Token)

## Tech Stack
- **Python** 
- **Selenium WebDriver**
- **PyTest** + **Allure Report**
- **Page Object Model (POM)**
- **MySQL** (Database verification)
- **Requests** (API Testing)

## Cấu trúc Project
- `pages/` : Chứa các Page Object (BasePage, LoginPage, EmployeePage...)
- `tests/` : Chứa tất cả test cases
- `data/` : Dữ liệu test (CSV, JSON...)
- `utils/` : Các hàm hỗ trợ chung
- `screenshots/` : Ảnh chụp khi test fail
- `reports/` : Báo cáo Allure
- `conftest.py` : Fixtures PyTest

## How to Run
```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy test
pytest tests/ -v --alluredir=reports/allure-results

# Xem báo cáo Allure
allure serve reports/allure-results
