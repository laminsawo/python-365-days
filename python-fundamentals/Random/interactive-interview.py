# Automated interview for a Network Engineer role
#Greet the job applicant
hello = "Hello, welcome to G Research"
my_name = "My name Lamin Sawo and I'll be interviewing you today"

name = input("What is your name? ")
age = int(input("How old are you? "))
address = input("What is your address: ")

role = input("What role are you interested in? ")
comment = str(input("Please tell me something about yourself and why you should be offered this JOB"))
certs = ""
which = ""
next_line = "\n"
if certs != "yes":
    certs = str(input("Do you have any certifications? (yes/no)")).lower()
    certs = certs
    if certs == "yes":
        which = str(input("Please type in the certification type you hold"))
    else:
        #prompt the user again
        print("Continuing to the other questions")
print(hello)
print(my_name)

print("My name is %s" %name)
print("I am %d years old" %age)
print("My address is %s" %address)
print("I am interested in the %s role you advertised" %role)
print("I have a %s certifications" %certs)
print(comment)
print("Bye")


'''
This is a comment and this is yet another comment
'''
