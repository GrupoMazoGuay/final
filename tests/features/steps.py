from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from nose.tools import assert_equals

from application import app
import os
import pdb
import time

#


@before.all
def before_all():
    world.app = app.test_client()

    is_travis = 'TRAVIS' in os.environ
    if is_travis:
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary("/usr/bin/firefox")
        d = webdriver.Firefox(firefox_binary=binary)
        world.driver = webdriver.Firefox(d)
        world.driver.get("http://localhost:8080/")
    else:
        world.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        world.driver.get("http://localhost:8080/")


@after.all
def end(aux):
    world.driver.close()
    world.driver.quit()


@step('I have the string "(.*)"')
def have_the_string(step, string):
    text = world.driver.find_element_by_name('text-box')
    text.send_keys(string)
    world.string = string


@step('Push execute')
def push_execute(step):
    execute = world.driver.find_element_by_id('submit')
    execute.send_keys("\n")


@step('Push reset')
def push_reset(step):
    reset = world.driver.find_element_by_id('reset')
    reset.send_keys("\n")


@step('I see results')
def i_see_results(step):
    results = world.driver.find_elements_by_tag_name('td')
    if len(results) > 0:
        result_exists = True
    else:
        result_exists = False
    assert_equals(result_exists, True)


@step('I see not results')
def i_see_not_results(step):
    reset = world.driver.find_element_by_id('reset')
    reset.send_keys("\n")
    time.sleep(1)
    results = world.driver.find_elements_by_tag_name('td')
    if len(results) > 0:
        result_exists = True
    else:
        result_exists = False
    assert_equals(result_exists, False)
