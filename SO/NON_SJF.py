

import Generator

class SJF_NON(Generator.Gen):

    #Tworzymy algorytm z wartosciami startowymi
    def __init__(self,num):
        super().__init__(num)
        self.readies =[]
        
        self.arrivals = []
        self.bursts =[]
        self.turnaround =[]
        self.wait_time =[]

        
    #Dodajemy do kolejki poszczegolne procesy
    def Appending(self):
        
        for i in self.processes:
            if i.arrival <= self.Timer and i.copied == False:
                self.readies.append(i)
                self.scheduling.append(i)
                i.copied = True
                
    
        
    def Write_into_file(self):
        
        with open("Results_SJF.txt","w") as file:
            file.write(f"Id\tArrival\tBurst\tTurnaround\tWait_time\n")
            for i in range(len(self.processes)):
                file.write(f"{i+1}\t   {SJF_N.readies[i].arrival}\t     {SJF_N.readies[i].brst}\t    {SJF_N.turnaround[i]}\t\t    {SJF_N.wait_time[i]}\n" )

            file.write(f"Average waiting time is {self.average_wait} and average turnaround time is {self.average_turnaround}\n")
    
    
    #Obliczamy czas koncowy procesu
    def Calc_finish_time(self):

       
            minn = '0'
            #Znajdujemy pierwszy niewykonany proces
            for i in range(len(self.readies)):
                if self.readies[i].done == False:
                    minn = i
                    break

           

           
            if minn != '0':
                    #Szukamy proces z najkrótszym czasem wykonywania
                    for i in range(minn,len(self.readies)):
                        if self.readies[i].done == False and self.readies[i].brst <self.readies[minn].brst :
                            minn = i
                    #Gdy jeszcze zaden proces nie zostal wykonany
                    if len(self.T_finish) == 0:

                        self.T_finish.append(self.readies[minn].arrival)
                        #obliczamy moment kiedy sie konczy
                        complementation = self.readies[minn].arrival + self.readies[minn].brst
                        self.T_finish.append(complementation)
                        #Podnosimy flage,ze zostal wykonany
                        self.readies[minn].done =True
                        #Przenosimy potrzebne dane do dalszych obliczen - waiting time
                        self.arrivals.append( self.readies[minn].arrival)
                        self.bursts.append(self.readies[minn].brst)
                        #Dodajemy czas wykonywania do ogolnego timeru
                        self.Timer += self.readies[minn].brst
                    else:
                         #obliczamy moment kiedy sie konczy
                        complementation = self.T_finish[len(self.T_finish)-1] + self.readies[minn].brst
                        
                        self.T_finish.append(complementation)
                        #Podnosimy flage,ze zostal wykonany
                        self.readies[minn].done =True
                        #Przenosimy potrzebne dane do dalszych obliczen - waiting time
                        self.arrivals.append( self.readies[minn].arrival)
                        self.bursts.append(self.readies[minn].brst)
                        #Dodajemy czas wykonywania do ogolnego timeru
                        self.Timer += self.T_finish[len(self.T_finish)-1]
    #Funkcja, ktora pomaga stwierdzic czy wszystkie procesy zostaly wykonane
    def Done(self):
        for i in self.readies:
            if i .done == False:
                return False
        return True

    #Funkcja obliczajaca średni czas oczekiwania procesu
    def Calc_wait_time(self):
       
        for j in range(1,len(self.T_finish)):
            self.turnaround.append(self.T_finish[j] - self.arrivals[j-1])
            continue

        for i in range(len(self.readies)):
            if i == 0:
                self.wait_time.append(0)
                continue

            
            self.wait_time.append(self.turnaround[i] - self.bursts[i])
        
        self.average_wait = sum(self.wait_time)/len(self.readies)
        self.average_turnaround = sum(self.turnaround)/len(self.readies)
       

SJF_N = SJF_NON(int(input("Name the number of the processes: ")))



while True:
    previous = len(SJF_N.scheduling)
    SJF_N.Appending()
    SJF_N.Calc_finish_time()
    if SJF_N.Done() == True and len(SJF_N.readies) == len(SJF_N.processes):
        break
    elif previous == len(SJF_N.readies):
        SJF_N.Timer += 1








SJF_N.Calc_wait_time()
print("Id\tArrival\t  Burst\tTurnaround\tWait_time")

for i in range(len(SJF_N.processes)):
    print(f"{i+1}\t   {SJF_N.readies[i].arrival}\t     {SJF_N.readies[i].brst}\t    {SJF_N.turnaround[i]}\t\t    {SJF_N.wait_time[i]}" )
    

print(f"Average waiting time is {SJF_N.average_wait} and average turnaround time is {SJF_N.average_turnaround} ")

SJF_N.Write_into_file()
          
    
   