from symbol_interaction import decrypt
import random as ran

def dein(inpu):
  if inpu == "a":
    a = "/"
    return a
  if inpu == "b":
    a = "|"
    return a
  if inpu == "c":
    a = '>'
    return a
  if inpu == "d":
    a = "<"
    return a
  if inpu == "e":
    a = "-"
    return a
  if inpu == "f":
    a = "_"
    return a
  if inpu == "g":
    a = "="
    return a
  if inpu == "h":
    a = "+"
    return a
  if inpu == "i":
    a = "~"
    return a
#╩╔╗╚╝╦╤═┴┬┘└┐┌│─
nums = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
cellstr = {'╩':1,'╔':2,'╗':3,'╚':4,'╝':5,'╦':6,'╤':7,'═':8,'┴':9,'┬':10,'┘':11,'└':12,'┐':13,'┌':14,'│':15,'─':16}

def unsym(inpu):
  a = []
  d = True
  x = ran.randint(1,6)
  c = 0
  for i in nums:
   for n in nums:
      if inpu == i+n and d == True:
        c += 1
        a = list(nums[i]+nums[n])
        if c == x:
          d = False
  b = ''
  for i in a:
    b += dein(i)
  return b
def deinteract ():
  a = list(input("what are the charectars?:"))
  b = []
  for i in a:
    b.append(cellstr[i])
  f = ''
  for n in b:
    f += unsym(n)
  print(f)
