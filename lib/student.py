#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)
        print(f"{self.first_name} learned: {new_knowledge}")

# Example usage:
student = Student("Dan", "Petro")
student.learn("Python is a powerful programming language.")
print(student.knowledge)

        

        