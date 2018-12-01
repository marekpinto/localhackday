import random
def attack():
  for x in [1]:
    r = random.randint(1,3)
  if r == 1:
    for x in [1]:
      n = [1,random.randint(1,10)]
  elif r==2:
    for x in [1]:
      n = [2,random.randint(20,30)]
  elif r == 3:
    for x in [1]:
      n = [3,random.randint(30,40)]
  else: n = [0,0]
  return n
print(attack())