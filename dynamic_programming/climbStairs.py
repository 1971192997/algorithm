class Salution(object):
    def climbStairs(self, n):
        """

        :param n:
        :return:
        """
        stepList = [1, 1, 2]
        i = n
        while i > 2:
            stepList.append(stepList[-1] + stepList[-2])
            i -= 1

        return stepList[n]


if __name__ == '__main__':
    n = 4
    s = Salution()
    count = s.climbStairs(n)
    print("count of step is %d" % count)
