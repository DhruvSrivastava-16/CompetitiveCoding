import math

def heapify(A,n,i):
    Largest = i;
    left = 2*i + 1;
    right = 2*i + 2;
    
    if(left < n and A[Largest] < A[left] ):
        Largest = left

        
    if(right < n and A[Largest] < A[right]):
        Largest = right
    
    if(Largest!=i):
        A[i], A[Largest] = A[Largest], A[i]
        heapify(A,n,Largest)
    
    
def Build_Heap(L_Heap,n):
    stdid = len(L_Heap)//2 - 1 
    
    for i in range(stdid,-1,-1):
        
        print("i is: ",i)
        heapify(L_Heap,n,i)
        
        

if __name__ == "__main__":
    L_Heap = [ 4, 3, 5, 1, 6, 13,  10, 9, 8, 15, 17 ]
    n = len(L_Heap)
    Build_Heap(L_Heap,n)
    print(L_Heap)