class lib:
    def __init__(self):
        self.bookno=0
        self.book=[]

    def addbook(self,book):
        self.book.append(book)
        self.nobooks=len(self.book)

    def info(self):
        print("Number of books in the library is ",self.nobooks)
        for book in self.book:
            print("\nBook name=",book)
            
l1=lib()
l1.addbook('Geeta')
l1.addbook('Ramayan')
l1.addbook('Mahabharat')
l1.info()