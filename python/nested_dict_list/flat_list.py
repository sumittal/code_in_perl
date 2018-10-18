def flattenList(a, res=None):
    if res is None:
        res = []

    for x in a:
        if isinstance(x, list):
            flattenList(x, res)
        else:
            res.append(x)

    return res

print(flattenList([[10, 20, [11, 22] ], [3, 6], 17]))
