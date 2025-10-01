class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}            
        hashmap['I']=1
        hashmap['V']=5
        hashmap['X']=10        
        hashmap['L']=50
        hashmap['C']=100
        hashmap['D']=500
        hashmap['M']=1000
        total=0
        s=s.replace('IV','IIII').replace('IX','VIIII')
        s=s.replace('XL','XXXX').replace('XC','LXXXX')
        s=s.replace('CD','CCCC').replace('CM','DCCCC')
        for num in s:
            total+=hashmap[num]
        return total
                                                       