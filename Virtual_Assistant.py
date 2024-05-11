import pyttsx3
# A text-to-speech conversion library 
import speech_recognition as sr
#A speech recognition Library that supports  several engines and APIs.
import webbrowser
# A library that displays web-based documents.
from datetime import date, timedelta, datetime
# A library that supplies classes for manipulating dates.
import sys
# The library is used here to exit from the program when needed.
from itertools import zip_longest
#This object is imported to iterates through lists and zip them together.
import re
#This library is imported utilize the regular expressions of searching and finding certain strings.
import operator
#This library provides mathematical operation functions.
import csv 
#This library implements classes to read and write tabular data in CSV format.


sum_in_out = []
#This list stores all the dates added by the user, whether it is the date of checking in or out the country
sum_out = []
#This list only stores the checking out dates
first_phase = []
#This list stores the dates, whether that of checking in or out, that belongs to the first phase
second_phase = []
#Likewise, this list stores the dates, whether that of checking in or out. However, it only accepts dates that belong to the second phase




def main():
    """ This function expects two inputs: 'leaving_date' and 'entery_date'. If the expectation is met, the "main" function runs three different functions:
        1)"confirm_leaving_date)": This function asserts the date format of the "leaving_date" input and split it into a list of three items.
        2)"confirm_entery_date()":This function asserts the date format of the "entery_date" input and split it into a list of three items.
        3)"calculate()": This function uses the return values of the previous two functions to perform several calculations.

    When the user chooses not to add more inputs, the user can exit the program, which will autumatically run the fourth function:
        4)"table()": This function generates a CSV table that registers and sorts all of users' inputs.
     """
    
    while True:
        #This is an infinite loop; the program will keep asking the user for an input until the the user breaks out of it.
        try:
            #"Try" and "except" are used to break the "while True" loop when needed; 
            #"Try" checks the inputs. If the inputs are valid, the program will keep asking for enteries
            leaving_date = input("Last check out: ")
            #This variable keeps storing departuring dates until the user breakes out of the loop, either by executing "except EOFError" or entering an invalid input.
            sum_out.append(leaving_date)
            # In each loop, The method of append() adds the string stored the variable "leaving_date" to a list called "sum_out". The list keeps accepting new variables until the loop breakes.
            entery_date = input("last check in: ")
            #This variable keeps storing arrival dates until the users breakes out of the loop, either by executing "except EOFError" or entering an invalid input.

            leaving_date_separated = confirm_leaving_date(leaving_date)
            #The return value of "confirm_leaving_date()" is stored in "leaving_date_separated" and then passed into "calculate()".
            enetry_date_separated = (confirm_entery_date(entery_date))
            #The return value of "confirm_entery_date()" is stored in "entery_date_separated" and then passed into "calculate()".
            print((calculate(leaving_date_separated, enetry_date_separated)))
            #By the end of each round of the loop, the return value of "calculate() is printed"
        except EOFError:
            #"except EOFerror" is executed when the inputs print "ctrl" + "z" + "enter" on Windows or "ctrl" + "d" + "enter" on online environments.
            table()
            # "table()" is a function that get called by "main()" when "except EOFerror" is executed. "table()" generates a file with the name "output.csv"
            sys.exit("FCR granted! Check the CSV file, sign it, print it out, and handed it in to any police station nearby")
            #If the user is able to keep up with the loops by inserting valid inputs, 
            #and then breaks out willingly of "while loop" by "exceuting EOFError," this means that he has the right of FCR. 
            #This is declard as the program autamtically exists and prints out a statemnt of that meaning. 
            

def confirm_leaving_date(leaving_date):
    """ This function validates the date form the paramater "leaving_date" and then returns it as a list of three items.
    :param leaving date: the is the variable that stores the input as string. Ideally, the paramter should follow the Gregorian calender system: YY-MM-DD.
    :return "separate_date_into_groups": The function returns a list of three items, which represent the year, month, and date.
    """
    date_form_validater = re.search(r"^[1-2]{1}([0]|[9]){1}[0-9]{2}-[0-9]{2}-[0-9]{2}$", leaving_date)
    #This is a regular expression that takes "leaving_date" as a parameter.
    #The regular expression checks if the string stored in the parameter contains speceific patterns. The patterns must adhere to the following conditions:
    #"[1-2]{1}([0]|[9]){1}[0-9]{2}}": starts with a number of four digits, which all present the year.
    #the first two from the left must be either 19 or 20, the last two digits must ranges from 00 to 99
    #[0-9]{2}: the second part of the pattern must be a number of two digits that ranges from 00 to 99, which presents the months
    #[0-9]{2}-[0-9]{2}: the third number of the pattern must be of two digits that range between 00 to 99, which represent the days.
    if date_form_validater:
            #This if condition is executed when the parameter follows the patterns and, by result, the regular expression returns True.
            separate_date_into_groups =  leaving_date.split("-")
            #Split function takes "leaving_date" as a parameter and scan it as a string.
            #The function then takes "-" as a separastor which devides the string into items.
            return separate_date_into_groups
            #Split function returns a list of three items, which represent the year, month, and date.
    else:
         sys.exit("Invalid Date")
         #However, if the regular expression returns False, that is when "leaving_date" does not follow that patterns, the program exits and prints "Invalid Date"

