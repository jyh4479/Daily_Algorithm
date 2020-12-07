test_case=int(input())
student_list=dict()
for _ in range(test_case):
    name,score=input().split()
    student_list[name]=int(score)

for i in sorted(student_list, key=lambda x: student_list[x]):
    print(i,end=" ")
#굳이 dict안쓰고 그냥 list로 편하게 출력가능