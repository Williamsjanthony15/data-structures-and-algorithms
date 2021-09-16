from code_challenges.linked_list import linked_list
from collections import Counter

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        sum = 0
        for char in key:
            num_val = ord(char)
            sum += num_val

        total = sum * 599

        index = total % self.size

        return index

    def add(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = linked_list()

        bucket = self.buckets[index]
        bucket.insert([key, value])

    def repeat(input):
        word = input.split('')
        dict = Counter(word)

        for i in word:
            if dict[i]>1:
                print (i)
                return
            