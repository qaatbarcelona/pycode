#!/usr/bin/python
import random
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('./chromedriver')
mainPage = "https://surgimap.com"
mainTitle = 'Surgimap.com: Official Site for Surgimap'
userEmail = "surgimap.test." + str(random.randint(1, 1000000000)) + "@gmail.com"
userPwd = 'someeasyPWD345'
accessPage = "https://www.surgimap.com/access/#/login"
registrationPage = "https://www.surgimap.com/access/#/register"


def fromlandingtoregistration(time_wait):

    login = driver.find_element_by_class_name("btn-login")
    login.click()

    create_account = time_wait.until(EC.element_to_be_clickable((By.ID, 'aCreateAccount')))
    assert driver.current_url == accessPage
    print('At Login Page')
    create_account.click()

    time_wait.until(EC.element_to_be_clickable((By.ID, 'txtConfirmPassword')))
    assert driver.current_url == registrationPage
    print('At Registration Page')


def registration(time_wait):

    try:
        send_cmd = "document.getElementById('txtEmail').value=" + '"' + userEmail + '"'
        driver.execute_script(send_cmd)
        send_cmd = "document.getElementById('btnRegister').disabled=false"
        driver.execute_script(send_cmd)
    except TimeoutException:
        print('email field not found')

    try:
        print('Find txtPwd')
        pwd_field = driver.find_element_by_id('txtPassword')
        pwd_field.send_keys(userPwd)
    except TimeoutException:
        print('pwd field not found')

    try:
        print('Find ConfirmPassword')
        repeat_pwd_field = driver.find_element_by_id('txtConfirmPassword')
        repeat_pwd_field.send_keys(userPwd)
    except TimeoutException:
        print('pwd repetition field not found')

    try:
        print('Find btnregister')
        time_wait.until(EC.element_to_be_clickable((By.ID, 'btnRegister')))
        register_new_account = driver.find_element_by_id('btnRegister')
        register_new_account.click()
        print('Sent Register')
    except TimeoutException:
        print('registerAccount button not found')


def main():

    print('Creating New Account for:' + userEmail)

    try:
        driver.get(mainPage)
        wait = WebDriverWait(driver, 10)
        assert mainTitle in driver.title

        fromlandingtoregistration(wait)
        registration(wait)

        try:
            time.sleep(3)
            send_cmd = "document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()"
            driver.execute_script(send_cmd)
            print('Accepted dialog')
        except TimeoutException:
            print('No confirmation shown')

    except TimeoutException:
        driver.quit()

    driver.quit()


if __name__ == '__main__':
    main()