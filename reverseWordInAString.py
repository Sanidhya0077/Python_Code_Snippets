# https://leetcode.com/problems/reverse-words-in-a-string/submissions/1857675855/?envType=study-plan-v2&envId=leetcode-75
def reverseWords(self, s: str) -> str:
        sequence = s.split(" ")
        sequence_without_space = [wds for wds in sequence if len(wds) != 0]
        sequence_without_space.reverse()
        reversed_seq = " ".join(sequence_without_space)
        return reversed_seq
