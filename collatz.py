def collatz(num):
  if num%2==0:
    print(str(num/2))
    return num/2
  if num%2==1:
    print(str(3*num+1))
    return 3*num+1
r=int(input())
while r!=1:
  r=collatz(r)
  if r==1:
    break
print('you got it')
