from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Firefox()
driver.get ('https://saucedemo.com')
driver.maximize_window()
time.sleep(2)

print('THỰC HIỆN 3 TESTCASE')

#Testcase 1: Usernam, password => đúng
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

if 'inventory.html' in driver.current_url:
    print('\nPASS: Login thành công')
else:
    print('\nFAIL: Login thất bại')

time.sleep(2)
driver.back()

#Testcase 2: Usernam, password => sai mật khẩu
driver.find_element(By.ID, 'user-name').clear()
driver.find_element(By.ID, 'password').clear()

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('123456789')
driver.find_element(By.ID, 'login-button').click()
time.sleep(2)

msg=driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
print('\nerror_massage: ',msg)
print('PASS: Hiển thị lỗi đúng khi sai mật khẩu')

#Testcase 3: Usernam, password => trống
driver.find_element(By.ID, 'user-name').clear()
driver.find_element(By.ID, 'password').clear()
driver.find_element(By.ID, 'login-button').click()
time.sleep(2)

msg2=driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
print('\nerror_massage: ',msg2)
print('PASS: Hiển thị lỗi đúng khi trống')

print('\nĐÃ HOÀN THÀNH 3 TESTCASE')
driver.quit()