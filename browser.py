import logging
import re

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER


class Browser:
    driver = None

    def __init__(self, download_location):
        LOGGER.setLevel(logging.NOTSET)
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": download_location}
        chromeOptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
    
    def login(self, username, password):
        self.driver.get("https://elearning.unimib.it/login/index.php")

        # Press "Login"
        self.driver.find_element_by_css_selector("a[class='btn btn-primary btn-block']").click()

        self.driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        self.driver.find_element_by_css_selector("button[class='form-element form-button']").click()

    def go_to(self, link):
        self.driver.get(link)

    def go_to_lesson(self, lesson_id):
        self.go_to(f'https://elearning.unimib.it/mod/kalvidres/view.php?id={lesson_id}')

    def go_to_course(self, course_id):
        self.go_to(f'https://elearning.unimib.it/course/view.php?id={course_id}')

    def get_lesson_src(self, lesson):
        self.go_to_lesson(lesson)
        frame = self.driver.find_element_by_class_name('kaltura-player-iframe')
        src = frame.get_attribute("src")
        return src

    def parse_src(self, link):
        self.go_to(link)
        return self.driver.execute_script('return $("#kplayer_ifp").contents().find("body").find("video").attr("src")')

    def get_lessons_from_course(self, course):
        # Get links
        resources = self.driver.find_elements_by_css_selector('a')
        resources_links = list()

        for resource in resources:
            try:
                # Enumerate links
                href = resource.get_attribute('href')
                if 'kalvidres' in href:
                    resources_links.append(href[href.index('id=') + 3 : len(href)])
            except:
                pass
        
        return resources_links

    def quit(self):
        self.driver.quit()