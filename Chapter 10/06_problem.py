from random import randint

class Train:

    def __init__(Harry, TrainNo):
        Harry.TrainNo = TrainNo

    def book(Harry, fro, to):
        print(f"Ticket is booked in train no {Harry.TrainNo} from {fro} to {to}")

    def status(Harry):
        print(f"train no {Harry.TrainNo} is running on time")

    def getfare(Harry, fro , to):
        print(f"Ticket fare in train no {Harry.TrainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12388)
t.book("rampur","Delhi")
t.status()
t.getfare("rampur","Delhi")
    