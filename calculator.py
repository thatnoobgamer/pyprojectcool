def calculator():
  caloperator = input("What math operator are you going to use? ") 
  if caloperator == "addition":
    a = int(input("First number "))
    b = int(input("Second number "))
    c = a + b
    print("The sum is "+str(c))
    calculator()
  
  if caloperator == "subtraction":
    d = int(input("First number "))
    e = int(input("Second number "))
    f = d - e
    print("The difference is " +str(f))
    calculator()

  if caloperator == "multiplication":
    g = int(input("First number "))
    h = int(input("Second number "))
    i = g * h
    print("The product is "+str(i))
    calculator()

  if caloperator == "division":
    j = int(input("First number "))
    k = int(input("Second number "))
    l = j / k
    print("The quotient is "+str(l))
    calculator()
  
  else:
    print("Please do addition, subtraction, multiplication, or division.")
    calculator()

