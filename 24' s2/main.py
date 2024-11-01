T,N = ' '.split(input()) # T --> lines, N --> lowercase letters of alphabet
strings = []
heavies = []
truths = []

for i in range(T):
    strings.append(str(input()))


for index1, string in enumerate(strings):
    for index2, letter in enumerate(string):
        if string.count(letter) > 1:
            heavies.append(letter)
            truths.append([index1,index2, 1])
        else:
            truths.append([index1,index2,0])

print(truths)



# for string in strings:
#     for letter in strings:
#         if letter not in heavies and string