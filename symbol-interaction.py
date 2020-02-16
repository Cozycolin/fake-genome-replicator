
def unfunc(inpu):
  if inpu == "/":
    a = "a"
    return a
  if inpu == "|":
    a = "b"
    return a
  if inpu == ">":
    a = 'c'
    return a
  if inpu == "<":
    a = "d"
    return a
  if inpu == "-":
    a = "e"
    return a
  if inpu == "_":
    a = "f"
    return a
  if inpu == "=":
    a = "g"
    return a
  if inpu == "+":
    a = "h"
    return a
  if inpu == "~":
    a = "i"
    return a
def letnum(inpu):
  a = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
  b = a[inpu]
  return str(b)
cellstr = list("╩╔╗╚╝╦╤═┴┬┘└┐┌│─")

def decrypt(inpu):
  c = 0
  d = []
  for i in range(inpu.__len__()//2):
      d.append(inpu[c]+inpu[c+1])
      c += 2
  return d
def numero(inpu):
  a = cellstr[inpu-1]
  
  return a


smcombinations = list("///|/>/</-/_/  /+/~|/|||>|<|-|_| |+|~>/>|>>><>->_> >+>~</<|<><<<-<_< <+<~-/-|->-<---_- -+-~_/_|_>_<_-___ _+_~ / | > < - _   + ~+/+|+>+<+-+_+++~~/~|~>~<~-~_~ ~+~~")
symcombinations = decrypt(smcombinations)
def inter(inpu):
  q = 0
  a = list(inpu)
  for i in a:
    q += int(letnum(unfunc(i)))
  b = numero(q)
  return b

def interact():
  c = list(input("what are the symbols:"))
  a = decrypt(c)
  b = ''
  for i in a:
    b += str(inter(i))
  print(b)
