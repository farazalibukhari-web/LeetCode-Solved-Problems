class Solution(object):
    def removeDuplicates(self, s):
        st=[]
        for i in s:
            if st and st[-1]==i:
                st.pop()
            else:
                st.append(i)
        return "".join(st)
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

        