class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0  # Pointer for 'name'
        j = 0  # Pointer for 'typed'
        n = len(name)
        m = len(typed)

        while j < m:
            # 1. Standard Match: If characters match, advance both pointers.
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            
            # 2. Long Press Match: If 'typed' has extra characters (long press)
            #    it must match the PREVIOUS character in 'name'.
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            
            # 3. Mismatch: The character in 'typed' does not match 
            #    the current character in 'name' NOR is it a valid long press.
            else:
                return False
            # 4. Final Check: Ensure ALL characters in 'name' were consumed.
            #    (If i < n, it means 'typed' ended early or was missing characters)
        return i == n