filename = ARGV[0] #file name is passed as an arguement
count = 0 #initalize 'count' variable
file = open(filename) #open a specified file
while text = file.gets #loop reading next line to 'text'
	count += 1 
end
file.close # close the file
puts count #print the content of 'count'

