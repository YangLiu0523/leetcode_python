class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = bin(n)[2:]
        bits = ('0' * 32 + bits)[-32:]
        return int(bits[::-1], 2)
