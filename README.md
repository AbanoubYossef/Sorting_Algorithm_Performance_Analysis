# Sorting Algorithm Performance Analysis

This project is a Python-based analysis of sorting algorithms, including Bubble Sort, Insertion Sort, and Selection Sort. It evaluates their performance under different scenarios, such as best-case, average-case, and worst-case input data. The analysis includes metrics like total operations, execution time, comparisons, and assignments, and the results are visualized using matplotlib.

## Table of Contents
- [Sorting Algorithms](#sorting-algorithms)
- [Input Data Generation](#input-data-generation)
- [Algorithm Analysis](#algorithm-analysis)
- [Metrics](#metrics)
- [How to Use](#how-to-use)

### Sorting Algorithms
1. **Bubble Sort**: This algorithm iteratively compares adjacent elements and swaps them if they are in the wrong order until the entire list is sorted.

2. **Insertion Sort**: It builds the final sorted array one item at a time, inserting each element into its correct position.

3. **Selection Sort**: This algorithm repeatedly selects the minimum element from the unsorted portion and places it at the beginning.

### Input Data Generation
Three types of input data are generated for the analysis:
- **Best Case**: Sorted input data.
- **Average Case**: Randomly shuffled input data.
- **Worst Case**: Reverse-sorted input data.

### Algorithm Analysis
The analysis is performed for each sorting algorithm and each type of input data. It includes the following metrics:
- **Total Operations**: The total number of operations (comparisons and assignments).
- **Execution Time (seconds)**: The time taken to execute the sorting algorithm.
- **Comparisons**: The number of element comparisons made during sorting.
- **Assignments**: The number of value assignments made during sorting.

### How to Use
1. Ensure you have Python installed on your system.
2. Import the necessary libraries: `random`, `matplotlib.pyplot`, and `time`.
3. Run the script to analyze and visualize the performance of the sorting algorithms under various scenarios.

You can adjust the input sizes and other parameters to customize the analysis as needed.

Feel free to explore and modify the code to further understand and experiment with sorting algorithms and their performance characteristics.
