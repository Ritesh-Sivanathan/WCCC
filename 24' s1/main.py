N = int(input())
hat_number = []

for i in range(N):
    hat_number.append(int(input()))

matches = []
div_num = int(N/2) 
total = 0

for i,j in enumerate(hat_number):
    if i <= div_num-1:
        matches.append([j,hat_number[i+div_num]])

for match in matches:
    if match[0] == match[1]:
        total += 2

print(total)
