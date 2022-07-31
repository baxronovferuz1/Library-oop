import sys

class Library:
    def __init__(self,listofbooks):
        self.availablebooks=listofbooks

    def displayAvaiablebooks(self):
        print("Kutubxonamizdagi kitoblar quyidagilardan iborat:")
        for book in self.availablebooks:
            print(book)

    
    def lendBook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("Siz so'ragan kitob,endi qarzga olindi")
            self.availablebooks.remove(requestedBook)

        else:
            print("Kechirasiz, siz so'ragan kitob hozirda kutubxonada yo'q")


    def addBook(self,returnedBook):
        self.availablebooks.append(returnedBook)
        print("olgan kitobingizni qaytarib berganingiz uchun tashakkur")

    
class Person:
    def requestBook(self):
        print("Olmoqchi bo'lgan kitobingizni kiriting>>>")
        self.book=input()  
        return self.book

    def returnBook(self):
        print("qaytarmoqchi bo'lgan kitobingizni nomini kiriting>>>")
        self.book=input()
        return self.book


def main():
    library=Library(["Maqsad","Amir Temur","Robin Sharma","Stiv Jobs"])
    person=Person()
    done=False
    while done==False:
        print(""">>>>>Kitoblar To'plami
        1.Barcha kitoblar Ro'yxati
        2.kitob xarid qilmoq
        3.kitobni qaytarish
        4.chiqish↩️
        """)

        choise=int(input("Tanlashingiz mumkin>>>"))
        if choise==1:
            library.displayAvaiablebooks()

        elif choise==2:
            library.lendBook(person.requestBook())
        elif choise==3:
            library.addBook(person.returnBook())

        elif choise==4:
            sys.exit()

main()

        

    
