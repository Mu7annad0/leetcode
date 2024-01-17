from collections import Counter

def uniqueOccurrences(arr):
    count = Counter(arr)

    values = [x for x in count.values()]
    if len(set(values)) == len(values):
        return True
    else:
        return False

if __name__ == '__main__':
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(uniqueOccurrences(arr))
