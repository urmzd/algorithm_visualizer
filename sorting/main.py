from visualizer import Visualizer
from algorithms import bubble_sort
from visualizer import Visualizer
import matplotlib.pyplot as plt

array_to_test = Visualizer.array;

bubble_sort(array_to_test)

animation = Visualizer.camera.animate()

plt.show()