def merge_the_tools(string, k):
    for s in [string[i:i + k] for i in range(0, len(string), k)]:
        from collections import OrderedDict
        print("".join(OrderedDict.fromkeys(s)))


if __name__ == '__main__':
    merge_the_tools("AABCAAADA", 3)
