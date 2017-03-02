# ryan_tools
Initializes often used libraries and functions.
Is pretty much a convenience package.


## Functions Available:

*mround()*<br />
Helper function for the round function. The only thing different it does is that it defaults to rounding by 2 if no value is provided

*find_column_id( findme, row )*<br />
findme = Word to look for<br />
row = iterable of strings<br />
returns index of 'findme'<br />
-It is Case insensitive<br />

*get_month( datetime )*<br />
Returns The full month name. Same as strftime("%B") but easier to remember

*read_date(text)*<br />
Parses strings and returns datetime values. Warning, Functions american style (mm/dd/yy)

*get_date_str( datetime, sep ='/' )*<br />
Returns a nicely formatted string from a datetime value, useful for producing clean reports. Warning, Functions american style (mm/dd/yy)

*s_s( number, spaces = 8 )*<br />
Left Adjusts a number and adds spaces to allow cleaner printing.

*read_cash( text )*<br />
Cleans and reads accounting style cash strings and returns numbers, removes dollar signs, reads brackets as negative numbers, etc

*get( identity, item_list)*<br />
Given a list of objects with id fields, returns the object that matches the id

*unix_time_millis(dt)*<br />
Takes datetime values and converts them into seconds since epoch

*def print_list(list_of_things):*<br />
Given a list of objects, tries to print them all

*def last_date_of_month(date_time)*<br />
Given a datetime value, gets the last day of the month.
