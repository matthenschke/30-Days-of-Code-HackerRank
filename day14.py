
class Difference:
    def __init__(self, a):
        self.__elements = a

        # Add your code here
    def computeDifference(self):
        sortedElements = sorted(self.__elements)
        self.maximumDifference = abs(
            sortedElements[0] - sortedElements[len(sortedElements) - 1])

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
