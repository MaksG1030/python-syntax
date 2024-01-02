def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for el in nums:
        #print (type(el))
        if el == 7:
            return (True)
            #break
       
    return (False)

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

