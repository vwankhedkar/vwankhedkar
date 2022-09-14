class Solution:
    def isValid(self, s: str) -> bool:
        mapp = dict({'[':']', '(':')', '{':'}'})
        need_list = []
        for ind, char in enumerate(s):
            if char in mapp.keys():
                need_list.append(mapp[char])
            elif char in '])}':
                if char not in need_list:
                    return False
                elif char != need_list.pop():
                    return False
        if need_list:
            return False
        return True

OUTPUT: "()"
true
