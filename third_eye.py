import requests

# Kolide API Reference: https://kolidek2.readme.io/docs
# curl -H "Authorization: Bearer $MYTOKEN" -X GET 'https://k2.kolide.com/api/v0/devices'

ACCESS_TOKEN = ''
K2_DEVICES_URL = 'https://k2.kolide.com/api/v0/devices'

header = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}


def fetch_devices():
    response = requests.get(K2_DEVICES_URL, headers=header)
    
    data = response.json().get('data')
    print('Total number of devices enrolled: {}\n'.format(len(data)))
    for device in data:
        print('Device ID: {}'.format(device.get('id')),
              'Device Name: {}'.format(device.get('name')), 
              'Platform: {}'.format(device.get('platform')), 
              'OS: {}'.format(device.get('operating_system')),
              'Enrolled At: {}'.format(device.get('enrolled_at')),
              'Last Seen At: {}'.format(device.get('last_seen_at')),
              'Primary User: {}'.format(device.get('primary_user_name')),
              'Remote IP: {}'.format(device.get('remote_ip')),
              'Location: {}'.format(device.get('location')), 
              '', sep='\n')

def fetch_live_queries():
    K2_LIVE_QUERY_URL = 'https://k2.kolide.com/api/v0/live_queries'
    response = requests.get(K2_LIVE_QUERY_URL, headers=header)

    data = response.json().get('data')
    print('Total number of live queries: {}'.format(len(data)))
    for query in data:
        # print(query.get('name'), query.get('osquery_sql'))
        
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

# fetch_devices()
#print_banner()
fetch_live_queries()
