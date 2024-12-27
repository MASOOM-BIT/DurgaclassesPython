#input : ABCABCABC
#output : A-->2
#B --> 2
#C --> 2
InputString= input('Enter the String : ')

d={} #declaring empty String
for x in InputString:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
for k,v in d.items():
    print("{} occurs {}".format(k,v))