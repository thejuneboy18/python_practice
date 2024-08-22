# convert string to lower case

inp= "HELLO"
res= ""
for ch in inp:
    if "A" <= ch <= "Z":
        lwr=chr(ord(ch)+32)
        res += lwr
print(res)        













# # convert string to upper case

# inp = "hello"
# rslt = ""
# for ch in inp:
#     if "a" <= ch <= "z":
#         upr= chr(ord(ch)-32)
#         rslt += upr
#     else:
#         rslt += ch
# print(rslt)             

# convert string to swapcase

# inp = "Hello"
# res= ""
# for ch in inp:
#     if 'A' <= ch <= 'Z':
#         sw=chr(ord(ch)+32)
#         res += sw
#     elif'a' <= ch <= 'z':
#         sw=chr(ord(ch)-32)
#         res += sw
# print(res)     


# remove space from string 

# inp= "Hello world"
# res=''
# for ch in inp:
#     if ord(ch) != 32:
#         res += ch
# print(res)
