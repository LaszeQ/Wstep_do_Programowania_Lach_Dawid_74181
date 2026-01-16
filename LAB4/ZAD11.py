def odwroc_string(s):
    if len(s) == 0:
        return s
    else:
        return odwroc_string(s[1:]) + s[0]

print(odwroc_string("Python"))