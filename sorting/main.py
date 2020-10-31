from algorithms import selection_sort, bubble_sort, insertion_sort, shell_sort, merge_sort, quick_sort, heap_sort
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from typing import List

#####################################
def inputNumber(min_num, max_num):
    while True :
        try:
            input_value = int(input())
            if (min_num <= input_value <= max_num):
                return input_value;

        except:
            print(f"Invalid number was entered, select a number between {min_num} and {max_num}. Try again!")

############################################

print ("How many integers would you like sorted?: ")

array_length = inputNumber(1, 2**64)
array = random.sample(range(1, array_length), k = array_length - 1)

algorithm_data = {
    1: ("Selection Sort", selection_sort(array)),
    2: ("Bubble Sort", bubble_sort(array)),
    3: ("Insertion Sort", insertion_sort(array)),
    4: ("Shell Sort", shell_sort(array)),
    5: ("Merge Sort", merge_sort(array)),
    6: ("Quick Sort", quick_sort(array, 0, len(array) - 1)),
    7: ("Heap Sort", heap_sort(array))
}
print("Welcome to Urmzd's Sorting Algorithm Visualizer: ")
print("Select one of the following sorting algorithms: ")

for k, v in algorithm_data.items(): 
    print (f"Type {k} for {v[0]}")

algorithm_number = inputNumber(1, 7)

algorithm_name, algorithm = algorithm_data.get(algorithm_number)

counter = [0]

def update_plot(array: List[int], plt_bar, counter: int):
    for bar, val in zip(plt_bar, array):
        bar.set_height(val)
    counter[0] += 1
    text.set_text(f"No. of Comparisons: {counter[0]}")


fig, ax = plt.subplots()
plt.title(f"Algorithm Name: {algorithm_name}")
plt_bar = ax.bar(range(len(array)), array, align="center")

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


visualization = anim.FuncAnimation(fig, func=update_plot,
                                   fargs=(plt_bar, counter), frames=algorithm, interval=1, repeat=False)
plt.show()
