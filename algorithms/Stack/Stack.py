import sys, io
# Print out for Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.is_empty():
      return None
    return self.items.pop()

  def size(self):
    return len(self.items)

  def is_empty(self):
    if len(self.items) == 0:
      return True
    return False

  def top(self):
    if self.is_empty():
      return None
    return self.items[-1]

# Main Function
def main():
  s = Stack()
  s.push(1)
  s.push(2)
  print(s.size())
  print(s.is_empty())
  print(s.top())

  print(s.pop())
  print(s.size())
  print(s.is_empty())
  print(s.top())

  print(s.pop())
  print(s.size())
  print(s.is_empty())
  print(s.top())

  print(s.pop())
  print(s.size())
  print(s.is_empty())
  print(s.top())

if __name__ == '__main__':
  main()
