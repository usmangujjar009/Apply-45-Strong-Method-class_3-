#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Concatination Method with **+**:

first_name = "Muhammad"
last_name = "Usman"
ins_name = "Saylani Mass IT Training Program"
course_name = "A.I Batch-4"
roll_num = 119542
print("Institute Name: "+ins_name,  "\nStudent Full Name: "+first_name +' '+ last_name, "\nCourse Name: "+course_name, "\nRoll number: "+str(roll_num))


# In[2]:


# Concatination Method with **.format method**:

first_name = "Muhammad"
last_name = "Usman"
ins_name = "Saylani Mass IT Training Program"
course_name = "A.I Batch-4"
roll_num = 119542

card = '''Institude Name: {}
Student Full Name: {} {}
course Name: {}
Roll Number: {}'''.format(ins_name,first_name,last_name,course_name,roll_num)

print(card)


# In[16]:


# 1-capitalize Method
# The method returns a new string with the first character capitalized.

name = "pakistan zindabad"
print(name.capitalize())


# In[17]:


# 2-CaseFold Method
# The method returns a new string with all the alphabetic characters converted to lowercase.

name = "PAKISTAN ZINDABAD"
print(name.casefold())


# In[18]:


# 3-Center Method
# method returns a new string with the original string centered within the specified width

name = "Pakistan zindabad"
print(name.center(100))


# In[19]:


# 4-Count Method
# returns the number of occurrences of the specified substring or character.

name = "Pakistan zindabad"
print(name.count('a'))


# In[20]:


# 5-encode method
# returns an encoded version of the original string.

name = "My name is Ståle"
print(name.encode())


# In[21]:


# 5-endswith method
# returns a boolean value indicating whether the string ends with a specified suffix or not.

name = "Pakistan zindabad"
print(name.endswith('n'))
print(name.endswith('d'))


# In[22]:


# 6-expandtabs
# returns a copy of the string with all tab characters (\t) replaced by one or more spaces.

name = "Pakistan\tzindabad"
print(name.expandtabs(6))


# In[23]:


# 7-Find method
# returns the lowest index in the string where a specified substring is found.

name = "Pakistan zindabad"
print(name.find("t"))      # Returns value of t at specified index
print(name.find("zin"))    # Returns value of "z" only at specified index
print(name.find("x"))      # Returns No value with "-1" as "x" is not found in above string


# In[24]:


# 8-format Method
# Already descibe above


# In[25]:


# 9-index Method
# Index method is used to find the index of the first occurrence of a specified substring in a string.
# It also returns value error "substrings is not found"

name = "Pakistan zindabad"
print(name.index('t'))
# print(name.index('x'))


# In[26]:


# 10-isalnum Method
# used to check whether a string contains only alphanumeric characters or not.

name1 = "Pakistan123"
name2 = "Pakistan!!123"
print(name1.isalnum())
print(name2.isalnum())       # It returns false due to non-alphanumeric charachter "!"


# In[27]:


# 11-isalpha Method
# used to check whether a string contains only alphabetic characters or not.

name1 = "Pakistan"
name2 = "Pakistan123"
print(name1.isalpha())
print(name2.isalpha()) 


# In[28]:


# 12-isascii Method
# used to check whether a string contains only ASCII characters or not.

name1 = "Pakistan"
name2 = "¡Hello¡"
print(name1.isascii())
print(name2.isascii())


# In[29]:


# 13-isdecimal Method
# used to check whether a string contains only decimal characters or not

num1 = "1234"
num2 = "12.345"
print(num1.isdecimal())
print(num2.isdecimal())


# In[30]:


# 14-isdigit Method
# used to check whether a string contains only digits or not.

num1 = "1234"
num2 = "12.345"
print(num1.isdigit())
print(num2.isdigit())


# In[31]:


# 15-isidentifier
# used to check whether a string is a valid identifier or not.
# An identifier is a sequence of characters in Python that represents a name, such as variable names, function names, class names, etc. 
# An identifier must follow certain rules, such as starting with a letter or underscore, and only containing letters, numbers, and underscores.

name1 = "my_var"
name2 = "1myvar"
print(name1.isidentifier())
print(name2.isidentifier())


# In[5]:


# 16-islower Method
# used to check whether all the characters in a string are lowercase or not.

name1 = "Usman"
name2 = "Usman"
print(name1.islower())
print(name2.islower())


# In[33]:


# 17-isnumeric
# used to check whether all the characters in a string are numeric characters or not.

num1 = "1234"
num2 = "12.345"

print(num1.isnumeric())
print(num2.isnumeric())


# In[34]:


# 18-isprintable Method
# used to check whether all the characters in a string are printable or not.

n = "Hellow World"
m = "Hellow \n World"
print(n.isprintable())
print(m.isprintable())


# In[35]:


# 19-isspace Method
# used to check whether all the characters in a string are whitespace characters or not.

n = "Hellow World"
m = "\t\n"
p = ""

print(n.isspace())
print(m.isspace())
print(p.isspace())


# In[36]:


# 20-istitle Method
# used to check whether a string is a titlecased string or not.
# A titlecased string is a string where the first letter of each word is capitalized and all other letters are lowercase.

n = "The Pakistan"
m = "the pakistan"

