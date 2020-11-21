array=[5,6,2,4,9,1,3,8,7]

def quick_sort(array,start,end):
    if start>=end:
        return
    else:
        pivot=start #기준값 설정
        left=start+1 #왼쪽에서 오는값
        right=end #오른쪽에서 오는값
        while left<=right:
            while left<=end and array[left]<=array[pivot]:
                left+=1
            while right>start and array[right]>=array[pivot]:
                right-=1
            if left>right:
                array[pivot],array[right]=array[right],array[pivot]
            else:
                array[right],array[left]=array[left],array[right]
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)


        
quick_sort(array,0,len(array)-1)
print(array)