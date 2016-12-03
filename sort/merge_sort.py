import random


def merge(array1, array2):
    result=[None]*(len(array1)+len(array2))
    index1 = 0
    index2 = 0
    for i in range(len(result)):
        if index1 == len(array1):
            result[i] =array2[index2]
            index2+=1
        elif index2 == len(array2):
            result[i] = array1[index1]
            index1+=1
        elif (array1[index1] < array2[index2]):
            result[i] = array1[index1]
            index1+=1
        else:
            result[i] = array2[index2]
            index2+=1
    return result



def merge_sort(input_array):
    if len(input_array) == 1:
        return input_array
    else:
        arr1 = merge_sort(input_array[0:len(input_array)//2])
        arr2 = merge_sort(input_array[len(input_array)//2:])
        return merge(arr1, arr2)



if __name__ == '__main__':
    input_array= [int(10*random.random()) for _ in range(10)]
    print("Input array {}".format(input_array))
    print("Sorted array {}".format(merge_sort(input_array)))
