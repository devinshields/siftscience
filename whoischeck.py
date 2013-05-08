#!/usr/bin/python

import os
import json

def get_ip_range_data(fin_path='ip_country.json'):
  ''' pulls json data from a file '''
  for line in open(fin_path, 'rb'):
    yield json.loads(line)


def fetch_from_whois(target_ip):
  ''' uses the system whois tool to verify the JSON data externally '''
  cmd      = "whois {0} | grep -i -e 'City' -e 'Country' | tr '[:lower:]' '[:upper:]' | sort | uniq".format(target_ip)
  response = '\n'.join(map(lambda s: '\t' + s, os.popen(cmd).read().strip().split('\n')))
  return '\tTesting IP: {0}'.format(target_ip) + '\n' + response


def main ():

  for js in get_ip_range_data():
    print js
    print fetch_from_whois(js['ip_start'])
    print

  pass

if __name__ == '__main__':
  main()
