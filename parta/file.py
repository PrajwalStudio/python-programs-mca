src=open("source.txt","r")
dest=open("destination.txt","w")

for line in src:
    dest.write(line)
src.close()
dest.close()
print("File copied Successfully")