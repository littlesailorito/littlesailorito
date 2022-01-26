from random import randint
import Process

left_border = 0
right_border = 10
class Gen():
    def __init__(self,number):

        self.Timer = 0
        self.processes = []

        self.scheduling = []
        self.T_finish = []

        

        

        for i in range(number):

            burst = randint(1,right_border)

            arrival = randint(left_border,right_border)
            
            
            self.processes.append(Process.Process(i+1,burst,arrival))
        self.processes = sorted(self.processes ,key = lambda x: x.arrival)