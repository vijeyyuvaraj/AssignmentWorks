inputStr = "I want to become a Data Scientist."
def strEncrypt(i):
    i = ord(i)-96;
    return chr((26-i)+97)
def encrypt(i):
    if i == ' ':
        return '$'
    elif i == '.':
        return i
    else:
        return strEncrypt(str.lower(i))

for i in inputStr:
    print(encrypt(i),end='')