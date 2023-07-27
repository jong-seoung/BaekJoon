test_cnt = int(input())

for i in range(test_cnt):
    result = ''
    cnt, word = input().split()
    word_list = list(word)
    for j in word_list:
        result += j * int(cnt)
    print(result)