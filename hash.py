from os import system
while True:
  print("\nCreated By : DarkSmile")
  print("\n1)Lock\n2)UnLock\n3)Exit")
  n = str(input("Choose number > "))
  
  if (n) == ("1"):
    t1 = str(input("your text : "))
    print("your text is:")
    system('echo '+t1+" | base64")
    
  elif (n) == ("2"):
    t2 = str(input("your text : "))
    print("your text is:")
    system('echo '+t2+" | base64 -d")
    
  elif (n) == ("3"):
    break
  else:
    break
