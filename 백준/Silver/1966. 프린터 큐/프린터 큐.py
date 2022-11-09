import sys
n = int(sys.stdin.readline())

for _ in range(n):
    n,m = list(map(int,sys.stdin.readline().split( )))
    lst = list(map(int,sys.stdin.readline().split( )))
    lst2 = list(range(n))
    lst2[m] = 't'
  
    
    cnt = 0
    
    while(1):
        
        if lst[0]==max(lst):
            cnt += 1
                        
            
            if lst2[0]=='t':
                print(cnt)
                break
            else:
                lst.pop(0)
                lst2.pop(0)

        else:
            lst.append(lst.pop(0))
            lst2.append(lst2.pop(0))   