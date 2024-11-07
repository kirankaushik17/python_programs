#develop three programs using class and object concept for demonstrating local, static, instancevariables
#1. local variable
class LocalVariables:
    def display_local_variables(self, name, age):
        local_name = name
        local_age = age

        print("Local Variables:")
        print("Name:", local_name)
        print("Age:", local_age)
A = LocalVariables()
A.display_local_variables("kaushik", 19)

#2.static variable
class StaticVariables:
    static_variable = "I'm kaushik"

    def display_static_variable(self):
        print("Static Variable:", StaticVariables.static_variable)
A= StaticVariables()
B= StaticVariables()
StaticVariables.static_variable = "I'm kiran kaushik"
A.display_static_variable()
B.display_static_variable()

#3.Instance variables
class InstanceVariables:
    def __init__(self, name, age):
        self.instance_name = name
        self.instance_age = age

    def display_instance_variables(self):
        print("Instance Variables:")
        print("Name:", self.instance_name)
        print("Age:", self.instance_age)

X = InstanceVariables("kaushik", 19)
Y = InstanceVariables("varun", 25)

X.display_instance_variables()
Y.display_instance_variables()



