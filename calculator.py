while True:
  num1 = float(input("enter a num: "))
  num2 = float(input("enter secound num: "))

  print("ENTER CHOICE(1-5)")
  print("1-addition")
  print("2-subtract")
  print("3-multiply")
  print("4-divide")
  print("5-quatioent")

  choice = input("chose between (1-5): ")
  if choice == "1":
      print("SOLUTION:",num1+num2)
  elif choice == "2":
      print("SOLUTION:",num1-num2)
  elif choice == "3":
      print("SOLUTION:",num1*num2)
  elif choice == "4":
      print("SOLUTION:",num1/num2)
  elif choice == "5":
      print("SOLUTION:",num1%num2)
  else:
      print("invalid option")
print()