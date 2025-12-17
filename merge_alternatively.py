
def mergeAlternately(self, word1, word2):
        merge_part = ""
        merge_string = ""
        if len(word1) > len(word2):
            merge_part = word1[len(word2):]
        elif len(word2) > len(word1):
            merge_part = word2[len(word1):]
        
        for idx in range(len(word1)):
            if merge_part in word1 and len(merge_part) != 0:
                # print(idx)
                # print(merge_string)
                if idx == len(word2):
                    # print()
                #    print(merge_string)
                   merge_string += merge_part
                   return merge_string 
                merge_string += word1[idx] + word2[idx]
                # print(merge_string,"Line 20")
            else:
                merge_string += word1[idx] + word2[idx]
            # print(merge_string,"Line 23")
        
        # print(merge_string)
        return merge_string + merge_part