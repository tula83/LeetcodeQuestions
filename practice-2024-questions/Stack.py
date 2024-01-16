class stack:

    def __init__(self):
        pass

    arr=[]


    def push(self,data):

        self.arr.insert(0,data)


    def pop(self):

        if self.arr:
             pop_data=self.arr[0]
             self.arr=self.arr[1:]
             return pop_data
        else:
            return "empty stack"
       
      
    
    def length(self):
        return len(self.arr)
    




class queue:
    def __init__(self):
        pass

    arr=[]

    def enqueue(self,data):

        self.arr.append(data)


    def dequeu(self):

        if self.arr:
            print(self.arr)
            deque_data=self.arr[0]
            self.arr=self.arr[1:]
            print(self.arr)
            return deque_data
        
        else:
            return "empty queue"
        
    
    def length(self):
        return len(self.arr)
    
    



# implement stack using queue
class stackQueue:
    def __init__(self):
        self.q1=queue()
        
    def push(self,data):

        self.q1.enqueue(data)

        self.q1.arr.reverse()
        
       # print(self.q1.arr)
    

    def pop(self):
        return self.q1.dequeu()
    



st2=stackQueue()
st2.push(1)
st2.push(2)
print(st2.pop())




