class Student:
    students = 0
    def __init__(self,name,staff):
        self.name = name
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)

    def visit_office_hours(self,staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self,name):
        self.name = name
        self.student = {}

    def add_student(self,student):
        self.student[student.name] = student

    def assist(self,student):
        student.understanding += 1

class MinList:
    def __init__(self):
        self.items = []
        self.size = 0

    def append(self,item):
        """
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items += [item]
        self.size += 1

    def pop(self):
        """
        >>> m = MinList
        >>> m.append(4)
        >>> m.append(1)
        >>> m.apppend(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        min_item =  min(self.items)
        self.items = [i for i in self.items if i != min_item]
        self.size -= 1#默认最小元素只有一个
        return min_item

class  Email:
    def __init__(self,msg,sender_name,recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    def __init__(self):
        self.clients = {}

    def send(self,email):
        if email.recipient_name in self.client:
            email.recipient_name.receive(email)

    def register_client(self,client,client_name):
        self.clients[client_name] = client

class Client:
    def __init__(self,server,name):
        self.name = name
        self.server = server
        self.inbox = []

    def compose(self,msg,recipient_name):
        email = Email(msg,self.name,recipient_name)
        self.server.send(email)

    def receive(self,email):
        self.inbox.append(email)


class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self,name,owner,lives=9):
        self.lives = lives
        Pet.__init__(self,name,owner)

    def talk(self):
        print(self.name + ' says meow!')

    def lose_life(self):
        if not self.is_alive:
            print(self.name + ' has no more live to lose.')
        else:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False


class NoisyCat(Cat):
    def talk(self):
        super().talk()
        super().talk()

    def __repr__(self):
        return "NoisyCat('{}','{}')".format(self.name, self.owner)
