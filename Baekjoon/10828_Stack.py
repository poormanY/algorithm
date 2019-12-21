import sys, os
sys.path.append(os.path.abspath('../algorithm/algorithms/Stack'))
from Stack import Stack

def main():
  s = Stack()

  N = int(sys.stdin.readline())
  for line in sys.stdin:
    words = list(line.split())
    command = words[0]

    if command == 'push':
      X = words[1]
      s.push(int(X))
    elif command == 'pop':
      value = s.pop()
      if value == None:
        print(-1)
      else:
        print(value)
    elif command == 'size':
      print(s.size())
    elif command == 'empty':
      if s.is_empty():
        print(1)
      else:
        print(0)
    elif command == 'top':
      if s.is_empty():
        print(-1)
      else:
        print(s.top())

main()
