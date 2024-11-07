# ques--> create a employee class with all his details method ?


class employee:
    def __init__(self, name, role, dep, sal):
        self.name = name
        self.role = role
        self.dep = dep
        self.sal = sal

    def show_details(self):
        print(
            "name of employee is: ",
            self.name,
            "role is: ",
            self.role,
            "department is: ",
            self.dep,
            "salary is: ",
            self.sal,
        )

    #    def per(self):
    #       print("the perimeter of the circle is: ", 2 * 3.141 * self.r)

    e1 = employee("madhav", "senior executive", "r&d", 20000000)
    print(e1.show_details())
    # print(c1.per())
