"""
https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
핵심 : sort가 어떻게 되는가?
list안에 int형일경우 숫자 오름차순으로 정렬
list안에 string일경우 앞숫자 순서대로 정렬, 문자면 문자순서 ex) ["12351","151","583","26432"] => ["12351","151","26432","583"]
sort(key=len) => 문자 길이순서대로 정렬
sort() => 순서대로 정렬 문자or 숫자

"""


def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer
phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)
