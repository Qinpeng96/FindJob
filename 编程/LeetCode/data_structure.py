import numpy as np 

class Node:
    def __init__(self,data):

        self.data = data
        self.next = None

        return 

    def hasValue(self,value)->bool:
        if self.data == value:
            return True
        else:
            return False