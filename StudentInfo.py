class StudentInfo():
    """
    Simple class to hold student information:
      - First name
      - Last Name
      - BCIT student ID

    This is the first object of my Python career
    Implementing the __eq__ was key to answer
    Is the object already in a list
    Implementing the __repr__ help test the class to see if it is working
    
    """
    def __init__(self, first:str = 'John', last:str = 'Doe', id:str = 'ANNNNNNNN'):
        """
        Classic class constructor for Student info
        If you do not send data then defaults will be set
        """
        self.firstName = first
        self.lastName = last
        self.bcitID = id

    def __eq__(self, other):
        """
        Are two objects equal? Yes, if their BcitID
        is the same ... do not care about first and last
        """
        equal = False
        if (self.bcitID == other.bcitID):
            equal = True
        return equal

    def __repr__(self):
        """
        Convert the class to a string representation
        """
        return(f'{self.firstName}:{self.lastName}:{self.bcitID}')
        
    def studentDir(self) -> str:
        """
        Standard student directory name
        """
        return(f'{self.lastName}_{self.firstName}_{self.bcitID}')
# =============================================
# AD 99 - Run stuffer
# =============================================
if __name__ == "__main__":
    print('This module in not meant to be runnable; just IKEA for code')
    print('Instead, try running main.py in the terminal')