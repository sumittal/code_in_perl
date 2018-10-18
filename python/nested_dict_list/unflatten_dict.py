def unflatten_dict(in_dict):
    result = {}
    for k,v in in_dict.items():
        keyss = k.split('.')
        d = result
        for key in keyss[:-1]:
            if key not in d:
                d[key] = {}
            d = d[key]
        d[keyss[-1]] = v
    return result

d = {'a.c.e': 30, 'a.c.d': 20, 'f': 40, 'a.b': 10} 
#d = {'a.c.e':30} 
res = unflatten_dict(d)
print(res)

# {'f': 40, 'a': {'b': 10, 'c': {'d': 20, 'e': 30}}}
