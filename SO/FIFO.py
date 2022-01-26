from random import randint
import Page
left_board =1
right_board = 10

class FIFO():
    def __init__(self,size_frame, num):

        #iterator przechodzacy po kazdym elemencie w odwolaniach
        self.all_pages_iterator =0

        #obecne polozenie
        self.frame_iterator = 0

        #maksymalna ilosc ramek
        self.max_size = size_frame

        #Iterator ile bylo chybien
        self.miss =0

        #ramka
        self.frame =[]

        #Id procesow
        self.idies =[]

        #Wszystkie odwolania do stron
        self.all_pages =[]
        
        #zmienna pomocnicza zwiazana z powtorzeniem iteracji jesli pojawilo sie powtorzenie
        self.actual_misses =0

        #przebyte kroki
        self.steps = 1

        #Tworrzymy strony i je zapisujemy do pliku txt
        for i in range(num):
            self.all_pages.append(Page.Page(randint(left_board, right_board)))
            self.idies.append(self.all_pages[i].id)
           
        with open("Results_FIFO.txt","w") as file:
                file.write(f"{self.idies}\n")

        
    #W momencie kiedy ramka jest pelna lub jej wielkosc wciaz nie osiagnela maksymalnej wielkosci
    def Begin(self):

       if self.steps == 1 :

           print(f'{self.steps}. {self.frame}')
           with open("Results_FIFO.txt","a") as file:
                file.write(f"{self.steps}. {self.frame}\n")
           self.steps+=1

           
        
        #Powtarzamy do momentu kiedy ramka nie osiagnela maksymalna wielkosc
       while len(self.frame)<self.max_size:

            if self.Check_if_reapets() ==False:
                #Dodajemy strone na koniec ramki  
                        self.frame.append(self.all_pages[self.all_pages_iterator].id)

                        print(f"{self.steps}. {self.frame}")
                        with open("Results_FIFO.txt","a") as file:
                            file.write(f"{self.steps}. {self.frame}\n")

                        #zmieniamy flage na wykonane
                        self.all_pages[self.all_pages_iterator].done =True

                        #Zwiekszamy iterator wszystkich odwolan
                        self.all_pages_iterator+=1 

                        #Zwiekszamy krok
                        self.steps+=1
                        
            #Kiedy ramka osiagnela maksymalna wielkosc
            else: 
                #Jesli pojawilo sie powtorzenie to
                #Sprawdzamy czy iterator w odwolaniach juz nie przeszedl wszystkich odwolan
                if self.all_pages_iterator <len(self.all_pages)-1:

                    #Jesli nie to zwiekaszamy go oraz licznik chybien
                    self.all_pages_iterator+=1
                    self.miss+=1

                    print(f"{self.steps}. {self.frame}")

                    with open("Results_FIFO.txt","a") as file:
                        file.write(f"{self.steps}. {self.frame}\n")

                    self.steps+=1
                else:
                    #inaczej konczymy algorytm
                    break

            
           
    
    def Replacing(self):
        #Sprawdzamy czy iterator w odwolaniach juz nie przeszedl wszystkich odwolan
        while self.all_pages_iterator <len(self.all_pages)-1:

            #Sprawdzamy czy strona jz nie sie nie pojawila w ramce
            if self.Check_if_reapets() == False:

                #usuwamy pierwszy element
                del self.frame[0]

                #Wstawiamy strone na koniec ramki strone z odwolan
                self.frame.append(self.all_pages[self.all_pages_iterator].id) 
                
                #zmieniamy flage na wykonane
                self.all_pages[self.all_pages_iterator].done =True
                

                print(f"{self.steps}. {self.frame}")
                with open("Results_FIFO.txt","a") as file:
                            file.write(f"{self.steps}. {self.frame}\n")


                self.steps+=1
                #Zwiekszamy iterator wszystkich odwolan jesli jest mniejszy niz index ostatniego elementu
                if self.all_pages_iterator <len(self.all_pages)-1:
                    self.all_pages_iterator+=1
                else:
                    break
            else:
                #Jesli strona sie powtorzyla to zwiekszamy iterator oraz licznik chybien
                if self.all_pages_iterator <len(self.all_pages)-1:

                    self.all_pages_iterator+=1

                    self.miss+=1
                    print(f"{self.steps}. {self.frame}")

                    with open("Results_FIFO.txt","a") as file:
                        file.write(f"{self.steps}. {self.frame}\n")

                    #Zmienna pomagajaca w powtorzeniu jesli zostalo odnotowane chybienie
                    self.actual_misses +=1
                    self.steps+=1

                else:
                    
                    break


                
        


           

        
                

    def Check_if_reapets(self):
        for i in self.frame:
            if i == self.all_pages[self.all_pages_iterator].id:
                self.miss+=1
                return True
        return False

#Prosimy uzytkownika o wielkosc ramki
max_size = int(input("Name the max size of the frame: "))
#Prosimy uzytkownika o ilosc procesow
max_ref = int(input("Name the max number of pages: "))
#Tworzymy klase FIFO
FIFO_T =FIFO(max_size,max_ref)

FIFO_T.Begin()
FIFO_T.Replacing()
print(f"It has been {FIFO_T.steps-1} steps and {FIFO_T.miss} misses")
with open("Results_FIFO.txt","a") as file:
    file.write(f"It has been {FIFO_T.steps-1} steps and {FIFO_T.miss} misses\n")

                    

                
                    

   
        





    

