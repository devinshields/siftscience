#!/usr/bin/python
'''
'''

from binarytree import CBOrdTree
from binarytree import CNode


import json


def get_ip_range_data(fin_path='ip_country.json'):
  ''' pulls json data from a file '''
  for line in open(fin_path, 'rb'):
    ip_info       = json.loads(line)
    node = CNode(ip_info['ip_start'], ip_info['ip_end'], ip_info['country'])
    print node
    yield node


def main():
  # fetch the data from disk and init the binary tree
  ip_ranges = get_ip_range_data()
  bin_tree = CBOrdTree()

  # start inserting IP ranges into the tree
  for new_node in get_ip_range_data():
    bin_tree.root = bin_tree.insert(bin_tree.root, new_node)

  # test the lookup
  print bin_tree.lookup(bin_tree.root, '124.24.53.119')
  pass

if __name__ == '__main__':
  main()
