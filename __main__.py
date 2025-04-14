import sys
import math


#interprete the user input smt like this

line = input(f"\nEnter your numbers and operators >> ")
line = line.strip() 
parts = line.split(" ")

program = []

for part in parts:

  if line == "":
      continue
  
  try:
    if part.isdigit():      
      program.append(int(part))
    elif part in ["+", "-", "*", "/"]:
      program.append(part)
  except:
    raise Exception("Error: well well well. what did you enter? check your input")


#you can delete this line, it is for testing only
print("  >> the numbers you entered: ", program, "\n")

#the calculator class
#takes the interpreted input and calculates the result depending on operators and other shi

class Calculator:
  def __init__(self, program):
    self.pc = 0
    self.result = None

  def calculate(self):
    try:
      self.pc = 0
      while self.pc < len(program):
          
          self.result = None
          opcode = program[self.pc]
          print(f"{self.result}, {self.pc}, {program}")

          if opcode == "*":
            self.result = program[self.pc-1]
            a = self.result
            b = program[self.pc+1]
            self.result = a * b
            print(f">>> {a} * {b} = {self.result}")
            program[self.pc-1] = self.result
            program.pop(self.pc)
            program.pop(self.pc)
            self.pc -= 1
          elif opcode == "/":
            self.result = program[self.pc-1]
            a = self.result
            b = program[self.pc+1]
            self.result = a / b
            print(f">>> {a} / {b} = {self.result}")
            program[self.pc-1] = self.result
            program.pop(self.pc)
            program.pop(self.pc)
            self.pc -= 1

          self.pc += 1
          
    except:
      raise Exception("Error 1: something went wrong, check your input")


    try:
      self.pc = 0
      while self.pc < len(program):
        self.result = None
        opcode = program[self.pc]
        print(f"{self.result}, {self.pc}, {program}")


        if isinstance(opcode, int):
          self.pc += 1

        elif opcode in ["+", "-", "*", "/"]:
          if opcode == "+":  #this is the addition
            a = program[self.pc-1]
            b = program[self.pc+1]
            self.result = a + b
            print(f">>> {a} + {b} = {self.result}")
            program[self.pc-1] = self.result
            program.pop(self.pc)
            program.pop(self.pc)
            self.pc -= 1
            
          if opcode == "-":  #this is the subtraction
            a = program[self.pc-1]
            b = program[self.pc+1]
            self.result = a - b
            print(f">>> {a} - {b} = {self.result}")
            program[self.pc-1] = self.result
            program.pop(self.pc)
            program.pop(self.pc)
            self.pc -= 1

        self.pc += 1     #move to the next opcode, making the result the first operand for the next operation

    except:
      raise Exception("Error 2: something went wrong, check your input")

calculator = Calculator(program)  #starting and running the calculator
calculator.calculate()