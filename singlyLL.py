class node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    
    def display(self):
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                print(n.ref)
                n=n.ref
    def add(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
ll1=linkedlist()
ll1.add(10)
ll1.add(20)
ll1.display()





