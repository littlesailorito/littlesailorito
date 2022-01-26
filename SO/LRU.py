from random import randint
import Page








class Pages(Page.Page):
    def __init__(self, id):
        super().__init__(id)
        

left_board =1
right_board = 10

class LFU:
    def __init__(self,max_size,num_ref):
        self.steps = 1
        self.references_ref =[]
        self.max_size = max_size
        self.box =[]
        self.ref_ids =[]
        
        self.iterator = 0
        self.it_box =0
        self.all_num ={

    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0,
    "10" : 0



}

        for i in range(num_ref):
            self.references_ref.append(Page.Page(randint(left_board, right_board)))
            self.ref_ids.append(self.references_ref[i].id)
        for i in  range(max_size):
            self.box.append("")
        self.change =0


    def Begin(self):


        for i in range(self.it_box,len(self.box)):

            for j in range(self.iterator,len(self.references_ref)):

                
                if  self.steps == 1 :
                    print(f"{LFU_T.steps}. {LFU_T.box}")
                    break

                if self.box[i] == "":

                    del self.box[i]
                    self.box.insert(i, self.references_ref[j].id)

                    self.all_num[str(self.references_ref[j].id)]+=1

                    self.references_ref[j].done = True
                    
                    self.iterator+=1
                    print(f"{self.steps}. {self.box}")

                    if self.it_box <len(self.box)-1:
                        self.it_box+=1
                    else:
                        self.it_box = 0
                    break

                if i <len(self.box)-1:

                    self.steps+=1
                    return
            
            self.steps+=1
            return
                    

    def Placing_pages(self):
        if self.Is_it_full() == True:

            self.it_box =0

            while True:

                for i in range(self.it_box,len(self.box)):
                    
                    #sortujemy nasz dictionary wszystkich liczb
                    self.all_num =sorted(self.all_num.items(),key = lambda v :v[1])

                    #Z powrotem konwertujemy na dict
                    self.all_num =dict(self.all_num)

                    #Poruszamy sie po kluczach w dict
                    for key in self.all_num.keys():
                        
                        #porownujemy klucz do wartosci tablicy
                        if int(key) !=0 and int(key) == self.box[i]:

                            del self.box[i]
                            self.box.insert(i, self.references_ref[self.iterator].id)
                            
                            self.references_ref[self.iterator].done = True
                            
                            #Zwiekszamy ilosc powtorzen elementu dict
                            self.all_num[str(self.references_ref[self.iterator].id)]+=1
                            #jesli osiagnelismy iteratorem ostatni element to konczy petle
                            if self.iterator == len(self.references_ref)-1:
                                return
                            print(f"{self.steps}. {self.box}")
                            
                            self.iterator+=1
                            self.steps+=1
                            if self.it_box < len(self.box)-1:
                                self.it_box+=1
                            else:
                                self.it_box=0
                            break
                    
                        
                    
                        

                        
                        
                        
                        

    def Is_it_full(self):
        for i in self.box:
            if i == "":
                return False
        return True

    def Is_done(self):
        for i in self.references_ref:
            if i.done == False:
                return False
        return True
    
    def Write_into_file(self):
        new_dict ={}
        for i in sorted(self.all_num):
            new_dict[i]=self.all_num[i]
        
        with open("Results_LRU.txt","w") as file:
            file.write("  Usage\n")
            for key in new_dict.keys():
                file.write(f"{key}. {new_dict[key]}\n")
            


#Prosimy uzytkownika o wielkosc ramki
max_size = int(input("Name the max size of the frame: "))
#Prosimy uzytkownika o ilosc procesow
max_ref = int(input("Name the max number of pages: "))
#Tworzymy klase LFU
LFU_T = LFU(max_size, max_ref)

while LFU_T.iterator<len(LFU_T.ref_ids):
    #Sprawdzamy czy ramka jest juz pelna

    if LFU_T.Is_it_full() == False:
        LFU_T.Begin()

    #Jesli tak to zaczynamy podmieniac strony najdawniej uzywane
    else:
        
        LFU_T.Placing_pages()

        #Sprawdzamy czy juz wszystkie strony zostaly uzyte
        if LFU_T.Is_done() == True:
            break
print(f"The algorithm LFU has been completed in {LFU_T.steps-1} steps.")
LFU_T.Write_into_file()