
"""
    Generate all permutation of a string in lexicographically sorted order with repetition of characters possible.
    Link : https://www.educative.io/page/11000001/90001
"""

def permute(input_str):
    count_map = {}
    for ch in input_str:
        if ch in count_map.keys():
            count_map[ch] += 1
        else:
            count_map[ch] = 1
    
    keys = sorted(count_map)
    alphas = []
    count = []
    
    for key in keys:
        alphas.append(key)
        count.append(count_map[key])
        
    result = [0 for x in range(len(input_str))]
    
    permute_util(alphas, count, result, 0)
    
def permute_util(alphas, count, result, level):
    
    if level == len(result):
        print(result)
        return
    
    for i in range(len(alphas)):
        if count[i] == 0:
            continue;
        
        result[level] = alphas[i]
        count[i] -= 1
        permute_util(alphas, count, result, level + 1)
        count[i] += 1
        
if __name__ == '__main__':
    string = ['B', 'C', 'A', 'A']
    permute(string)

