class AVL_Tree:

  class _AVL_Node:
    # Private class 

    def __init__(self, value):
      self._value = value
      self._left = None
      self._right = None
      self._height = 0


  def __init__(self):
    self._root = None


  def _check_height(self, location):
    # Method that checks the height of subtrees after a recursive delete or insert
    if location is None:
      return 0
    else:
      return max(self._check_height(location._left), self._check_height(location._right)) + 1

  def _balance_factor(self, location):
    # Used by self._balance to determine the balance of the subtree root
    # and the correspondign subtrees
    if location is None:
      return 0
    elif location._right is None and location._left is None:
      return 0
    elif location._right is None:
      return 0 - location._left._height
    elif location._left is None:
      return location._right._height
    else:
      return location._right._height - location._left._height


  def _balance(self, location):
    # Comprehensive balancing method for all 4 cases of un-balanced trees
    bal = self._balance_factor(location)
    bal_left = self._balance_factor(location._left)
    bal_right = self._balance_factor(location._right)

    # left heavy
    if bal == -2:

      # left, left rotation
      if bal_left == -1:
        if location._left._right is None:
          temp_tree = None
        else:
          temp_tree = location._left._right
        new_root = location._left
        location._left = temp_tree
        new_root._right = location
        to_return = new_root

      # left, right rotation
      else:
        # first rotation
        if location._left._right._left is None:
          temp_tree = None
        else:
          temp_tree = location._left._right._left
        new_left = location._left._right
        temp2 = location._left
        temp2._right = temp_tree
        new_left._left = temp2
        location._left = new_left

        # second rotation
        if location._left._right is  None:
          temp = None
        else:
          temp = location._left._right
        new_root = location._left
        location._left = temp
        new_root._right = location
        to_return = new_root 


      to_return._left._height = self._check_height(to_return._left)
      to_return._height = self._check_height(to_return)
      return to_return

    # right heavy
    elif bal == 2:

      # right, right
      if bal_right == 1:
        if location._right._left is  None:
          temp_tree = None
        else:
          temp_tree = location._right._left
        new_root = location._right
        location._right = temp_tree
        new_root._left = location
        to_return = new_root

      # right, left
      else: 
        # first rotation
        if location._right._left._right is None:
          temp_tree = None
        else:
          temp_tree = location._right._left._right
        new_right = location._right._left
        temp2 = location._right
        temp2._left = temp_tree
        new_right._right = temp2
        location._right = new_right

        # second rotation
        if location._right._left is None:
          temp = None
        else:
          temp = location._right._left
        new_root = location._right
        location._right = temp
        new_root._left = location
        to_return = new_root 


      to_return._right._height = self._check_height(to_return._right)
      to_return._height = self._check_height(to_return)
      return to_return

    # no balance necessary
    else:
      return location


  def _recursive_insert(self, val, location):
    # Recursive function for insertions. Called by insert_element
    if location is None:
      location = self._AVL_Node(val)
    elif location._value > val:
      location._left = self._recursive_insert(val, location._left)
    elif location._value < val:
      location._right = self._recursive_insert(val, location._right)
    location._height = self._check_height(location)
    location = self._balance(location)
    return location


  def insert_element(self, value):
    # Insert the value specified into the tree using a helper, recursive method
    self._root = self._recursive_insert(value, self._root)


  def _get_new_root(self, location):
    # Used by _recursive_remove to find the new root value for a deletion
    if location._left is None:
      return location._value
    else:
      return self._get_new_root(location._left)

  def _recursive_remove(self, val, location):
    # Helper method used to remove elements
    if location is None:
      return location
    elif val < location._value:
      location._left = self._recursive_remove(val, location._left)
      location._height = self._check_height(location)
      location = self._balance(location)
      return location
    elif val > location._value:
      location._right = self._recursive_remove(val, location._right)
      location._height = self._check_height(location)
      location = self._balance(location)
      return location
    else:
      if location._right is None and location._left is None:
        location = None
      elif location._right is None:
        location = location._left
        location._height = self._check_height(location)
        location = self._balance(location)
      elif location._left is None:
        location = location._right
        location._height = self._check_height(location)
        location = self._balance(location)
      else:
        location._value = self._get_new_root(location._right)
        location._right = self._recursive_remove(location._value, location._right)
        location._height = self._check_height(location)
        location = self._balance(location)
      return location


  def remove_element(self, value):
    # Remove the value specified from the tree with a helper method
    if self._root is not None:
      self._root = self._recursive_remove(value, self._root)

  def _recursive_in_order(self, location):
    # In-order tree traversal
    to_return = []
    if location._left is not None:
      to_return.extend(self._recursive_in_order(location._left))
    to_return.append(location._value)
    if location._right is not None:
      to_return.extend(self._recursive_in_order(location._right))
    return to_return

  def _recursive_pre_order(self, location):
    # Pre-order tree traversal
    to_return = []
    to_return.append(location._value)
    if location._left is not None:
      to_return.extend(self._recursive_pre_order(location._left))
    if location._right is not None:
      to_return.extend(self._recursive_pre_order(location._right))
    return to_return

  def _recursive_post_order(self, location):
    # Post-order tree traversal
    to_return = []
    if location._left is not None:
      to_return.extend(self._recursive_post_order(location._left))
    if location._right is not None:
      to_return.extend(self._recursive_post_order(location._right))
    to_return.append(location._value)
    return to_return

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ].
    if self._root is None:
      return "[ ]"
    else:
      to_return = self._recursive_in_order(self._root)
      to_return = '[ ' + ', '.join(str(i) for i in to_return) + ' ]'
      return to_return


  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    if self._root is None:
      return "[ ]"
    else:
      to_return = self._recursive_pre_order(self._root)
      to_return = '[ ' + ', '.join(str(i) for i in to_return) + ' ]'
      return to_return

  def post_order(self):
    # Construct and return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    if self._root is None:
      return "[ ]"
    else:
      to_return = self._recursive_post_order(self._root)
      to_return = '[ ' + ', '.join(str(i) for i in to_return) + ' ]'
      return to_return

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1.
    if self is None:
      return 0
    elif self._root is None:
      return 0
    else: 
      return self._root._height

  def __str__(self):
    return self.in_order()


