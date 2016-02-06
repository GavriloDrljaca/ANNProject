import numpy as np
from collections import Counter


def compare_results(test_results, output_results):
    length = len(test_results)
    test = np.array(test_results)
    output = np.array(output_results)
    equal = test == output
    c = Counter(equal)
    num_of_true = c.get(True)
    print num_of_true, length
    overall_results = float(num_of_true) / float(length)
    return overall_results


def compare_results_by_topic(test_results, output_results):
    if (len(test_results) != len(output_results)):
        return None
    # initialize dictionary
    counter = Counter(test_results)
    dict = {}
    for key in counter.keys():
        dict[key] = 0

    for idx, value in enumerate(test_results):
        if (value == output_results[idx]):
            dict[value] += 1

    for key in dict:
        dict[key] = float(dict[key]) / float(counter.get(key))

    return dict


def calculate_topic_percent(results):
    c = Counter(results)
    dict = {}
    for idx, key in enumerate(c.keys()):
        dict[key] = (float(c[idx]) / float(len(results)))*100
    return dict


x = [0, 1, 1, 2, 2, 3, 5, 6]
y = [0, 0, 1, 0, 0, 3, 0, 5]
print compare_results_by_topic(x, y)
print "Percentege: ", calculate_topic_percent(x)
