def QuickSort(array,begin,end):
    if not begin <end:
        return
    pivot=paratition(array,begin,end)
    QuickSort(array,begin,pivot-1)
    QuickSort(array,pivot+1,end)



def paratition(array,begin,end):
    pivot=end
    counter=begin
    for i in range(begin,end):
        if array[i]<array[pivot]:
            array[i],array[counter]=array[counter],array[i]
            counter+=1
    array[pivot],array[counter]=array[counter],array[pivot]
    return counter

a=[3,4,5,3,2,1,0]
QuickSort(a,0,6)
print(a)


