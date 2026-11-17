class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        a=[]
        for i in intervals:
            if not a or i[0]>a[-1][1]:
                a.append(i)
            else:
                a[-1][1]=max(a[-1][1],i[1])
        return a 
