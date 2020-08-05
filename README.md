# ThirdEye
[![osquery](https://img.shields.io/static/v1?label=osquery&message=kolide&color=blueviolet)](https://www.osquery.io)
[![osquery](https://img.shields.io/static/v1?label=made%20with&message=python%203&color=blue)](https://www.osquery.io)

<br/>

![image](https://user-images.githubusercontent.com/61026070/89407121-ebf68500-d73d-11ea-8605-d17a29a0a2d4.png)

## Description

This project is to audit Kolide instances by exploiting the API provided by Kolide. 

If you don't know about [Kolide](https://www.kolide.com) then, it's never too late to learn about this awesome product based on [osquery](https://www.osquery.io).

In short, osquery is an OS instrumentation framework for that exposes an OS as a high-performance relational database. This allows you to write SQL queries to explore operating system data. 

And, Kolide is a front-end for efficiently deploying osquery across multiple endpoints. Also, that UI is love.

## Motivation

Motivation for this project is to monitor your Kolide instance by looking at any tamperings or un-authorized use like adding of a new unknown device, or running of queries by new actors.

Compromise of your Kolide means, now the adversary has a high performance framework available for reconnaisance.

## Requirements

```sh
pip3 install requests
```

## Usage

### Testing

This project requires three values to be set before running:
- Add your Kolide Access Token
- Add a list of valid users
- Add a list of valid locations (like United States, Sweden, etc)

```sh
python3 third_eye.py
```

### Normal Use

For normal use, clone this repository and create a scheduled task to run this project for say, every 2 days.

## Output

### Enrolled Devices Summary

```
Generated at: 03:57 PM, Wed Aug 05, 2020

Total number of devices enrolled: 1

Device ID: 1102
Device Name: Win07
Platform: windows
OS: Microsoft Windows 10 Pro Version: 10.0.19041 | UBR: 388
Enrolled At: 2020-08-01T12:43:55.016Z
Last Seen At: 2020-08-05T07:57:43.000Z
Primary User: sam
Remote IP: 8.8.8.8
Location: China
```

### Live Query by New Author Detected Alert

```
alert_id=200 timestamp=04:49 PM, Wed Aug 05, 2020 log_ts=2020-08-02T07:21:19.503Z author=John query=SELECT pid, name, path, cmdline, parent FROM processes WHERE name = 'svchost.exe' AND cmdline not LIKE '% -k %'; message=Live query by new author detected
```

### New Device Location Detected Alert

```
alert_id=100 timestamp=04:11 PM, Wed Aug 05, 2020 location=Russia device=Win10 remote_ip=100.44.116.43 message=New device location detected
```

### New Actor Detected in Audit Log Alert

```
alert_id=200 timestamp=04:19 PM, Wed Aug 05, 2020 log_ts=2020-08-05T07:55:05.428Z actor=Kira message=New Actor detected in Audit Log
```

## TODO

- [x] Audit enrolled devices
- [x] Audit live queries
- [x] Fetch Audit logs
- [x] Detect queries by new authors
- [x] Detect abonormality in location
- [ ] Visualize live query and API usage statistics
