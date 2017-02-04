class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num = num1
            num1 = num2
            num2 = num

        if len(num1) < 2:
            return str(int(num1) * int(num2))

        num_before = num1[:(len(num1)/2)]
        num_end = num1[(len(num1)/2):]

        mul_before = self.multiply(num_before, num2) \
            + '0'*(len(num1) - len(num1)/2)
        mul_end = self.multiply(num_end, num2)

        print 'a', mul_before, mul_end
        sum = ''
        flag = 0
        sum = int(mul_before) + int(mul_end)
        sum = str(sum)
        # while mul_before != '' and mul_end != '':
            # flag = 0
            # temp = int(mul_before[-1]) + int(mul_end[-1]) + flag
            # if temp > 9:
                # flag = 1
            # sum = str(temp)[-1] + sum
            # mul_before = mul_before[:-2]
            # mul_end = mul_end[:-2]
            # print 'b', sum, mul_before, mul_end

        if mul_before == '':
            sum = num_end + sum
        else:
            sum = num_before + sum

        if flag == 1:
            sum = '1' + sum

        print num1, num2, sum
        return sum


if __name__ == "__main__":
    print "'1234'*'5678'", Solution().multiply('1234', '5678')
