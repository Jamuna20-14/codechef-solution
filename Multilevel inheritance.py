class College:
    def college_name(self):
        print("College: SMVEC Engineering College")

class Volleyball(College):
    def volleyball_players(self):
        print("Volleyball Team:")
        print("Arun")
        print("Bala")
        print("Kavin")
        print(" ")
class Football(Volleyball):
    def football_players(self):
        print("Football Team:")
        print("Raj")
        print("Vijay")
        print("Ajay")
        print(" ")
class HundredMeters(Football):
    def runners(self):
        print("100 Meters Participants:")
        print("Surya")
        print("Rahul")
        print("Karthik")
        print(" ")
obj = HundredMeters()

obj.college_name()
obj.volleyball_players()
obj.football_players()
obj.runners()
o/p:
College: SMVEC Engineering College
Volleyball Team:
Arun
Bala
Kavin
 
Football Team:
Raj
Vijay
Ajay
 
100 Meters Participants:
Surya
Rahul
Karthik
 
