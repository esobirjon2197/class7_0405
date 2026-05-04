13-m
class Universitet:
    def __init__(self, nomi, studentlar):
        self.nomi = nomi
        self.__studentlar = studentlar

    def qabul(self, n):
        self.__studentlar += n

    def bitiruv(self, n):
        self.__studentlar -= n

    def info(self):
        print(f"Universitet: {self.nomi}")
        print(f"Studentlar: {self.__studentlar}")


u1 = Universitet("TATU", 1000)
u1.info()

u1.qabul(200)
u1.info()

u1.bitiruv(150)
u1.info()


# 14-m
class Kafe:
    def __init__(self, nomi, daromad):
        self.nomi = nomi
        self.__daromad = daromad

    def sotuv(self, summa):
        self.__daromad += summa

    def harajat(self, summa):
        self.__daromad -= summa

    def info(self):
        print(f"Kafe: {self.nomi}")
        print(f"Daromad: {self.__daromad}")


kf1 = Kafe("Coffee Time", 5000)
kf1.info()

kf1.sotuv(2000)
kf1.info()

kf1.harajat(1000)
kf1.info()

