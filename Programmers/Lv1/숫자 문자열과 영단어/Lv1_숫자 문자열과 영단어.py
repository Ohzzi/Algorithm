def solution(s):
    text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, value in enumerate(text):
        s = s.replace(value, str(idx))
    return int(s)