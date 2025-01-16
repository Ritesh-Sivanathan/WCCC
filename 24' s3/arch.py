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