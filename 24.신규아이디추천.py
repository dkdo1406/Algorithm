# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

new_id = 	"=.="
#1
a = new_id.lower()
print(a)
answer = ''
#2
for i in a:
    if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i== '.':
        answer +=i
print(answer)
#3

answer+='!'
for i,c in enumerate(answer):

    # i 가 3일때 터짐, 당연히 3이면 실행이 안되어야 하는데?
    # [2]와 [3]을 비교하고 실행후 [3]삭제
    # while문으로 다시 돌아와 [2]와 [3]을 비교 하지만 [3]은 없어서 터짐
    if i<=len(answer)-1:
        while answer[i] =='.' and answer[i+1] =='.':
            answer = answer[:i] + answer[i+1:]

answer = answer[:-1]
print(answer)



#4
if len(answer)!=0:
    if answer[0] == '.':
        answer = answer[1:]
if len(answer)!=0:
    if answer[-1] == '.':
        answer = answer[:-1]
if len(answer)!=0:
    if answer[0] =='.' and len(answer)==1:
        answer =''

#5
if len(answer) ==0:
    answer = 'a'

#6
if len(answer)>15:
    answer = answer[:15]
    if answer[14]=='.':
        answer = answer[:14]

#7

if len(answer)<=2:
    while len(answer)<=2:
        answer += answer[-1]
print(answer)

# 48~57
# 97~122
# 45,46, 95