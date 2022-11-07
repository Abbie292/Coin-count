while True:
  print("Welcome to the coin counter!")
  menuChoice = int(input("Enter 1 to enter a bag weight or 2 to display bags checked: "))
  if menuChoice == 1:
    volName = input("Please enter the volunteer name ")
    coinType = input("What is your coin type? \n£2 \n£1 \n£0.5 \n£0.2 \n£0.1 \n£0.05 \n£0.02 \n£0.01 \nEnter value: ")
    accuracy = 1
    if coinType == ("£2"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 120:
        coinsNeeded = bagWeight - 120 
        extraCoins = coinsNeeded / 12
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1
      elif bagWeight < 120:
        coinsNeeded = 120 - bagWeight 
        extraCoins = coinsNeeded / 12
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1
      else:
        print("Correct bag weight")
        accuracy = accuracy + 1 

    elif coinType == ("£1"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 175:
        coinsNeeded = bagWeight - 175 
        extraCoins = coinsNeeded / 8.75
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1
      elif bagWeight < 175:
        coinsNeeded = 175 - bagWeight 
        extraCoins = coinsNeeded / 8.75
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1
      else:
        print("Correct bag weight")
        accuracy = accuracy + 1
    
    elif coinType == ("0.50"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 160:
        coinsNeeded = bagWeight - 160 
        extraCoins = coinsNeeded / 8
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1
        
      elif bagWeight < 160:
        coinsNeeded = 160 - bagWeight 
        extraCoins = coinsNeeded / 8
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1
        
      else:
        print("Correct bag weight")
        accuracy = accuracy + 1
        
    elif coinType == ("0.20"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 250:
        coinsNeeded = bagWeight - 250 
        extraCoins = coinsNeeded / 5
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1

      elif bagWeight < 250:
        coinsNeeded = 175 - bagWeight 
        extraCoins = coinsNeeded / 5
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1

      else:
        print("Correct bag weight")
        accuracy = accuracy + 1

    elif coinType == ("£0.10"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 325:
        coinsNeeded = bagWeight - 325 
        extraCoins = coinsNeeded / 6.5
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1

      elif bagWeight < 325:
        coinsNeeded = 325 - bagWeight 
        extraCoins = coinsNeeded / 6.5
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1
        
      else:
        print("Correct bag weight")
        accuracy = accuracy + 1

    elif coinType == ("£0.05"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 235:
        coinsNeeded = bagWeight - 235 
        extraCoins = coinsNeeded / 2.35
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1
        
      elif bagWeight < 235:
        coinsNeeded = 235 - bagWeight 
        extraCoins = coinsNeeded / 2.35
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1
        
      else:
        print("Correct bag weight")
        accuracy = accuracy + 1
        
    elif coinType == ("£0.02"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 356:
        coinsNeeded = bagWeight - 356 
        extraCoins = coinsNeeded / 7.12
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1
        
      elif bagWeight < 356:
        coinsNeeded = 356 - bagWeight 
        extraCoins = coinsNeeded / 7.12
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1
        
      else:
        print("Correct bag weight")
        accuracy = accuracy + 1

    elif coinType == ("£0.01"):
      bagWeight = float(input("Enter total bag weight: "))
      if bagWeight > 356:
        coinsNeeded = bagWeight - 356 
        extraCoins = coinsNeeded / 3.56
        print("You have " + str(extraCoins) + " more coins than needed!")
        accuracy = accuracy - 1
        
      elif bagWeight < 356:
        coinsNeeded = 356 - bagWeight 
        extraCoins = coinsNeeded / 3.56
        print("You have " + str(extraCoins) + " less coins than needed!")
        accuracy = accuracy - 1
        
      else:
        print("Correct bag weight")
        accuracy = accuracy + 1
          
    else:
      print("Invalid coin type. Please enter again")
    CoinCountFile = open("coincount.txt","a")
    CoinCountFile.write(volName)
    CoinCountFile.write(",")
    CoinCountFile.write(str(coinType))
    CoinCountFile.write(",")
    CoinCountFile.write(str(bagWeight))
    CoinCountFile.write(",")
    CoinCountFile.write(str(accuracy))
    CoinCountFile.write("\n")
    CoinCountFile.close()
  else:
    myFile=open("coincount.txt","r")
    records=myFile.read()
    print(records)
    myFile.close()


 
 
 
