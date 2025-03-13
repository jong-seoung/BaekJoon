def solution(dartResult):
    num_lst = []

    dartResult = dartResult.replace("10", "&")
    for idx, dart in enumerate(dartResult):
        try:
            dart = int(dart)
            num_lst.append(dart)        
        except:
            if dart == '&':
                num_lst.append(10)        
            if dart == 'S':
                num_lst[-1] = num_lst[-1] ** 1
            elif dart == 'D':
                num_lst[-1] = num_lst[-1] ** 2
            elif dart == 'T':
                num_lst[-1] = num_lst[-1] ** 3
            elif dart == '*':
                if idx == 2:
                    num_lst[-1] = num_lst[-1] * 2
                else:
                    num_lst[-1] = num_lst[-1] * 2
                    num_lst[-2] = num_lst[-2] * 2
            elif dart == '#':
                num_lst[-1] = num_lst[-1] * -1
    return sum(num_lst) 