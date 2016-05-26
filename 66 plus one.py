class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum / 10
        if carry: digits = [1] + digits
        return digits