from re import split


get_ST = input()

ST = get_ST.split()
try:
  S = ST [0]
  T = ST [1]
except:
  print("")
def get_x():
  for i in range(len(S)):
    if(S[i]=='X' or S[i]=='x'):
      return i

def using_x(j):
  return T[j]


#main
print(using_x(get_x()))
