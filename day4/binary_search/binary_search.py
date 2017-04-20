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

        
        # check if val is the first element
        if item== self[first]:
            found = True
            index = 0
        # check if val is the last element
        elif item == self[last]:
            found = True
            index = self.index(item)

        # check if val is not present in the list
        elif  item not in self:
            found = True
            index = -1
            count = 3

        # Now implement binary search alogorith to search for it
        else:         
            while first<=last and not found:
                midpoint = (first + last)//2
                if self[midpoint] == item:
                     found = True
                     index = midpoint

                else:
                    count +=1
                    if item < self[midpoint]:
                        last = midpoint-1
                    else:
                        first = midpoint+1
                

        if found == True:
            output['count'] = count
            output['index'] = index
    

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

