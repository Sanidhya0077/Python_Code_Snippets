# https://leetcode.com/problems/plus-one/?envType=daily-question&envId=2026-01-01
def plusOne(digits):
    num_in_str  = ""
    num_in_lst = []
    for digit in digits:
        num_in_str += str(digit) 
    combined_digit =  int(num_in_str)
    combined_digit += 1
    combined_digit = str(combined_digit)
    for idx in range(len(combined_digit)):
        num_in_lst.append(int(combined_digit[idx]))
    
    return num_in_lst

print(plusOne([1,2,4,5,9]))