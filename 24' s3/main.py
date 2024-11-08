N = int(input())

A = (input()).split(" ")
B = (input()).split(" ")

if A == B:
    print("YES")
    print(0)

if A != B:

    for i,j in enumerate(A):
        for k in range(N):
            temp = []
            for l,m in enumerate(A[i:k]):
                rep = len(A[i:k])
                temp.append(A[:i]+([A[i]*rep])+A[k:])
                print(temp)