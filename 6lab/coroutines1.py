s="The quick brown fox jumped over the lazy old dog."

def capitalize():
    while True:
        value=yield
        print value.upper()

c=capitalize()
c.next()
for word in s.split():
    c.send(word)
