# The **Dependency Inversion Principle (DIP)** is one of the SOLID principles, which states:

# - High-level modules (business logic) should not depend on low-level modules (details); both should depend on abstractions.
# - Abstractions should not depend on details; details should depend on abstractions.

# This principle encourages using interfaces or abstract classes to decouple high-level logic from low-level implementations.



# ### **Violating DIP**

# Here's an example where a high-level module depends directly on a low-level module:


class Keyboard:
    def get_input(self):
        return "Keyboard Input"

class Monitor:
    def display_output(self, output):
        print(f"Displaying on Monitor: {output}")

class Computer:
    def __init__(self):
        self.keyboard = Keyboard()
        self.monitor = Monitor()

    def operate(self):
        input_data = self.keyboard.get_input()
        self.monitor.display_output(input_data)


#### Problem:
# 1. The `Computer` class (high-level module) directly depends on `Keyboard` and `Monitor` (low-level modules).
# 2. If you want to replace `Keyboard` with a `TouchScreen` or `Monitor` with a `Projector`, you must modify the `Computer` class.



### **Adhering to DIP**

# We introduce abstractions for `InputDevice` and `OutputDevice` and make the `Computer` class depend on these abstractions.


from abc import ABC, abstractmethod

# Abstractions
class InputDevice(ABC):
    @abstractmethod
    def get_input(self):
        pass

class OutputDevice(ABC):
    @abstractmethod
    def display_output(self, output):
        pass

# Low-level modules
class Keyboard(InputDevice):
    def get_input(self):
        return "Keyboard Input"

class TouchScreen(InputDevice):
    def get_input(self):
        return "TouchScreen Input"

class Monitor(OutputDevice):
    def display_output(self, output):
        print(f"Displaying on Monitor: {output}")

class Projector(OutputDevice):
    def display_output(self, output):
        print(f"Displaying on Projector: {output}")

# High-level module
class Computer:
    def __init__(self, input_device: InputDevice, output_device: OutputDevice):
        self.input_device = input_device
        self.output_device = output_device

    def operate(self):
        input_data = self.input_device.get_input()
        self.output_device.display_output(input_data)

# ### **Benefits of the Refactored Code**
# 1. **Abstraction Dependence**:
#    - The `Computer` class depends on `InputDevice` and `OutputDevice` abstractions rather than specific implementations.
# 2. **Flexibility**:
#    - You can easily swap `Keyboard` with `TouchScreen` or `Monitor` with `Projector` without modifying the `Computer` class.
# 3. **Extensibility**:
#    - Adding new input or output devices (e.g., `VoiceInput`, `VRHeadset`) only requires implementing the respective interface without altering the `Computer` class.



### Example Usage

# Using Keyboard and Monitor
keyboard = Keyboard()
monitor = Monitor()
computer = Computer(keyboard, monitor)
computer.operate()

# Using TouchScreen and Projector
touch_screen = TouchScreen()
projector = Projector()
computer = Computer(touch_screen, projector)
computer.operate()

# ### Key Takeaways:
# 1. DIP ensures that high-level modules (like `Computer`) are not tightly coupled with low-level modules (like `Keyboard` or `Monitor`).
# 2. It fosters a flexible and maintainable design, enabling easy substitution of implementations.
# 3. It reduces the impact of changes in low-level details on high-level modules.