#Sample python code that depicts the usage of bcrypt function  for hashing of the specified input text   
  
# Importing the required libraries that will be used across the code.  
import bcrypt  
import sys  
  
#We have written a class that will be used for the encryption of the specified input text there are two functions in this class one is the Constructor and another is the actual function that will perform the actual hashing of the specified input string   
class NirnayEncryptor:  
      
    # This is the constructor function in which we have initialized the class variables with the input string taken from the users and this input string is used for hashing   
    def __init__(self,string_to_encrypt):  
        self.string_to_encrypt = "{}".format(string_to_encrypt)  
        self.string_to_encrypt = self.string_to_encrypt.encode('utf-8')  
  
    #This is the actual function which is going to perform the hashing operation on the specified input string taken as input in the previous step there is one parameter to this function that is number of rounds this variable represents the number of rounds that we want to use while hashing our input string by default the value of number of rounds variable is 16 but we can change this value by passing the actual value as parameters while calling this function   
    def encrypt_the_string(self,number_of_rounds=16):  
        salt_object = bcrypt.gensalt(rounds=number_of_rounds)  
        resultant_hashed_str = bcrypt.hashpw(self.string_to_encrypt, salt_object)  
        print("The encrypted text or password is: {}".format(resultant_hashed_str))  
        return resultant_hashed_str  
  
  
#We have written a class that will be used for the decryption of the specified input text there are two functions in this class one is the Constructor and another is the actual function that will perform the actual hashing of the specified input string   
class NirnayDecryptor:  
  
        # This is the constructor function in which we have initialized the class variables with the input string taken from the users and this input string is used for hashing   
    def __init__(self,str_to_decrypt):  
        self.str_to_decrypt = "{}".format(str_to_decrypt)  
        self.str_to_decrypt = self.str_to_decrypt.encode('utf-8')  
  
    # This is a function that actually decrypts the hashed string and compares the value of the decrypted string with the actual string and Returns a Boolean value  if the match is successful and both the encrypted and the decrypted strings are matching then the return type of this function is true on the other hand if the encrypt and decrypt strings are not matching the return type of this function will be false  there is one parameter to this function that is the number of rounds this variable represents the number of rounds that we want to use while hashing our input string by default the value of the number of rounds variable is 16 but we can change this value bypassing the actual value as parameters while calling this function  
    def decrypt_the_string(self,number_of_rounds=16):  
        salt_object = bcrypt.gensalt(rounds=number_of_rounds)  
        resultant_hashed_str = bcrypt.hashpw(self.str_to_decrypt, salt_object)  
        if bcrypt.checkpw(self.str_to_decrypt, resultant_hashed_str):  
            return True  
        else:  
            return False  
  
#This is the main function which is called to create the objects of both the above-written classes to perform the encryption and decryption on the specified input string   
def main():  
  
    while(True):  
        print("Please choose one of the appropriate option::")  
        print("1. To enter a string and print the resultant hashed string for it using bcrypt.")  
        print("2. To enter a string and check is it matching with the hashed password or not using bcrypt.")  
        print("3. To exit from the code execution.")  
        menu_choice = input()  
        menu_choice = int(menu_choice)  
  
          
        # For the encryption of the string first of all the string to be encrypted is taken as input from the user once we have the input string we create the the object of the encryption class and call the encrypt_the_string fucntion with the help of this created object of the NirnayEncryptor class  
        if menu_choice == 1:  
            print(">Enter the string that you want to convert to the hashed string::")  
            input_str = input()  
            encryptor = NirnayEncryptor(input_str)  
            encryptor.encrypt_the_string()  
  
                      ## For the encryption of the string first of all the string to be decrypted is taken as input from the user once we have the input string we create the the object of the encryption class and call the decrypt_the_stringfucntion with the help of this created object of the NirnayDecryptor class  
        elif menu_choice == 2:  
            print(">Enter the string that you want to check against hashed string::")  
            input_str = input()  
            decryptor = NirnayDecryptor(input_str)  
            comparison_result = decryptor.decrypt_the_string()  
            if comparison_result == True:  
                print("The entered string has matched successfully with the hashed password/string.")  
            else:  
                print("The entered string has not matched with the hashed password/string.")  
          
        print("Do you want to continue or exit the code execution?[y/n]")  
        continue_or_exit = input()  
  
        #After the completion of one round a question is prompted to the user asking whether you want to continue the code execution or you want to exit the code depending upon the input provided by the user further actions are taken if the user wants to continue the code execution and perform further operations related to encryption and decryption of the string the code is continued whereas on the other hand if the user wants to exit the code execution the exit function is called and the program is ended  
          
                      if continue_or_exit == 'y' or continue_or_exit == 'Y':  
            pass  
        elif continue_or_exit == 'n' or continue_or_exit == 'N':  
            sys.exit()  
  
#In the end for the execution of program the main function is called that has the steps for the encryption and decryption on the specified input string   
if __name__ == '__main__':  
    main()  