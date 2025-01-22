email = input("Enter Your Email:").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"your username is {username} & domain is {domain}")


# strip : remove any leading or trailing spaces from input .
# Ensures that extra spaces around the email address don't cause problems

# 'email.index('@)'
# finds the position (index)of the @ symbol in the email string.
# example if the email is "user@exmaple.com", the @ is at index 4.

# email[:email.index('@')];
# uses slicing to extract all characters from the beginning of the email string up to @
# this is slice becomea the username  

# email.index('@')+1    
# finds the index just after the @ symbol
# if @ symbol at index 4 , email.index('@')+1 is at index is 5

# email[email.index('@')+1:]
# use slicing to extract all characters from just after the @ to end of the string.
# this slice becomes the domain

# f"...":
# this is f-string , used to formate strings dynamically
# the placeholders {username} and {domain} are replaces with their respective variable values