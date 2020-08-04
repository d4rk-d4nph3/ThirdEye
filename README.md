# ThirdEye
[![osquery](https://img.shields.io/static/v1?label=osquery&message=kolide&color=blueviolet)](https://www.osquery.io)
[![osquery](https://img.shields.io/static/v1?label=made%20with&message=python%203&color=blue)](https://www.osquery.io)
[![osquery](https://img.shields.io/static/v1?label=code%20quality&message=B&color=green)](https://www.osquery.io)
[![osquery](https://img.shields.io/static/v1?label=ready&message=no&color=red)](https://www.osquery.io)

## Description

This project is to audit Kolide instances by exploiting the API provided by Kolide. Motivation for this project is to monitor your Kolide instance by looking at any tamperings or un-authorized use like adding of a new unknown device, or running of malicious queries.

## Requirements

```sh
pip3 install requests
```

## Usage

### Testing

Add your Kolide Access Token in the script before running the project.

```sh
python3 third_eye.py
```

### Normal Use

For normal use, clone this repository and create a scheduled task to run this project for say, every 2 days.

## TODO

- [x] Audit enrolled devices
- [x] Audit live queries
- [x] Fetch Audit logs
- [ ] Detect queries by new authors
- [ ] Detect abonormality in location
- [ ] Visualize live query and API usage statistics
