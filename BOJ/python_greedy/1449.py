N,L=map(float,input().split())
hole=list(map(float,input().split()))
hole=sorted(hole)

ans=0
end=0 #테이프의 끝 위치
for i in hole: #각 구멍 순회
    if end<i-0.5: #구멍 유효거리에 아예 닿지 않는경우
        ans+=1
        end=i-0.5+L

    elif i-0.5<=end<i+0.5: #구멍 유효거리에 있는경우
        ans+=1
        end=end+L

    elif end>=i+0.5:
        continue

print(ans)