# Mask Py by Sam v 1.0
# Apply Mask to string

def strmask(value , mask , regexreplace="[^0-9]" , debugenable=False):
    """
        keymask(value , mask , regexreplace="[^0-9]" , debugenable=False)
        the chars # be replaced
        Ex.
            Mask    (###) ###.###.###
            Digited 123456789123
            Masked  (123) 456.789.123
        Enjoy ;)
    """

    import re
    if re.match(r"[\b]", value[-1:]) :
        return value[0:-1]

    if len( value ) > len( mask ):
        return value[0:-2]

    if debugenable:
        print 'value unmasked: ' + value

    value = re.sub( regexreplace , "" , value )

    if debugenable:
        print 'value replaced: ' + value

    n = 0
    masked = ''
    if debugenable:
        print 'init masked: ' + masked

    for cm in mask:
        if cm != '#':
            masked += cm
            if debugenable:
                print 'masked + char: ' + masked
        else:
            if n < (len( value ) - 1 ) :
                masked += value[n:n + 1]
                n += 1
                if debugenable:
                    print 'masked + char mask: ' + masked
            else:
                break


    if debugenable:
        print 'end masked: ' + masked
    return masked

