"""
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

Desired output: 

cwen@iupui.edu 5

"""
lst = list()
name = raw_input("Enter file: ")
handle = open(name)

for line in handle:
	if line.startswith("From:") :
		line = line.rstrip()
		line = line.split()
		lst.append(line[1])

count = dict()
for word in lst:
	count[word] = count.get(word,0) + 1

bigcount = None
bigword = None
for word,count in count.items():
	if bigcount == None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount