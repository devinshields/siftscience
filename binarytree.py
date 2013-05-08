#!/usr/bin/python
''' binary tree and node classes
      some code borrowed from: http://code.activestate.com/recipes/286239-binary-ordered-tree/

    TODO, IMPROVEMENTS, OPTIMIZATIONS:
        1) make the tree self balancing to avoid long tail inserts/lookups
        2) cache popular lookups/IP ranges
        3) merge adjacent nodes, e.g. merge (12, 17) and (18-21) into (12-21)
'''


def ip_as_int(ip):
  ''' converts string IP addresses to ints '''
  ip_as_bytes = map(int, ip.split('.'))
  return sum(i * j for i,j in zip(ip_as_bytes, [16777216, 65536, 256, 1]))  # multipliers are: [256**i for i in range(4)][::-1]


def ip_ranges_do_overlap(range0, range1):
  ''' checks if two IP ranges overlap. Assumes that each 2tuple IP is ordered '''
  return not ((range1[0] < range0[0] and range1[1] < range0[0]) or (range0[0] < range1[0] and range0[1] < range1[0]))


class CNode:
  ''' encapsulation of a range of IP addresses. also serves as a node object in a binary tree '''
  left, right, data = None, None, None
  
  def __init__(self, ip_start, ip_end, country_code):
    self.ip_start = ip_start
    self.ip_end   = ip_end
    self.data = tuple(map(ip_as_int, (ip_start, ip_end)))
    self.country_code = country_code

  def contains(self, target_ip):
    ''' tests if a node's IP range contains the target '''
    return self.data[0] <= target_ip and target_ip <= self.data[1]

  def __str__(self):
    return str((self.ip_start, self.ip_end,  self.country_code))


class CBOrdTree:
  '''  '''
  def __init__(self):
    self.root = None

  def insert(self, cur_node, new_node):
    ''' add a new node to the binary tree '''
    if not cur_node:
      return new_node
    else:
      if ip_ranges_do_overlap(cur_node.data, new_node.data):
        raise Exception("Oh no! the IP range you're trying to insert overlaps with an existing IP range. Mega-fail.")
      if new_node.data <= cur_node.data:
        cur_node.left = self.insert(cur_node.left, new_node)
      else:
        cur_node.right = self.insert(cur_node.right, new_node)
      return cur_node

  def lookup(self, cur_node, target_ip):
    if not cur_node:
      raise Exception('LOOKUP ERROR: No country avilable for this IP address.')
    if cur_node.contains(target_ip):
      return cur_node.country_code
    else:
      if target_ip < cur_node.data[0]:
        return self.lookup(cur_node.left, target_ip)
      else:
        return self.lookup(cur_node.right, target_ip)

  pass
