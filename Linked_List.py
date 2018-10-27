class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.cd
      self._value = val
      self._next = None
      self._previous = None
      
#have to use self._Node() instead of _Node()
  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    self._header = self._Node(None)
    self._trailer = self._Node(None)
    self._header._next = self._trailer
    self._trailer._previous = self._header
    self._size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    count = 0
    current = self._header
    while current._next is not self._trailer:
      #if current._value is not None
      count += 1
      current = current._next
    return count

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the tail position.
    newDude = self._Node(val)
    current = self._header
    while current._next is not self._trailer:
      current = current._next
    newDude._next = self._trailer
    newDude._previous = current
    current._next = newDude
    self._trailer._previous = newDude
    self._size +=1
    
    
  def insert_element_at(self, val, index):
    # assuming the head position is indexed 0, add a
    # node containing val at the specified index. If 
    # the index is not a valid position within the list,
    # ignore the request. This method cannot be used
    # to add an item at the tail position.
    newDude = self._Node(val)
    current = self._header
    count = 0
    if index>=self._size or index<0:
      return
    while count<index:
      current = current._next
      count += 1
    newDude._previous = current
    newDude._next = current._next
    current._next._previous = newDude
    current._next = newDude
    self._size+=1
    
  def remove_element_at(self, index):
    # assuming the head position is indexed 0, remove
    # and return the value stored in the node at the 
    # specified index. If the index is invalid, ignore
    # the request.
    current = self._header
    count = 0
    if index>=self._size or index<0:
      return
    while count<index:
      current = current._next
      count += 1
    daVal = current._next._value
    current._next = current._next._next
    current._next._previous = current
    self._size -= 1
    return daVal  

  def get_element_at(self, index):
    # assuming the head position is indexed 0, return
    # the value stored in the node at the specified
    # index, but do not unlink it from the list.
    current = self._header
    count = 0
    if index>self._size or index<0:
      return
    while count<index:
      current = current._next
      count += 1
    return current._next._value

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    if self._size==0:
      return "[ ]"
    current = self._header._next
    string ="[ "
    while current is not self._trailer._previous:
      string += str(current._value)+", "
      current = current._next
    string+= str(current._value)+" ]"
    return string
   
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

  l1 = Linked_List()
  print("Length of Empty List")
  print(l1.__len__())
  l1.append_element(1)
  print("Appended 1")
  print(l1)
  l1.append_element(2)
  print("Appended 2")
  print(l1)
  l1.append_element(3)
  print("Appended 3")
  print(l1)
  print("Length")
  print(l1.__len__())
  print("Get at -1")
  print(l1.get_element_at(-1))
  print(l1)
  print("Get at 4")
  print(l1.get_element_at(4))
  print(l1)
  print("Get at 1")
  print(l1.get_element_at(1))
  print(l1)
  print("Length")
  print(l1.__len__())
  l1.insert_element_at(5,1)
  print("Insert 5 at 1")
  print(l1)
  l1.insert_element_at(5,4)
  print("Insert at 4 (tail)")
  print(l1)
  print("Remove at 4")
  print(l1.remove_element_at(4))
  print(l1)
  print("Remove at 1")
  print(l1.remove_element_at(1))
  print(l1)
 
  # The following code should appear after your tests for your
  # linked list class.

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
  p1cur = 0
  p2cur = 0
  p3cur = 0
  while p1cur!=p1.__len__() and p2cur!=p2.__len__():
    #For Testing
    #print("p1cur: " + str(p1cur))
    #print("p2cur: " + str(p2cur))
    #print("p3cur: "+ str(p3cur))
    p1elem = p1.get_element_at(p1cur)
    p2elem = p2.get_element_at(p2cur)
    if p1elem.get_exponent()>p2elem.get_exponent():
      p3.append_element(p1elem)
      p1cur+=1
      p3cur+=1
    if p1elem.get_exponent()<p2elem.get_exponent():
      p3.append_element(p2elem)
      p2cur+=1
      p3cur+=1
    if p1elem.get_exponent()==p2elem.get_exponent():
      p3.append_element(Poly_Val(p1elem.get_coefficient()+p2elem.get_coefficient(), p1elem.get_exponent()))    
      p1cur+=1
      p2cur+=1
      p3cur+=1
  while p1cur==p1.__len__() and p2cur!=p2.__len__():
    p2elem = p2.get_element_at(p2cur)
    p3.append_element(p2elem)
    p2cur+=1
  while p2cur==p2.__len__() and p1cur!=p1.__len__():
    p1elem = p1.get_element_at(p1cur)
    p3.append_element(p1elem)
    p1cur+=1
  print(p3)
  
  # here, create the Poly_Val objects that should comprise p3
  # and add them to the list. Make sure that p3 is constructed
  # correctly regardless of the contents of p1 and p2. Try
  # building different polynomials for p1 and p2 and ensure that
  # they sum correctly.
