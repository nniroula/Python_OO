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
    def __init__(self, start = 0):
        """ Create a instance generator at given starting point"""
        self.start = start
        #self.count = count
        self.count = start
    
        def generate(self):
            """ It should return next serial number accompanying start"""
            #self.count +=  1
            self.count = count + 1
            # return self.start + 1
            return self.count - 1
        
        def reset(self):
            """Reset start point to the original start number."""
            self.count = self.start



