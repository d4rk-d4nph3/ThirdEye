# ThirdEye
[![osquery](https://img.shields.io/static/v1?label=osquery&message=kolide&color=blueviolet)](https://www.osquery.io)
[![osquery](https://img.shields.io/static/v1?label=made%20with&message=python%203&color=blue)](https://www.osquery.io)

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
- Add a list of valid locations

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

### New User Detected Alert

```
Alert ID: 1
"Generated at: 02:53 PM, Tue Aug 04, 2020"
New user detected: Sam
"Running query: SELECT DISTINCT processes.name, processes.path, listening_ports.port FROM listening_ports
JOIN processes USING (pid)
WHERE listening_ports.family = 2
AND listening_ports.address <> '127.0.0.1';"
At: 2020-08-02T13:22:47.907Z
```

### New Device Location Detected Alert

```
Alert ID: 10
"Generated at: 02:59 PM, Tue Aug 04, 2020"
New location detected: China
For Device: Win10
Remote IP: 104.22.88.112
```

### New Actor Detected in Audit Log Alert

```
Alert ID: 12
New actor detected in Audit Log: Julius
At: 2020-08-02T16:50:25.386Z
Description: CSV Downloaded For Device Win10 - Live Query Campaign ID 2624
```

## TODO

- [x] Audit enrolled devices
- [x] Audit live queries
- [x] Fetch Audit logs
- [x] Detect queries by new authors
- [x] Detect abonormality in location
- [ ] Visualize live query and API usage statistics
