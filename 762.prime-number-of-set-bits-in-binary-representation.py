class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # turn each number in left to right to binary and store in an array of array
        # count the set bits of each binary number array and store back
        # create a prime array store all the prime number smaller than 32(since int is at most 32 bits)
        # check and add one if the number od set bits in the array is in the prime array
        # return the number of prime 
