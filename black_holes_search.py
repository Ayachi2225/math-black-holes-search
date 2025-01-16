import numpy as np
for n in range(10):
    for b in range(10):
        n += 1
        b += 1
        a1 = np.random.randint(0, b, [1, n])
        l1 = a1.tolist()[0]
        l1.sort(reverse=True)
        max = 0
        min = 0
        l0 = [max]
        for x in range(n):
            max += pow(b, n - x - 1) * l1[x]
            min += pow(b, n - x - 1) * l1[n - x - 1]
        while 1:
            if max in l0 and max == l0[len(l0) - 1]:
                with open('number_balck_holes_search.txt', 'a', newline='\n') as file:
                    c = max
                    l2 = []
                    for x in range(n):
                        a2 = (c - c % pow(b, n - x - 1)) / pow(b, n - x - 1)
                        l2.append(int(a2))
                        c = c % pow(b, n - x - 1)
                    print('number of number：',n,'and', b, 'th system:', 'success!,black hole is', l2, l0, file=file)
                    break
            elif max in l0 and max != l0[len(l0) - 1]:
                with open('number_balck_holes_search.txt', 'a', newline='\n') as file:
                    print('number of number：',n,'and', b, 'th system:', 'fail,we do not find black hole', l0, file=file)
                    break
            else:
                l0.append(max)
                c = max - min
                l2 = []
                for x in range(n):
                    a2 = (c - c % pow(b, n - x - 1)) / pow(b, n - x - 1)
                    l2.append(a2)
                    c = c % pow(b, n - x - 1)
                l2.sort(reverse=True)
                max = 0
                min = 0
                for x in range(n):
                    max += pow(b, n - x - 1) * l2[x]
                    min += pow(b, n - x - 1) * l2[n - x - 1]