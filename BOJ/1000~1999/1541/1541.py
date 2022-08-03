equation = list(input())

number = ""
is_in_bracket = False
answer = 0
while equation:
    temp = equation.pop(0)
    if temp.isdecimal():
        number += temp
    elif temp == '-':
        if is_in_bracket:
            answer -= int(number)
        else:
            answer += int(number)
            is_in_bracket = True
        number = ""
    elif temp == '+':
        if is_in_bracket:
            answer -= int(number)
        else:
            answer += int(number)
        number = ""
if is_in_bracket:
    answer -= int(number)
else:
    answer += int(number)
print(answer)
