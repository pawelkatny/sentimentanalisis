patterns_list = {
    'emots': r'([\(\)\<\>]?[\-\=]?[\:\;\=B8X\<][\-\=\^\\\/]{1}?[\(\)\<\>\@\$\%\[\]DOoPp3]?|\:\w+\:)|(?=\s|$)',
    'emojis' : u'[\\U0001F1E6-\\U0001F1FF]',
    'http': r'http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    'at': r'\@\S+',
    'hash': r'\#\S+',
    'amp' : r'\&amp;',
    'special_char_one': r'\s+[^a-zA-Z0-9 ]{1}\s+',
    'leftovers': r'\s+[a-zA-Z]\s+',
    'split_pattern': r'\W+',
}