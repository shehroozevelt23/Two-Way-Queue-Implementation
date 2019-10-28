class Double:
    """
    Fields: _value stores any value
            _next points to the next node in the list
            _prev points to the previous node in the list
    """

    ## Double(value) produces a newly constructed doubly-linked node
    ##     storing value.
    ## __init__: Any -> Double
    def __init__(self, value, next = None, prev = None):
        self._value = value
        self._next = next
        self._prev = prev

    ## repr(self) produces a string with the information in self.
    ## __repr__: Double -> Str
    def __repr__(self):
        if self._value == None:
            return "Empty node"
        else:
            return str("Node containing " + self._value)

    ## self.access() produces the value stored in self.
    ## access: Double -> Any
    def access(self):
        return self._value

    ## self.next() produces the node to which self is linked
    ##    using next or None if none exists.
    ## next: Double -> (anyof Double None)
    def next(self):
        return self._next

    ## self.prev() produces the node to which self is linked
    ##    using prev or None if none exists.
    ## next: Double -> (anyof Double None)
    def prev(self):
        return self._prev

    ## self.store(value) stores value in self.
    ## Effects: Mutates self by storing value in self.
    ## store: Double, Any -> None
    def store(self, value):
        self._value = value

    ## self.link_next(node) links node using the next pointer.
    ## Effects: Mutates self by linking node using the next pointer.    
    ## link: Double (anyof Double None) -> none
    def link_next(self, node):
        self._next = node

    ## self.link_prev(node) links node using the prev pointer.
    ## Effects: Mutates self by linking node using the prev pointer.
    ## link: Double (anyof Double None) -> none
    def link_prev(self, node):
        self._prev = node


class TwoWayQueue:

    def __init__(self):
        self.front = None
        self.end = None 
        self.size = 0
    
    def is_empty(self):
        return self.front == None

    def first(self):
        return self.front._value
    
    def last(self):
        return self.last._value
    
    def enqueue_first(self, data):
        Node = Double(data)
        Node._prev = None
        
        if self.size == 0:
            self.end = Node
            self.front = Node
            Node._next = None
            
        elif self.size == 1:
            self.end._prev = Node
            Node._next = self.end
            self.front = Node
        else:
            Node._next = self.front
            self.front._prev = Node
            self.front = Node 
            
        self.size += 1
        
    def dequeue_first(self):
        if self.is_empty():
            return None
        elif self.size == 1:
            ret = self.front._value
            self.front = None
            self.end = None
            self.size = 0
        else:
            ret = self.front._value
            self.front = self.front._next
            self.front._prev = None
            self.size -= 1
        return ret
    
    def enqueue_last(self, data):
        Node = Double(data)
        Node._next = None
        
        if self.size == 0:
            self.front = Node
            self.end = Node
            Node._prev = None
        
        elif self.size == 1:
            self.front._next = Node
            Node._prev = self.front
        
        else:
            Node._prev = self.end
            self.end._next = Node
            self.end = Node
            
        self.size += 1
   
    def dequeue_last(self):
        if self.is_empty():
            return None
        elif self.size == 1:
            ret = self.end._value
            self.front = None
            self.end = None
            self.size = 0
        else:
            ret = self.end._value
            self.end = self.end._prev
            self.end._next = None
            self.size -= 1
        return ret 
    
    def shift_first(self):
        val = self.dequeue_first()
        self.enqueue_last(val)
    
    def shift_last(self):
        val = self.dequeue_last()
        self.enqueue_first(val)
    
    def dequeue_all(self):
        self.front = None
        self.end = None
        self.size = 0
        




    