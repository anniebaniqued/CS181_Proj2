import sys

filename = "nut_poi_1234.txt"
infile = open(filename, 'r')

image_1 = []
image_2 = []
lines = 0 
n = 0
p = 0
line_0= 2
while True:
  line = infile.readline().strip()
  if len(line)==0:
    line2 = infile.readline().strip()
    if len(line2)==0:
      break
  if len(line)>0:
    if line[0] == "(":
      if len(image_1)==5:
        image_2.append(line)
      else:
        image_1.append(line)
    if line[0] == "N" or line[0] == "P" :
      for i in range(0,len(image_1)):
        if line[0] == "N" and n<1000:
        #if line[0] == "N": 
          print line[0]
          n+=1
          img1_form = image_1[i].strip('(').strip().strip(')').split(',')
          for k in range(0,36):
            if (k+1)%6==0:
              sys.stdout.write(str(int(img1_form[k])) + "\n")
            else: 
              sys.stdout.write(str(int(img1_form[k])) + "   ")
        if line[0] == "P" and p<3333:
        #if line[0] == "P": 
          print line[0]
          p+=1
          img1_form = image_1[i].strip('(').strip().strip(')').split(',')
          for k in range(0,36):
            if (k+1)%6==0:
              sys.stdout.write(str(int(img1_form[k])) + "\n")
            else: 
              sys.stdout.write(str(int(img1_form[k])) + "   ")
      image_1 = []
      if len(image_1)==0 and len(image_2)>0:
        for i in range(0,len(image_2)):
          if line[0] == "N" and n<1000:
          #if line[0] == "N": 
            print line[0]
            n+=1
            img2_form = image_2[i].strip('(').strip().strip(')').split(',')
            for k in range(0,36):
              if (k+1)%6==0:
                sys.stdout.write(str(int(img2_form[k])) + "\n")
              else: 
                sys.stdout.write(str(int(img2_form[k])) + "   ")
          if line[0] == "P" and p<3333:
          #if line[0] == "P": 
            print line[0]
            p+=1
            img2_form = image_2[i].strip('(').strip().strip(')').split(',')
            for k in range(0,36):
              if (k+1)%6==0:
                sys.stdout.write(str(int(img2_form[k])) + "\n")
              else: 
                sys.stdout.write(str(int(img2_form[k])) + "   ")
        image_2 = []
  lines += 1
  #if n>=1000:
  #  break
print "number of nutritious plants = " + str(n)
print "number of poisonous plants = " + str(p)
