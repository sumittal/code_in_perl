"""
Given a nested, dict only data, return a flat dict. eg. {a:{b:10, c:{d:20, e:30}}, f:40}
should give {a.b:10, a.b.c.d:20, a.b.c.e:30, f:40}
"""
def flatDict(d, flatten_d={}, prev_keys=[]):

    for k, v in d.items():
        if isinstance(v, dict):
            flatDict(v, flatten_d, prev_keys + [k])
        else:
            tmp_key = '.'.join(prev_keys + [k])
            flatten_d[tmp_key] = v

    return flatten_d

d = {"a":{"b":10, "c":{"d":20, "e":30}}, "f":40}
print(flatDict(d))
