#!/usr/bin/python
'''
'''

from binarytree import CBOrdTree
from binarytree import CNode
from binarytree import ip_as_int
import json


def get_ip_range_data(fin_path='ip_country.json'):
  ''' pulls json data from a file '''
  for line in open(fin_path, 'rb'):
    ip_info       = json.loads(line)
    yield CNode(ip_info['ip_start'], ip_info['ip_end'], ip_info['country'])


def main():
  # fetch the data from disk and init the binary lookup tree
  ip_ranges = get_ip_range_data()
  bin_tree = CBOrdTree()

  print 'Adding new IP ranges to the lookup tree'
  for new_node in get_ip_range_data():
    print '\t', new_node
    bin_tree.root = bin_tree.insert(bin_tree.root, new_node)

  print
  print 'Finished adding new IP ranges\n'

  test_data = ['0.115.0.0', 
               '0.116.0.0',
               '0.119.255.255',
               '0.120.0.0',
               '1.8.5.255'
              ]

  def test_lookup(target_ip):
    try:
      print '\t', target_ip, bin_tree.lookup(bin_tree.root, ip_as_int(target_ip))
    except Exception, ex:
      print ex
  
  print 'Testing IP lookup'
  for target_ip in test_data:
    test_lookup(target_ip)
  
  pass

if __name__ == '__main__':
  main()
