import pandas as pd
import numpy as np
import datetime

from dateutil.parser import parse as date_parse
import calendar
from .name_fixer import fix_human_name
import ryan_tools.wrangler as wrangler
import time

def mround( number, by = 2 ):
    return round( number, by )

def get_str_index(findme , string_list ):
    'Finds the the i-th index of your findme string in a string list.'
    iterator = 0
    while ( iterator < len(string_list) ):
        if  (findme.lower() in string_list[iterator].lower()) :
            return iterator
        iterator = iterator + 1
    return False

def get_index(findme, whatever_list ):
    'Finds the the i-th index of your findme in a list uses == operator.'
    iterator = 0
    while ( iterator < len(whatever_list) ):
        if  findme == whatever_list[iterator]:
            return iterator
        iterator = iterator + 1
    return False

    
def get_month( datetime):
    'Returns Month name'
    return datetime.strftime("%B")

        
def read_date(text):
    'You should probably just use pd.to_datetime() but on very rare occasions this works better Whaddaya know '
    text = text.strip('\'')
    text = text.strip('\"')
    for fmt in ( '%m/%d/%y' , '%M/%D/%y' , '%m/%d/%Y', '%Y/%m/%d', '%Y/%M/%D', 'Report Date :%m/%d/%Y', '%Y%M%D' , '%Y%m%d', '%M/%D/%y %H:%M:%S %p', '%m/%d/%Y %H:%M:%S %p'):
        try:
            return datetime.datetime.strptime(text, fmt)
        except ValueError:
            return date_parse(text)            
            pass
    raise ValueError('No Valid Date found in :' + str(text))


def get_date_str(date, sep ='/'):
    'Gets a string from a datetime, great for slapping at the top right corner of reports'
    try:
        return str(date.month) + sep + str(date.day) + sep + str(date.year)
    except AttributeError:
        return get_date_str(read_date(date), sep )

def s_s( number, spaces = 8 ):
    'For prettier printing, I almost never use this, you probably never need to'
    return ( str(number).ljust(spaces) )

def read_cash(text):
    'Reads Accounting format cash ( $ only as of yet)'
    text = str(text)
    if text == '':
        return 0
    temp = text.replace(' ', '')
    temp = text.replace(',', '')
    temp = temp.replace('$', '')

    if ('(' in temp or ')' in temp):
        temp = temp.replace('(', '')
        temp = temp.replace(')', '')
        ans = float(temp) * -1.0
        return ans
    ans = round(float(temp),2)
                
    return ans

def get( identity, item_list  ):
    '''If you have tiems with ID's it will return the item for the corresponding ID'''
    for items in item_list:
        if items.id == identity:
            return items
        
def unix_time_millis(dt):
    'Takes a datetime, returns unix time'
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

def print_list(list_of_things):
    'it will print your list items one by one. '
    try:
        for items in list_of_things:
            items.print()
        return
    except AttributeError:
        for items in list_of_things:
            print(items)
            
def sql_date( date_time ):
    'Converts Datetime to sql date function '
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

def last_date_of_month(date_time):
    'Give it a datetime, and it will shove out the last second of the month  )'
    last = calendar.monthrange( date_time.year, date_time.month)[1]
    return datetime.datetime(date_time.year, date_time.month, last, 23, 59, 59, 999999 )

def load_quickbooks(filename):       
    data = pd.read_csv(filename)
    for column in data.columns:
        if 'Unnamed' in column:
            data[column] = data[column].ffill()
        if all(data[column].isnull()):
            del data[column]
            
    data = data[~data['Date'].isnull()]
    
    data['Date'] = pd.to_datetime(data["Date"])
    
    for thing in ['Debit', 'Credit', 'Balance']:
        data[thing] = data[thing].apply(read_cash)
        
    data['cash'] = data['Debit'] - data['Credit']
    
    data.columns = data.columns.map(lambda x: x.replace('Unnamed: ', 'A'))

    
    
    for column in data.columns:
        if all(data[column].isnull()):
            del data[column]   
            
        
    return data





class progress_bar():
    bar_pos = 0
    left = None
    i = 0
    stepsize = None
    estimates = []
    last_time = None
    last_bar = ''
    def __init__(self, to_do, stepsize = 1):
        self.left = to_do
        self.stepsize = stepsize
        self.last_time = time.time()
        
    def progress(self):
        i = self.i
        bar_pos = self.bar_pos
        left = self.left
        
        if not i%self.stepsize:
            now = time.time()
            difference = now - self.last_time
            self.last_time = now
            difference = difference/self.stepsize
            self.estimates.append(difference)
            
            bar_pos = bar_pos + 1
            power_of_one_dot = 100/left
            pos = int(power_of_one_dot * i)
            bar = ''

            for num in range(0, pos -1 ):
                if (num + bar_pos) %2 == 0:
                    bar = bar + 'o'
                if (num + bar_pos) %2 != 0:
                    bar = bar + '0'             
            bar = bar + '>'
            for num in range(0, 100 - pos):
                bar = bar + ' '
            bar = bar + '| {:.2f} % \nDone: {} Remaining: {}, Remaining Time: {:.0f}s'.format(
                    100 * i/(left -1),
                    i, left - i, np.mean(self.estimates) * (self.left - i) )
            self.i = i + 1
            self.last_bar = bar
            return bar
  
        self.i = i + 1
        return self.last_bar
