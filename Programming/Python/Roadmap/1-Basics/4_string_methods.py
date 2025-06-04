#index
#index always starts from 0.
#index should be mentioned in square brackets[].
#integer doesnt have any idx.
start_idx : end_idx
'ajithkumar'[0:] #ajithkumar
'ajithkumar'[1:] #jithkumar
'ajithkumar'[:1] #a
'ajithkumar'[0:5] #ajith
#it will reverse the input string
'ajithkumar'[::-1] #ramukhtija
#prints every second letter of the string
'ajithkumar'[::2]
#prints every second letter of the string from reverse side
'ajithkumar'[::-2]
#String Methods

There is lots of string methods.
Below are basic and frequently used methods.


1.Padding functions

    Only works with str. Otherwise it will throw syntax error.

        center()
            Args : str.center(length,fillchar)
                length - length of char
                fillchar - char need to be filled on length
            What : It aligns the string to center by using specified character.

                'ajith'.center(10,"*") #'**ajith***'
                'ajith'.center(8,'*') #'*ajith**'
                'ajith'.center(12,'*') #'***ajith****'
                'ajith'.center(14,'*') #'****ajith*****'
                'ajith'.center(11,'*') #***ajith***
                'ajith'.center(10,'**') #'TypeError: The fill character must be exactly one character long'
                'ajith'.center(10,'ajith') #'TypeError: The fill character must be exactly one character long'
                'ajith'.center(10,1) #'TypeError: The fill character must be a unicode character, not int'
                'ajith'.center(3,'*') #ajith
                1234.center(10,'*') #Invalid Syntax

        ljust()
            Args : str.ljust(length,fillchar)

            'ajith'.ljust(10,'*') #'ajith*****'

        rjust()
            Args : str.rjust(length,fillchar)
        
            'ajith'.rjust(10,'*')  #'*****ajith'

2. count()
    This method returns the count of given value appears in a string.
    Only works for string.
    string based.
    it will search the whole string in target.

    syntax : str.count(value,start_position,end_position)

'aajith'.count('ajy',0,10)  #0

string = '12345222'

string.count('2')  #4
string.count('24') #0
'ajith likes to call himself aji'.count('aji')  #2

number = 123321
number.count(1) #error 'int' object has no attribute

3.Case functions

        uppper()
            Whatever case of input it will swap it into upper case.
            if the numbers are string it will return numbers as it is.

        'ajith'.upper() #'AJITH'
        'AJITH'.upper() #'AJITH'
        '123'.upper() #'123'

        lower()
            Whatever case of input it will swap it into lower case.
            if the numbers are string it will return numbers as it is.

        'ajith'.lower() #'ajith'
        'AJITH'.lower() #'ajith'
        '123'.lower() #'123'
        'abc123'.lower() #abc123

        capitalize()
            Whatever the input it will swap the first letter into upper case and swap all other letters into smallwe case.

            'ajith'.capitalize() #Ajith
            'ajith kumar'.capitalize() #Ajith kumar
            'AJITH KUMAR'.capitalize()  #Ajith kumar
            '123abc'.capitalize()  #123abc

        title()
            It is like initcap in oracle.
            It makes every first letter of word into uppercase and make other into lower case.

            'ajith kumar j'.title()  #Ajith Kumar J
            'AJITH KUMAR J'.title()   #Ajith Kumar J
            
        swapcase()
            This method swap the case to opposite case. If input is smallercase then it will swap into upper and vice versa.
            Works only for string.
            It works char based. It will check each char in string and swap(*)

            str.swapcase()

            'ajith'.swapcase()  #'AJITH'
            'AJITH'.swapcase()  #'ajith'
            'AjithKumar'.swapcase() #'aJITHkUMAR'
4.startswith() and endswith()
    output is boolean.
    Python start search from string  whitespace
    from the start index.
    
    str.startswith(value,start,end)

    'ajith'.startswith('a')  #True
    'ajith kumar'.startswith('ajith ') #True
    'ajith kumar'.startswith('k',6)  #True
    'ajith kumar'.startswith('a ') #False

    str.endswith(value,start,end)

    'ajithkumar'.endswith('a',-10)  #False
    'ajithkumar'.endswith('r',-10)  #True
    'ajithkumar'.endswith('R',-10)  #False
    'ajithkumar'.endswith('u',-6,7)
    'ajithkumar'[-6] #'h'
    'ajithkumar'[7] #'m'

    #start idx consider the starting idx.
    #ending idx consider till privious to ending idx.
    #always the process goes from left to right.

