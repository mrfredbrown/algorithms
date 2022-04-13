
def breakstring(string):
    newstring1 = [];
    newstring2 = [];
    halflength = round(len(string)/2);
    fulllength = len(string);
    print("halflength is",halflength);

    #for element in string:
    for i in range(0, int(halflength)):
       newstring1.append(string[i])
            #for i in range(int(halflength)+1,int(fulllength)):
            #    newstring2.append(element)
    for i in range(int(halflength),int(fulllength)):
       newstring2.append(string[i])


    print("1st half of string is",newstring1);
    print("2nd half of string is",newstring2);


breakstring("abcdef");
breakstring("1234567");





#return(new_string1,newstring2)