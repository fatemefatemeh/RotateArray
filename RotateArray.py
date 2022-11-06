def RotateArray(nums,k):
    i=0
    while i<k:
        a=nums[-1]
        nums.insert(0,a)
        nums.pop()
        i+=1

    print(nums)
   

RotateArray([1,2,3,4,5,6,7],3)