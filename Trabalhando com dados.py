# explorando os dados
import math
import random
from collections import Counter
from matplotlib import pyplot as plt
from probabilidades import inverse_normal_cdf


def bucketsize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    return Counter(bucketsize(point, bucket_size) for point in points)


def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title('')
    plt.show()

def compare_two_distributions():

    random.seed(0)

    uniform = [random.random(-100, 101) for _ in range(10000)]
    normal = [57 * inverse_normal_cdf(random.random())
              for _ in range(10000)]


    plot_histogram(normal, 10, "histograma normal" )

def random_normal():
    return inverse_normal_cdf(random.random)

xs=[random_normal() for _ in range(1000)]
ys1=[x + random_normal()/2 for x in xs]
ys2=[-x +random_normal()/2 for x in xs]

plt.scatter(xs, ys1, marker='.', color='b', label='ys1')
plt.scatter(xs, ys2, marker='.', color='r', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title('distribuciones conjuntas muito diferentes')
plt.show()

