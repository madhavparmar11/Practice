# claculating the average marks of a student


class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        def avg_marks(self):
            sum = 0
            for i in marks:
                sum += i
                print("hello", self.name, " your average score is: ", sum / 3)

        s1 = student("madhav", [21, 31, 45])
        print(s1.avg_marks)
