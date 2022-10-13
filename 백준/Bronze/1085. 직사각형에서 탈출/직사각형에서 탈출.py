x, y, w, h = map(int,input().split())

a =[abs(0-x),abs(0-y),abs(w-x),abs(y-h)]

print(min(a))