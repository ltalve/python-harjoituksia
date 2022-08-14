class Calculator:
  def __init__(self):
    self.file_name = "history.txt"

  def help(self):
    print("Commands: ")
    print("0 - end program")
    print("1 - calculate addition (+)")
    print("2 - calculate subtraction (-)")
    print("3 - calculate multiplication (*)")
    print("4 - calculate division (/)")
    print("5 - show history")
    print("6 - empty history")
    print("7 - show commands")
    
  def execute(self):
    print("Calculator")
    print(f"{self.length_of_history()} calculations stored in history")
    self.help()
    while True:
      command = input("Select command: ")
      if command == "0":
        print("Shutting down program...")
        break
      elif command == "1":
        self.addition()
      elif command == "2":
        self.subtraction()
      elif command == "3":
        self.multiplication()
      elif command == "4":
        self.division()
      elif command == "5":
        self.show_history()
      elif command == "6":
        self.empty_history()
      elif command == "7":
        self.help()
      else:
        self.help()

  def ask_for_inputs(self):
    first_number = float(input("Input number: "))
    second_number = float(input("Input number: "))
    return (first_number, second_number)

  def addition(self):
    print("Addition (+)")
    numbers = self.ask_for_inputs()
    operator = "+"
    result = numbers[0] + numbers[1]
    self.write_to_history(numbers[0], numbers[1], operator, result)
    print(f"Result: {result}")
  
  def subtraction(self):
    print("Subtraction (-)")
    numbers = self.ask_for_inputs()
    operator = "-"
    result = numbers[0] - numbers[1]
    self.write_to_history(numbers[0], numbers[1], operator, result)
    print(f"Result: {result}")
  
  def multiplication(self):
    print("Multiplication (*)")
    numbers = self.ask_for_inputs()
    operator = "*"
    result = numbers[0] * numbers[1]
    self.write_to_history(numbers[0], numbers[1], operator, result)
    print(f"Result: {result}")

  def division(self):
    print("Division (/)")
    numbers = self.ask_for_inputs()
    if numbers[1] == 0:
      print("Division by 0 is not possible")
      return
    operator = "/"
    result = numbers[0] / numbers[1]
    self.write_to_history(numbers[0], numbers[1], operator, result)
    print(f"Result: {result}")

  def show_history(self):
    try:
      with open(self.file_name) as history_file:
        print(f"{self.length_of_history()} calculations in history:")
        for line in history_file:
          line = line.replace("\n", "")
          line = line.split(";")
          print(f" {line[0]} {line[1]} {line[2]} = {line[3]}")
    except:
      print("No history available.")

  def empty_history(self):
    with open(self.file_name, "w") as history_file:
      print("History cleared.")
      pass

  def write_to_history(self, operand1: float, operand2: float, operator: str, result: float):
    calculation = f"{operand1};{operator};{operand2};{result}\n"
    with open(self.file_name, "a") as history_file:
      history_file.write(calculation)

  def length_of_history(self):
    try:
      with open(self.file_name) as history_file:
        no_of_calculations = 0
        for line in history_file:
          no_of_calculations += 1
      return no_of_calculations
    except:
      return 0


application = Calculator()
application.execute()
