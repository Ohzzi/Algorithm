# def is_palindrome(word):
#     return word == word[::-1]

# def len_shortest_palindrome(word):
#     if is_palindrome(word):
#         return len(word)
#     for i in range(len(word)):
#         if is_palindrome(word + word[i::-1]):
#             return len(word) + i + 1

# word = input()
# print(len_shortest_palindrome(word))

word = input()
for i in range(len(word)):
    if word[i:] == word[i:][::-1]:
        print(len(word) + i)
        break
