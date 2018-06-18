import math
from operator import itemgetter
# classes is a list of tuples [(g_1, b_1), (g_2, b_2), ... , (g_{n-1}, b_{n-1})] (see handout for definitions).
# T is some positive number.
def inefficient_allocate_time(classes, T):
    time_allocated = 0
    total_benefit = 0

    while time_allocated < T:
        # Find which remaining class would be best to allocate our time to.
        best_ratio = -float('inf')
        best_i = -1
        for i, (goal, benefit) in enumerate(classes):
            if benefit/goal > best_ratio:
                best_ratio = benefit/goal
                best_i = i

        if best_i == -1:
            # If we run out of classes, return.
            return total_benefit

        # Allocate as much time as we can to the best class found.
        goal, benefit = classes[best_i]
        # We can't go over our limit T or over the goal limit for this class.
        time_to_allocate = min(T - time_allocated, goal)
        time_allocated += time_to_allocate
        total_benefit += benefit/goal * time_to_allocate

        # We can't allocate any more time to this class, so delete it.
        del classes[best_i]
    return total_benefit
 
def countingSort(arr, exp1):
 
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
 
    for i in range(0, n):
        index = (arr[i][1]/exp1)
        count[int((index)%10 )] += 1
    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i>=0:
        index = (arr[i][1]/exp1)
        output[ count[ int((index)%10) ] - 1] = arr[i]
        count[ int((index)%10) ] -= 1
        i -= 1
        
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
 

def radixSort(arr):
    max1 = max([i[1] for i in arr])
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

def allocate_time(classes, T):
##    benefit_ratio= [(i,int(float("{0:.15f}".format(float(b)/g))*math.pow(10,15))) for i, (g, b) in enumerate(classes)]
    benefit_dict = {}
    for (g,b) in classes:
        ratio = b/g
        benefit_dict[(g, ratio)]= benefit_dict.get((g, ratio),0)+1

    benefit_ratio= []
    for key,value in benefit_dict.items():
        benefit_ratio.append((value, key[0],key[1]))

    benefit_ratio.sort(key= itemgetter(2), reverse= True)

##    benefit_ratio = [(g, b/g) for (g,b) in classes]
##    benefit_ratio.sort(key= itemgetter(1), reverse= True)
##    print (classes[0:10])
##    radixSort(benefit_ratio)
##    benefit_ratio.reverse()
    #print(benefit_ratio)
    
    time_allocated = 0
    total_benefit = 0
    for ratio in benefit_ratio:
##        goal = classes[ratio[0]][0]
        time_to_allocate = min(T - time_allocated,ratio[1]*ratio[0])
        time_allocated += time_to_allocate
##        total_benefit += (ratio[1]/math.pow(10,15)) * time_to_allocate
        total_benefit += ratio[2]*time_to_allocate
        if time_allocated == T:
            print ("here")
            break

    return total_benefit

##classes = []
##print (allocate_time(classes, 12))
           
