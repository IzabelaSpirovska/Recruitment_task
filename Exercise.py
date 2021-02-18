# Function which check if user arguments are valid
def check_if_strings_ok(userStrings):
    # Static numbers from issue description
    MAX_NUM_OF_STRING = 5
    NUM_OF_STRINGS = 3
    # Split entered string via one space sign
    splitedStrings = userStrings.split(" ")
    # Check if user inserted 3 strings separated by ony space
    if len(splitedStrings) != NUM_OF_STRINGS:
        print("You entered wrong number of strings! Enter 3 strings!")
        return None
    # Flag which can terminate function execution
    wrongLenFlag = False
    # Check if all entered strings are shorter than 5 signs
    for word in splitedStrings:
        if len(word) > MAX_NUM_OF_STRING:
            print("String \"{}\" is too long. Max length: 5!".format(word))
            wrongLenFlag = True
 
    if wrongLenFlag == True:
        return None
 
    return splitedStrings
# Function which check if entered stings are a anagrams
def are_anagrams(str1, str2, str3):
    # Set all entered strings in one list
    listOfStrings = [str1, str2, str3]
    # Invert all strings and set in new list
    invStrings = [string[::-1] for string in listOfStrings]
    # Compare list before and after inversion
    if listOfStrings == invStrings:
        print("Entered words are a anagrams!")
        return True
 
    else:
        print("Entered words are not a anagrams!")
        return False
 
# Main declaration
if __name__ == "__main__":
 
    print("Hello! Program will check if your three strings are a anagrams.")
    # Get string from user
    getStrings = input("Enter 3 strings separated by one space: ")
    # If user inserted strings go to next operations
    if getStrings:
        # Check if inserted string are valid in check_if_strings_ok function
        userWords = check_if_strings_ok(getStrings)
        # If strings from user are valid go to next operations
        if userWords:
            # Insert user words in another variables, cause function take 3 separated arguments
            string1 = userWords[0]
            string2 = userWords[1]
            string3 = userWords[2]
 
            # Check if entered words are a anagrams
            areAnagrams = are_anagrams(string1, string2, string3)
            # Print result of anagram function
            print("Result of anagram function: {}".format(areAnagrams))
 
    else:
        # If user dont enter any strings
        print("You not entered any strings!")
 
