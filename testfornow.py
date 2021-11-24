from calculator import calculator
from appopener import openapp 
name = input("Hello! What is your name? ")
age = int(input("How old are you? "))
yesorno = input("Hello, " +str(age)+ " year old " +name+ "! You have successfully logged in.")
whatyouliketodo = input("What would you like to do? ")
if whatyouliketodo == "calculator":
  calculator()

if whatyouliketodo == "open an app":
	openapp()