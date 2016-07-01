#MAJOR PYTHON TUTORIALS WITH EXAMPLES COMPLETE.
#ALL THE DESCRIPTION IS AVAIBLABLE WITHIN THE CODE ITSELF
#PROGRAM DONE USING SIMPLE PRINT AND LOOPING STATEMENTS
#!/usr/bin/python
#By A.SAI RAVI TEJA - 13003061
from datetime import datetime
f1=True

while 1:
    print("\n"*50)
    print("\t"*5,"__________________________________________________________________________________")
    print("\t"*5,"|++++++++++++++++++++++++++++++++PYTHON TUTORIALS++++++++++++++++++++++++++++++++|")
    print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n","\t"*9,"1.)PYTHON SYNTAX")
    print("\n","\t"*9,"2.)STRINGS & OUTPUT CONSOLE")
    print("\n","\t"*9,"3.)DATE & TIME")
    print("\n","\t"*9,"4.)CONDITIONALS & CONTROL FLOW")
    print("\n","\t"*9,"5.)FUNCTIONS")
    print("\n","\t"*9,"6.)LISTS")
    print("\n","\t"*9,"7.)TUPLES")
    print("\n","\t"*9,"8.)QUIT THE PROGRAM")
    print("\t"*5,"__________________________________________________________________________________")
    print("\t"*5,"|++++++++++++++++++++++++++++++++PYTHON TUTORIALS++++++++++++++++++++++++++++++++|")
    print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    n=int(input("\n\n\n SELECT AN OPTION: "))
    if(n==1):#PYTHON BASICS
        print("\n"*25)
        print("\n\n\n\t\t\t\tThis Concept will introduce you to strings and console output in Python,  including creating strings,\n\n\t\t\t        calling a variety of string methods, and using the 'print' keyword.")
        input("\n To proceed press Enter....")
        while f1:
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++++BASIC CONCEPTS+++++++++++++++++++++++++++++++++|")#PYTHON SYNTAX
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n","\t"*9,"1.)VARIABLES")
            print("\n","\t"*9,"2.)BOOLEANS")
            print("\n","\t"*9,"3.)WHITE SPACES")
            print("\n","\t"*9,"4.)SINGLE LINE COMMENTS")
            print("\n","\t"*9,"5.)MULTI-LINE COMMENTS")
            print("\n","\t"*9,"6.)MATH OPERATIONS[CALCULATOR]")
            print("\n","\t"*9,"7.)MAIN MENU")
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++++BASIC CONCEPTS+++++++++++++++++++++++++++++++++|")
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            n1=int(input("\n\n\n SELECT AN OPTION: "))
            if(n1==1):
                print("\t\t\t\tCreating web apps, games, and search engines all involve storing and working with different types of data. \n\n\t\t                They do so using variables. A variable stores a piece of data, and gives it a specific name.")
            # Write your code below!
                input("\n To proceed click Enter....")
                mv=input("\n\tTo create a variable type any letter or word: ")
                print("\n\tThe variable ",mv,"is assigned a value","104[Can be Changed]") #104 can be Changed to desired value.
                mv=104
                print("\n\tType print(mv) to get the value of mv")
                print("\n\tThe value of the variable is: ",mv)
                input("\n\tPress Enter to go back...")
            if(n1==2):
                print("\t\t\t\tA boolean is like a light switch. It can only have two values. Just like a light switch can only be on or off, \n\n\t\t\t        a boolean can only be True or False.")
                input("\n To proceed click Enter....")
                b=input("\n\tTo create a variable type any letter or word: ")
                input("\n\tSet the above variable to True for execution [TYPE True]: ")
                b=True
                if(b==True):
                    print("\n\tThe variable is True and this is executed.")
                    input("\n\tPress Enter to go back...")
            '''elif(b!=True and b!=False):
                print("\n\tThe variable is set to False and this is executed.")'''
            
            if(n1==3):
                print("\n\t\t\t\tIn Python, whitespace is used to structure code. Whitespace is important, so you have to be careful with how you use it.\n\n\t\t\t        Usually in Loops")
                input("\n\tPress Enter to go back...")
            if(n1==4):
                print("\n\t\t\t\tThe # sign is for comments. A comment is a line of text that Python won't try to run as code. It's just for humans to read. \n\n\t\t\t        Check The source code for Comments.")
                input("\n\tPress Enter to go back...")
            if(n1==5):
                print("\n\t\t\t\tFor multi-line comments, you can include the whole block in a set of triple quotation(''') marks.Check the \n\n\t\t\t        source code for Triple quotes ")
                input("\n\tPress Enter to go back...")
            if(n1==6):
                print("\n"*50)
                print("\n\t\t\t\t\t\tBASIC MATH OPERATIONS LIKE '+ = * /' Can be done in a basic Calculator")#exception handing included
                def men():
                    print('\n\t\t\t\t\t\t##############################CALCULATOR##############################\n')
                    x=int(input("\n\t\t\t\t\t\t\t\tEnter First number: "))
                    y=int(input("\n\t\t\t\t\t\t\t\tEnter Second nubmer: "))
                    print("\n","\t"*9,"1.Addition")
                    print("\n","\t"*9,"2.Subtraction")
                    print("\n","\t"*9,"3.Multiplication")
                    print("\n","\t"*9,"4.Division")
                    print("\n","\t"*9,"5.Power")
                    print("\n","\t"*9,"6.Go Back")
                    print('\n\t\t\t\t\t\t##############################CALCULATOR##############################\n')
                    n=int(input("\n\tEnter your option: "))
                    if(n==1):
                        add(x,y);
                    if(n==2):
                        Sub(x,y);
                    if(n==3):
                        Mul(x,y);
                    if(n==4):
                        div(x,y);
                    if(n==5):
                        pw(x,y);
                def add(a,b):
                    print("\n\tThe Sum of two numbers is: ",a+b);
                def Sub(a,b):
                    print("\n\tThe Substraction of two numbers is: ",a-b);
                def Mul(a,b):
                    print("\n\tThe Multiplication of two numbers is: ",a*b);
                def pw(a,b):
                    print("\n\tThe Power of two numbers is: ",a**b);
                def div(a,b):
                    while 1:
                        try:
                            print("\n\tThe division of ", a,"/",b,"is",a/b)
                            break
                        except ZeroDivisionError:
                            print("\n\tUndefined Value Cannot divide with Zero!!!")
                            break
                men()
                input("\n\tPress Enter to go back...")
            if(n1==7):
                break
    if(n==2):#STRING CONCEPTS
        print("\n"*25)
        print("\n\n\n\t\t\t\tAnother Useful data type is the string. A string can contain letters, numbers, and symbols. String can be assigned\n\n\t\t\t        a variable to any string such type p='This is a String' assigns p that String.")
        p="This is a String"
        while 1:
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++++STRING CONCEPTS+++++++++++++++++++++++++++++++++|")
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n","\t"*9,"1.)ASSIGNING A STRING TO A VARIABLE")
            print("\n","\t"*9,"2.)ACCESS BY INDEX")
            print("\n","\t"*9,"3.)LENGTH OF THE STRING")
            print("\n","\t"*9,"4.)LOWER CASE OF STRING")
            print("\n","\t"*9,"5.)UPPER CASE OF STRING")
            print("\n","\t"*9,"6.)NON-STRINGS TO STRINGS")
            print("\n","\t"*9,"7.)MAIN MENU")
            n2=int(input("\n\n\n SELECT AN OPTION: "))
            if(n2==1):
                input("\n\tInitially p is assigned 'This is a String' value. ")
                print("\n\tWhen p is printed we get the String....:",p)
                input("\n\tPress Enter to go back...")
            if(n2==2):
                input("\n\tThe Character in the String can be accessd by indexing.")
                print("\n\tIf we want to get the Character at certain index we can type p[index]")
                input("\n\tLet the String be PYTHON")
                p="PYTHON"
                ind=int(input("\n\tEnter the index [0-5]: "))
                print("\n\tThe Character is: ",p[ind])                                
                input("\n\tPress Enter to go back...")
            if(n2==3):
               st=input("\n\tEnter string: ")
               print("\n\tThe Length of the String is: ",len(st))
               input("\n\tPress Enter to go back...")
            if(n2==4):
               st=input("\n\tEnter string: ")
               print("\n\tThe lowercase of the String is: ",st.lower())
               input("\n\tPress Enter to go back...")
            if(n2==5):
               st=input("\n\tEnter string: ")
               print("\n\tThe UPPERCASE of the String is: ",st.upper())
               input("\n\tPress Enter to go back...")
            if(n2==6):
               inte=float(input("\n\tEnter any NUMBER:"))
               print("\n\tChanging the non String to String.....")
               print("\n\tThe Number is now a String",str(inte))
               input("\n\tPress Enter to go back...")
            if(n2==7):
                break
    if(n==3): #DATE AND TIME
        print("\n\t\t\t\t\tDATE AND TIME can be imported from predefined header file.The header file is 'from datetime import datetime\n\n\n\t\t\t\t        which can be used to include the date and time values.")
        print("\n\t\t\t\t\tTo print the current Date and time assign a Variable datetime.now() to now")
        now = datetime.now()
        input()
        print ('\n\n\t\t\t\t\t\t MM/DD/YY HH:MH:SH --- %s/%s/%s  %s:%s:%s' % (now.month, now.day, now.year,now.hour,now.minute,now.second))
        input("\n\tPress Enter to go back...")
    if(n==4): #CONDITIONAL STATEMENTS
        print("\n\n\n\t\t\t\tJust like in real life, sometimes we'd like our code to be able to make decisions.The Python programs we\'ve written\n\n\t\t\t so far have had one-track minds: they can add two numbers or print something, but they don\'t have the ability to pick one of these outcomes\n\n\t\t\t        over the other. Control flow gives us this ability to choose among outcomes based off what else is happening in the program.")
        print("\n\n\tConsider an Example which shows the control of Statements.")
        def hall(): #hall function is defined
            print ("\n\tYou've just entered the Hallway!!")
            print ("\n\tDo you take the door on the left or the right?")
            answer = input(("\n\tType left or right and hit 'Enter': "))
            if answer == ("left" or answer == "l"): #Choosing left or right a Condition!
                print ("\n\tHAHA! You entered Left room, You should have entered right!")
            elif (answer == "right" or answer == "r"):
                print ("\n\tALAS! You entered right room, But the exit is left!")
            else:
                print ("\n\tYou didn't pick left or right! Try again!!")
                hall()

        hall()
        print("\n\n\tThis is an Example of Conditional and Control Flow Statement. Check the Source Code for details......")
        input("\n\tPress Enter to go back...")
    if(n==5):
        print("\n"*25)
        print("\n\n\n\n\t\t\t\t\t\t\t\tThere are several types of Functions in Python.")
        print("\n\n\n\n\t\t\t\t\t\t\t\t    Let's do some programs using Functions")
        while 1:
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++FUNCTION EXAMPLES++++++++++++++++++++++++++++++++|")
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n","\t"*9,"1.)FACTORIAL")
            print("\n","\t"*9,"2.)LARGEST")
            print("\n","\t"*9,"3.)MAIN MENU")
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++FUNCTION EXAMPLES++++++++++++++++++++++++++++++++|")
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            m=int(input("\n\tENTER YOUR OPTION: "))
            if(m==1):
                def fact():
                    f=int(input("\n\tEnter number: "))
                    fac=1
                    if f<0:
                        nofac();
                    elif f==0:
                        print("\n\tThe factorial of 0 is 1")
                    else:
                        for i in range(1,f+1):
                            fac=fac*i
                        print("\n\tThe factorial of",f,"is",fac)
    
                def nofac():
                    print("\n\tNo factorial");
                fact()
                input("\n\tPress Enter to go back...")
            if(m==2):
                def men1():
                    print("\n\t\tEnter any 3 numbers ")
                    a=int(input("\n\t\tEnter 1st num: "))
                    b=int(input("\n\t\tEnter 2nd num: "))
                    c=int(input("\n\t\tEnter 3rd num: "))
                    if(a>b and a>c):
                        abig();
                    if(b>c and b>a):
                        bbig();
                    if(c>a and c>b):
                        cbig();
         
                def abig():
                    print("\n\t\tA is big!!!");
                def bbig():
                    print("\n\t\tB is big!!!");
                def cbig():
                    print("\n\t\tC is big!!!");

                men1()
                input("\n\tPress Enter to go back...")
            if(m==3):
                break
    if(n==6):
        print("\n"*25)
        print("\n\t\tLists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name. ")
        s1=input("\n\n\n\n\t\t\tEnter string to split into lists: ")
        l1=s1.split()
        print("\n\n\n\n\n\t\tThe given list is: ",l1)
        print("\n\n\n\n\n\t\tThe Type is ",type(l1))
        while 1:
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++++LISTS FUNCTIONS++++++++++++++++++++++++++++++++|")
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n","\t"*9,"1.APPEDING THE LIST")
            print("\n","\t"*9,"2.CLEAR THE LIST")
            print("\n","\t"*9,"3.COUNTING A PARTICULAR ELEMENT")
            print("\n","\t"*9,"4.EXTENDING THE LIST")
            print("\n","\t"*9,"5.INDEX OF ELEMENT")
            print("\n","\t"*9,"6.INSERTING A LIST INSIDE A LIST") 
            print("\n","\t"*9,"7.POPPING OF ELEMENT")
            print("\n","\t"*9,"8.REMOVING AN ELEMENT")
            print("\n","\t"*9,"9.REVERSING THE LIST")
            print("\n","\t"*9,"10.SORTING THE LIST")
            print("\n","\t"*9,"11.DISPLAYING THE LIST")
            print("\n","\t"*9,"12.MAIN MENU")
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++++LISTS FUNCTIONS++++++++++++++++++++++++++++++++|")
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            n=int(input("\n\tEnter your option: "))
            if(n==1):
                s=input("\n\tEnter String to Append: ")
                print("\n\t",l1.append(s))#ADDING AT THE END
                print(l1)
                input("\n\tPress Enter to go back...")
            if(n==2):
                print(l1.clear())
                print(l1) #DELETE THE LIST
                print("\n\tThe list is cleared")
                input("\n\tPress Enter to go back...")
            if(n==3):
                print("\n\tThe Given list is : ",l1)
                sc=input("\n\tEnter the string to count: ")
                print("\n\tThe count is: ",l1.count(sc))
                input("\n\tPress Enter to go back...")
            if(n==4):
                print("\n\tThe Given list is : ",l1)
                ex=input("\n\tEnter String to insert and extend in list: ")
                print(l1.extend(ex))
                print("\n\tThe extended List is: ",l1)
                input("\n\tPress Enter to go back...")
            if(n==5):
                print("\n\tThe given list is: ",l1)
                ind=input("\n\tEnter the word to get index: ")
                print("\n\tThe index of",ind,"is",l1.index(ind))
                input("\n\tPress Enter to go back...")
            if(n==6):
                print("\n\tThe given list is: ",l1)
                ins=input("\n\tEnter the string to insert: ")
                sins=ins.split()
                pos=int(input("\n\tEnter the position to enter the string: "))
                l1.insert(pos,sins)
                print("\n\tThe modified list is: ",l1)
                input("\n\tPress Enter to go back...")
            if(n==7):
                print("\n\tThe given list ",l1)
                print("\n\tPopping the last element....")
                l1.pop()
                print("\n\tThe popped element is: ",l1.pop())
                input("\n\tPress Enter to go back...")
            if(n==8):
                print("\n\tThe given list is: ",l1)
                rem=input("\n\tEnter element to remove from list: ")
                l1.remove(rem)
                print("\n\tList after removing the element is :",l1)
                input("\n\tPress Enter to go back...")
            if(n==9):
                print("\n\tThe given list is: ",l1)
                l1.reverse()
                print("\n\tThe reverse of the list is ",l1)
                input("\n\tPress Enter to go back...")
            if(n==10):
                print("\n\tThe given list is: ",l1)
                l1.sort()
                print("\n\tSorted list is: ",l1)
                input("\n\tPress Enter to go back...")
            if(n==11):
                print("\n\tThe Modified list is ",l1)
                input("\n\tPress Enter to go back...")
            if(n==12):
                break
    if(n==7):
        print("\n"*30) #TUPLES
        print("\n\t\tA tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, \n\n\t\tthe tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.Tuples are immutable which \n\n\t\tmeans you cannot update or change the values of tuple elements.")
        while 1:
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++++TUPPLE FUNCTIONS+++++++++++++++++++++++++++++++|") #UNDER CONSTRUCTION
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n","\t"*9,"1.CREATING A TUPLE")
            print("\n","\t"*9,"2.UPDATING THE TUPLE")
            print("\n","\t"*9,"3.DELETING A TUPLE")
            print("\n","\t"*9,"4.MAIN MENU")
            print("\t"*5,"__________________________________________________________________________________")
            print("\t"*5,"|+++++++++++++++++++++++++++++++++TUPPLE FUNCTIONS+++++++++++++++++++++++++++++++|")
            print("\t"*5,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            n=int(input("\n\tEnter your option: "))
            if(n==1):
                input("\n\tLet the tuples are tup1 = ('physics', 'chemistry', 1997, 2000);tup2 = (1, 2, 3, 4, 5, 6, 7 );")
                tup1 = ('physics', 'chemistry', 1997, 2000);
                tup2 = (1, 2, 3, 4, 5, 6, 7 );
                print("\n\tFor the given let's print 0 index of tup1 and 1:5 index of tup2")
                print ("\n\ttup1[0]: ", tup1[0])
                print ("\n\ttup2[1:5]: ", tup2[1:5])
                input("\n\tPress Enter to go back...")
            if(n==2):
                print("\n\t\tSince two tuple cannot be updated..Create a new tuple and add the first two tuples..")
                print("\n\t\tLet the two tuples be  tup1 = (12, 34.56) tup2 = ('abc', 'xyz')")
                tup1 = (12, 34.56);
                tup2 = ('abc', 'xyz');
                tup3 = tup1 + tup2;
                print ("\n\t",tup3)
                input("\n\tPress Enter to go back...")
            if(n==3):
                print("\n\t\tLet the TUPLE be ('physics', 'chemistry', 1997, 2000)")
                tup = ('physics', 'chemistry', 1997, 2000);
                del tup;
                print ("\n\t\tTuple is Deleted")
                input("\n\tPress Enter to go back...")
            if(n==4):
                break
    if(n==8):
        break
