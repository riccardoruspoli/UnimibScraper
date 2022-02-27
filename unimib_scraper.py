from downloader import Downloader
import argparse
import pathlib
import os
import time

parser = argparse.ArgumentParser("unimib_scraper.py")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-l", "--lesson", help="Lesson Id", type=int)
group.add_argument("-c", "--course", help="Course Id", type=int)
threads_group = parser.add_argument_group()
threads_group.add_argument("-t", "--threads", type=int)
args = parser.parse_args()

username = ""
password = ""

download_location = os.path.join(str(pathlib.Path(__file__).parent.absolute()), 'download')
downloader = Downloader(download_location, args.threads)
downloader.login(username, password)

if args.lesson is not None:
    downloader.download_lesson(args.lesson)

if args.course is not None:
    downloader.download_course(args.course)

downloader.quit()