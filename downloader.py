import os
import time

from browser import Browser
from file import FileManager


class Downloader:
    _threads = 1
    browser = None
    file_manager = None

    def __init__(self, download_location, threads):
        self.browser = Browser(download_location)
        self.file_manager = FileManager(download_location)

        if threads is not None:
            self._threads = threads

    def download_lesson(self, lesson):
        src_filename = self.download_src(lesson)
        m3u8_filename = self.download_m3u8(src_filename)
        self.download_video(m3u8_filename)

    def download_course(self, course):
        self.browser.go_to_course(course)
        lesson_list = self.browser.get_lessons_from_course(course)
        for lesson in lesson_list:
            print(f'--- Downloading lesson {lesson_list.index(lesson) + 1} of {len(lesson_list)}')
            self.download_lesson(lesson)
    
    def login(self, username, password):
        self.browser.login(username, password)

    def quit(self):
        self.browser.quit()

    def download_src(self, lesson):
        src = self.browser.get_lesson_src(lesson)
        title = self.browser.driver.title.replace(' ', '_').replace('/', '_').replace(':', '_').replace('\"', '_').replace('\'', '_').replace('<', '_').replace('>', '_').replace('=', '_') + '.m3u8'
        src = self.browser.parse_src(src)
        self.browser.go_to(src)
        time.sleep(1)
        return self.file_manager.rename_m3u8('a.m3u8', title)

    def download_m3u8(self, filename):
        with open(filename) as file:
            url = file.readlines()[-1] # Only latest row of file matters to us (highest quality)
        
        self.file_manager.delete(filename)
        self.browser.go_to(url)
        time.sleep(1)
        return self.file_manager.rename_m3u8('index.m3u8', filename)
    
    def download_video(self, filename):
        os.system('m3u8-dl -t ' + str(self._threads) + ' "file:' + filename + '" "' + filename.replace('m3u8', 'mp4') + '"')
        os.remove(filename)