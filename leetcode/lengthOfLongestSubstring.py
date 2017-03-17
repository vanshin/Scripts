def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    length_list = []
    index = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    for n in range(1, len(s)):
        if s[n] in s[index:n]:
            length_list.append(n-index)
            index = index + s[index:n].index(s[n]) + 1
        elif n+1 == len(s):
            length_list.append(n-index+1)
    length_list.sort()
    return length_list.pop()

def main():
    s = 'abcddfggdwwsefdgrefwcer'
    result = lengthOfLongestSubstring(s)
    print(result)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))