def confirm_entery_date(entery_date):
    """ This function validates the date form the paramater "leaving_date" and then returns it as a list of three items.
    :param leaving date: the is the variable that stores the input as string. Ideally, the paramter should follow the Gregorian calender system: YY-MM-DD.
    :return "separate_date_into_groups": The function returns a list of three items, which represent the year, month, and date.
    """
    date_form_validater = re.search(r"^[1-2]{1}([0]|[9]){1}[0-9]{2}-[0-9]{2}-[0-9]{2}$", entery_date)
    #This is a regular expression that takes "leaving_date" as a parameter.
    #The regular expression checks if the string stored in the parameter contains speceific patterns. The patterns must adhere to the following conditions:
    #"[1-2]{1}([0]|[9]){1}[0-9]{2}}": starts with a number of four digits, which all present the year.
    #the first two from the left must be either 19 or 20, the last two digits must ranges from 00 to 99
    #[0-9]{2}: the second part of the pattern must be a number of two digits that ranges from 00 to 99, which presents the months
    #[0-9]{2}-[0-9]{2}: the third number of the pattern must be of two digits that range between 00 to 99, which represent the days.
    if date_form_validater:
        #This if condition is executed when the parameter follows the pattern and, by result, the regular expression returns True.
        separate_date_into_groups =  entery_date.split("-")
        #Split function takes "entery_date" as a parameter and scan it as a string.
        #The function then takes "-" as a separastor which devides the string into items.
        return separate_date_into_groups
        #Split function returns a list of three items, which represent the year, month, and date.
    else:
         sys.exit("Invalid Date")
         #However, if the regular expression returns False, that is when the "entery_date" does not follow that pattern, the program exits and prints "Invalid Date"

