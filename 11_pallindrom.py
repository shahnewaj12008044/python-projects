def isPalindrome(s):


    def toChar(s):
        ans = ''
        s = s.lower()
        for c in s: 
            if c in 'abcdefghijklmnopqrstuwxyz':
                ans += c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:    
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))

string = input('enter a string: ')
print(isPalindrome(string))