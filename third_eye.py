import csv
import requests

from datetime import datetime

# Kolide API Reference: https://kolidek2.readme.io/docs

ACCESS_TOKEN = ''
header = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}


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
        writer.writerow(['Generated at: {}'.format(datetime.now().strftime(
                                                        "%I:%M %p, %a %b %d, %Y"))])
        writer.writerow(['Total number of devices enrolled: {}\n'.format(len(data))])

    for device in data:
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
        with open('Audit Logs.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([log.get('id'), log.get('timestamp'), 
                             log.get('actor_name'), log.get('description')])

def print_banner():
    banner = '''                                        ,   ,
                                        $,  $,     ,
                                        "ss.$ss. .s'
                                ,     .ss$$$$$$$$$$s,
                                $. s$$$$$$$$$$$$$$`$$Ss
                                "$$$$$$$$$$$$$$$$$$o$$$       ,
                               s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                              s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                              s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                             s$$$$$$$$$$'         `"""ss"$"$s""
                             s$$$$$$$$$$,              `"""""$  .s$$s
                             s$$$$$$$$$$$$s,...               `s$$'  `
                         `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                           `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                 "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                  "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                   $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                  $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                             ,   ,"     '  $$$$$$$$$$$$$$$$####s
                             $.          .s$$$$$$$$$$$$$$$$$####"
                 ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                 $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                 Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                  "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
           ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
           $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
           $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
            "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
              $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
   )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
  ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
  ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
 (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
 )  ( (       $$"$$$$$$$$$$$#####.$$$$$###'                .###$$$$$$$$$$"
 (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
 ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
(   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
(   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
 )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
  (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
    \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
        `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
            `"""""""""""""'         '           '           '
https://asciiart.website
'''
    print(banner)

print_banner()
fetch_devices()
fetch_live_queries()
fetch_audit_logs()
