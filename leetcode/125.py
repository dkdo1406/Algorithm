"""
https://leetcode.com/problems/valid-palindrome/
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
조건문일경우 filter를 사용해야한다. 그래야 원소들이 나옴
만약 map을 사용하면 True False로 반환한다.
"""

# 42 ms	14.7 MB
s = "A man, a plan, a canal: Panama"
temp = ''.join(filter(str.isalnum,s))
temp= temp.lower()
if temp[::-1]!=temp:
    print("false")
print("True")

exit()
for i in s:
    if i.isalnum():
        temp.append(i.lower())
temp_reverse= list(reversed(temp))
if temp == temp_reverse:
    print("True")
else:
    print("False")


"""
# 이전 내코드
Runtime: 59 ms
Memory Usage: 20 MB
s = "A man, a plan, a canal: Panama"
temp = []
for i in s:
    if i.isalnum():
        temp.append(i)
temp_reverse=list(reversed(temp))
if temp!=temp_reverse:
    return False
return True
"""
