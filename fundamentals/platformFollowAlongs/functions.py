def add(a,b):
      x = a + b
      return x

print(add(4,5))

sum = add(3,5)
print(sum)

def introduction(name):
      print('Hi, ' + name)

introduction('Nat')
introduction('Mat')
introduction('looney')

def parting(name):
      return "goodbye " + name

print(parting('bob'))

def newadd(a,b):
      r = a + b
      return r

result1 = newadd(4,6)
result2 = newadd(1,4)
result3 = result1 + result2
print(result3)