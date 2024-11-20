# DSA-Simplified: Sorting Solutions in O(n*logn)

This repository contains solutions to common **Data Structures and Algorithms (DSA)** problems that can be efficiently solved using **sorting**. The goal is to demonstrate how sorting algorithms like **QuickSort**, **MergeSort**, and **HeapSort** can be applied to a wide range of problems while ensuring an optimal time complexity of **O(n log n)** with **O(1)** space complexity.

## Table of Contents

- [Overview](#overview)
- [Sorting Algorithms](#sorting-algorithms)
  - [QuickSort](#quicksort)
  - [MergeSort](#mergesort)
  - [HeapSort](#heapsort)
- [Problem Categories](#problem-categories)
  - [Array Manipulation](#array-manipulation)
  - [Search Optimization](#search-optimization)
  - [Combinatorial Problems](#combinatorial-problems)
- [Code Examples](#code-examples)
  - [Find Missing Number](#find-missing-number)
- [Best Practices](#best-practices)
- [Time Complexity Explanation](#time-complexity-explanation)
- [Contributing](#contributing)

## Overview

The repository is designed for learners who want to master DSA concepts with a focus on **sorting** techniques. It covers a variety of problems that can be solved efficiently by sorting the data first, which can simplify the problem-solving process and lead to optimized solutions with **O(n log n)** time complexity.

The primary goal is to:
- Master sorting algorithms and their applications.
- Solve common DSA problems using **O(n log n)** time complexity.
- Use **in-place** sorting methods that ensure **O(1)** extra space.

## Sorting Algorithms

### QuickSort
QuickSort is an efficient **divide-and-conquer** algorithm. It works by selecting a pivot element, partitioning the array around that pivot, and then recursively sorting the two partitions.

**Time Complexity**: \(O(n \log n)\) on average, \(O(n^2)\) in the worst case.

**Space Complexity**: \(O(\log n)\) for recursive calls.

### MergeSort
MergeSort also follows the divide-and-conquer strategy. It splits the array into halves, recursively sorts each half, and then merges the sorted halves.

**Time Complexity**: \(O(n \log n)\) for all cases (best, average, worst).

**Space Complexity**: \(O(n)\) due to the auxiliary array used for merging.

### HeapSort
HeapSort converts the array into a **binary heap** and then sorts it by repeatedly extracting the maximum (or minimum) element from the heap.

**Time Complexity**: \(O(n \log n)\) for all cases.

**Space Complexity**: \(O(1)\) since it sorts the array in place.

## Problem Categories

### Array Manipulation
Sorting is often the first step in array manipulation problems. Some examples include:
- Finding the missing number in an array.
- Merging two sorted arrays.
- Reordering data based on conditions.

### Search Optimization
Once an array is sorted, search operations become more efficient:
- Binary search for faster lookup.
- Finding the kth largest or smallest element in a sorted array.

### Combinatorial Problems
Many combinatorial problems are easier to solve once the data is sorted:
- Finding pairs, triplets, or subsets that satisfy certain conditions.
- Scheduling or interval problems, such as meeting room scheduling.

## Code Examples

### Find Missing Number

In this example, we solve the problem of finding the missing number in an array of size \(n-1\) containing numbers from 1 to \(n\).

```python
def find_missing_number(arr, n):
    # Step 1: Sort the array
    arr.sort()  # In-place sort: O(n*logn) time, O(1) space
    
    # Step 2: Check the missing number
    for i in range(1, n):
        if arr[i - 1] != i:
            return i
    
    # If all numbers are present, return n
    return n

# Example Usage
arr = [3, 7, 1, 2, 8, 4, 5]
n = 8
print(find_missing_number(arr, n))  # Output: 6
