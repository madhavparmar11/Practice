# normal class and object syntax practice


class student:
    college_name = "abc univ"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        ####
        s1 = student("madhav", 21)
        print(s1.name, s1.age)
        print(s1.college_name)
