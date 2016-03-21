def make_tags(tag, word):
    
    return ("<%s>%s</%s>" % (tag,word,tag) )


print make_tags('i','yay')
print make_tags('i','hello')
print make_tags('cite','yay')

