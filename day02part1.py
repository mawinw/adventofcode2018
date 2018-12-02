s=input().strip()
ans={}
ans[2]=0
ans[3]=0
l=[]
while(s!="-1"):
  l.append("".join(sorted(s)))
  s=input().strip()
for s in l:
  substr=[]
  while(s!=""):
    i=0
    letter=s[0]
    while(i<len(s) and letter==s[i]):
      i+=1
    substr.append(s[0:i])
    s=s[i:]
  doubleletterflag=False
  tripleletterflag=False
  for e in substr:
    if(len(e)==2):
      doubleletterflag=True
    elif(len(e)==3):
      tripleletterflag=True
  if(doubleletterflag):
    ans[2]+=1
  if(tripleletterflag):
    ans[3]+=1
print("eiei")
print(ans[2])
print("eieiei")
print(ans[3])
