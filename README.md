# searx checker

A small command line tool to check which engines return results of an instance.

In case of older searx versions the engines `currency` return error when in fact it is working. To make it work correctly, please update the instance examined to the latest commit.

## Requirements

 * Python 3.5

## Installation

```
git clone git@github.com:kvch/searx-checker.git
cd searx-checker
vitualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

```
python3 checker/checker.py <instance-url>
```

Example output of an instance with 2 non-responsive engines and 3 working engines.

```
python3 checker/checker.py http://localhost:8888
Testing 5 engines of http://localhost:8888
google.OK
bing.OK
gitlab......ERROR
vimeo......ERROR
twitter.OK

Engines of http://localhost:8888 not returning results:
gitlab
vimeo
You might want to check these manually...
```
