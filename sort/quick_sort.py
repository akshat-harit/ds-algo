import random


def quick_sort(ia, start, end):
    if start >= end:
        return ia

    partition_index = (start+end)//2
    #Swap partition to the end
    ia[partition_index], ia[end] = ia[end], ia[partition_index]

    partition = ia[end]
    i = start
    j = end
    while (i < j):
        if ia[i] > partition:
            j-=1
            ia[i], ia[j] = ia[j], ia[i]
        else:
            i+=1
    ia[end], ia[j] = ia[j], ia[end]
    quick_sort(ia,start, j-1)
    quick_sort(ia, j+1, end)
    return ia



if __name__ == '__main__':
    input_array= [int(10*random.random()) for _ in range(10)]
    print("Input array {}".format(input_array))
    print("Sorted array {}".format(quick_sort(input_array, 0, len(input_array) - 1)))
