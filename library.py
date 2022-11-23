class library:
    def __init__(self, books):
        self.availablebooks = books

    def lending(self, requested1):
        if requested1 in self.availablebooks:
            print(requested1, "book is yours")
            self.availablebooks.remove(requested1)
        else:
            print("not available")

    def adding(self, collector):
        self.availablebooks.append(collector)
        print("you successfully returned")


class reader:
    def request(self):
        book = input("enter the book you want:")
        return book

    def returnbook(self):
        returnbook1 = input("enter which book you want to return")
        return returnbook1


l1 = library(["the indian", "the mind", "the best friend"])
r1 = reader()


def show():
    for i in l1.availablebooks:
        print(i)


while True:
    option = ["1.display books", "2.lending books", "3.addingbooks", "4.exit"]
    for i in option:
        print(i)
    user = int(input("enter your choice"))
    if user == 1:
        print(l1.availablebooks)
    elif user == 2:
        requested = r1.request()
        l1.lending(requested)
        show()
    elif user == 3:
        collector = r1.returnbook()
        l1.adding(collector)
        show()
    else:
        print("thank you")
    break