print(n.istitle())
print(m.istitle())


# In[37]:


# 21-isupper Method
# used to check whether all the alphabetic characters in a string are uppercase or not.

n = "hellow world"
m = "HELLOW WORLD"

print(n.isupper())
print(m.isupper())


# In[38]:


# 22-join Method
# used to join a sequence of strings together into a single string, using a specified separator string.

separator = ","
name = "Pakistan"

print(separator.join(name))


# In[39]:


# 23-ljust Method
# used to left justify a string within a specified width by padding it with a specified character on the right.

name = "Hello"
print(name.ljust(10,'!'))


# In[4]:


# 24-lower Method
# used to convert all the alphabetic characters in a string to lowercase.

name = "Muhammad Usman"
print(name.lower())


# In[3]:


# 25-lstrip Method
# used to remove leading whitespace characters from a string.

name = "    Usman   !!"
print(name.lstrip())


# In[42]:


# 26-maketrans Method
# used to create a translation table that can be used by the translate() method to replace specified characters in a string.

name = "Hello World"
n = name.maketrans('el','ip','o')
m = name.translate(n)
print(m)
      


# In[43]:


# 27-partition Method
# used to split a string into three parts based on a specified separator.

name = "Welcome, Muhammad"
print(name.partition(','))


# In[44]:


# 28-removeprefix Method
# used to remove a specified prefix from a string(If start with specified string).

name = "Hello World"
print(name.removeprefix('Hello'))


# In[45]:


# 29-removesuffix Method
# used to remove a specified suffix from a string. 
# If the string ends with the specified suffix, the suffix is removed and the modified string is returned.

name = "Hello World"
print(name.removesuffix("World"))


# In[46]:


# 30-replace Method
# used to replace all occurrences of a specified substring in a string with another substring.

name = "Hello World"
print(name.replace("World","Universe"))


# In[47]:


# 31-rfind Method
# returns the highest index in the string where a specified substring is found. 
# The method searches the string from right to left, starting from the specified position, and returns -1 if the substring is not found.

name = "Hello World"
print(name.rfind("o"))
print(name.rfind("e"))
print(name.rfind("z"))


# In[6]:


# 32-rindex Method
# similar to the rfind() method, but instead of returning -1 when the substring is not found, it raises a ValueError exception.

name = "Hello World"
print(name.rindex("o"))
print(name.rindex("e"))
print(name.rindex("z"))


# In[49]:


# 33-rjust Method
# returns a right-justified version of a given string by padding it with a specified character (or space) on the left side. 
# This method returns a new string and does not modify the original string.

name = "Hello"
print(name.rjust(10))
print(name.rjust(10,'-'))


# In[50]:


# 34-rpartition Method
# separates the given string into three parts using a separator (also called a delimiter) specified as an argument. 
# The separation occurs from the right side of the string.

n = "apple,banana,mango"
print(n.rpartition(","))


# In[51]:


# 35-rsplit Method
# splits a given string into a list of substrings, starting from the right side of the string, using a specified separator (also called a delimiter). 
# If no separator is specified, the method splits the string at whitespace characters (spaces, tabs, and newlines)

name = "Hello World"
print(name.rsplit())


# In[52]:


# 36-rstrip Method
# returns a new string with trailing whitespace characters (spaces, tabs, and newlines) removed from the right side of the original string.

name = "Hello World!!"
print(name.rstrip('!'))


# In[53]:


# 37-split Method
# splits a given string into a list of substrings, using a specified separator (also called a delimiter). If no separator is specified, the method splits the string at whitespace characters (spaces, tabs, and newlines).

name = "   Hello World  "
print(name.split())


# In[54]:


# 38-splitlines Method
# splits a given string into a list of substrings, using the newline character(s) (\n, \r, and \r\n) as the delimiter.

name = "Hello\nWorld\nGoodnight"
print(name.splitlines())


# In[7]:


# 39-startswith Method
# returns a boolean value indicating whether a given string starts with a specified prefix.

name = "Muhammad Usman"
print(name.startswith('Muhammad'))
print(name.startswith('Usman'))


# In[8]:


# 40-strip Method
# returns a new string with any leading or trailing whitespace removed.

name = "   \t\nMuhammad Usman!  "
print(name.strip())


# In[9]:


# 41-swapcase Method
# returns a new string where all the uppercase characters are converted to lowercase and vice versa

name = "Muhammad Usman"
print(name.swapcase())

n = "HELLO WORLD"
print(n.swapcase())


# In[10]:


# 42-title Method
# returns a new string with the first character of each word in uppercase and the rest of the characters in lowercase.

name = "Muhammad Usman"
print(name.title())


# In[59]:


# 43-translate Method
# returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

name = "Hello World"
n = name.maketrans('el','ip','o')
m = name.translate(n)
print(m)


# In[11]:


# 44-upper Method
# returns a new string with all the characters converted to uppercase.

name = "Muhammad Usman"
print(name.upper())


# In[12]:


# 45-zfill Method
# returns a new string with zeros (0) added to the left side of a string until it reaches a specified length.

name = "Usman"
print(name.zfill(10))  # It added 3 zeros to left to complete the total length of 10 charachters


# In[ ]:




