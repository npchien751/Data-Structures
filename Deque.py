from Linked_List import Linked_List

class Deque:

  def __init__(self):
    self._list = Linked_List()

  def __str__(self):
    return str(self._list)

  def __len__(self):
    return len(self._list)

  def push_front(self, val):
    if len(self._list) == 0:
      self._list.append_element(val)
    else:
      self._list.insert_element_at(val, 0)
  
  def pop_front(self):
    return(self._list.remove_element_at(0))

  def peek_front(self):
    return(self._list.get_element_at(0))

  def push_back(self, val):
    self._list.append_element(val)
  
  def pop_back(self):
    return(self._list.remove_element_at(len(self) - 1))

  def peek_back(self):
    return(self._list.get_element_at(len(self) - 1))

if __name__ == '__main__':
  test1 = Deque()
  print(test1)
  print(len(test1))
  test1.push_front(3)
  print(test1)
  test1.push_front(5)
  print(test1)
  test1.push_front(7)
  print(test1)
  test1.push_back(8)
  print(test1)
  print(test1.pop_front())
  print(test1)
  print(test1.peek_front())
  print(test1)
  print(test1.pop_back())
  print(test1)
  print(test1.peek_back())
  print(test1)
  print(len(test1))
