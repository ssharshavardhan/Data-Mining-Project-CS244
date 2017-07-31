import os
from datetime import datetime

def ngrams(input, n):
  output = {}
  input = input.split(' ')
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

def print1(lis,dic,name,num):
  var = str(num)+"-grams/"+ name+"-final.txt"
  bar = open('/Users/harshavardhan/Downloads/ADFA-LD/'+var, 'w')
  r = ": 0"
  bar.write(name + "\n")
  for i in range(len(lis)):
    k = lis[i]
    if k in dic:
      bar.write(str(k)+" : "+str(dic[k]) + "\n")
    else:
      bar.write(str(k) + " : 0\n")
  bar.close()

def magic(numb):
  top3 = []

  with open('/Users/harshavardhan/Downloads/ADFA-LD/input/A-concat.txt',"r") as xyz:
    abc = xyz.read()
  
    A3=(ngrams(abc,numb))
    sortedlist=sorted(A3.items(), key=lambda x:x[1], reverse=True)
    for i in range(int(0.3*len(sortedlist))):
      top3.append(sortedlist[i][0])
  xyz.close()

  with open('/Users/harshavardhan/Downloads/ADFA-LD/input/F-concat.txt',"r") as xyz:
    abc = xyz.read()
  
    F3=(ngrams(abc,numb))
    sortedlist=sorted(F3.items(), key=lambda x:x[1], reverse=True)
    for i in range(int(0.3*len(sortedlist))):
      top3.append(sortedlist[i][0])
  xyz.close()

  with open('/Users/harshavardhan/Downloads/ADFA-LD/input/J-concat.txt',"r") as xyz:
    abc = xyz.read()
  
    J3=(ngrams(abc,numb))
    sortedlist=sorted(J3.items(), key=lambda x:x[1], reverse=True)
    for i in range(int(0.3*len(sortedlist))):
      top3.append(sortedlist[i][0])
  xyz.close()

  with open('/Users/harshavardhan/Downloads/ADFA-LD/input/M-concat.txt',"r") as xyz:
    abc = xyz.read()
  
    M3=(ngrams(abc,numb))
    sortedlist=sorted(M3.items(), key=lambda x:x[1], reverse=True)
    for i in range(int(0.3*len(sortedlist))):
      top3.append(sortedlist[i][0])
  xyz.close()

  with open('/Users/harshavardhan/Downloads/ADFA-LD/input/S-concat.txt',"r") as xyz:
    abc = xyz.read()
  
    S3=(ngrams(abc,numb))
    sortedlist=sorted(S3.items(), key=lambda x:x[1], reverse=True)
    for i in range(int(0.3*len(sortedlist))):
      top3.append(sortedlist[i][0])
  xyz.close()

  with open('/Users/harshavardhan/Downloads/ADFA-LD/input/T-concat.txt',"r") as xyz:
    abc = xyz.read()
  
    T3=(ngrams(abc,numb))
    sortedlist=sorted(T3.items(), key=lambda x:x[1], reverse=True)
    for i in range(int(0.3*len(sortedlist))):
      top3.append(sortedlist[i][0])
  xyz.close()

  with open('/Users/harshavardhan/Downloads/ADFA-LD/input/W-concat.txt',"r") as xyz:
    abc = xyz.read()
  
    W3=(ngrams(abc,numb))
    sortedlist=sorted(W3.items(), key=lambda x:x[1], reverse=True)
    for i in range(int(0.3*len(sortedlist))):
      top3.append(sortedlist[i][0])

  top = list(set(top3))
  xyz.close()

  print1(top,A3,"Adduser",numb)
  print1(top,F3,"Hydra-FTP",numb)
  print1(top,J3,"Java",numb)
  print1(top,M3,"Meterpreter",numb)
  print1(top,S3,"Hydra-SSH",numb)
  print1(top,T3,"Train",numb)
  print1(top,W3,"Web",numb)

startTime = datetime.now()

magic(3)
magic(5)
magic(7)

print datetime.now() - startTime






