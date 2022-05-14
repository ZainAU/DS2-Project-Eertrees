from random import randint
# from timeit import timeit
from time import time
chars = ["C", "G", "T", "A"]
sequence = ""


def generate_sequence(length):
    s = ""
    for i in range(length):
        s += chars[randint(0, 3)]
    return s


prefixes = []


def create_prefixes(s):
    for i in range(len(s)):
        prefixes.append(s[0:i])


if __name__ == "__main__":
    start_times = []
    trials = [10, 100000, 1000000]
    for trial_no in range(len(trials)):
        print(trials[trial_no])
        sequence = generate_sequence(trials[trial_no])
        print(sequence)
        start = time()
        create_prefixes(sequence)
        x = time() - start  # start_time - curr_time
        print(prefixes, "\nTook", x, "seconds.")
