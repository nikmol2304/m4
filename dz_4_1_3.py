def check_palindrom(str):
    if str == str[::-1]:
        return True
    else:
        return False
print(check_palindrom('лепспел'))
