# mergesort.py
# 9/9/08 Lecture 2 -- 6.006 Introduction to algorithms

def merge_sort(A):
    """
    Sort list A into order, and return result.
    """
    n = len(A)
    if n==1: 
        return A
    mid = n//2     # floor division
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(L,R):
    """
    Given two sorted sequences L and R, return their merge.
    """
    i = 0
    j = 0
    answer = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

# routines for timing mergesort (and other sorting routines)

import math
import random
import time

def random_list(n):
    """
    Return a list of length n of random numbers
    """
    return [random.randint(0,1000000000) for i in range(n)]

def lg(n):
    """
    Return base-two logarithm of n.
    """
    return math.log(n)/math.log(2.0)

def test_merge(n):
    """ 
    Run mergesort once on random list of length n 
    Print out running time divided by n*lg(n)
    """
    L = random_list(n)
    t0 = time.clock()
    merge_sort(L)
    t1 = time.clock()
    elapsed = t1-t0
    print "%g seconds elapsed for n = %d (= %g * n lg(n))"%(elapsed,n,elapsed/(n*lg(n)))

def test(f):
    """ Run function f on inputs 1,2,4,8,... until 30 seconds pass """
    t0 = t1 = time.clock()
    n = 1
    while (t1-t0)<30.0: 
        n = n * 2
        f(n)
        t1 = time.clock()

def insertion_sort(A):
    """
    Sort list A into order, in place.

    From Cormen/Leiserson/Rivest/Stein,
    Introduction to Algorithms (second edition), page 17,
    modified to adjust for fact that Python arrays use 
    0-indexing.
    """
    for j in range(len(A)):
        key = A[j]
        # insert A[j] into sorted sequence A[0..j-1]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

def test_insertion(n):
    """ 
    Run insertion sort once on random list of length n 
    Print out running time divided by n**2
    """
    L = random_list(n)
    t0 = time.clock()
    insertion_sort(L)
    t1 = time.clock()
    elapsed = t1-t0
    print "%g seconds elapsed for n = %d (= %g * n**2)"%(elapsed,n,elapsed/(n**2))

def test_sorted(n):
    """ 
    Run built-in 'sorted' sort once on random input of length n 
    Print out running time divided by n*lg(n)
    """
    L = random_list(n)
    t0 = time.clock()
    sorted(L)
    t1 = time.clock()
    elapsed = t1-t0
    print "%g seconds elapsed for n = %d (= %g * n lg(n))"%(elapsed,n,elapsed/(n*lg(n)))

