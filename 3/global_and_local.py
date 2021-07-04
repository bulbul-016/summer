name = 'John' # Global Variable

def greeting():
  print(f'hello {name}')
greeting()


def greeting2(n):
  name = 'Bob' # Local variable
  print(f'hello {name}')
greeting2('Alice')

