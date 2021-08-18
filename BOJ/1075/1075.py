n = int(input())
f = int(input())

n = int(str(n)[:-2] + '00')
result = ''

while True:
    if n % f == 0:
        result = n % 100
        break
    else:
        n += 1
if result < 9:
    result = '0' + str(result)

print(result)
