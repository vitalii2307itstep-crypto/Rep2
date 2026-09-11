class Student:
    print("Hi")
    id_num = 0
    def __init__(self, id_num, height=180, name=None, money=0, knowledge=100):
        self.name = name
        self.height = height
        self.money = money
        self.knowledge = knowledge
        print(self.height)
        self.id_num = id_num
    def grow(self, height=1):
        self.height += height
    def __str__(self):
        return f"I am a student my name st: {self.name}"
    def __del__(self):
        print("")
    def work(self, money=60):
        self.money += money
        self.knowledge -= 20
    def rest(self, money=25):
        self.money -= money
        self.knowledge -= 25
    def study(self):
        self.knowledge += 50
        self.money -= 20
    def simulation(self):
        if self.money < 40:
            print(self.name, "працює")
            self.work()
            self.grow()
        elif self.knowledge < 50:
            print(self.name, "навчається")
            self.study()
            self.grow()
        else:
            print(self.name, "відпочиває")
            self.rest()
            self.grow()
first_student = Student(
    id_num=1,
    height=180,
    name="Max",
    money=100,
    knowledge=80)
second_student = Student(
    id_num=2,
    height=190,
    name="Ren",
    money=50,
    knowledge=120)
for month in range(1, 13):
    first_student.simulation()
    second_student.simulation()
    print("ID of first student equals:", first_student. id_num)
    print("ID of second student equals:", second_student. id_num)
    print("Max's Height:", first_student. height)
    print("Ren's Height:", second_student. height)
    print("Max's new money:", first_student. money)
    print("Ren's new money:", second_student. money)
    print("Max's new knowledge:", first_student. knowledge)
    print("Ren's new knowledge:", second_student. knowledge)
    print("Max's new money:", first_student. money)
    print("Ren's new money:", second_student. money)
    print("Max's new knowledge:", first_student. knowledge)
    print("Ren's new knowledge:", second_student. knowledge)
    print("Max's new money:", first_student. money)
    print("Ren's new money:", second_student. money)
