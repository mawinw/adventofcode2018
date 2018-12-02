l=[]
i=input()
while(i!='a'):
  opcode=i[0]
  operand=int(i[1:])
  if(opcode=="-"):
    operand=-operand
  l.append(operand)
  i=input()
d={0:1}
s=0
found=False
while(not found):
  for i in l:
    s+=i
    if s not in d.keys():
      d[s]=0
    else:
      found=True
      print("found at !")
      print(s)
      print("found at !")
      break
