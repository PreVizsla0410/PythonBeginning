#def greetings_function(name, age):
    #print('Welcome ' +name); #str(name) - so can man einen String mit einem Integer verbinden
   # print('Welcome ' +name+ '. You are '+str(age)+' years old'); # nur indem wir den Integer in einen String konvertieren, können wir diese Funktion verbinden
#greetings_function('John', 27);

#def greetings_function2(*name): # so kann man von mehreren Namen eines Heraussuchen
 #   print('Welcome ' +name[1]);
#greetings_function2('John', 'Tim', 'Tom');

def greetings_function(name, age):
    print('Welcome ' +name+ '. You are '+str(age)+' years old'); 

name = input('Enter your name: ');
age = input('Enter your age: ');

greetings_function(name, age); # mit dieser Konstruktion kann man es dynamische gestalten



#def greetings_function(name):
 #   print('Welcome ' +name);

#greetings_function('John');

#outcome: Welcome John




#def greetings_function():
 #   print('Welcome user');

#greetings_function();