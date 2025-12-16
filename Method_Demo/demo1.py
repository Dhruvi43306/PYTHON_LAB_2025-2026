# s = "hello"

#SEARCH/FIND :-
#==============================================================================
#find():-
# This mehtod to find first occurence of index and  if above given string inside a letter or string are not exit inside my method return -1.
# print(s.find('i',0,12))

#rfind():-
# This mehtod to find first occurence of index from right and  if above given string inside a letter or string are not exit inside my method return -1.
# print(s.rfind('i',0,12))

# ------------------------------------------------------------------------
#index():-
#This method same as find method but if above given string inside a letter or string are not exit for index then throw valueError.
# print(s.index('0'))

# ------------------------------------------------------------------------
#rindex():-
#This method same as find method but if above given string inside a letter or string are not exit for index from right then throw valueError.
# print(s.rindex('0'))

# ------------------------------------------------------------------------
#count():-
#This Method return how many time are letter or string.
# print(s.count("o"))



#==============================================================================
#ALIGNMENT/FORMATING :-
# ------------------------------------------------------------------------
#ljust():-
#This Method are remaining chracter are fill the specifie space in right side like this Hello_____.
# print(s.ljust(10,"_"))


# ------------------------------------------------------------------------
#rjust():-
#This Method are remaining chracter are fill the specifie space in left side like this _____Hello.
# print(s.rjust(10,"_"))


# ------------------------------------------------------------------------
#center():-
#This Method are remaining chracter are arrange in center like this ___Hello____.
# print(s.center(12,"_"))



# ------------------------------------------------------------------------
#Zfill():-
#This Method are remaing char are fill the zero in always left side.
# print(s.zfill(10))







#==============================================================================
#REMOVE SPACES / CHARCATERS :-
# ------------------------------------------------------------------------
#lstrip():-
#lstrip() only removes characters until the first unmatched character appears.
#if you can not write _ then you consider by defult space.(Sequence dosnt metter)
#s = "@%_|Hello"
# print(s.lstrip("_@%"))


# ------------------------------------------------------------------------
#Rstrip():-
#Rstrip() only removes characters until the first unmatched character appears.(Sequence dosnt metter)
#s = "Hello|@%_"
# print(s.rstrip("_%@|"))


# ------------------------------------------------------------------------
#strip():-
# strip() only removes characters both side until the first unmatched character appears.
#s = "@%_|Hello|@%_"
# print(s.strip("@%_|"))




#==============================================================================
#REPLACE/MODIFIE:-
# ------------------------------------------------------------------------
#replace():-
#replace() returns a new string with specified text replaced.if i write step count = 1 then replase only 1 time but bydefult replase all
# s = 'h-e-l-l-o'
# print(s.replace("-","+",1))


# ------------------------------------------------------------------------
#translate():-
# Step-by-Step Explanation

# str.maketrans("abc", "123")
# Creates a mapping:
# 'a' → '1', 'b' → '2', 'c' → '3'
# s.translate(table)
# Replaces characters in the string according to the mapping

# table = str.maketrans("abc", "123")
# s = "abcde"
# print(s.translate(table))   #"123de"


#MCQ PRECTICE:
#EXPLNATION:
# str.maketrans(x, y, z) creates a translation table for translate()
# Parameters:
# x → string of characters to replace
# y → string of characters to replace with
# z → string of characters to delete/remove
# table = str.maketrans("", "", "aeiou")  # remove vowels
# s = "hello world"
# print(s.translate(table)) #hll wrld





#==============================================================================
#SPILT & JOIN :-
# ------------------------------------------------------------------------
#join():-
#li.join(" ")   # AttributeError
#join() belongs to STRING because the string decides the separator.
#' ' is a string → strings have join() 
#li is a list → lists do NOT have join()

# Methods belong to the object that controls the behavior
# Separator controls joining → string and A string made to formate text,change txt,join text
# List only holds values → list and A list is made it store items,add/remove,loop items 


# JavaScript and Python are designed differently
# JavaScript allows array.join()
# Python allows "separator".join(list)
# Both are correct, just different design philosophies.

# JS Way
# “People connect themselves”
# Python Way
# “The connector connects people”

#if i merge the string then i will use it join method!
# li = ["hi","hello","how","are","you"]
# print(' '.join(li))



# ------------------------------------------------------------------------
#split():-
#split() always returns a list, even if split once.
# s = "a/b/c/d"
# l = s.split("/",1)  # split only ONCE from left → ['a', 'b/c/d']
# print(l)
# print(type(l))   # result is always a list


# ------------------------------------------------------------------------
#rsplit():-
# s = "a/b/c/d"
#split() always returns a list, even if split once in right side.
# l = s.rsplit("/",1)  # split only ONCE from left → ['a/b/c', 'd']
# print(l) 
# print(type(l))  # result is always a list


