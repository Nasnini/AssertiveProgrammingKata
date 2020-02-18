#Assertive Programming
  
# Morse code dictionary storing letters and cipher text
MORSE_CODE_DICTIONARY = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 


# Function to encrypt the text using the morse code dictionary 
def letters_to_morse_code(text): 
    cipher = '' 
    for letter in text: 
        if letter != ' ': 
  
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            cipher += MORSE_CODE_DICTIONARY[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    return cipher 
  
# Function to decrypt the text 
def morse_code_to_letters(text): 
  
    # append space
    # last morse code 
    text += ' '
  
    decipher = '' 
    cypher_text = '' 
    for letter in text: 
  
        # checks if theres space 
        if (letter != ' '): 
  
            # keeps track of space 
            i = 0
  
            # stores morse code  
            cypher_text += letter 
   
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MORSE_CODE_DICTIONARY.keys())[list(MORSE_CODE_DICTIONARY 
                .values()).index(cypher_text)] 
                cypher_text = '' 
  
    return decipher 



# The main function - parsing the 'text' in encrypt and decrypt function 
def main(): 
    print("\n\tThe Morse code translator")
    # Text parse
    text = "Hi there" 
    print("\nThe encrpted code is:")

    result_to_code = letters_to_morse_code(text.upper()) 
    #Assertion to check that the right number of spaces are represented in the output
    assert len(text) !=0, "The number of spaces should be the same"
    print (result_to_code) 
  
    print("\nThe decrpted text is:")
    # Code parsed
    text = ".... ..  - .... . .-. ."
    
    
    result_to_letters = morse_code_to_letters(text)
    # Assertion to check that results to code and result in letters have the same number of characters
    assert result_to_code != result_to_letters, "The text should have the same number of characters"
    print(result_to_letters) 
  
# Executes the main function 
if __name__ == '__main__': 
    main() 