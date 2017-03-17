def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 1:
            return s
    result = s[0:1]
    for index in range(len(s)):
        # right_index = len(s)
        limit = index
        while s[index] in s[limit+1:len(s)]:
            index_of_same = s[limit+1:].index(s[index]) + limit + 1
            length_palin = index_of_same - index + 1
            right_half = left_half = 0
            if length_palin%2 == 0:
                left_half = right_half = length_palin//2
            else:
                left_half = length_palin//2+1
                right_half = length_palin//2
            if s[index:left_half+index] == s[index+right_half:index+length_palin][::-1]:
                if len(s[index:length_palin+index]) > len(result):
                    result = s[index:length_palin+index]
            limit = index_of_same
    return result

def main():
    s1 = 'bdbfigbid'
    s = 'cbbd'
    s3 = 'abvvba'
    s = longestPalindrome(s)

    print(s)
if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
