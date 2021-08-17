def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        words = [s[j:j + i] for j in range(0, len(s), i)]
        compressed = ""
        prev = words[0]
        cnt = 1
        for word in words[1:]:
            if word == prev:
                cnt += 1
            else:
                if cnt != 1:
                    compressed += str(cnt)
                compressed += prev
                cnt = 1
            prev = word
        if cnt != 1:
            compressed += str(cnt)
        compressed += words[-1]
        if len(compressed) < answer:
            answer = len(compressed)

    return answer
