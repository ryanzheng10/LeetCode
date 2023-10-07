
'''
Note:
    this provides heap operations for lists
    natively this is a min heap, but by multiplying the key by -1, 
    you can mimick a max heap behavior

Operations:
    to push just numbers ->
        heapq.heappush(min_heap, 5) 
    to push obects --> 
        * This works because the comparison (1, cat, "string") < (2, dog, "string2") only
        * compares the first element in the tuple
        heapq.heappush(min_heap, (5, "Object A"))
        heapq.heappush(min_heap, (2, "Object B"))
        heapq.heappush(min_heap, (9, "Object C"))
    to pop --> 
        min_pair = heapq.heappop(min_heap)
        max_pair = heapq.heappop(max_heap)
        * max works the same way because of the -1 trick




--> youre kidding me
    max_heal = max() is a thing for heapq
'''
import heapq 

class Median:
    # idea 
    def __init__(self, initial: int):
        self.leftHalf = [-1 * initial] # this is a maxHeap
        self.rightHalf = [] # this is a minHeap
    
    def add(self, num: int):
        if(num < self.leftHalf[0] * -1):
            heapq.heappush(self.leftHalf, -1 * num) 
        elif(num > self.leftHalf[0] * -1):
            heapq.heappush(self.rightHalf, num) 
        else:
            # num == self.leftHalf[0] * -1 is true
            heapq.heappush(self.leftHalf, -1 * num)
        
        leftLen = len(self.leftHalf)
        rightLen = len(self.rightHalf)
        if(abs(leftLen-rightLen) > 1):
            if(leftLen > rightLen):
                popped = -1 * heapq.heappop(self.leftHalf)
                heapq.heappush(self.rightHalf, popped)
            else:
                popped = -1 * heapq.heappop(self.rightHalf)
                heapq.heappush(self.leftHalf, popped)


    def get_median(self) -> int:
        if len(self.leftHalf) == len(self.rightHalf):
            return (-1*self.leftHalf[0] + self.rightHalf[0])/2
        elif len(self.leftHalf) > len(self.rightHalf):
            return -1 * self.leftHalf[0]
        else:
            return self.rightHalf[0]



# testing ------------------------------------------
# I could automate random experiments of a set of inserts and checks against stats.median(li)
import statistics
        
def add_to_med_and_list(med: Median, li: list, num):
    med.add(num)
    li.append(num)

med = Median(1)
li = [1]

add_to_med_and_list(med, li, 2)
add_to_med_and_list(med, li, 3)
add_to_med_and_list(med, li, 5)
add_to_med_and_list(med, li, 20)
add_to_med_and_list(med, li, 22)
add_to_med_and_list(med, li, 22)
add_to_med_and_list(med, li, 22)
add_to_med_and_list(med, li, 22)
add_to_med_and_list(med, li, 22)
add_to_med_and_list(med, li, 22)
add_to_med_and_list(med, li, 12)
add_to_med_and_list(med, li, 4)
add_to_med_and_list(med, li, 19)

print(med.get_median())
print(statistics.median(li))

        

    

# # leetcode 295
# import heapq 

# class MedianFinder:

#     def __init__(self):
#         self.leftHalf = [] # this is a maxHeap
#         self.rightHalf = [] # this is a minHeap

#     def addNum(self, num: int) -> None:
#         if(len(self.leftHalf) == 0):
#             self.leftHalf = [-1 * num]
#             return 
#             # not proper coding but oh well, 
#             # this part just checks for first insert

#         if(num < self.leftHalf[0] * -1):
#             heapq.heappush(self.leftHalf, -1 * num) 
#         elif(num > self.leftHalf[0] * -1):
#             heapq.heappush(self.rightHalf, num) 
#         else:
#             # num == self.leftHalf[0] * -1 is true
#             heapq.heappush(self.leftHalf, -1 * num)
        
#         leftLen = len(self.leftHalf)
#         rightLen = len(self.rightHalf)
#         if(abs(leftLen-rightLen) > 1):
#             if(leftLen > rightLen):
#                 popped = -1 * heapq.heappop(self.leftHalf)
#                 heapq.heappush(self.rightHalf, popped)
#             else:
#                 popped = -1 * heapq.heappop(self.rightHalf)
#                 heapq.heappush(self.leftHalf, popped)

#     def findMedian(self) -> float:
#         if len(self.leftHalf) == len(self.rightHalf):
#             return (-1*self.leftHalf[0] + self.rightHalf[0])/2
#         elif len(self.leftHalf) > len(self.rightHalf):
#             return -1 * self.leftHalf[0]
#         else:
#             return self.rightHalf[0]