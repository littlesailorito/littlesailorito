class Process():
    
    def __init__(self,id,burst,arrival):
       
        self.waiting = 0
        self.brst = burst
        self.arrival =arrival
        self.copied = False
        self.done = False
        self.id = id