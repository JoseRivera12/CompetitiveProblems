def even_odds(nums):
    len_nums = len(nums)
    #two pointers 
    left, right = 0, len_nums - 1
    #stop when pointers are in same position
    while left < right:
        #if all the elements in left side are even just increment the pointer
        while(nums[left] % 2 == 0 and left < right):
            left += 1
        #same for right side
        while(nums[right] % 2 == 1 and left < right):
            right -= 1
        #if not pass this just swap element in this position and continue
        if(left < right):
            nums[left], nums[right] =  nums[right], nums[left]
            left += 1
            right = right - 1
    return nums

def main():
    input = [12, 34, 45, 9, 8, 90, 3]
    even = even_odds(input)
    print("{0}".format(even))

if __name__ == "__main__":
    main()
