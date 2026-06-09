
def is_palindrome(word):
    word = word.lower()
    
    if word == word[::-1]:
        return True
    else:
        return False

user_input = input("Check Palindrome: ")
print(is_palindrome(user_input))


