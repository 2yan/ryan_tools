import array
import base64




def encode(text, password):
    
    
    encoded = base64.urlsafe_b64encode(text.encode())
    encoded_array = bytearray(encoded)
    
    pointer = get_start_position(password)
    
    done = []
    for i, letter in enumerate(encoded_array):
        position_in_pass = go_round(i, len(password)- 1)
        password_char = password[position_in_pass]
        value = get_start_position(password_char)
        letter = go_round(letter + value, 256)
        pointer = pointer + value
        done.append(letter)
    return list_to_bytes(done).decode()

def decode(text, password):
    
    text = text.encode()
    encoded_array = bytearray(text)
    pointer = get_start_position(password)
    
    done = []
    
    
    for i, letter in enumerate(encoded_array):    
        position_in_pass = go_round(i, len(password)- 1)
        password_char = password[position_in_pass]
        value = get_start_position(password_char)
        letter = go_round(letter - value, 256)
        pointer = pointer + value
        done.append(letter)
        
    decoded = base64.b64decode(list_to_bytes(done)).decode()
    return decoded

def get_positions(letter = None):
    eng_letters = 'qwertyuiopasdfghjklzxcvbnm'
    
    
    letters = eng_letters + eng_letters.upper()
    letters = letters + '1234567890-=][;\'/.,]~!@#$%^&*()_+`'
    positions =  dict(zip(letters,range(1, len(letters))))
    
    if letter == None:
        return positions
    
    return positions[letter]

def get_start_position(text):
    start = 0
    for i, letter in enumerate(text):
        if i%2:
            start = start - get_positions(letter)
        if not i%2:
            start = start + get_positions(letter)
    return start

def go_round(number, maximum):
    if number == 0:
        return 0 
    while True:
        if maximum/number < 1:
            number = number - maximum
        if maximum/number >= 1:
            return number
        
def list_to_bytes(list_o):
    return array.array('B', list_o).tobytes()



