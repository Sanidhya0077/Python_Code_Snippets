
# Input
nums = [1,2,3]

# Expected Output
[[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3],[]]
# Total 8 elements
# We will traverse till the end of array and pick one element or not pick the other element
def printAllSubsequences(arr,idx,res=[]):

    if idx == len(arr):
        return
        # print(idx)
    printAllSubsequences(arr,idx+1,res + [arr[idx]])
    printAllSubsequences(arr,idx+ 1,res)
        # res.append(arr)

    return res
    # pick
    # printAllSubsequences(res + [nums[idx]],idx + 1)
   
    # not pick
    # printAllSubsequences(res,idx + 1)
   
print(printAllSubsequences(arr=nums,idx=0))