# ryan_tools
Initializes often used libraries and functions 


## Functions Available:

#### mround()
Helper function for the round function. The only thing different it does is that it defaults to rounding by 2 if no value is provided

#### find_column_id( findme, row )
findme = Word to look for<br />
row = iterable of strings<br />
returns index of 'findme' <br />
-It is Case insensitive<br />

#### get_month( datetime )
Returns The full month name. Same as strftime("%B") but easier to remember


#### read_date(text)
Parses strings and returns datetime values. American format( Month before day )

#### get_date_str( datetime, sep ='/' )
Returns a nicely formatted string from a datetime value, useful for producing clean reports. American format( Month before day )


