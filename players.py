


class Player:

    def __init__(self, name):
        self.name = name
        self.used_ans = []


    def count_used(self):
        return len(self.used_ans)

    def use_ans(self, ans):
        self.used_ans.append(ans)

    def check_used(self,ans):
        return ans in self.used_ans
