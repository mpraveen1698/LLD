
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value

# Define Square as above
square = Square(5)
print(square.width)  # Output: 5
print(square.height)  # Output: 5

square.width = 7
print(square.width)  # Output: 7
print(square.height)  # Output: 7  (automatically updated)

#here we cannot calculate the area of the rectange using the child class Square as the square has only side value and rectange has width and height. So with the Subclass "Square" we cannot calculate Area for Rectangle which violates the liskov principle


# shapes_lsp.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


#the parent class has calcualtearea method , which will be sucessfully implemented and executed irrespective of shapes

#updated implementation adheres to the **Liskov Substitution Principle (LSP)** more effectively than the original design.

# ### Explanation of LSP Violation in the Original Code:
# 1. **Liskov Substitution Principle** states that objects of a subclass should be replaceable with objects of the parent class without altering the correctness of the program.
# 2. In the original design:
#    - The `Square` class inherits from `Rectangle`.
#    - `Square`'s `__setattr__` method ensures that any change to `width` or `height` affects both dimensions to maintain the square's properties.
#    - This behavior breaks the `Rectangle` contract because a `Rectangle` should allow independent modification of `width` and `height`. Therefore, substituting a `Rectangle` with a `Square` leads to unexpected results.

# ### Correct Design with `Shape`:
# The updated code introduces an abstract base class, `Shape`, with a common interface (`calculate_area`). Both `Rectangle` and `Square` inherit from `Shape` and implement `calculate_area` independently:
# - **`Rectangle`**: Accepts `width` and `height` for its dimensions.
# - **`Square`**: Accepts a single `side` for its dimensions.
# - The `Square` and `Rectangle` classes no longer interfere with each other's behavior, fulfilling LSP requirements.

# ### Advantages of the Updated Design:
# 1. **Proper Abstraction**:
#    - The abstract base class `Shape` ensures that all shapes share a common interface (`calculate_area`).
# 2. **Compliance with LSP**:
#    - Both `Square` and `Rectangle` are valid `Shape` objects and behave consistently with their respective definitions.
# 3. **Improved Extensibility**:
#    - Adding new shapes (e.g., `Circle`, `Triangle`) only requires implementing the `calculate_area` method, without affecting existing code.

# By decoupling the `Square` and `Rectangle` classes and providing a shared abstraction (`Shape`), you achieve a more robust, scalable, and LSP-compliant design.