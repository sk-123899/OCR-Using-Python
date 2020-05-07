"""def check1():
    fh = open(r"C:\shreyas\ocr project\lc.txt","r")
    name=input("Enter name of student")
    temp=False
    read=fh.readlines()
    
    for i in read:
        l= i.split()
        y = len(l)
        for x in range(y):
            word = l[x].lower()
            if word == name.lower():
                temp = True
        

    if temp:
        print("true")
    else:
        print("false")
   """



	

def name_check():
   fh = open(r"lc.txt","r")
   word = input("Enter word to search")
   a = word.lower()
   s=" "
   count=1
   while(s):
      s = fh.readline()
      lower=s.lower()
      if a  in lower:
          print("NAME FOUND")
          print('Line Number:',count)
      count+=1
      elif a not in fh:
         print("NOT")




   
