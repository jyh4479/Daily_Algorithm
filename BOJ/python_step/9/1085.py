x,y,w,h=map(int,input().split())
new_y=min((h-y),y)
new_x=min((w-x),x)
print(min(new_y,new_x))