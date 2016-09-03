class Counter(object):

    def __init__(self, name):
        self.name = name
        self.value = 0

    def incr(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def __str__(self):
        return "Counter({}, value={})".format(self.name, self.value)

comparisons = Counter(name="comparisons")
swaps = Counter(name="swaps")
