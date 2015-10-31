class Parent():
    def __init__(self, last_name_parent, eye_color_parent):
        print("parent constructor called")
        self.last_name = last_name_parent
        self.eye_color = eye_color_parent

    def show_info(self):
        print("last name -"+self.last_name)
        print("eye color -"+self.eye_color)

# this shows inheritance and showing that child class inherits parent class such
# that all the attributes of the parent class are inherited by the child class
# all the functions are also inherited in the child class
class Child(Parent):
    def __init__(self, last_name_parent, eye_color_parent, number_of_toys_child):
        # what is done here is to initialize the two agruments we call the init
        # method of the parent class and no need to again initialize the object
        print("child constructor called")
        Parent.__init__(self, last_name_parent, eye_color_parent)
        self.number_of_toys = number_of_toys_child

    # what we see here is subclass can override the functions of the parent class
    def show_info(self):
        print("last name -"+self.last_name)
        print("eye color -"+self.eye_color)
        print("number of toys-"+self.number_of_toys)

billy_cyrus = Parent("cyrus", "blue")
#print(billy_cyrus.last_name)
miley_cyrus = Child("cyrus", "blue", "100")
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
#billy_cyrus.show_info()
miley_cyrus.show_info()