def calculate(leaving_date_separated, enetry_date_separated):
     """This function calculates the following:
     1)The day difference between "leaving_date" and "entery_date": if the difference between the two dates or the sum of differences is less than 120 days, FCR is granted.
     2)The date 2 years back from the first "leaving_date": This sets the timeframe for the user's inputs; if the user's first input is 2024-08-01, all inputs should not got back further than 2024-08-01
     3)The date 1 year back from the first "leaving_date": This is used to split the timeframe into two halves; which creates a fist phase and a second phase.
        ###parameters
     "param "leaving_date_separated": This paramater is a list of three items, which represent the year, month, and date.
     return => The function return the day difference between "entery_date" and "leaving_date"
     """
     day, mounth, year  = int(leaving_date_separated[2]), int(leaving_date_separated[1]), int(leaving_date_separated[0])
     #Three variables are created to store each item from the "leaving_date_separated" separately. 
     #Adding [] next to "leaving_date_separated" enables us to access each item of the list through inserting an integer that represents the item's location.
     #Using the function "int" to convert each item from a string to an integer, which is essential for the following functions of calculation.
     date_converted = date(year, mounth, day)
     #"date()" is a function that takes three parameterts and returns a date object in the year-month-day format.
     #Therefore, what was passed from "leaving_date_separated" as a list of three items is now cenverted to a one-date object.
     iday, imounth, iyear  = int(enetry_date_separated[2]), int(enetry_date_separated[1]), int(enetry_date_separated[0])
     #Three variables are created to store each item separately from the "entery_date_separated". 
     #Adding [] next to "enetry_date_separated" enables us to access each item of the list through inserting an integer that represents the item's location.
     #Using the function "int" to convert each item from a string to an integer, which is essential for the following functions of calculation.
     in_date_converted = date(iyear, imounth, iday)
     #"date()" is a function that takes three parameterts and returns a date object in the year-month-day format.
     #Therefore, what was passed from "leaving_date_separated" as a list of three items is now cenverted to a one-date object.
     staying_in_Tunisia = ((operator.sub(date_converted, in_date_converted)).days)
     #The sub() method of operation substracts the parameter "in_date_converted", which represents the date of "entery_date", and "date_converted", which represnts the date of "leaving_date",
     #The sub's return value in each loop is the day difference between the two dates.

     two_years_period = timedelta(days=730)
     one_years_period = timedelta(days=365)
     #"timedelta" is a method that sets a time unit based on the parameter "days".
     #"two_years_period" takes a parameter of 730 days to later calculate a two-year-difference between two dates. 
     #"one_years_period" takes a parameter of 365 days to later calculate a one-year-difference between two dates. 

     first_leaving_date = sum_out[0]
     #Any timeframe has a start time point and an end time point. This program's timeframe follows a reserve chronology where the start time point is the user's firt input.
     
     first_leaving_date_converted = datetime.strptime(first_leaving_date,"%Y-%m-%d").date()
     #"strptime()" converts the string into a DateTime objects. It takes two parameters, the first input of the user, and the Gregorian calender format.
     #following the format "%Y-%m-%d" is essential so that the return value of "strptime()" matches with the return value of "calculate()"
     start_of_second_phase = first_leaving_date_converted - one_years_period
     #This operation returns the the date that is one year back from the first "leaving_date".  
     start_of_first_phase = first_leaving_date_converted - two_years_period
     #This operation returns the date that is two years back from the first "leaving_date".

     if 0 < staying_in_Tunisia < 120:
          sum_in_out.append(staying_in_Tunisia)
          #Each differene between two dates shouldn't exceede 120 days for the duration of two years.
          if sum(sum_in_out) > 120:
               sys.exit("no more than 120 days")
               #Even if the user still has more dates to add, the loop breakes if the total difference is more than 120.
          elif  date_converted < start_of_first_phase:
               sys.exit("stay withing two years")
               #Any input in each loop should predate the first "leaving_date" by at least a day, and by 2 years at the most.  
               
          elif date_converted > start_of_second_phase: 
              if sum(second_phase) < 120:
                  second_phase.append(staying_in_Tunisia)
          #When the current "leaving_date" falls after the first "leaving_date" by atleast a year,
          #and the difference between "leaving_date" and "entery_date" is less than 120 days,
          #The date is classidied as a "second_phase" date
          elif date_converted < start_of_second_phase:
              if sum(first_phase) < 120:
                  first_phase.append(staying_in_Tunisia)
          return staying_in_Tunisia
          #When the current "leaving_date" falls after the first "leaving_date" by a year at the most,
          #and the difference between "leaving_date" and "entery_date" is less than 120 days,
          #The date is classidied as a "first_phase" date

     elif (str(staying_in_Tunisia)).startswith("-"):
          sys.exit("leaving the country must proceed entering it")
          #It is unacceptable when the user inserts "entering_date" before "leaving date"; this rturns a negative integer.
          #By result, the programs exits. 
     else:
          sys.exit("no more 120")
          #when the difference between the two dates doesn't follow up with the if conditionals, the program exists.
def table():
     """ This function prints out the items of the global lists "first_phase" and "second_phase" as tabular data
     :"parameter": no direct parameters are directly passed to the function; it uses global lists.
     return: No return vakue as the function generates a CSV file instead.
     """
     schema = {"first_phase": first_phase, "second_phase": second_phase}
     #Creating a dictionary that takes the lists' names as key and the lists' items as values.
     head, value = zip(*schema.items())
     #The zip functiom generates two tuples: one for the keys, and another for the vlaues.
     #The values still takes the items of "first_phase" and "second_phase".
     placement_of_each_date = (dict(zip(head, row)) for row in zip_longest(*value, fillvalue='_'))
     #"zip_longest()" function creates a list where each item of the list "first_phase" is paired together with an item from the list "second_phase" as a tuple.
     #the absence of such an item is compensated with a "-".
     #A "dict() function takes each pair returned by "zip_longest" as a dictionary value.
     #The "dict" function assigns each dictionary value to the items in the previously created tuple, "head".
     #The head is either "first_phase" or "second_phase".
     with open('output.csv', 'w') as f:
        #"f" is a file opened for writing a CSV table.
        wrtr = csv.DictWriter(f, fieldnames=head)
        wrtr.writeheader()
        wrtr.writerows(placement_of_each_date)
        #"DictWriter()" is a method that organizes a CSV's rows based on the structure of a dictionary "(dict(zip(head, row))"
        #"writeheader()": the first row contains the dictionary keys : "first_phase" and "second_phase". Each key takes a column as each is previously set as a head.
        #"writerows()": the rest of the rows contain the dictionary values, which represent the difference in days between the "entery_date" and "leaving_date".
        # Each value is written under its key row by row.
        
