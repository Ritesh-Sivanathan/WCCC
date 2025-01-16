N = int(input())

# tc1 = '3 1 2'
# tc2 = '3 1 1'

tc1 = '3 1 2 4 3 1 2 3 4 5 6'
tc2 = '3 1 1 4 5 6 1 2 3 4 5'

A = [int(i) for i in ((tc1).split(' '))]
B = [int(i) for i in ((tc2).split(' '))]

# A = [int(i) for i in ((input()).split(' '))]
# B = [int(i) for i in ((input()).split(' '))]

# A = [int(i) for i in ((input()).split(' '))]
# B = [int(i) for i in ((input()).split(' '))]

state = False
equal = False
rt = A.copy()
lt = A.copy()
temp = A.copy()
dir, p, o, f = '', 0, 0, 0

if A == B:
    print("YES")
    print(0)
    state = True
    equal = True

if state == False:

    for i in reversed(range(len(lt))):
        s = i
        for j in reversed(range(s)):      
            lt[j] = temp[i]      
            if lt == B:       
                dir = 'L'
                o = A[i]
                p = A[j]
                f = s-j
                state = True
                break
        lt = A.copy()
        
    for i in rt:

        s = len(rt)

        for j in range(s):
            rt[j] = i
            if rt == B:
                dir = 'R'
                p = i
                o = A[j]
                f = s-j
                state = True
                break
        rt = A.copy()

if not state:
    print("NO")

if state and not equal:
    print("YES")
    print(f)
    print(dir, p, o)




# tc1 = '1 2 3 4'
# tc2 = '3 3 3 4'

# tc1 = '1 2 3'
# tc2 = '1 2 3'