string="she is beautiful and she is good dancer"
# replace() method
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))
print(string.replace("is","was",3))
# find() method
print(string.find("is"))
is_pos1=string.find("is")
is_pos2 = string.find("is",is_pos1+1)
print(is_pos2)