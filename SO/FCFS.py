try:
    from random import randint
    import Generator
    
except:
    print("It can not be proceed including modules")

class FCFS(Generator.Gen):
    
    def __init__(self,number):
        super().__init__(number)
       
        self.arrivals = []
        self.bursts = []

        self.Turnaround_arr= []
        self.wait_time= []


    #Dodawanie do kolejki
    
    def Appending(self):
       for i in self.processes :
           if i.arrival == self.Timer and i.copied == False:
               self.arrivals.append(i.arrival)
               self.bursts.append(i.brst)
               i.copied  = True
               
    #Ustawianie w chronologii początek - koniec     
    def Calc_finish_time(self):
        for i in range(len(self.processes)):
            if i == 0:
                self.T_finish.append(self.arrivals[i] + self.bursts[i])
            else:
                self.T_finish.append(self.T_finish[i-1] + self.bursts[i])
    
    #Obliczanie czasu oczekiwania procesu
    def Calc_wait_time(self):

        self.wait_time.append(0)

        for i in range(1,len(self.arrivals)):

            self.wait_time.append(self.T_finish[i-1] - self.arrivals[i]) 

        return sum(self.wait_time)

    #Obliczanie czasu pracy procesu oraz zwrócenie jego sumy
    def Calc_Turnaround_time(self):
        for i in range(len(self.arrivals)):
            self.Turnaround_arr.append(self.T_finish[i] - self.arrivals[i])
        return sum(self.Turnaround_arr)
    
    #Zapis do pliku
    def Write_into_file(self):
        print(f"The average waiting time is {self.Calc_wait_time()/len(self.processes)}s and the average turnaround time is {FCFS_T.Calc_Turnaround_time()/len(FCFS_T.processes)}s")
        with open("Results_FCFS.txt","w") as file:
            file.write(f"Id\t Arrival\tBurst\n")
            for i in range(len(self.arrivals)):
                file.write(f"{i+1}.      {self.processes[i].arrival}\t   {self.processes[i].brst}\n")
            file.write(f"The average waiting time is {self.Calc_wait_time()/len(self.processes)}s and the average turnaround time is {round(FCFS_T.Calc_Turnaround_time()/len(FCFS_T.processes))}s\n\n")
        



    
    
FCFS_T = FCFS(int(input("Name the num of processes: ")))

while True:
    
    
    FCFS_T.Appending()
    FCFS_T.Timer+=1

    if len(FCFS_T.arrivals) == len(FCFS_T.processes):
        
        break
    
FCFS_T.Calc_finish_time()

FCFS_T.Calc_Turnaround_time()

FCFS_T.Write_into_file()

    

    
    