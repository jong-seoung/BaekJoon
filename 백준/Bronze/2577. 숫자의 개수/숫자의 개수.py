num = 1

for i in range(3):
    a = int(input())
    num = a * num

num_list = list(str(num))

for i in range(10):
    print(num_list.count(str(i)))
