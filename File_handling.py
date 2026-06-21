#open file in write mode to open there is an open function
file=open("File_handling.txt","w")
file.write("Hello, what is your name?\n")
file.write("My name is Craig\n")
file.close()
#write mode overrides morelines and edits what you previously wrote
#use the append mode is a 
file=open("File_handling.txt","a")
file.write("Good morning Craig\n")
file.write("Good morning to you to\n")
file.close()
#opening file in read mode
file=open("File_handling.txt","r")
conversation=file.read()
file.close()
print(conversation)