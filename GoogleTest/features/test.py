"""Webdriver support for lettuce"""
import time
from lettuce import step
from lettuce import world
from lettuce_webdriver.util import assert_true
from lettuce_webdriver.util import AssertContextManager


@step('I go to "(.*?)"$')
def go_to(step, url):
    with AssertContextManager(step):
        world.browser.get(url)


@step('I press "(.*?)"$')
def press(step, input_button_text):
    with AssertContextManager(step):
        button = world.browser.find_element_by_name(input_button_text)
        button.click()


@step('I fill in the textfield with "(.*?)"$')
def fill_in_textfield(step, entry):
    with AssertContextManager(step):
        textfield = world.browser.find_element_by_id("lst-ib")
        textfield.clear()
        textfield.send_keys(entry)


@step('I should see the follwing website"(.*?)"$')
def should_see(step, text):
    with AssertContextManager(step):
        time.sleep(2)
        assert_true(step, text)

