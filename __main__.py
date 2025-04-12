import sys
import math


#interprete the user input smt like this

line = input(f"\nEnter your numbers and operators >> ")
line = line.strip() 
parts = line.split(" ")

program = []

for part in parts:

  if line.lower() == "exit":
      break
  if line == "":
      continue
  
  try:
    if part.isdigit():      
      program.append(int(part))
    elif part in ["+", "-", "*", "/"]:
      program.append(part)
  except:
    print("Error: well well well. what did you enter? check your input")
    continue


#you can delete this line, it is for testing only
print("  >> the numbers you entered: ", program, "\n")


#the calculator class
#takes the interpreted input and calculates the result depending on operators and other shi

class Calculator:
  def __init__(self, program):
    self.program = program
    self.pc = 0
    self.result = 0

  def calculate(self):
    try:
      while self.pc < len(self.program):
        opcode = program[self.pc]
        
        if isinstance(opcode, int):
          self.result = program[self.pc]
          self.pc += 1
        elif opcode in ["+", "-", "*", "/"]:
          if opcode == "+":  #this is the addition
            a = self.result
            b = program[self.pc+1]
            self.result = a + b
            print(f">>> {a} + {b} = {self.result}")
          elif opcode == "-":  #this is the subtraction
            a = self.result
            b = program[self.pc+1]
            self.result = a - b
            print(f">>> {a} - {b} = {self.result}")
          elif opcode == "*":  #this is the multiplication
            a = self.result
            b = program[self.pc+1]
            self.result = a * b
            print(f">>> {a} * {b} = {self.result}")
          elif opcode == "/":  #this is the division
            a = self.result
            b = program[self.pc+1]
            if b <= 0:
              print("Error: you can't divide by 0 lol")
              break
            self.result = a / b
            print(f">>> {a} / {b} = {self.result}")
          self.pc += 2     #move to the next opcode, making the result the first operand for the next operation
    except:
      print("Error: hell nah smt went wrong, check input")
      return

calculator = Calculator(program)  #starting and running the calculator
calculator.calculate()

