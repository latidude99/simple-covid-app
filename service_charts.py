from update import Update
import service

FIRST_SUN = 2 # first saturday record
REPEAT = 7 # week


def get_back_colours_bar(FIRST_SUN, REPEAT):
    count = 0
    colours = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[0]:
        if count % REPEAT == FIRST_SUN:
            colours.append('rgba(54, 162, 235, 0.2)')
            count += 1
        else:
            colours.append('rgba(0, 0, 0, 0.1)')
            count += 1
    return colours


def get_border_colours_bar(FIRST_SUN, REPEAT):
    count = 0
    colours = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[0]:
        if count % REPEAT == FIRST_SUN:
            colours.append('rgba(54, 162, 235, 1)')
            count += 1
        else:
            colours.append('rgba(0, 0, 0, 0.1)')
            count += 1
    return colours


def get_labels_uk():
    labels = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[0]:
        labels.append(d.date)
    return labels


# new cases -------------------------------------

def get_values_uk_new_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[0]:
        val = d.new_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_en_new_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[1]:
        val = d.new_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_sco_new_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[2]:
        val = d.new_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values

def get_values_wa_new_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[3]:
        val = d.new_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_ni_new_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[4]:
        val = d.new_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


# total cases -------------------------------------

def get_values_uk_total_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[0]:
        val = d.total_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_en_total_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[1]:
        val = d.total_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_sco_total_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[2]:
        val = d.total_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_wa_total_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[3]:
        val = d.total_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_ni_total_cases():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[4]:
        val = d.total_cases
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values

# new deaths -------------------------------------

def get_values_uk_new_deaths():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[0]:
        val = d.new_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_en_new_deaths():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[1]:
        val = d.new_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_sco_new_deaths():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[2]:
        val = d.new_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_wa_new_deaths():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[3]:
        val = d.new_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_ni_new_deaths():
    values = []
    if Update.data_obj_list == '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[4]:
        val = d.new_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values

# total deaths -------------------------------------

def get_values_uk_total_deaths():
    values = []
    if Update.data_obj_list== '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[0]:
        val = d.total_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_en_total_deaths():
    values = []
    if Update.data_obj_list== '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[1]:
        val = d.total_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_sco_total_deaths():
    values = []
    if Update.data_obj_list== '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[2]:
        val = d.total_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_wa_total_deaths():
    values = []
    if Update.data_obj_list== '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[3]:
        val = d.total_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values


def get_values_ni_total_deaths():
    values = []
    if Update.data_obj_list== '':
        data_uk = service.get_nations_data()
    else:
        data_uk = Update.data_obj_list
    for d in data_uk[4]:
        val = d.total_deaths
        if val == 'no data':
            val = '0'
        values.append(int(val))
    return values

def get_colors_uk():
    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
    return colors

