# Enter your code here. Read input from STDIN. Print output to STDOUT

#Mean: We sum all  elements in the array, divide the sum by , and print our result on a new line.
def getMean(list):
    sum = 0;
    for i in list:
        sum = sum + i
    mean = float(sum)/len(list)
    return mean

#Median: To calculate the median, we need the elements of the array to be
#sorted in either non-increasing or non-decreasing order.
#We then average the two middle elements:
def getMedian(list):
    list.sort()
    size = len(list)
    if(size % 2 == 0):
        return float(list[size//2 - 1] + list[size//2]) / 2
    return float(list[(size-1)/2]) / 2

#Mode: We can find the number of occurrences of all the elements in the array
#Every number occurs once, making  the maximum number of occurrences for any number.
#Because we have multiple values to choose from, we want to select the smallest one
def getMode(list):
    mode = 0
    size = len(list)
    count, max = 0, 0
    copy = list
    copy.sort()
    current = 0
    for i in copy:
        if (i == current):
            count += 1
        else:
            count = 1
            current = i
        if (count > max):
            max = count
            mode = i
    return mode
# Get the input
n = input()
numbers = list(map(int, input().split()))
print(getMean(numbers))
print(getMedian(numbers))
print(getMode(numbers))
