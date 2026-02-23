import re

txt = "The rain in Spain"

x = re.findall("[a-m]" , txt)
print(x)

txt2 = "That will be cost 29 dollar"
d = re.findall("\\d" , txt2)
print(d) #output ['2' , '9']



txt3 = "Hello world , i know that press is karma perfume regret u just want attention"
thr = re.findall("w.r.." , txt3)
y = re.findall("^attention" , txt3)
z = re.findall("want$" , txt3)
print(thr )


txt = "The rain in Spain falls mainly in the plain! , stays"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")





