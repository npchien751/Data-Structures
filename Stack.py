from Deque import Deque

class Stack:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return(str(self._dq))

  def __len__(self):
    return(len(self._dq))

  def push(self, val):
    self._dq.push_back(val)

  def pop(self):
    return(self._dq.pop_back())

  def peek(self):
    return(self._dq.peek_back())

if __name__ == '__main__':
  test1 = Stack()
  print(test1)
  print(len(test1))
  test1.pop()
  test1.push(44)
  print(test1)
  test1.push(56)
  print(test1)
  test1.push(999)
  print(test1)
  print(test1.pop())
  print(test1)
  print(test1.peek())
  print(test1)
  print(len(test1))
  
