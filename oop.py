class students():

    def __init__(self):
        self.name = ""
        self.age = 0

    def register(self,name,age):
        self.name = name
        self.age = age
        return "ok"



amil = students()

akhil = students()

amil.register("amil",50)

akhil.register("akhil",40)

print(amil.name,amil.age)
print(akhil.name,akhil.age)