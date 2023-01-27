"""
https://leetcode.com/problems/most-common-word/

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
banned를 뺀 나머지 중 가장 많이 언급된 단어 찾기
문자를 제외한 나머지는 다 무시

re.findall 
re.sub（정규 표현식, 치환 문자, 대상 문자열 ）
정규식 몇개 알아 놓을 것
"""
import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph = paragraph.lower()
words = [word for word in re.sub(r'[^\w]',' ',paragraph).split() if word not in banned]
print(words)

count = collections.Counter(words)

print(count.most_common(1)[0][0])

print(paragraph)
paragraph.replace(" ","aaaa")
# for ban in banned:
#     paragraph.replace("hit","")
print(paragraph)