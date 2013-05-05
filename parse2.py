import sys

filename = "nut_poi_new_12347.txt"
infile = open(filename, 'r')

number = 332
sample = 100.0
image_1 = []
image_2 = []
lines = 0 
n = 0
p = 0
line_0 = 2
while True:
  line = infile.readline().strip()
  #print line
  if len(line)==0:
    line2 = infile.readline().strip()
    if len(line2)==0:
      break

  # If there's something there
  if len(line)>0:
    # If it's an image
    if line[0] == "(":
      # Means there's two images
      if len(image_1)==sample:
        image_2.append(line)
      else:
        image_1.append(line)

    # If it's a label
    if line[0] == "N" or line[0] == "P" :
      # Initialize the sum image
      ex = []
      for j in range(0,36):
        ex.append(0)

      # Get the first image
      if line[0] == "N" and n<number:
      #if line[0] == "N": 
        print line[0]
        for i in range(0,len(image_1)):
          img1_form = image_1[i].strip('(').strip().strip(')').split(',')
          for m in range(0,36):
            ex[m] += int(img1_form[m])/sample
        for k in range(0,36):
          if (k+1)%6==0:
            sys.stdout.write(str(ex[k]) + "\n")
          else: 
            sys.stdout.write(str(ex[k]) + "   ")
        n+=1
      if line[0] == "P" and p<number:
      #if line[0] == "P": 
        print line[0]
        for i in range(0,len(image_1)):
          img1_form = image_1[i].strip('(').strip().strip(')').split(',')
          for m in range(0,36):
            ex[m] += int(img1_form[m])/sample
        for k in range(0,36):
          if (k+1)%6==0:
            sys.stdout.write(str(ex[k]) + "\n")
          else: 
            sys.stdout.write(str(ex[k]) + "   ")
        p+=1
      image_1 = []
      if len(image_1)==0 and len(image_2)>0:
        # Initialize the sum image
        line = infile.readline().strip()
        ex = []
        for j in range(0,36):
          ex.append(0)
        try: 
          if line[0] == "N" and n<number:
          #if line[0] == "N": 
            print line[0]
            for i in range(0,len(image_2)):
              img2_form = image_2[i].strip('(').strip().strip(')').split(',')
              for m in range(0,36):
                ex[m] += int(img2_form[m])/sample
            for k in range(0,36):
              if (k+1)%6==0:
                sys.stdout.write(str(ex[k]) + "\n")
              else: 
                sys.stdout.write(str(ex[k]) + "   ")
            n+=1
          if line[0] == "P" and p<number:
          #if line[0] == "P": 
            print line[0]
            for i in range(0,len(image_2)):
              img2_form = image_2[i].strip('(').strip().strip(')').split(',')
              for m in range(0,36):
                ex[m] += int(img2_form[m])/sample
            for k in range(0,36):
              if (k+1)%6==0:
                sys.stdout.write(str(ex[k]) + "\n")
              else: 
                sys.stdout.write(str(ex[k]) + "   ")
            p+=1
          image_2 = []
        except Exception:
          pass
  lines += 1
  #if n>=1000:
  #  break
print "number of nutritious plants = " + str(n)
print "number of poisonous plants = " + str(p)
