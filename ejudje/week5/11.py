import re
class Find:
    def upper(self ,s):
        x = re.findall(r"[A-Z]" , s)
        print(len(x))

obj = Find()
obj.upper(input())