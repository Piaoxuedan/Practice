class Solution(object):
    def parity(self,num):
        if (num % 2)==0:
            return True
        else:
            return False

    def twoSum(self, nums, target):
        index_dic = dict()
        count = 0
        for i in nums:
            cal_num = nums.count(i)
            index_dic[i] = cal_num
        for num in index_dic.keys():
            dis = target-num
            if dis == num :
                if self.parity(index_dic[num]):
                    count += index_dic[num] / 2
                else:
                    count += (index_dic[num]-1)/2
                del index_dic[num]

            if dis in index_dic.keys() and (dis!=num):
                fre = min(index_dic[num],index_dic[dis])
                count += fre
                del index_dic[num]
                del index_dic[dis]
        return count

if __name__ == '__main__':
    reversestr = Solution()
    result = reversestr.twoSum([1,1,5,5,5,2,2,4,3,3,3,6,7],6)
    print result
