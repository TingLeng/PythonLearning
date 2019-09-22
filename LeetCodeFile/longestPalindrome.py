# * -coding = utf-8 -*
def longestPalindrome(s):
     def expandCenter(s, left, right):
         while left>=0 and right<len(s) and s[left]==s[right]:
             left -= 1
             right += 1
         return right - left -1
     start, end = 0, 0
     n = len(s)
     if n == 0:
         return ''
     if n == 1:
         return s
     for i in range(n-1):
         len1 = expandCenter(s, i, i)
         len2 = expandCenter(s, i, i+1)
         Len = max(len1, len2)
         if (Len >= end - start):
             start = i + 1 - Len // 2
             end = i + Len // 2
     return s[start:end+1]

a6 = 'aaaaaa'
a5 = 'aaaaa'
d = 'abadb'
e = 'ceecdcb'
a6_t = longestPalindrome(a6)
a5_t = longestPalindrome(a5)
d_t = longestPalindrome(d)
e_t = longestPalindrome(e)
print(a6_t)
print(a5_t)
print(d_t)
print(e_t)