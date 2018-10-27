from Deque import Deque

class Queue:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return(str(self._dq))

  def __len__(self):
    return(len(self._dq))

  def enqueue(self, val):
    self._dq.push_back(val)

  def dequeue(self):
    return(self._dq.pop_front())

if __name__ == '__main__':
  test1 = Queue()
  print(len(test1))
  print(test1)
  test1.dequeue()
  test1.enqueue('apple')
  print(test1)
  test1.enqueue('dog')
  print(test1)
  test1.enqueue('banana')
  print(test1)
  print(test1.dequeue())
  print(test1)
  print(len(test1))
