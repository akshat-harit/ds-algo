import copy

class Node:
    def __init__(self, data):
        self.next=None
        self.data = data

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, data=0):
        self.head = Node(data)
        self.end = self.head
        self.current = self.head

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return self.head

        prev = self.head
        curr = self.head.next
        # Can't use iterator due to inplace modifications
        while curr != None: 
            if curr.data == data:
                prev.next = curr.next
                return self.head
            else:
                prev = curr
                curr = curr.next
        raise ValueError("Element not found")

    def __str__(self):
        lst  = []
        for item in self:
            lst.append(str(item))
        return '->'.join(lst)

    def push(self, data):
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp

    def insert(self, data):
        if self.end is self.head:
            self.end = Node(data)
            self.head.next = self.end
        else:
            self.end.next = Node(data)
            self.end = self.end.next

    def __len__(self):
        l = 0;
        for i in self:
            l+=1
        return l

    def find(self, data):
        for i in self:
            if i.data == data:
                return i
        return None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current ==  None:
            self.current = self.head
            raise StopIteration
        else:
            self.ret = copy.copy(self.current)
            self.current = self.current.next
            return self.ret

    def head(self):
        return self.head

    def tail(self):
        y = LinkedList()
        y.head = self.head.next
        y.end = self.end
        return y


if __name__ == '__main__':
    x = LinkedList(data=1)
    x.insert(2)
    x.push(3)
    x.insert(5)
    print(x)
    x.delete(5)
    print(x)
