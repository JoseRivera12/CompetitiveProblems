#Find a triplet that sum to a given value
#https://adventofcode.com/2020/day/1
          
def find3Numbers(A, arr_size, sum): 
    A.sort() 
    for i in range(0, arr_size-2): 
        l = i + 1 
        r = arr_size-1 
        while (l < r):   
            if( A[i] + A[l] + A[r] == sum): 
                print(A[i]*A[l]*A[r])
                return True
            elif (A[i] + A[l] + A[r] < sum): 
                l += 1
            else:  
                r -= 1
    return False
  
def find2Numbers(A, arr_size, sum):
    s = set()
    for i in range(0, arr_size):
        if (sum - A[i]) in s:
            print((sum - A[i])*A[i])
            return True
        s.add(A[i])
    return False
    
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
int_list = [int(i) for i in Lines]

find2Numbers(int_list, len(Lines), 2020)
find3Numbers(int_list, len(Lines), 2020)
