# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/easy/text-formatting
import re
import string
intext = input()

def fixme(text: str):
    textArr = [char for char in text]
    result = []
    needs_capital = True
    
    for ind, char in enumerate(textArr):
        if ind == 0:
            if char in string.ascii_letters:
                result.append(char.capitalize())
                needs_capital =  False
        else:
            if char in string.punctuation:
                if char == '.':
                    needs_capital = True

                if result[-1] == ' ':
                    result.pop()

                if result[-1] == char:
                    continue
                  
                result.append(char)

            elif char == ' ':
                if result[-1] == ' ':
                    continue
                else:
                    result.append(char)
            else:
                if result[-1] in string.punctuation:
                    result.append(' ')

                if needs_capital:
                    result.append(char.capitalize())
                    needs_capital = False
                else:
                    result.append(char.lower())

    return "".join(char for char in result)

def correct_text(text):

    texxt = text.lower()
    # Step 1: Remove repeated punctuation marks
    pattern_repeated_punc = r'([{}])\1+'.format(re.escape(string.punctuation))
    text = re.sub(pattern_repeated_punc, r'\1', text)
    
    # Step 2: Remove spaces preceding punctuation
    pattern_preceding = r'\s([{}])'.format(re.escape(string.punctuation))
    text = re.sub(pattern_preceding, r'\1', text)
    
    # Step 3: Ensure a space follows each punctuation, except the last one
    pattern_following = r'([{}])(?!\s|$)'.format(re.escape(string.punctuation))
    text = re.sub(pattern_following, r'\1 ', text)
    
    # Step 4: Capitalize the first letter of each sentence
    pattern_capitalize = r'(?<=[.!?]\s)(\w)'
    text = re.sub(pattern_capitalize, lambda match: match.group(0).upper(), text)
    
    # Step 5: Capitalize the first letter of the text itself
    text = text.strip()  # Remove leading/trailing spaces
    text = text[0].upper() + text[1:]
    
    # Step 6: Remove excess spaces between words
    text = ' '.join(text.split())
    
    return text


print(fixme(intext))
