class A:
    def __init__(self, A = None, B = None):
        self.A = A
        self.B = B
        self.headers = dict()
        self.headers.update({"A" : self.A, "B" : self.B})

    def method(self):
        head = ""
        for x,y in self.headers.items():
            if y != None:
                head += str(x) + " :" + str(y) + "\r\n"
        return head

a = A(2)
print(a.method())