if __name__ == '__main__':

  # Does an empty AVL tree print properly?
  test01 = AVL_Tree()
  print('Expected: [ ] Actual: ', test01)
 
  # Does an AVL tree insert properly?
  test01.insert_element(10)
  print('Expected: [ 10 ] Actual: ', test01)
  test01.insert_element(5)
  test01.insert_element(15)
  print('Expected: [ 5, 10, 15 ] Actual: ', test01)

  # Does an AVL tree balance properly when it needs to make a single rotation
  # to the right?
  test01.insert_element(3)
  test01.insert_element(1)
  print('Expected: [ 1, 3, 5, 10, 15 ] Actual: ', test01)

  # Does an AVL tree balance properly when it needs to make a single rotation
  # to the left?
  test01.insert_element(20)
  test01.insert_element(25)
  print('Expected: [ 1, 3, 5, 10, 15, 20, 25 ] Actual: ', test01)

  # Does an AVL tree balance properly when it needs to make a left, right 
  # rotation?
  test01.insert_element(13)
  test01.insert_element(14)
  print('Expected: [ 1, 3, 5, 10, 13, 14, 15, 20, 25] Actual: ', test01)


  # Does an AVL tree balance properly when it needs to make a right, right 
  # rotation AND a second rotation (left, right) higher up the tree?
  test01.insert_element(17)
  print('root', test01._root._value)
  test01.insert_element(16)
  print('Expected: [ 1, 3, 5, 10, 13, 14, 15, 16, 17, 20, 25 ] Actual: ', test01)
  print('root', test01._root._value)
  print(test01.pre_order())
  print(test01.post_order())


  # Does an AVL tree remove a node with two subtrees properly?
  test01.remove_element(15)
  print('Expected: [ 1, 3, 5, 10, 13, 14, 16, 17, 20, 25 ] Actual: ', test01)

  # Does an AVL tree remove a node with one subtree properly?
  test01.remove_element(14)
  print('Expected: [ 1, 3, 5, 10, 13, 16, 17, 20, 25 ] Actual: ', test01)
  print(test01.pre_order())
  print(test01.post_order())


  # Does an AVL tree remove a leaf node properly?
  test01.remove_element(1)
  print('Expected: [ 3, 5, 10, 13, 16, 17, 20, 25 ] Actual: ', test01)

  # Does deleting every node return an empty tree? Is the tree height correct?
  test01.remove_element(16)
  print(test01.post_order())
  print(test01.get_height())

  test01.remove_element(17)
  print(test01.post_order())
  print(test01.get_height())

  test01.remove_element(10)
  print(test01.post_order())
  print(test01.get_height())

  test01.remove_element(20)
  print(test01.post_order())
  print(test01.get_height())

  test01.remove_element(25)
  print(test01.post_order())
  print(test01.get_height())

  test01.remove_element(5)
  print(test01.post_order())
  print(test01.get_height())

  test01.remove_element(13)
  print(test01.post_order())
  print(test01.get_height())

  test01.remove_element(3)
  print(test01.post_order())
  print(test01.get_height())










