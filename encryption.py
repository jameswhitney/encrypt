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
        random.seed(seed)
        self.seed = seed

        # Create an empty string attribute to hold the encrypted phrase
        self.encrypted_phrase = ''

        # Use the string and random libraries to create two attributes
        # One is the correct alphabet, another is a shuffled alphabet
        self.original_alphabet = list(string.ascii_lowercase)
        self.rand_alphabet = random.sample(self.original_alphabet, len(self.original_alphabet))
        
    def encryption(self, message):
       
        '''
        INPUT: A string message to be encrypted
        OUTPUT: An encrypted version of the message
        '''


        # Create an empty string for the first phase of encryption
        result = ''


        ########################################################################
        ### STEP 1: ADD RANDOM LETTER AFTER EACH ORIGINAL LETTER IN MESSAGE  ###
        ########################################################################
        for letter in range(len(message)):

            # Append original letter from message to result string
            result += message[letter]
            
            # Append a random letter after each original letter in message string
            result += random.sample(self.original_alphabet, 1)[0]
            

        #################################################
        ### STEP 2: REVERSE THE STRING  ################
        ###############################################
        
        self.encrypted_phrase = result[::-1]


        ##########################################################################
        ##### STEP 3: USE THE RANDOM SHUFFLED ALPHABET FOR A Caeser CIPHER ######
        ########################################################################

        # Cast encrypted phrase into a list and assign it
        encryption_phase_two = list(range(len(self.encrypted_phrase)))

        # Enumerate over encrypted phrase. Check if the letter or character in the message is found in the class's alphabet
        # If the element contains something other than a letter in the alphabet make sure
        # it is part of the encryption process. Assign the orignal alphabet's index to the class's random alphabet
        # in order to encrypt and later decrypt the message

        for i, char in enumerate(self.encrypted_phrase.lower()):

            if char in self.original_alphabet:

                original_index = self.original_alphabet.index(char)
                encryption_phase_two[i] = self.rand_alphabet[original_index]

            else:

                encryption_phase_two[i] = char

        # Join the encrypted phrase and assign it to the encrypted phrase
        # return encrypted phrase
        self.encrypted_phrase = ''.join(encryption_phase_two)
        return self.encrypted_phrase
    

    def decryption(self, message, seed):
        
        '''
        This method takes in a messsage and a seed for the random shuffled alphabet.
        It then returns the decrypted alphabet.
        '''

        # Use the seed argument to create the same pseudo random sequence
        # created in the Encryption class. Create another random sampled
        # alphabet that is local to this method
        random.seed(seed)
        decrypt_rand_alphabet = random.sample(self.original_alphabet, len(self.original_alphabet))

        # Create a variable to hold the message as a list
        # and assign it as a list to a decrypted phrase variable
        decrypted_phrase = list(range(len(message)))

        # Enumerate through the message grabbing the index value
        # for each element as well as the contents of each element
        for i, char in enumerate(message.lower()):

            # Check if the letter or character in the message is found in the class's original alphabet
            if char in self.original_alphabet:
                
                # Assign the orignal alphabet's index to the local random alphabet
                # in order to decrypt the message
                rand_index = decrypt_rand_alphabet.index(char)
                decrypted_phrase[i] = self.original_alphabet[rand_index]

            # If the element contains something other than a letter in the alphabet make sure
            # it is not encrypted.  
            else:
                decrypted_phrase[i] = char
        
        # Join the decrypted phrase list
        decrypted_phrase = ''.join(decrypted_phrase)
        
        # Reverse decrypted phrase and drop every other character
        original_phrase = decrypted_phrase[::-1][::2]

        # Finally return complete decrypted phrase
        return original_phrase.title()


def test_cases():
    message = 'Hello World'
    seed = 20

    print('Original message is: {}\nThe seed value is: {}'.format(message, seed))

    # Create instance of Encryption Class passing in a seed value
    e = Encryption(seed)
    # Assign encrypted message to a new variable
    encrypted_message = e.encryption(message)
    print('\nThe encrypted message is: {}\n'.format(encrypted_message))

    decrypted_message = e.decryption(encrypted_message, seed)
    print('The decrypted message is: {}'.format(decrypted_message))


test_cases()

        
