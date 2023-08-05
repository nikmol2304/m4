def check_palindrom(stroka):
    if stroka == stroka[::-1]:
        return True
    else:
        return False
print(check_palindrom('лепспел'))
