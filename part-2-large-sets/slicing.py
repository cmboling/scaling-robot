s = "Thisbisba test to figure how this shit works"
print(s[0:7])
print(s[:8])
print(s[8:])
print(s[:])

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
print "###########"
print(s[::2])

print "###########"
print(s[::-1])    # all items in the array, reversed
print(s[1::-1])   # the first two items, reversed
print(s[:-3:-1])  # the last two items, reversed if negative its -1 + 1 exclusive
print(s[-3::-1])  # everything except the last two items, reversed

print "###########"

print s[-1:]
print s[-1:]