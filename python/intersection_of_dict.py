def intersection_dict(a1, a2):

    res = {}
    k1 = set(a1.keys())
    k2 = set(a2.keys())

    common_k = list(k1 & k2)

    
    for key in common_k:
        val1 = a1[key]
        val2 = a2[key]

        if isinstance(val1, dict) and isinstance(val2, dict):
            res[key] = get_common(val1, val2)
        elif val1 == val2:
            res[key] = val1
        else:
            print("Values for same key are not same")


    return res

def get_common(d1, d2):

    for k in list(set(d1.keys()) & set(d2.keys())):
        print("Debug : ", k)
        if isinstance(d1[k], dict):
            return {k: get_common(d1[k], d2[k])}
        else:
            return {k : d1[k]}
    

a1 = { "name": "asdf", "age": 10, "address": { "Street1": "asdfs" ,  "City": "asdaj" }, "phone": 19093109 }
a2 = { "name": "asdf", "address": { "Street1": "asdfs", "City": "asdaj" }, "phone": 19093109 }

print(intersection_dict(a1, a2))
