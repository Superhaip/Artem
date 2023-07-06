def is_palindrome(string):
    return string == string[::-1]

s = input("введи строку для проверки на полидром: ")
print(is_palindrome(s))