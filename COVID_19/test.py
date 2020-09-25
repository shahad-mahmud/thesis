list = ['#4008 (Pending update)',
        'Age 1 Female',
        'Onset date',
        '-',
        '#4007 (Pending update)',
        'Onset date',
        'Asymptomatic',
        'Confirmed date',
        '-',
        '+',
        '#4006 (Pending update)',
        'Age 65 Female',
        'Onset date',
        '-',
        'Place of residence',
        '-']

new_list = []  # this will be the output list
temp_list = []  # holds sub lists

for item in list:  # iterate on each item in the list
    if item[0] == '#':  # of the list item starts with a #,
        # the previous temp list is a separate group
        new_list.append(temp_list)  # add the previous list in the output list
        temp_list = [item]  # create new group start with the current item
    else:
        temp_list.append(item)
new_list.append(temp_list)  # add the remaining last group

new_list = new_list[1:]  # remove the first group as it is empty
print(new_list)
