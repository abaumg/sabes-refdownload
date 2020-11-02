# sabes-refdownload

This script takes a fiscal code (*Steuernummer*) and a token provided by SABES and checks if there are any new reports on https://refonline.sabes.it. If so, the script sends a Telegram notification.


## Requirements
- Firefox
- Xvfb
- Python3
- Python3 modules from `requirements.txt`

## Installation
* Clone repository: `git clone ssh://git@github.com/abaumg/sabes-refdownload && cd sabes-refdownload`
* Install Python3 modules: `pip3 install -r requirements.txt`
* Install Xvfb: `apt install xvfb`
* Install Firefox Selenium driver: `wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz && tar xfvz geckodriver-v0.27.0-linux64.tar.gz`
* Copy sample configuration file: `cp config.ini.example config.ini`