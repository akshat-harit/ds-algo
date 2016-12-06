
def binary_search(arr, x):
    start = 0
    end = len(arr)
    while end - start>1:
        mid = (start+end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid
        else:
            start = mid
    return None

if __name__=='__main__':
    a =[1,2,3,4,5,6,1234,12314,99999999]
    x = binary_search(a, 1234)
    print("Index for 1234 = {}".format(x))
    x = binary_search(a, 1234323)
    print("Index for 1234323 = {}".format(x))

