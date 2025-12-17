
def reverseWords(self, s: str) -> str:
        sequence = s.split(" ")
        sequence_without_space = [wds for wds in sequence if len(wds) != 0]
        sequence_without_space.reverse()
        reversed_seq = " ".join(sequence_without_space)
        return reversed_seq
