class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        min_list,max_list=nums1,nums2
        if len(nums1)>len(nums2):
            min_list,max_list=max_list,min_list

        total_len=len(nums1)+len(nums2)
        half_total_len=total_len//2
        
        l,r=0,len(min_list)-1
        
        while True:
            mid_min_list=(l+r)//2
            mid_max_list=half_total_len-mid_min_list-2
            
            left_mid_min_list=min_list[mid_min_list] if mid_min_list>=0 else float('-inf')
            left_mid_max_list=max_list[mid_max_list] if (mid_max_list)>=0 else float('-inf')
            right_mid_min_list=min_list[mid_min_list+1] if (mid_min_list+1)<len(min_list) else float('+inf')
            right_mid_max_list=max_list[mid_max_list+1] if (mid_max_list+1)<len(max_list) else float('+inf')
            
            if left_mid_min_list<=right_mid_max_list and left_mid_max_list<=right_mid_min_list:
                if total_len%2:
                    return min(right_mid_min_list,right_mid_max_list)
                else:
                    med1=max(left_mid_min_list,left_mid_max_list)
                    med2=min(right_mid_min_list,right_mid_max_list)
                    return (float(med1) + float(med2)) / 2.0
            elif left_mid_min_list>right_mid_max_list:
                r=mid_min_list-1
            
            else:
                l=mid_min_list+1