#### The "main()" function block ends here, but it is still not called.
### The following blocks are responsible of creating a voice assistant system (voice_user interface).
### This part's main purpose is interacting with the user.
### Based on the user's order, the "main()"" function is called.

bob = pyttsx3.init()
#Initializing the engine to convert a text to a speech
voices = bob.getProperty('voices')
bob.setProperty('voices', voices[0].id)
bob.setProperty('volume', 1.0) 
bob.setProperty('rate', 150)
#A voice is imported and customized to my liking.

def speech(text):
    """ The is the function that converts any sequence of strings passed to it to a speech. 
        This function is used as a part of voice-user interface;
        the function uses speech to prompt the user for spoken commands.
        :param "text": any text, sequence of strings", which is later passed to the function. 
        """
    bob.say(text)
    #"say()" is the method that converts any string stored in "text" to a speech
    bob.runAndWait()
    #"runAndWait" is essential so that later functions are only called after the engine reads the text
speech("This is the FCR calculation system; a system that enables its users to calculate the duration of residency in Tunisia. if you would like to know more about the FCR coditions, say yes. If you wish to start calculating, say calculate, If you wish to exit, say exit")
#The function reads the text passed to it, which is used to make the user choose between two options.
#The sequences "say yes" and say "calculate" assure to the user that the program will take auditory input.
    
def TakeCommands():
    """ As opposed to the previous function, 
    "TakeCommands()" converts a speech to a text.
    This function is split into two parts:
    1) Recording the input
    2) Recognizing the input
    """
    command = sr.Recognizer()
    #"Recognizer" is a class whose methods convert speech to text.
    with sr.Microphone() as mic:
        print("Listening...")
        #Priniting to confirm virtual assistant is recording the auditory input.
        #"Micrphone()" is a class whose methods uses the user's device to capture the sound waves of the auditory input.
        
        command.phrase_threshold = 1
        #"phrase_threshold" sets the duration of waiting for an input before moving to the next line of code
        mic_input = command.listen(mic)
        #The method "listen()" records the speech accessed by the method "Microphone"
        try:
        #This block will test the auditory input.
        #The pprogam will raise an "unKownValueError" when the user fails to provide such an input.
            print("Recording...")
            recognized_material = command.recognize_google(mic_input, language="en")
            #"recognize_google()" is a method that uses Google Speech API to recognize the recorded auditory input.
            #After sound recognition, this method converts the audio to a text.
            #"recognized_material" is a variable that stores the auditory input as a sequence of strings. 
            print(f"The order is: {recognized_material} ")
            #The printed statement illustrates to the user what the method "recognize_google" has recognized.
            return recognized_material.lower()
            #Adding the method "lower()" is essential as the recognized string will be later compared to pre_selectes strings, which represent the programs orders.
                    
        except AttributeError:
            sys.exit(1)
            # The program exits if the user does not provide an input




while True:
    
    query = TakeCommands()
    #This is an infinite loop that keeps comparing the speaker's input with some pre_selectes strings, which represent the programs orders
    #until the speaker exits the program, either willingly or by providing an input that is not previously defined.
    #By storing the function "TakeCommand" in the varioable "query", the program can simultaneously call the function and access the strings returned to it.
    #If one of the options matches the input, the program will perform at least one of the following: run "main", open a web page, or provide an auditory reply to the command 
    #Converting a sequence of strings to an audio is performed by the function "speech".
    #opening a web page is done via the module "webbrowser" and the method "open_new_tab".
    #
    if "yes" in query:
        speech("Declare the last date of leaving Tunisia. Then, declare all the entry and leaving dates within the frame of two years from the last leaving date the country. your stay shouldn't exceede 120 days in each year. If you wish to know if you have the right of FCR, say Calculate. If you need more information, say more information. If you wish to exit the program, say exit")
    elif "more information" in query:
        speech("ok sir")
        webbrowser.open_new_tab("https://www.douane.gov.tn/ar/")
    elif "calculate" in query:
        speech("ok sir")
        x = main()
        #Throughout the whole program , "main" is only called here.
    elif "exit" in query:
        sys.exit("Take care!")
    else:
         speech("Come again!")
         print("Come again!")

    
#The program ends here. I hope you enjoyed it!