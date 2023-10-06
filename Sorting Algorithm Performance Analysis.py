import random
import matplotlib.pyplot as plt
import time

# Bubble Sort Algorithm
def bubble_sort(my_list):
    comparisons_counter = 0
    assignments_counter = 0
    list_length = len(my_list)  
    
    for pass_num in range(list_length): 
        swapped_flag = False
        for current_index in range(0, list_length - pass_num - 1):  
            comparisons_counter += 1
            if my_list[current_index] > my_list[current_index + 1]:
                assignments_counter += 3  # Swap requires 3 assignments
                my_list[current_index], my_list[current_index + 1] = my_list[current_index + 1], my_list[current_index]
                swapped_flag = True
        if not swapped_flag:
            break
    return comparisons_counter, assignments_counter


# Insertion Sort Algorithm
def insertion_sort(my_list):
    comparisons_counter = 0
    assignments_counter = 0
    list_length = len(my_list)  
    
    for current_index in range(1, list_length):  
        key = my_list[current_index]
        previous_index = current_index - 1 
        
        while previous_index >= 0 and my_list[previous_index] > key :
            comparisons_counter += 1
            my_list[previous_index + 1] = my_list[previous_index]
            assignments_counter += 1
            previous_index -= 1
            
        my_list[previous_index + 1] = key
        assignments_counter += 1
        
    return comparisons_counter, assignments_counter


# Selection Sort Algorithm
def selection_sort(my_list):
    comparisons_counter = 0
    assignments_counter = 0
    list_length = len(my_list)  
    
    for current_index in range(list_length):  
        min_index = current_index
        
        for next_index in range(current_index + 1, list_length):  
            comparisons_counter += 1
            if my_list[next_index] < my_list[min_index]:
                min_index = next_index
                
        my_list[current_index], my_list[min_index] = my_list[min_index], my_list[current_index]
        assignments_counter += 3  # Swap requires 3 assignments
        
    return comparisons_counter, assignments_counter


# Function to generate sorted input
def generate_sorted_input(size_of_list):
    return list(range(1, size_of_list + 1))


# Function to generate random input
def generate_random_input(size_of_list):
    my_list = list(range(1, size_of_list + 1))
    random.shuffle(my_list)
    return my_list


# Function to generate reverse-sorted input
def generate_reverse_sorted_input(size_of_list):
    return list(range(size_of_list, 0, -1))


"""Function to analyze  Sorting algorithms
that takes the 
sorting function insertion, bubble or selection 
and the type of input list sorted or not sorted 
and the name of case that appears 
and list of the values that every num in it will generate  list
it will return lists of values that we will use to mke the plot"""
def analyze_sorting_algorithms(sorting_function, input_generator, case_name, sizes):
    comparisons_list = []
    assignments_list = []
    total_operations_list = []
    execution_time_list = []

    for size in sizes:
        input_data = input_generator(size)
        comparisons_counter = 0
        assignments_counter = 0

        # Measure execution time
        start_time = time.time()
        
        comparisons_counter, assignments_counter = sorting_function(input_data.copy())
        
        # Measure execution time
        end_time = time.time()
        execution_time = end_time - start_time
        
        total_operations_counter = comparisons_counter + assignments_counter
        
        comparisons_list.append(comparisons_counter)
        assignments_list.append(assignments_counter)
        total_operations_list.append(total_operations_counter)
        execution_time_list.append(execution_time)

    return comparisons_list, assignments_list, total_operations_list, execution_time_list


# Main function
if __name__ == "__main__":
    sizes = list(range(100, 1001, 100))

    # Define sorting algorithms and cases
    sorting_algorithms = [("Bubble Sort", bubble_sort), ("Insertion Sort", insertion_sort), ("Selection Sort", selection_sort)]
    cases = [("Best Case", generate_sorted_input), ("Average Case", generate_random_input), ("Worst Case", generate_reverse_sorted_input)]
    metrics = [("Total Operations", "_operations"), ("Execution Time (seconds)", "_times"), ("Comparisons", "_comparisons"), ("Assignments", "_assignments")]

    # Create subplots for each metric
    for metric, metric_suffix in metrics:
        plt.figure(figsize=(12, 12))
        
        # Iterate through sorting algorithms
        for algorithm_name, algorithm_function in sorting_algorithms:
            # Plot the results for the current algorithm and metric
            plt.subplot(1, len(sorting_algorithms), sorting_algorithms.index((algorithm_name, algorithm_function)) + 1)
            
            for case_name, input_generator in cases:
                # Analyze and plot the current metric for the current algorithm and case
                comparisons_list, assignments_list, total_operations_list, execution_time_list = analyze_sorting_algorithms(
                    algorithm_function, input_generator, f"{case_name} ({algorithm_name})", sizes)
                
                if metric == "Total Operations":
                    plt.plot(sizes, total_operations_list, label=f"{case_name}")
                    plt.ylabel("Total Operations")
                    plt.title(f"{algorithm_name} Complexity Analysis ({metric})")
                elif metric == "Execution Time (seconds)":
                    plt.plot(sizes, execution_time_list, label=f"{case_name}")
                    plt.ylabel("Execution Time (seconds)")
                    plt.title(f"{algorithm_name} Execution Time Analysis")
                elif metric == "Comparisons":
                    plt.plot(sizes, comparisons_list, label=f"{case_name}")
                    plt.ylabel("Comparisons")
                    plt.title(f"{algorithm_name} Comparisons Analysis")
                elif metric == "Assignments":
                    plt.plot(sizes, assignments_list, label=f"{case_name}")
                    plt.ylabel("Assignments")
                    plt.title(f"{algorithm_name} Assignments Analysis")
            
            plt.xlabel("Input Size")
            #adding a legend to distinguish different cases. 
            plt.legend()
            # and enabling gridlines for better visualization.
            plt.grid(True)
    #After creating and configuring all subplots, 
    # plt.tight_layout() ensures that the subplots are properly arranged within the figure.
    plt.tight_layout()
    plt.show()