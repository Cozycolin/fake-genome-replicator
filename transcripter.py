def unfunc(inpu):
  if inpu == "/":
    a = "AA"
    return a
  if inpu == "|":
    a = "AB"
    return a
  if inpu == ">":
    a = 'BA'
    return a
  if inpu == "<":
    a = "BB"
    return a
  if inpu == "-":
    a = "AC"
    return a
  if inpu == "_":
    a = "CA"
    return a
  if inpu == "=":
    a = "BC"
    return a
  if inpu == "+":
    a = "CB"
    return a
  if inpu == "~":
    a = "CC"
    return a

symbols = list("|/<>~-_=+")
def transvert():
  inpu = input("starting symbols:")
  output1 = []
  output2 = []
  final = ''
  for a in inpu:
    for b in symbols:
      if a == b:
        output1.append(a)
  for i in output1:
    output2.append(unfunc(i))
  output3 = []
  for c in output2:
    output3.append(unshift(c))
  print("output1: "+str(output3))
  for g in output3:
    final += g
  print("genome: "+final)
    
def unshift(inpu):
  if inpu == "AB":
    a = "AA"
    return a
  if inpu == "BA":
    a = "AB"
    return a
  if inpu == "BB":
    a = "BA"
    return a
  if inpu == "AC":
    a = "AB"
    return a
  if inpu == "CA":
    a = "AC"
    return a
  if inpu == "BC":
    a = "CA"
    return a
  if inpu == "CB":
    a = "BC"
    return a
  if inpu == "CC":
    a = "CB"
    return a
  if inpu == "AA":
    a = "CC"
    return a
