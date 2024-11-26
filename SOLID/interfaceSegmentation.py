# **Interface Segregation Principle (ISP)** states that no client should be forced to depend on methods it does not use. Instead of one large interface, it's better to have multiple smaller, more specific interfaces that are relevant to the clients.

# Here’s an example that demonstrates how to refactor code to adhere to the Interface Segregation Principle.



### **Violating ISP**

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

    @abstractmethod
    def fax_document(self, document):
        pass

# Clients
class BasicPrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        raise NotImplementedError("BasicPrinter does not support scanning.")

    def fax_document(self, document):
        raise NotImplementedError("BasicPrinter does not support faxing.")


#### Problem:
# - The `BasicPrinter` client is forced to implement methods it does not support, violating ISP. This makes the design rigid and error-prone.



# ### **Adhering to ISP**
# We refactor by splitting the large `Printer` interface into smaller, more specific interfaces.


from abc import ABC, abstractmethod

# Smaller, specific interfaces
class Print(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scan(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass

# Clients
class BasicPrinter(Print):
    def print_document(self, document):
        print(f"Printing: {document}")

class AdvancedPrinter(Print, Scan, Fax):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")

    def fax_document(self, document):
        print(f"Faxing: {document}")


# ### **Benefits of the Refactored Code**
# 1. **Smaller Interfaces**:
#    - `Print`, `Scan`, and `Fax` are independent interfaces. Clients only implement the functionality they need.
   
# 2. **Flexible Design**:
#    - Basic devices like `BasicPrinter` implement only the `Print` interface, while advanced devices like `AdvancedPrinter` implement multiple interfaces (`Print`, `Scan`, `Fax`).

# 3. **Extensibility**:
#    - Adding new functionalities (e.g., `Copy`) does not require changes to existing classes.

# 4. **Compliance with ISP**:
#    - Clients are not forced to depend on methods they do not use.

# ---

### Example Usage

# Using BasicPrinter
basic_printer = BasicPrinter()
basic_printer.print_document("Basic Document")

# Using AdvancedPrinter
advanced_printer = AdvancedPrinter()
advanced_printer.print_document("Advanced Document")
advanced_printer.scan_document("Advanced Document")
advanced_printer.fax_document("Advanced Document")
# ```

# ---

# This approach ensures that each client class only depends on relevant interfaces, adhering to the **Interface Segregation Principle**.