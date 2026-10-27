"""
Name: (Safia)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ Asks user for letter, checks if it is a single charachter and if it is the right charachter """
    # remove the default return and add your code
    while True:
        letter=input("Give an single uppercase letter: ")
        if len(letter)!=1:
            print("Error: it needs to be a single character.")
            continue
        elif letter not in ("A", "B", "C"):
            print("Error: You provided the wrong character.")
            continue
        else:
            return letter
    


def get_digit():
    """ Asks user for digit, checks if it is a single number charachter and if it is in the right range """
    # remove the default return and add your code
    while True:
        digit=input("Give an single number character: ")
        if not digit.isdigit():
            print("Error: your input should be only digits.")
            continue
        elif digit not in ("1", "2", "3"):
            print("Error: a single digit needs to be in [1,3].")
            continue
        else:
            return digit


def check_pattern(letter, digit, lst):
    """ Checks each charachter in list,if a charachter is a letter it checks the following charachters for digits and if true it prints the word """
    print("Strings with the pattern:")
    for word in lst:
        for i in range(len(word)):
            if word[i]==letter:
                for j in range(i+1, len(word)):
                    if word [j]== digit:
                        print (word)
                break
                        
    
                        
 
        
    # remove the default pass and add your code
    


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""
    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    check_pattern(get_letter(), get_digit(), st_list)
    ans = input("Try Again? (y/n): ")
    while ans == "y":
            check_pattern(get_letter(), get_digit(), st_list)
            ans = input("Try Again? (y/n): ")
    print("The End")
    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    
    

# Do not modify these two lines
if __name__ == "__main__":
    main()