# employee.py

class Employee:
    """
    A class to represent an employee with encapsulated fields:
    - name (cannot be empty)
    - age (must be positive)
    - salary (must be above a minimum wage)
    Uses @property decorators to control access and validation.
    """

    MINIMUM_WAGE = 10000

    def __init__(self, name: str, age: int, salary: float):
        # Internal attributes (with underscore prefix)
        self._name = None
        self._age = None
        self._salary = None

        # Use setters to initialize with validation
        self.name = name
        self.age = age
        self.salary = salary

    # -------------- NAME PROPERTY --------------

    @property
    def name(self):
        """
        Getter for name.
        This allows 'emp.name' to return the employee's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter for name.
        Validates that the name is not empty.
        """
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @name.deleter
    def name(self):
        """
        Deleter for name.
        Allows 'del emp.name'.
        """
        print("Deleting name...")
        self._name = None

    # -------------- AGE PROPERTY --------------

    @property
    def age(self):
        """Getter for age."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age with validation."""
        if value <= 0:
            raise ValueError("Age must be positive.")
        self._age = value

    # -------------- SALARY PROPERTY --------------

    @property
    def salary(self):
        """Getter for salary."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """
        Setter for salary.
        Ensures salary is above the minimum wage.
        """
        if value < self.MINIMUM_WAGE:
            raise ValueError(f"Salary must be at least {self.MINIMUM_WAGE}.")
        self._salary = value

    # -------------- BONUS CALCULATION (Read-only) --------------

    @property
    def yearly_bonus(self):
        """
        Read-only property.
        Calculates 10% bonus of current salary.
        """
        return self.salary * 0.10

    # -------------- DISPLAY METHOD --------------

    def display_info(self):
        """Prints all employee details."""
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Salary : {self.salary}")
        print(f"Bonus  : {self.yearly_bonus}")


# ----------- USAGE EXAMPLE -----------

if __name__ == "__main__":
    emp = Employee(name="Aslam", age=25, salary=20000)

    print("Employee Details:")
    emp.display_info()

    print("\nUpdating salary to 30000...")
    emp.salary = 30000

    print("\nUpdated Employee Details:")
    emp.display_info()

    print("\nDeleting name...")
    del emp.name

    print(f"Name after deletion: {emp.name}")


'''

🔍 Key Points:
@property turns a method into a getter.

@<property>.setter defines a setter for the property.

@<property>.deleter defines a deleter.

The internal variables use _name, _age, etc. to emphasize they are private.

The code also includes error handling (e.g., raise ValueError) and readable output.



Method Signatures
The getter, setter, and deleter methods must have the correct signatures. Typically:
Getter (@property): should accept only self and return a value.
Setter (@x.setter): should accept self and one argument (the value to set).
Deleter (@x.deleter): should accept only self.

'''