5.find()

    returns the first idx of value in a string
    works left to right.

        str.find(value,start,end)
    name = 'My name is Ajith. But she call me aji'
    name.find('aji')  #34
    name.lower().find('aji')  #11
    'ajithkumar'.find('a',4) #8
    'ajithkumar'.find('a') #0

    rfind()
        same as find but it returns the last appearnce idx value.
        works right to left.

        name.rfind('aji')  #34
        name.lower().rfind('aji')  #34
        'ajithkumar'.rfind('m')  #7
        'ajithkumar'.rfind('a') #8
6.replace()
    str.replace(oldval,newval,count)
    string based.
    #count - how many occurence need to change. if we give 1 then first occurence only changed.
    # if we dont give value it will change all the values
    name = 'aji aji aji'
    name.replace('aji','-')

    name = 'My name is ajith'
    name.replace('ajith','steve')
    name.replace('ajith','')
    name.replace(' ','-') #My-name-is-ajith
    name.replace('','1') #it will insert the newval between every letter of the string.
    'ajith'.replace('','1') #1a1j1i1t1h1
    'ajith'.replace('','') #ajith
    'ajith'.replace('ak','sj') #

7.strip()
    # This method remove the chars from leading and trailing. 
    # Default char is whitespace.
    # char based. search each char and removes it.
    str.strip(char)

    name = '  I am ajith  '
    name
    name.strip()
    name = '*/**! ajith kumar */*!'
    name.strip('/*! ') #ajithkumar
    '*/**aji*th/*/kumar/**///*'.strip('/*')  #aji*th/*/kumar
    It will search and remove the char until it fails. Once it is failed it wont search further.
    it is char based.
    ovvoru char poi target la search panum if that matches it will remove the untill it fails.

    
    rstrip() and lstrip()
    rstrip - removes chars from right side.
    lstrip - removes char from left side.

8.zfill()
    Adds the zeros at the beginning of the string.

    str.zfill(length)  #total length including zero's

    'ajith'.zfill(10) #00000ajith
    'ajith'.zfill(3)  #ajith (No zeros were added since length is smaller than input's length)

9.split()
    It splits the sentence into list of words by seperator.(default seperator is whitespace).
    
    str.split(Separator,maxsplit)

    maxsplit : denotes the number of splits. Default is 1.

    sentence = 'The name is tony'
    sentence.split()
    
    name = '   '
    name.split() #empty list

    sentence = 'thisziszajithz'
    sentence.split('z')  #4 words

    sentence = 'this is ajith'
    sentence.split()
    'ajith'.split()
    'ajith'.split('') #ValueError: empty separator

    'the_name_is_ajith__'.split('_')
    #last la ethana space irunthalum athu consider pannathu.
    #But seperator use panna ethana time sep use panromo athana time split aagum.

    name = 'the name is ajithkumar the engineer'
    name.split(' ',2)   #the,name,is ajithkumar the engineer
    name.split(maxsplit=4) #the.name.is.ajithkumar.the engineer


    num = 1234
    num.split()

    #split wont work for numbers.

rsplit()
    same as split.
    but it splits the sentence from right.

    name='I am ajthkumar'
    name.rsplit()
    name = 'I am ajithkumar'
    name.split(maxsplit=1)

10.join()
    join the strings,list elements by the joining char.
    
    joining_char.join(str or list,tuble,set,dict)

    '$'.join('Ajith')  #$A$j$i$t$h

    list1=['the','name','is','ajith']
    '-'.join(list1)  #the-name-is-ajith
    
    ''.join(['a','j','i'])
    ' '.join(['a','j','s'])
    '-'.join('ajith')

# split each char into split

' '.join('ajith').split()

11.isalnum():
    Returns True if all characters in the string are number or alpha or mixed
12.isalpha():	
    Returns True if all characters in the string are in the alphabet
13.isascii():	
    Returns True if all characters in the string are ascii characters
14.isdecimal():	
    Returns True if all characters in the string are decimals
15.isdigit():	
    Returns True if all characters in the string are digits
16.isidentifier():	
    Returns True if the string is an identifier
17.islower():	
    Returns True if all characters in the string are lower case
18.isnumeric():
    Returns True if all characters in the string are numeric
19.isprintable():
    Returns True if all characters in the string are printable
20.isspace():
    Returns True if all characters in the string are whitespaces
21.istitle():
    Returns True if the string follows the rules of a title
22.isupper():
    Returns True if all characters in the string are upper case

