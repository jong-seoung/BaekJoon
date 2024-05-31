x = int(input())

def deciTobin(num):
  binary=""
  while num !=0:
    if num%2==0:
        binary="0"+binary
        num=num//2
    else:
        binary="1"+binary
        num=num//2
  return list(binary)

print(deciTobin(x).count('1'))