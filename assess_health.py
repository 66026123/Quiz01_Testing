def assess_health(fbs, bp):
    if fbs < 100 and bp <= 120:
        group = 'Status'
    elif fbs <= 125 and bp <= 138:
        group = 'Risk'
    elif fbs <= 154 and bp <= 159 :
        group = 'High Risk level 1'
    elif fbs <= 182 and bp <= 160 :
        group = 'High Risk level 2'
    elif fbs <= 183 and bp <= 180:
        group = 'High Risk level 3'
    else:
        group = 'Out of range'

    return group

result = assess_health(fbs, bp)
print(result)
