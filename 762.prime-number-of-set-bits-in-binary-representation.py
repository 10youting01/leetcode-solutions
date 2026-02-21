class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # turn each number in left to right to binary and store in an array of array -> bin
        # count the set bits of each binary number array and store back -> count('1')
        # create a prime array store all the prime number smaller than 32(since int is at most 32 bits)
        # check and add one if the number od set bits in the array is in the prime array
        # return the number of prime 
        arr = []
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        for num in range(left, right+1):
            arr.append(bin(num).count('1'))
        
        num_prim = 0
        for idx, set_bit in enumerate(arr):
            if set_bit in prime:
                num_prim += 1
        
        return num_prim


