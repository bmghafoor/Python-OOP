"""Python serial number generator."""



class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,num=0):
        """Initialize make a self next to increment and keep original copy to reset"""
        self.num = self.next = num
    
    def generate(self):
        """Increment 1"""
        self.next += 1
        return self.next -1

    def reset(self):
        """Return to start"""
        self.next = self.num
    


    


