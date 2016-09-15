import pandas as pd
import numpy as np
from collections import defaultdict
import itertools

class apriori:

    def __init__(self, file_, min_sup):
        self.file_ = file_
        self.min_sup = min_sup
        self.category_counter = {}


        self.read_fist_pass()
        self.determine_frequent_sets()

    def read_fist_pass(self):
        temp_category_counter = defaultdict(int)

        self.category_listing = []

        with open(self.file_, 'r') as f:
            for line in f:
                self.longest_line = 1
                if len(line.split(';')) > self.longest_line:
                    self.longest_line = len(line.split(';'))

                self.category_listing.append(line.replace('\n','').split(';'))

                for cat in line.split(';'):
                    temp_category_counter[cat.replace('\n','')] +=1

        self.determine_the_keepers(temp_category_counter)

    def determine_frequent_sets(self):
        temp_tup = set(self.category_counter.keys())

        temp_list = []
        for L in range(2, self.longest_line+1):
            temp_category_counter = defaultdict(int)
            for grouping in self.category_listing:
                for subset in itertools.combinations(grouping, L):
                    if temp_tup >= set(subset):
                        temp_category_counter[subset] +=1
            self.determine_the_keepers(temp_category_counter)

        print (self.category_counter)


    def determine_the_keepers(self, listing):
        for k,v in listing.items():
            if v >= self.min_sup:
                #print ('{}:{}'.format(v,k))
                self.category_counter[k] = v

if __name__ == '__main__':

    apriori('categories.txt', 771)
