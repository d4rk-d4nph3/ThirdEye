import csv
import requests

from datetime import datetime

# Kolide API Reference: https://kolidek2.readme.io/docs

# Manually set these values before running
ACCESS_TOKEN = ''  # <-- Add Your Kolide access token here!!
USERS = []         # <-- Add Valid Users with access to Kolide
LOCATIONS = []     # <-- Add Valid locations

header = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}
alert_count = 0

def fetch_devices():
    K2_DEVICES_URL = 'https://k2.kolide.com/api/v0/devices'
    response = requests.get(K2_DEVICES_URL, headers=header)

    if response.status_code == 401:
        print('Access Token value is wrong\n'
              'Exiting...')
        exit()
    
    data = response.json().get('data')

    with open('Devices.txt', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Generated at: {}'.format(
                        datetime.now().strftime("%I:%M %p, %a %b %d, %Y"))])
        writer.writerow(['Total number of devices enrolled: {}\n'.format(
                                                                len(data))])
        
    for device in data:
        if device.get('location') not in LOCATIONS:
            with open('Alert.txt', 'a') as alertfile:
                writer = csv.writer(alertfile)
                global alert_count
                alert_count += 1
                writer.writerow(['Alert ID: {}'.format(alert_count)])
                writer.writerow(['Generated at: {}'.format(
                        datetime.now().strftime("%I:%M %p, %a %b %d, %Y"))])
                writer.writerow(['New location detected: {}'.format(
                                                   device.get('location'))])
                writer.writerow(['For Device: {}'.format(device.get('name'))])
                writer.writerow(['Remote IP: {}\n'.format(
                                                    device.get('remote_ip'))])

        with open('Devices.txt', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Device ID: {}\nDevice Name: {}\n'
            'Platform: {}\nOS: {}\n'
            'Enrolled At: {}\nLast Seen At: {}\n'
            'Primary User: {}\nRemote IP: {}\n'
            'Location: {}\n\n'.format(device.get('id'), device.get('name'),
            device.get('platform'), device.get('operating_system'),
            device.get('enrolled_at'), device.get('last_seen_at'),
            device.get('primary_user_name'), device.get('remote_ip'),
            device.get('location'))])

def fetch_live_queries():
    K2_LIVE_QUERY_URL = 'https://k2.kolide.com/api/v0/live_queries'

    response = requests.get(K2_LIVE_QUERY_URL, headers=header)

    data = response.json().get('data')
    print('Total number of live queries: {}'.format(len(data)))
    
    # Write header
    with open('Queries.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Generated at: {}'.format(datetime.now(
                                    ).strftime("%I:%M %p, %a %b %d, %Y"))])
        writer.writerow(['Query Name', 'Query', 'Created At', 
                         'Tables Used', 'Author Name', 'Author Email'])

    for query in data:
        if query.get('author').get('name') not in USERS:
            with open('Alert.txt', 'a') as alertfile:
                writer = csv.writer(alertfile)
                global alert_count
                alert_count += 1
                writer.writerow(['Alert ID: {}'.format(alert_count)])
                writer.writerow(['Generated at: {}'.format(
                        datetime.now().strftime("%I:%M %p, %a %b %d, %Y"))])
                writer.writerow(['New user detected: {}'.format(
                                          query.get('author').get('name'))])
                writer.writerow(['Running query: {}'.format(
                                                 query.get('osquery_sql'))])
                writer.writerow(['At: {}\n'.format(query.get('created_at'))])

        with open('Queries.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([query.get('name'), 
                             query.get('osquery_sql'),
                             query.get('created_at'),
                             ', '.join(query.get('tables_used')),
                             query.get('author').get('name'),
                             query.get('author').get('email')])

def fetch_audit_logs():
    K2_AUDIT_LOG_URL = 'https://k2.kolide.com/api/v0/audit_logs'
    response = requests.get(K2_AUDIT_LOG_URL, headers=header)

    data = response.json().get('data')
    print('Total number of audit logs: {}'.format(len(data)))
    
    with open('Audit Logs.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Generated at: {}'.format(datetime.now(
                                    ).strftime("%I:%M %p, %a %b %d, %Y"))])
        writer.writerow(['ID', 'Timestamp', 'Actor Name', 'Description'])

    for log in data:
        if log.get('actor_name') not in USERS:
            with open('Alert.txt', 'a') as alertfile:
                writer = csv.writer(alertfile)
                global alert_count
                alert_count += 1
                writer.writerow(['Alert ID: {}'.format(alert_count)])
                writer.writerow(['New actor detected in Audit Log: {}'.format(
                                                       log.get('actor_name'))])
                writer.writerow(['At: {}'.format(log.get('timestamp'))])
                writer.writerow(['Description: {}\n'.format(
                                                      log.get('description'))])

        with open('Audit Logs.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([log.get('id'), log.get('timestamp'), 
                             log.get('actor_name'), log.get('description')])

fetch_devices()
fetch_live_queries()
fetch_audit_logs()
