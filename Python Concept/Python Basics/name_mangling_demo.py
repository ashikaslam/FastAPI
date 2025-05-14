class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance               # Protected attribute (convention only)
        self.__pin = "1234"                   # Private attribute (name mangled)

    def get_balance(self):
        return self._balance

    def access_pin(self):
        # Accessing name-mangled attribute inside the class
        return self.__pin

# Create object
acc = BankAccount("Alice", 5000)

# Access public attribute
print("Account holder:", acc.account_holder)  # ✅ OK

# Access protected attribute (not recommended, but possible)
print("Balance (protected):", acc._balance)   # ✅ OK but use with caution

# Access private attribute directly (will cause error)
try:
    print("PIN:", acc.__pin)  # ❌ Raises AttributeError
except AttributeError:
    print("Cannot access __pin directly!")

# Access private attribute using name mangling
print("PIN (via name mangling):", acc._BankAccount__pin)  # ✅ OK

# Access via method (recommended way)
print("PIN (via method):", acc.access_pin())  # ✅ OK
