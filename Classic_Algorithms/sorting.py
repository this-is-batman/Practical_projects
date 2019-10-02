# take a list of numbers and sort using bubble sort and merge sort

def bubble_sort(a): #routine for bubble sort
    i=0
    j=0
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]

def merge_sort(a): #routine for merge sort
    if len(a)>1:
        mid = int(len(a)/2)
        L = a[:mid]
        R = a[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                a[k]=L[i]
                i +=1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        
        while j<len(R):
            a[k] = R[j]
            j += 1
            k += 1            



