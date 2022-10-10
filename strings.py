# Want to give it a go yourself? Be my guest! Modify the first_and_last function
# so that it returns True if the first letter of the string is the same as the last letter of the string,
# False if they’re different. Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    if len(message) == 0 or message[0] == message[-1]:
        return False
    return True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# ***********************************************

word = "supercalifragilisticexpialidocious"
print(word.index('x'))

# **********************************************

pets = 'Cats & Dogs'
print(pets.index('C'))   # 0
print(pets.index('&'))   # 5
print('Cats' in pets)    # True
print('Birds' in pets)   # False

# ***************************************************
# ADVANCED STRING METHODS

# Imagine that your company has recently moved to using a new domain,
# but a lot of the company email addresses are still using the old one.
# You want to write a program that replaces this old domain with the new one in any outdated email addresses.
# The function to replace the domain would look like this.

def replace_domain(email, old_domain, new_domain):
    if '@'+old_domain in email:
        index = email.index('@'+old_domain)
        new_email = email[:index]+'@'+new_domain
        return new_email
    return email

print(replace_domain('ozturkae@gmail.com', 'gmail.com', 'yahoo.com'))

#
print('Forest'.isnumeric())
print('Forest'.endswith('rest'))
print('Forest'.count('e'))
print(' '.join(['This', 'is', 'a', 'string', 'joined', 'by', 'spaces']))
print('...'.join(['This', 'is', 'a', 'string', 'joined', 'by', 'spaces']))

#
# FORMATTING STRINGS

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS

# FORMATTING STRINGS

price = 7.5
with_tax = price*1.09
print(price, with_tax)
print('Best price: ${:.2f}. With tax: ${:.2f}'.format(price, with_tax))

#

def to_celcius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    print(x, to_celcius(x))   # in order to get a cleaner-nicer output, we can use format mothod.

for x in range(0, 101, 10):
    print('{:>3} F | {:>6.2f} C'.format(x, to_celcius(x))) #to align :>3 yani x girdisi 3 rakamlık hizada hizalanacak, diğer girdi ondan 6 space sonrasında hizalanacak

#

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

#"""Outputs:
#apple carrot banana
#"""

# *********************************************************************************

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string.lower():
        letter = letter.strip()
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if letter != ' ':
            new_string = letter + new_string
            reverse_string = reverse_string + letter
    # Compare the strings
    if new_string == reverse_string:
        return True

    return False

print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True

# ************************************************************************
def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rfind(old)    # finds the last string
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"



