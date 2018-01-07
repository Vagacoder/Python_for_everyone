## Ch08 P8.22

def main():
    a = {5:4, 9:2, 10:9}
    b = {1:1, 3:7, 6:2, 9:3}
    c = sparseArraySum(a, b)
    for key in sorted(c):
        print(key, ': ', c[key])

def sparseArraySum(dict1, dict2):
    result = {}
    for key in dict1:
        result[key] = dict1[key] + dict2.get(key, 0)
    
    for key in dict2:
        if key not in result:
            result[key] = dict2[key]
    return result

main()