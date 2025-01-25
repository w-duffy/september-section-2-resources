# Split Capitals

# Create a function which adds spaces before every capital in a word. Lower case
# the whole string afterwards.

#!!START
def split_capitals(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i].isupper():
            result += " "
        result += s[i]
        i += 1
    return result.lower()
#!!END


print(split_capitals("helloWorld"))     #> "hello world"
print(split_capitals("iLoveMyTeapot"))  #> "i love my teapot"
print(split_capitals("stayIndoors"))    #> "stay indoors"
