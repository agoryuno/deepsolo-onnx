import pickle


chars = [' ','!','"','#','$','%','&','\'','(',')','*',
         '+',',','-','.','/', '0','1','2','3','4','5',
         '6','7','8','9',':',';','<','=','>','?','@',
         '[','\\',']','^','_','`','{','|','}','~',]

with open("hebrew-chars.txt", "r") as f:
    hebc = f.read()
    hebc = list(hebc)
    chars += hebc

print (f"Dictionary size is: {len(chars)}")

with open("hebrew-dict.cp", "wb") as f:
    pickle.dump(chars, f)