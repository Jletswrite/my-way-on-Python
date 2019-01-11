def collatz(num):
  if num%2==0:
    print('this is oushu')
    return num/2
  if num%==1:
    print('this is jishu')
    return 3*num+1
r=int(input())
while r!=1:
  r=collatz(r)
  if r==1:
    break
print('you got it')
