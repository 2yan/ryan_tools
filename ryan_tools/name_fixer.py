def gl(text, loc):
    if loc < 0:
        return ''
    try:
        return text[loc]
    except IndexError:
        return ''
def is_seperator(thing, seperators = [' ','', '.', '\'', '-', '`', '\'']):
    
    if thing in seperators:
        return True
    return False

def capitalize(text, index):
    done_text = ''
    for i, letter in enumerate(text):
        if i in index:
            letter = letter.upper()
        done_text = done_text + letter
    return done_text
            
def vowel(letter):
    if letter.lower() in 'aeiou':
        return True
    return False

def fix_name(text):
    if text.upper() != text and text.lower() != text:
        return text

    text = ' ' + text + ' '
    text = text.lower()
    done_text = ''
    for i,letter in enumerate(text):
        if gl(done_text, i-1) == ' ':
            letter = letter.upper()
        if gl(done_text, i-1) == '.':
            letter = letter.upper()
        if i == 0:
            letter = letter.upper()
            
        if (gl(done_text, i-2) == 'M') and (gl(done_text, i-1) == 'c'):
            letter = letter.upper()
        
        if is_seperator(letter, ['', ' ']) and is_seperator(gl(done_text, i -3)) and not (vowel(gl(done_text, i - 1)) or vowel(gl(done_text, i - 2))): 
            done_text = capitalize(done_text, [i - 1, i - 2])
        
        #if (gl(done_text, i-3) == 'M') and (gl(done_text, i-2) == 'a') and (gl(done_text, i-1) == 'c'):
        #    letter = letter.upper()        
        
        done_text = done_text + letter
    done_text =  done_text[1: len(done_text)]
    return done_text
