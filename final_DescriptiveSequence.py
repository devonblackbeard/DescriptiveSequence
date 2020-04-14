# Create a global variable to track number of times function called
numberTimesCalled = 0
iterations = input("How many iterations N(x):  ")

def getDescriptiveSequence(number):
  # increment numberTimesCalled
  global numberTimesCalled
  global iterations

  numberTimesCalled += 1
  
  # begin our count
  count = 1
  myList = []
  lengthInput = len(number)

  if(lengthInput >=2):
      # loop through each number in the input string
      for i in range(1,lengthInput):
        # If there are consecutive numbers
        if(number[i] == number[i-1]):
          count +=1
          # Ensure not last index and number isnt start of a consecutive run
          if(i != lengthInput-1  and (number[i] != number[i+1])):
            myList.append(str(count) + str(number[i]))
          # if is at the last index
          elif (i== lengthInput-1):
            myList.append(str(count) + number[-1])

        # Start of a new run
        else:
          count = 1
          # left is the number to the left of the current index number
          left = number[i-1]
          num1 = 1
          # If first iteration
          if (i != lengthInput-1) and i == 1:
            myList.append(str(num1) + str(left))

          # Ensure not end of string and not end of a consecutive run
          # Second check is because if it is the end of a consec. run, 
          # it would have already been accounted for above
          elif (i != lengthInput-1) and (left != number[i-2]): 
            myList.append(str(num1)+ str(left))
           
          # Now at last index 
          elif (i == lengthInput-1):
            # At last index of list
            # Check that number to left and to the left of that dont match
            # Means we have a unique number that only occurs once
            if(number[i-1]!= number[i-2] ):
              myList.append(str(count) + number[i-1])
          
            # Otherwise, print the last digit
            myList.append(str(count) + number[-1])

  else:    
    if lengthInput == 1:     
      myList.append(str(1) + str(number))  

  
  # if finished iterations, return list
  if numberTimesCalled == int(iterations):
    # Display results after all iterations
    newString = ""
    for i in myList:
      newString += i
    print(newString)
       
  # otherwise, convert our list to a string so we
  # can re-input it (recursion) into the function

  # If not finished recursions, keep going until iteration number is hit
  else:
    newInput = ""
    for i in myList:
      newInput += i 
    getDescriptiveSequence(newInput)

#  END FUNCTION CALL


userInput = input("Enter descriptive sequence: ")
# Call the function the first time
getDescriptiveSequence(userInput)

