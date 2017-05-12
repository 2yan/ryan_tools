import pandas as pd
import numpy as np
import seaborn as sea
import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse as date_parse
import csv
import calendar

def mround( number, by = 2 ):
    return round( number, by )

def get_str_index(findme , string_list ):
    #Finds the the i-th index of your findme string in a string list.
    iterator = 0
    while ( iterator < len(string_list) ):
        if  (findme.lower() in string_list[iterator].lower()) :
            return iterator
        iterator = iterator + 1
    return False

def get_index(findme, whatever_list ):
    #Finds the the i-th index of your findme in a list uses == operator. 
    iterator = 0
    while ( iterator < len(whatever_list) ):
        if  findme == whatever_list[iterator]:
            return iterator
        iterator = iterator + 1
    return False

def rearrange_dataframe_columns(dataframe, order):
    #Takes a dataframe and a column order, the column order is litteraly the column names ordered correctly
    #IF you want to have it reversed, used python's built in reversed() function on <order>
    result = dataframe.copy()
    for column in result.columns:
        del result[column]
    for column in order:
        result[column] = dataframe[column]
    return result
    
def get_month( datetime):
    return datetime.strftime("%B")

        
def read_date(text):
    #You should probably just use pd.to_datetime() but sometimes this works better Whaddaya know 
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
    #Gets a string from a datetime, great for slapping at the top right corner of reports
    try:
        return str(date.month) + sep + str(date.day) + sep + str(date.year)
    except AttributeError:
        return get_date_str(read_date(date), sep )

def s_s( number, spaces = 8 ):
    #For prettier printing
    return ( str(number).ljust(spaces) )

def read_cash(text):
    #Reads Accounting format cash ( $ only as of yet)
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
    #If you have tiems with ID's it will return the item for the corresponding ID
    for items in item_list:
        if items.id == identity:
            return items
        
def unix_time_millis(dt):
    #Takes a datetime, returns unix time
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

def print_list(list_of_things):
    #it will print your list items one by one. 
    try:
        for items in list_of_things:
            items.print()
        return
    except AttributeError:
        for items in list_of_things:
            print(items)
            
def sql_date( date_time ):
    #Converts Datetime to sql date function 
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

def last_date_of_month(date_time):
    #Give it a datetime, and it will shove out the last second of the month  )
    last = calendar.monthrange( date_time.year, date_time.month)[1]
    return datetime.datetime(date_time.year, date_time.month, last, 23, 59, 59, 999999 )

def make_a_wordcloud( string = None, frequencies = None):
    #You need wordcloud installed (pip install wordcloud)
    #You can either give it a string (First argument)  or a dataframe.value_counts() object (Second Argument) 
    from wordcloud import WordCloud
    if type(frequencies) != type(None):
        x = WordCloud(width=1920, height=1080).generate_from_frequencies(frequencies)
    if (string != None) and type(frequencies) == type(None):
        x = WordCloud(width=1920, height=1080).generate_from_text(string)
    result = sea.plt.imshow(x, interpolation='bilinear')
    sea.plt.axis("off")
    return result
