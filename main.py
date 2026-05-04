class Dokon:
    def __init__(self, nomi, kassa):
        self.nomi = nomi
        self.__kassa = kassa

    def sotuv(self, summa):
        self.__kassa += summa

    def harajat(self, summa):
        self.__kassa -= summa

    def info(self):
        print(f"Do'kon nomi: {self.nomi}")
        print(f"Kassadagi pul: {self.__kassa}")


d1 = Dokon("Market", 100)
d1.sotuv(20)
d1.info()

d1.harajat(30)
d1.info()
