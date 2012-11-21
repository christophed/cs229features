
# Simple average
def avg(arr):
    arrSum = sum(arr)
    arrNum = len(arr)
    return arrSum * 1.0 / arrNum

# Standard deviation
def stdev(arr):
    avg_ = avg(arr)
    stdev_ = 0
    for i in arr:
        stdev_ += (i - avg_ ) ** 2
    return stdev_ 
