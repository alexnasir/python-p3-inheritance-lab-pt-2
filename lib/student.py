# Student class
class Student:
    def __init__(self, first_name="Unknown", last_name="Student"):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        '''Print a greeting message.'''
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        '''Prints a message indicating the student is raising their hand.'''
        print("Pick me!")

# ChattyStudent class
class ChattyStudent(Student):
    def hello(self):
        '''Uses super() to inherit behavior from Student's hello() and adds a chatty message.'''
        super().hello()  # Call the hello method from the parent class (Student)
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! "
              "What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        '''Uses super() to call the raise_hand() method 10 times.'''
        for _ in range(10):
            super().raise_hand()  # Call the raise_hand method from the parent class
