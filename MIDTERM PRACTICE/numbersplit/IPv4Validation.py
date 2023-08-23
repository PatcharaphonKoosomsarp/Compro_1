def isValidIP(ip):
    
    ip = ip.split(".")
    if len(ip) != 4:
        return False
    for i in ip:
        if not i.isdigit():
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True

print(isValidIP("1.2.3.4"))
print(isValidIP("1.2.3"))
print(isValidIP("1.2.3.4.5"))
print(isValidIP("123.45.67.89"))
print(isValidIP("123.456.78.90"))
print(isValidIP("123.045.067.089"))