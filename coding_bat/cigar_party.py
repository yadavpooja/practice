def cigar_part(cigars,weekend):
    if 40 <= cigars <=70: 
        return True
    elif cigars >= 40 and weekend:
        return True
    return False



print cigar_part(30, False)
print cigar_part(50, False)
print cigar_part(70, True)
