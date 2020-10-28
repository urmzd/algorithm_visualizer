import random
import matplotlib.pyplot as plt
from celluloid import Camera


class Visualizer:
    #fig = plt.figure()
    camera = Camera(plt.figure())
    
    array = random.sample(range(12), k=12)
    number_of_comparisons = 0

    colors = list(len(range(12)) * "b")

    algorithm_titles = {
        "selection-sort": "Selection Sort",
        "quick-sort": "Quick Sort",
        "heap-sort": "Heap Sort",
        "insertion-sort": "Insertion Sort",
        "merge-sort": "Merge Sort",
        "shell-sort": "Shell Sort",
        "bubble-sort": "Bubble Sort",
    }

    def __init__(self, title) -> None:
        self.title = title

    @staticmethod
    def visualize(swap_one, swap_two, array):
        Visualizer.number_of_comparisons += 1

        array_length = list(range(len(array)))

        Visualizer.colors[swap_one] = 'r'
        Visualizer.colors[swap_two] = 'g'

        plt.bar(array_length, array, color=Visualizer.colors)
        plt.title("selection-sort")
        plt.xlabel('Data Size: {}, Number Of Comparisons: {}'.format(
            len(array), Visualizer.number_of_comparisons))
        
        Visualizer.camera.snap()
