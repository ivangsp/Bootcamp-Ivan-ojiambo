class BinarySearch(list):
    def __init__(self, a, b):

        self.a = a      # length of the list to be created
        self.b = b      # the step or difference between consecutive values
        self.length = list()

        for item in range(b, (a*b)+1, b):
            self.append(item)

        self.length = len(self) # returns the number of elements in the array


    #implement the binary search algorithm
    def search(self, item): # c is the argument which is the value you are to find
        output ={}
        count =0
        index = 0
        first = 0
        last = len(self)-1
        found = False


        while first<=last and not found:
            midpoint = (first + last)//2
            if self[midpoint] == item:
                 found = True
                 index = midpoint

            else:
                if item < self[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
            count +=1

        if found == True:
            output['count'] = count
            output['index'] = midpoint
        else:
            output['count'] = 3
            output['index'] = -1

        return output

x = BinarySearch(100, 10)
y = BinarySearch(20, 2)

search1 = x.search(30)
search2 = y.search(40)
search3 = y.search(33)
print x
print search1
print y
print search2
print search3

