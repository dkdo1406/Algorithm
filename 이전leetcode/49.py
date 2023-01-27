"""
https://leetcode.com/problems/group-anagrams/
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs에 있는 원소들을 하나씩 꺼내 split으로 분리
분리한것을 sort한 후 join으로 str 변환 후 딕셔너리에 넣는다.
"""
import collections

strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = collections.defaultdict(list)

for word in strs:

    anagrams[''.join(sorted(word))].append(word)
print(anagrams.values())
