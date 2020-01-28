class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value) 
    val_index = len(self.storage) - 1
    self._bubble_up(val_index)



  def delete(self):
    max_num = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()

    self._sift_down(0)
    return max_num
 
  
  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      initial = (index - 1 ) // 2
      if self.storage[index] > self.storage[initial]:
          self.storage[index] , self.storage[initial] = self.storage[initial] , self.storage[index]
          index = initial 
      else:
          break

  def _sift_down(self, index):
    max_index = len(self.storage) - 1
    child_index = (2 * index) + 1

    while child_index <= max_index:
      right_child_index = child_index + 1
      if right_child_index <= max_index and self.storage[right_child_index] > self.storage[child_index]:
        child_index = right_child_index

      if self.storage[child_index] > self.storage[index]:
        self.storage[child_index], self.storage[index] = self.storage[index], self.storage[child_index]
        index = child_index
        child_index = (2 * index) + 1
      
      else:
          break