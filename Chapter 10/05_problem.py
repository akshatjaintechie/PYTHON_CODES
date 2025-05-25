from random import randint

class Train:

    def __init__(self, TrainNo):
        self.TrainNo = TrainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.TrainNo} from {fro} to {to}")

    def status(self):
        print(f"train no {self.TrainNo} is running on time")

    def getfare(self, fro , to):
        print(f"Ticket fare in train no {self.TrainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12388)
t.book("rampur","Delhi")
t.status()
t.getfare("rampur","Delhi")
    