array=[]#max heap

def insert_heap(array,num):
    array.append(num)
    if len(array)<=1: #root인경우
        return
    else: #root가 아닌경우
        index=len(array)-1
        while index>0 or array[index]<array[(index-1)//2]:
            array[index],array[(index-1)//2]=array[(index-1)//2],array[index] #swap
            index=(index-1)//2
        return

def pop_heap(array):
    if len(array)==0:
        print("데이터가 없습니다.")
    else:
        length,index=len(array)-1,0
        array[0],array[-1]=array[-1],array[0]
        num=array.pop()
        while (index+2<length and array[index+2] < array[index]) or (index+1<length and array[index+1] < array[index]): #왼쪽 오른쪽 바꿀게 있는경우 반복
            if index+2<length and array[index+2] < array[index]:
                array[index+2],array[index]=array[index],array[index+2]
                index=index+2
            if index+1<length and array[index+1] < array[index]:
                array[index+1],array[index]=array[index],array[index+1]
                index=index+1
    return num

insert_heap(array,1)
insert_heap(array,2)
insert_heap(array,3)
print(pop_heap(array))
insert_heap(array,3)
print(pop_heap(array))