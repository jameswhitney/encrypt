
#######################################################
# This is an exercise in creating a simple Encryption #
# class that encapsulates a encryption method         #
# as well as a decryption method. These methods use   #
# a modified version of a Ceaser Cypher for both the  #
# encryption method and the decyrption method.        #
#######################################################



# Import the string and random libraries
# to help create the encryption and decryption methods

import string
import random

class Encryption():

    # init method used initialize attributes of the class
    def __init__(self, seed):

        # Initialize the random number generator
        # The same seed value will be used to decrypt the 
        # encrypted phrase


        # Create an empty string attribute to hold the encrypted phrase


        # Use the string and random libraries to create two attributes
        # One is the correct alphabet, another is a shuffled alphabet

        pass
    

    def encryption(self, message):
       
        '''
        INPUT: A string message to be encrypted
        OUTPUT: An encrypted version of the message
        '''


        # Create an empty string for the first phase of encryption
        

        
        ################################################################
        ### STEP 1: REPLACE EVERY OTHER LETTER WITH A RANDOM LETTER ###
        ##############################################################



        #################################################
        ### STEP 2: REVERSE THE STRING  ################
        ###############################################



        ##########################################################################
        ##### STEP 3: USE THE RANDOM SHUFFLED ALPHABET FOR A Caeser CIPHER ######
        ########################################################################



        # Check if the letter or character in the message is found in the class's alphabet
        # If the element contains something other than a letter in the alphabet make sure
        # it is part of the encryption process. Assign the orignal alphabet's index to the class's random alphabet
        # in order to encrypt the message



        # Join the encrypted phrase and assign it to the encrypted phrase
        # return encrypted phrase


    

    def decryption(self, message, seed):
        
        '''
        This method takes in a messsage and a seed for the random shuffled alphabet.
        It then returns the decrypted alphabet.
        '''

        # Use the seed argument to create the same pseudo random sequence
        # created in the Encryption class. Create another random sampled
        # alphabet that is local to this method



        # Create a variable to hold the message as a list
        # and assign it as a list to a decrypted phrase variable



        # Enumerate through the message grabbing the index value
        # for each element as well as the contents of each element



        # Check if the letter or character in the message is found in the class's original alphabet
        # If the element contains something other than a letter in the alphabet make sure
        # it is not encrypted. Assign the orignal alphabet's index to the local random alphabet
        # in order to decrypt the message



        # Join the decrypted phrase and reassign it to the decrypted phrase variable
        # Reverse the string again and remove every other letter/character
        # Return the decrypted phrase 




        
