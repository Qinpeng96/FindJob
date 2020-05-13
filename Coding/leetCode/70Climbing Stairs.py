class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        num_1 = 0 #走阶数为1的次数
        num_2 = 0 #走阶数为2的次数
        num = 0
        #考虑全是1的情况
        num_1 = n
        steps = num_1 + num_2
        current_nums = self.caculate_range(steps,num_2)
        num += current_nums
        while n >= 2:
            n = n-2
            num_2 += 1
            num_1  = n
            steps = num_1 + num_2  #需要走的total
            #计算Astep(num_2)
            current_nums = self.caculate_range(steps,num_2)
            num += current_nums
        return num

    def caculate_range(self,m,n)->int:
        molecule = 1
        deenominator = 1
        sum  = 1
        if (m - n) < n:
            n = m - n
        if n == 0:
            return sum
        k = m
        p = n
        for i in range(n):
            molecule*=k
            deenominator*=p
            k = k-1
            p = p-1
        sum = molecule/deenominator
        return int(sum)
a= Solution()
print(a.climbStairs(28))