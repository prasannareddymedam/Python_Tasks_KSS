#  Write a program to find the student with the highest marks from a dictionary.

d = {"Usha":80,"Madhu":90,"Ram":75}
print(max(d,key=d.get),max(d.values()))
