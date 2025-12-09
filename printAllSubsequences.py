nums = [1,2,3]
def printAllSubsequences(res,idx,ans=[]):
    if idx == len(res):
        return
    
    # pick
    printAllSubsequences(res + [nums[idx]],idx + 1)
   
    # not pick
    printAllSubsequences(res,idx + 1)
   
printAllSubsequences([],0)