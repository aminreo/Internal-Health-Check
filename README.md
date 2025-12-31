# Internal-Health-Check
Simple Service Health Monitor that pings a list of URLs and logs their status


## Features
* Services are stored in JSON file
* Checker script that checks each url
* Logging function with timestamps and statues
* Alert if a service is currently down

## How to use

```python
pip install -r requirements.txt
python .\Scripts\checker.py
```

## Functionality
we use `requests` to make http requests and get their status code, we then alert the user via console if a service is down, results are saved in `Logs/checks.log`