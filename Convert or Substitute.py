print("Use C instead of S. Enter the type of sequence you have at hand.")
sugar = input("Enter R for RNA or D for DNA: ")
mode = input("Enter S for substitution or O for opposite: ")
sequence = input("Enter the sequence:\n")

result = ""

R = ["U","C","A","G"]
D = ["A","G","T","C"]

R2D = dict(zip(R, D))
D2R = dict(zip(D, R))

for letter in sequence:
  
  if sugar + mode == "RS":
    result += letter.replace("U","T")
    
  elif sugar + mode == "DS":
    result += letter.replace("T","U")
    
  elif sugar + mode == "RO":
    result += letter.replace(letter, R2D[letter])
    
  elif sugar + mode == "DO":
    result += letter.replace(letter, D2R[letter])
    
  else:
    print("Invalid!")
    break

print(result)
