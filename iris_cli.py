#!/usr/bin/python

"""Iris CLI.

Usage:
    iris_cli.py -u <username> -p <password> arm
    iris_cli.py -u <username> -p <password> disarm

Options:
    -h --help       Show this screen.
    --username   Username for Iris
    --password    Password for Iris

"""

from docopt import docopt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def main( arguments ):
    driver = webdriver.Firefox()
    driver.get("https://www.irissmarthome.com/myhome")

    username_element = driver.find_element_by_id('username')
    password_element = driver.find_element_by_id('password')
    login_element = driver.find_element_by_xpath("//*[@id='login_form']/div[3]/div[2]/a")

    time.sleep(10)

    username_element.send_keys(arguments['<username>'])
    password_element.send_keys(arguments['<password>'])
    login_element.submit()
    time.sleep(10)

    if arguments['arm']:
        driver.get("https://www.irissmarthome.com/myhome/link/#alarm/overview")
        time.sleep(10)
        arm_element = driver.find_element_by_xpath("//*[@id='widget_alarm_class_slider_wrapper']/div[1]")
        arm_element.click()
        time.sleep(30)
    if arguments['disarm']:
        driver.get("https://www.irissmarthome.com/myhome/link/#alarm/overview")
        time.sleep(10)
        disarm_element = driver.find_element_by_xpath("//*[@id='widget_alarm_class_slider_wrapper']/div[2]")
        disarm_element.click()
        time.sleep(15)

    result = driver.find_element_by_id('widget_alarm_text_status').text
    print result

    driver.close()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Iris Cli 1.0')
    print(arguments)
    print(arguments['<username>'])
    print(arguments['<password>'])
    print(arguments['arm'])
    print(arguments['disarm'])
    main(arguments)

