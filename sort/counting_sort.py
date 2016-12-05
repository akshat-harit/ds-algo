import random

def counting_sort(arr, k):
    c = [0]*k
    for elem in arr:
        c[elem]+=1
    b = [None]*len(arr)
    index_b = 0
    for elem in range(k):
        if c[elem]==0:
            continue
        else:
            for i in range(index_b, index_b+c[elem]):
                b[i] = elem
            index_b+=c[elem]
    return b

if __name__ == '__main__':
    k = 10
    a = [int(random.random()*k) for i in range(5)]
    b = counting_sort(a,k)
    print("Orig = {}\nSorted = {}".format(a,b))




