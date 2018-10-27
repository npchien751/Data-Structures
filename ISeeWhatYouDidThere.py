# Nathaniel Chien and Patrick Savage
# Team Name: I See What You Did There
# Project 2: Linked List class implementation

# Linked List class
class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      
      self._next = None
      self._prev = None
      self._val = val
      

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    
    self._header = self._Node(None)
    self._trailer = self._Node(None)
    self._header._next = self._trailer
    self._trailer._prev = self._header
    

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    
    if self._header._next is self._trailer:
      return 0
    current = self._header._next
    count = 0
    while current is not self._trailer:
      count += 1
      current = current._next
    return count

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the tail position.
    
    new = self._Node(val)
    if self._header._next is not self._trailer:
      current = self._header._next
      while current._next is not self._trailer:
        current = current._next
      new._next = current._next
      new._prev = current
      self._trailer._prev = new
      current._next = new
    else:
      new._next = self._trailer
      new._prev = self._header
      self._trailer._prev = new
      self._header._next = new

  def insert_element_at(self, val, index):
    # assuming the head position is indexed 0, add a
    # node containing val at the specified index. If 
    # the index is not a valid position within the list,
    # ignore the request. This method cannot be used
    # to add an item at the tail position.
    
    if (index > len(self) - 1) or (index < 0):
      return
    new = self._Node(val)
    if index == 0:
      new._next = self._header._next
      new._prev = self._header
      self._header._next = new
      new._next._prev = new
    else:
      current = self._header._next
      count = 0
      while count != index - 1:
        current = current._next
        count += 1
      new._next = current._next
      new._prev = current
      new._next._prev = new
      current._next = new
 
    	    
  def remove_element_at(self, index):
    # assuming the head position is indexed 0, remove
    # and return the value stored in the node at the 
    # specified index. If the index is invalid, ignore
    # the request.
    
    if (index > len(self) - 1) or (index < 0):
      return
    if index == 0:
      to_return = self._header._next._val
      self._header._next = self._header._next._next
      self._header._next._prev = self._header
    else:
      current = self._header._next
      count = 0
      while count != index - 1:
        current = current._next
        count += 1
      to_return = current._next._val
      current._next = current._next._next
      current._next._prev = current
    return to_return
    
    

  def get_element_at(self, index):
    # assuming the head position is indexed 0, return
    # the value stored in the node at the specified
    # index, but do not unlink it from the list.

    if index > len(self) or index < 0:
      return
    if index == 0:
      to_return = self._header._next._val
    else:
      current = self._header._next
      count = 0
      while count != index - 1:
        current = current._next
        count += 1
      to_return = current._next._val
    return to_return
    
  

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    
    current = self._header._next
    to_return = "[ "
    for i in range(len(self)):
      to_return = to_return + str(current._val)
      if i != (len(self) - 1):
        to_return += ", "
      current = current._next
    to_return = to_return + " ]"
    return to_return

class Poly_Val:
  
  def __init__(self, coef, exp):
    self._coefficient = coef
    self._exponent = exp
  
  def get_coefficient(self):
    return self._coefficient
  
  def get_exponent(self):
    return self._exponent
  
  def __str__(self):
    return str(self._coefficient) + 'x^' + str(self._exponent)

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods ignore your
  # requests when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location?
  
  # create an empty linked list and check that its length == 0
  test1 = Linked_List()
  print(test1)
  print(len(test1))
  
  # does the append method work?
  test1.append_element(7)
  print(test1)
  print(len(test1))
  test1.append_element(-8)
  print(test1)
  print(len(test1))
  test1.append_element('b')
  print(test1)
  print(len(test1))
  
  # does the insert_element_at method work?
  test1.insert_element_at('a', 3)
  print(test1)
  test1.insert_element_at(4, 1)
  print(test1)
  test1.insert_element_at('h', 0)
  print(test1)  
  test1.insert_element_at(999, -1)
  print(test1)
  test1.insert_element_at(999, 6)
  print(test1)
  
  # does the remove_element_at method work?
  print(test1.remove_element_at(5))
  print(test1)
  print(test1.remove_element_at(2))
  print(test1)
  print(test1.remove_element_at(-1))
  print(test1)
  print(test1.remove_element_at(0))
  print(test1)
  
  # does the get_element_at method work?
  print(test1.get_element_at(1))
  print(test1.get_element_at(0))
  print(test1.get_element_at(-1))
  print(test1.get_element_at(3))
  
  # does the length method work?
  test2 = Linked_List()
  print(len(test2))
  test2.append_element(3)
  test2.append_element(999)
  print(len(test2))
  test2.remove_element_at(1)
  print(len(test2))
  
  
  
  # creating polynomials with the linked list class
  p1 = Linked_List()
  p1.append_element(Poly_Val(10,1012))
  p1.append_element(Poly_Val(5,14))
  p1.append_element(Poly_Val(1,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,1990))
  p2.append_element(Poly_Val(-2,14))
  p2.append_element(Poly_Val(11,1))
  p2.append_element(Poly_Val(5,0))

  p3 = Linked_List()

  # add the newly created polynomials to create a third polynomial
  count1 = 0
  count2 = 0
  current1 = p1.get_element_at(count1)
  current2 = p2.get_element_at(count2)
  if current1 == None:
    p3 = p2
  if current2 == None:
    p3 = p1
  else:
    while (current1 != None) and (current2 != None):
      while current1.get_exponent() > current2.get_exponent():
        p3.append_element(current1)
        count1 += 1
        current1 = p1.get_element_at(count1)
      while current2.get_exponent() > current1.get_exponent():
        p3.append_element(current2)
        count2 += 1
        current2 = p2.get_element_at(count2)
      if current1.get_exponent() == current2.get_exponent():
        temp = current1.get_coefficient() + current2.get_coefficient()
        p3.append_element(Poly_Val(temp, current1.get_exponent()))
        count1 += 1
        count2 += 1
        current1 = p1.get_element_at(count1)
        current2 = p2.get_element_at(count2)
  
  print(p3)
  
  
  

  
  