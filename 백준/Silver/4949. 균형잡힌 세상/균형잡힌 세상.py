while(1):
    a = input()
    if a == ".":
        break
    cnt = []
    for i in a:
        if i == "[" or i == "(":
            cnt.append(i)
        elif i == "]":
            if len(cnt) == 0:
                cnt.append("NULL")
            elif cnt[-1] == "[":
                cnt.pop()
            else:
                cnt.append("NULL")
        elif i == ")":
            if len(cnt) == 0:
                cnt.append("NULL")
            elif cnt[-1] == "(":
                cnt.pop()
            else:
                cnt.append("NULL")
        elif i == ".":
            if len(cnt) == 0:
                print("yes")
            else:
                print("no")