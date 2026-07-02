class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums) #creates a set with all of the numbers from the list for O(1) lookup time
        longest = 0 #initializes the longest sequence 
        for num in consec: # goes through each number in the set
            if num - 1 not in consec: # if there is no "num - 1", then it has the potential to be the start of a sequence
                length = 1 #length of sequence starts at 1
                while num + length in consec: #goes through the sequence, if it exists, add it to the length
                    length += 1 #add length with 1
                longest = max(longest, length) #after going through each of the lengths of all of the potential sequences, the longest would be the biggest one using max function
        return longest #return the longest