name,char=input("enter comma separated name and character:").split(",")
print(f"length of your name is{len(name)}")
print(f"character count:{name.count(char)}")#case-sensitive
print(f"character count:{name.lower().count(char.lower())}")#case-insensitive
print(f"character count:{name.strip().lower().count(char.strip().lower())}")#case-insensitive without spaces