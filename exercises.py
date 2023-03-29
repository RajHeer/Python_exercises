""" Exercises from Codecademy intro to PYTHON2"""
""" Yes... PYTHON2 """

def is_int(x): 
    """ Identify in x is int, including with 'x.0' format"""
    if x - int(x) == 0: 
        return True
    else:
        return False 

def digit_sum(n): 
    """ Sum individual digits of n """
    # Note converting n to str for list() 
    digits = list(str(n)) 
    sum = 0 
    for digit in digits: 
        # Converting back into int for sum 
        sum += int(digit) 
    return sum 

def factorial(x): 
    """ e.g factorial(4) would equal 4 * 3 * 2 * 1 = 24 """ 
    total = 1 
    while x != 0: 
      total *= x 
      x -= 1 
    else: 
      return total 

def is_prime(x): 
    if x <= 0 or x == 1: 
        return False 
    for i in range(2, x): 
        if x % i == 0: 
        return False 
    else: 
        return True 

def reverse(text): 
    """ reverse text string without reversed() or x[::-1] approach """
    chars = list(text) 
    output = "" 
    index = len(text) - 1 
    while index != -1: 
        output += chars[index] 
        index -= 1 
    else: 
       return output 

def anti_vowel(text): 
    """ takes string and returns text with all vowels removed """ 
    chars_list = list(text) 
    output = "" 
    for char in chars_list: 
        if char == "A" or char == "a": 
           next 
        elif char == "E" or char == "e": 
            next 
        elif char == "I" or char == "i": 
            next 
        elif char == "O" or char == "o": 
            next 
        elif char == "U" or char == "u": 
            next 
        else: 
            output += char 
        return output 

""" Dictionary e.g. that would be used for the following def """
score = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,  
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,  
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,  
    "x": 8, "z": 10
} 

def scrabble_score(word): 
    """ Score letters in word using dict above """
    to_score = word.lower() 
    to_score_list = list(to_score) 
    score_sum = 0 
    for letter in to_score_list: 
        score_sum += score[letter] 
    return score_sum 

def censor(text, word): 
    """ take text str and redact given word and letters with *s"""
    word_list = text.split() 
    for index, item in enumerate(word_list): 
        if item == word: 
        word_list[index] = "%s" % ("*" * len(word)) 
    return " ".join(word_list) 

def count(sequence, item): 
    """ Count the number of given item in sequence """
    count = 0 
    for el in sequence: 
        if el == item: 
        count +=1 
    return count 
 
 def purify(sequence): 
    """ Remove all odd numbers from sequence """
    output =[] 
    for item in sequence: 
        if item % 2 == 0: 
        output.append(item) 
    return output 

def product(items): 
    """ Return product of all elements in list """
    total = 1 
    for item in items: 
        total *= item 
    return total 

def remove_duplicates(nums): 
    """ Remove any duplicates in list """
    output = [] 
    for num in nums: 
        if output.count(num) == 0: 
        output.append(num) 
    return output 

def median(sequence): 
    """ Return median - middle value in list with odd number of items, 
    or average between middle two numbers in list with even number items"""
    seq_sorted = sorted(sequence) 
    if len(seq_sorted) % 2 == 1: 
        return seq_sorted[len(seq_sorted) / 2] 
    else:  
        avg = (seq_sorted[len(seq_sorted) / 2 -1 ] \ 
        + seq_sorted[len(seq_sorted) / 2]) / 2.0 
    return avg 
