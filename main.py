import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print("Time to Study")
        self.progress += 0.15

    def to_chill(self):
        print("Time to chill!")
        self.gladness += 5
        self.progress -= 0.1

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 2

    def is_alive(self):
        if self.progress < -0.5:
             print("Cast out...")
             self.alive = False
        elif self.gladness <= 0:
             print("Depression...")
             self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"Glandness = {self.gladness}")
        print(f"Progress = {self.progress}")

    def live(self, day):
        d = f"Day {day} of {self.name} life"
        print(f"{d:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_study()

        elif live_cube == 2:
             self.to_sleep()

        elif live_cube == 3:
             self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Student("Nik")
for day in range(1, 366):
    if nick.alive == False:
        break
    nick.live(day)
