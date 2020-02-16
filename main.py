from transverter import *
from genomecreator import *
from symbol_interaction import *
from deinteraction import *
letters = ["A","B","C"]
a = input(">>>")
# the code is 2 letters long
# to get the symbols put in CCAAABBABBACCABCCB
def func(inpu):
  if inpu == "AA":
    a = "/"
    return a
  if inpu == "AB":
    a = "|"
    return a
  if inpu == "BA":
    a = '>'
    return a
  if inpu == "BB":
    a = "<"
    return a
  if inpu == "AC":
    a = "-"
    return a
  if inpu == "CA":
    a = "_"
    return a
  if inpu == "BC":
    a = " "
    return a
  if inpu == "CB":
    a = "+"
    return a
  if inpu == "CC":
    a = "~"
    return a
def shift(inpu):
  if inpu == "AA":
    a = "AB"
    return a
  if inpu == "AB":
    a = "BA"
    return a
  if inpu == "BA":
    a = "BB"
    return a
  if inpu == "BB":
    a = "AC"
    return a
  if inpu == "AC":
    a = "CA"
    return a
  if inpu == "CA":
    a = "BC"
    return a
  if inpu == "BC":
    a = "CB"
    return a
  if inpu == "CB":
    a = "CC"
    return a
  if inpu == "CC":
    a = "AA"
    return a
def translate():
  combinations = "AABBCCACABBACACBBC"
  b = input("what is the starting genome?:")
  b = list(b)
  genes = []
  output = []
  def decrypt(inpu):
    c = 0
    d = []
    for i in range(inpu.__len__()//2):
        d.append(inpu[c]+inpu[c+1])
        c += 2
    return d

  combinations = decrypt(list(combinations))
  genes = decrypt(b)
  def check(inpu):
    outpu = []
    for i1 in range(int(inpu.__len__())):
        a = inpu[i1-1]
        for i2 in combinations:
          if a == i2:
            outpu.append(a)
    return outpu
  genes = check(genes)
  for i in range(genes.__len__()):
    output.append(shift(genes[i]))
  print("genes:"+str(genes))
  print("output:"+str(output))
  output2 = ""
  output3 = ""
  for i in range(output.__len__()):
    output2 += output[i]
  for i in range(output.__len__()):
    output3 += func(output[int(i)])
  print("output2: "+output2 + "")
  print("output3: "+output3+"")
