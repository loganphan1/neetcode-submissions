class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) #creates list of 1's with same length of original list
        prefix = 1 # the first number will always be 1 when iterating through from left to right for multiplication
        for i in range(len(nums)): # for loop containing each number in the list
            output[i] = prefix #first one will be 1, but afterwards the next number will be multiplied by the previous
            prefix *= nums[i] #multiplies the previously multiplied number by the current number, eventually going the whole list 
        suffix = 1 #now we start at the end with 1
        for i in range(len(nums)-1, -1, -1): #for loop starting from the top going down
            output[i] *= suffix #since we've already established each output, we multiply the left side by the right side, (the rightmost is already multipled fully)
            suffix *= nums[i] #multiplies previously multipled by current number
        return output #returns the final list