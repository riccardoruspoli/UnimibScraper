# Unimib Scraper

Script in grado di scaricare i video dalla piattaforma [e-LEARNING](https://elearning.unimib.it/) dell'Università degli Studi di Milano-Bicocca.

## Installazione
Installare __Python 3__, poi eseguire i seguenti comandi:

```shell
cd UnimibScraper
pip install -r requirements.txt
```

È necessario scaricare i [Chrome Webdriver](https://chromedriver.chromium.org) ed aggiungerli nel PATH in modo che lo script possa funzionare correttamente.

## Utilizzo

Inserire all'interno del file unimib_scraper.py username e password nelle variabili corrispondenti, dopodiché avviare lo script.

```shell
usage: unimib_scraper.py [-h] (-l LESSON | -c COURSE) [-t THREADS]

optional arguments:
  -h, --help            show this help message and exit
  -l LESSON, --lesson LESSON
                        Lesson Id
  -c COURSE, --course COURSE
                        Course Id

  -t THREADS, --threads THREADS
```
