import numpy as np
from collections import Counter
from decimal import *

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

def winner(output): # output je vektor sa izlaza neuronske mreze
    return max(enumerate(output), key=lambda x: x[1])[0]


def winner_cut(output):
    max_idx = 0;
    max_val = 0;
    for idx, val in enumerate(output):
        if val>max_val:
            max_val = val
            max_idx = idx
    if max_val<0.45:
        return 6
    else:
        return max_idx


def winner_array(outputs, cut):
    ret = []

    for output in outputs:
        if (cut):
            ret.append(winner_cut(output))
        else:
            ret.append(winner(output))

    return ret

def print_results_by_topic(alphabet, dict):

    TWOPLACES = Decimal(10) ** -2
    str = ""
    for key in dict:
        str+= alphabet[key] + " : " + Decimal(dict[key]).quantize(TWOPLACES).__str__() + "% \n"
    return str

'''
x = [0, 1, 1, 2, 2, 3, 5, 6]
y = [0, 0, 1, 0, 0, 3, 0, 5]
print compare_results_by_topic(x, y)
print "Percentege: ", calculate_topic_percent(x)
'''