# ------------------------------------------------------------------------
#s.partition(",")       
# split into 3 parts
# Left part → full string
# Separator → empty
# Right part → empty
# s = "hello hi world"
# print(s.partition(",")) #('hello hi world', '', '')



# ------------------------------------------------------------------------
# s.rpartition(",")       
# split from right into 3 parts
# Left part → empty
# Separator → empty
# Right part → full string
# s = "hello hi world"
# print(s.rpartition(",")) #('', '', 'hello hi world')



###if i want to divide the string then i will use split method.



#==============================================================================
#PREFIX/SUFFIX CHECK :-
# ------------------------------------------------------------------------
#startswith():-
#if metch my perfix for given string then return true otherwise false.
# s = "Hello World"
# print(s.startswith("H"))


# ------------------------------------------------------------------------
#endswith():-
#if metch my suffix for given string then return true otherwise false.
# s = "Hello World"
# print(s.endswith("d"))





#==============================================================================
#MISCELLANEOUS :-
# ------------------------------------------------------------------------
#removeprefix():-
#if i metch my perfix for given string inside preffix remove else if not matched string then return all string.
# s = "Hello World"
# print(s.removeprefix("Hi"))


# ------------------------------------------------------------------------
#removesuffix():-
#if i metch my suffix for given string inside suffix remove else if not matched string then return all string.
# s = "Hello World"
# print(s.removesuffix("Hi"))

# ------------------------------------------------------------------------
#s.splitlines()
s = "Hello\nWorld\nPython"
lines = s.splitlines()
print(lines)


#**s.maketrans(x, y)


#==============================================================================
#CASE CONVERSION :-
# ------------------------------------------------------------------------
#upper():-
# given string are convert to Upper case latter
# s = "hello"
# print(s.upper())


# ------------------------------------------------------------------------
#lower():-
# given string are convert to Lower case latter
# s = "hello"
# print(s.lower())


# ------------------------------------------------------------------------
#title():-
# given string are convert to  First Letter Of Each Word
# s = "hello" #Hello
# print(s.title())



# ------------------------------------------------------------------------
#casefold():-
# given string are convert to Lower case latter
# casefold() best for comparison
# s = "HEllo"
# print(s.casefold())

# ------------------------------------------------------------------------
#capitalize():-
#This Method are return above given string inside make a only first letter uppercase.
#print(s.capitalize())


#**swepcase:-




#Check / Validation (Return True or False)
# ------------------------------------------------------------------------
#isupper():-
# if my given string inside all letter are uppercase then return true otherwise false.
# s = "hello"
# print(s.isupper());



# ------------------------------------------------------------------------
#islower():-
# if my given string inside all letter are lowercase then return true otherwise false.
# s = "hello"
# print(s.islower());


# ------------------------------------------------------------------------
#istitle():-
# if my given string inside First Each letter are uppercase then return true otherwise false.
# s = "Hello World"
# print(s.istitle());


# ------------------------------------------------------------------------
#isalpha():-
# if my given string inside all letter are [A-Z a-z] then return true otherwise false.
# s = "123"
# print(s.isalpha());



# ------------------------------------------------------------------------
#isalnum():-
# if my given string inside all letter are [0 to n and A-Z or a-z] then return true otherwise false.
# s = "0123abc"
# print(s.isalnum());


# ------------------------------------------------------------------------
#isdigit():-
# if my given string inside all letter are only [0 to n] then return true otherwise false.
# s = "0123abc"
# print(s.isdigit());


# ------------------------------------------------------------------------
#isspace():-
# True if ALL characters are spaces/tabs/newlines, else False
# s = " "
# print(s.isspace());



# ------------------------------------------------------------------------
#isnumeric():-
# True if ALL characters are numeric (digits or unicode numbers), else Falses
# s = "0123"
# print(s.isnumeric());


# ------------------------------------------------------------------------
#isdecimal():-
# True if ALL characters are decimal (0-9 only), else False
# s = "1/2"
# print(s.isdecimal());


# ------------------------------------------------------------------------
#isascii():-
# True if ALL characters are ASCII (0-127), else False
# s = "0123"
# print(s.isascii());


# ------------------------------------------------------------------------
#isidentifires():-
# True if string is a valid Python identifier (can be variable/function name)
# s = "var_1"
# print(s.isidentifier());



# ------------------------------------------------------------------------
#s.isprintable()  
#Printable = letters, numbers, punctuation, space
#Non-printable characters = control characters like \n, \t, \r
# True if ALL characters are printable (no special control chars), else False
# s = "\n";
# print(s.isprintable());