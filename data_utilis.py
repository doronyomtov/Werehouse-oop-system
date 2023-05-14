import csv


def validate_gender(gender):
    if gender == 'M' or gender == 'F':
        return gender
    else:
        return None


def validate_number(num):
    if isinstance(num, str) and len(num) == 11 and num[0:2] == "05" and num[2].isdigit() and num[
                                                                                             4:].isdigit() is True and \
            num[3] == "-":
        return True
    else:
        return False


def check_employee_list(l1, num):
    if len(l1) > int(num):
        while len(l1) > int(num):
            l1.pop(len(l1) - 1)
    return l1


def read_csv_file(file_name):
    rows = []
    csv_file = open(file_name, 'r', newline='')
    reader = csv.reader(csv_file)
    for row in reader:
        rows.append(row)
    csv_file.close()
    return rows


def validate_id_number(id):
    if id.isdigit() == False or len(id) != 9:
        return False
    sum = 0
    int_id = int(id)//10
    counter = 2
    while int_id >0:
        if counter%2 == 0:
            if int_id%10 >=5:
                current_num = (int_id%10)*2//10 +(int_id%10)*2%10
                sum +=current_num
                counter +=1
                int_id //= 10
            else:
                sum += (int_id % 10)*2
                counter += 1
                int_id //= 10
        else:
            sum += int_id%10
            counter +=1
            int_id //=10
    if int(id[8]) == 0:
        last_num = 0
    else:
        last_num = 10 - int(id[8])
    return sum % 10 == last_num
