def commify(num):
    if num is None:
        return None

    num = str(num)
    if '.' in num:
        f, s = num.split(".")
    else:
        f, s = num, None

    r = []
    for i, c in enumerate(str(f)[::-1]):
        if i and ( i%3 == 0):
            r.insert(0,',')
        r.insert(0,c)

    out = ''.join(r)
    if s:
        out = out + "." + s
    return out

print(commify(1))
print(commify(123))
print(commify(1234))
print(commify(1234567890))
print(commify(123.0))
print(commify(123.50))
print(commify(1234.56789))
print(commify(None))


