# Problem Link  : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

# can be solved using recursion but for larger inputs stack is preferred


def removeDuplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
    
        else:
            stack.append(char)

    return "".join(stack)

print(removeDuplicates(s="abbbcaa"))