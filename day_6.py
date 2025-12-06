lines = open('input.txt', 'r').read().splitlines()

def first():
    ans = 0
    arr = []

    for line in lines:
        if len(arr) == 0:
            a = []
            for w in map(lambda x: x.strip(), line.split(' ')):
                if w == '':
                    continue
                a.append([int(w)])
            arr.append(a)
        elif line[0] == '+' or line[0] == '*':
            s = line.split(' ')
            ind = 0
            for w in map(lambda x: x.strip(), line.split(' ')):
                if w == '':
                    continue
                sum = 1 if w == '*' else 0
                for item in arr[0][ind]:
                    # print(item)
                    if w == '*':
                        sum *= item 
                    else:
                        sum += item 
                ans += sum
                ind += 1
            print(ans)
        else:
            s = line.split(' ')
            ind = 0
            for w in map(lambda x: x.strip(), line.split(' ')):
                if w == '':
                    continue
                a[ind].append(int(w))
                ind += 1

def second():
    ans = 0
    mat = []

    for line in lines:
        l = []
        if len(mat) == 0:
            for i in range(len(line)):
                l.append(line[i])
            mat.append(l)
        elif line[0] == '+' or line[0] == '*':
            word = [''] * len(mat[0])
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    word[j] += mat[i][j]
            # print('##########################')
            # print(word)

            ind = 0
            for w in map(lambda x: x.strip(), line.split(' ')):
                if w == '':
                    continue

                sum = 1 if w == '*' else 0
                while ind < len(word) and word[ind].strip(' ') != '':
                    num = int(word[ind].strip(' '))
                    # print(num, end = ' ')
                    if w == '*':
                        sum *= num
                    else:
                        sum += num
                    ind += 1
                ind += 1
                # print(sum)
                ans += sum
            print(ans)
        else:
            for i in range(len(line)):
                l.append(line[i])
            mat.append(l)

second()