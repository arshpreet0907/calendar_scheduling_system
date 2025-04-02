import maskpass
from datetime import datetime


def custom_input(message):
    print(message,end='')
    while True:
        try:
            user_input=input()
            return user_input
        except BaseException as e:pass
    
def int_input(message):
    input=0
    input_flag=True
    while input_flag:
        try:
            input=int(custom_input(message))
            input_flag=False
        except ValueError :
            print('input should be an integer')
    return input

def float_input(message):
    input=0
    input_flag=True
    while input_flag:
        try:
            input=float(custom_input(message))
            input_flag=False
        except ValueError :
            print('input should always be a float')
    return input

def password_input(prompt,check_valid=False):
    password=''
    pass_flag=True
    while pass_flag:
        try:
            if check_valid:
                print(
                '''
    password should be as follows : 
    at least 12 character long
    at least one upper case letter
    at least one lower case letter
    at least one numeric digit
    at least one special character (!,@,#,$,%,^,&,*,(,),-,_,+,=)
    ''')
            password=maskpass.advpass(prompt,mask='*')
            if password=='0':
                return '0'
            password_is_valid=True
            if check_valid:
                password_is_valid=is_valid_password(password)
            
            if password_is_valid:
                pass_flag=False
            
        except Exception :
            pass
    return password

def is_valid_password(password):
    
    is_valid_password=False
    if len(password)>=12:
        has_digit=False
        has_uppercase=False
        has_lowercase=False
        has_special_char=False
        valid_special_char=["!","@","#","$","%","^","&","*","(",")","-","_","+","="]
        
        for index_char in password:
            if index_char.isdigit():
                has_digit=True
            elif index_char.isupper():
                has_uppercase=True
            elif index_char.islower():
                has_lowercase=True
            elif index_char in valid_special_char:
                has_special_char=True
            if(has_digit and has_lowercase and has_uppercase and has_special_char):
                is_valid_password=True
                break
        if(is_valid_password):
            return True
    return False

def phone_number_input(message):
    phone_number_flag=True
    while phone_number_flag:
        phone_number=custom_input(message)
        if not phone_number.isdigit():
            print('Phone number can only have digits 0-9')
        if len(phone_number)!=10:
            print('Phone number should be 10 digits long')
        else:
            return int(phone_number)
   
def email_address_input(message):
    email_flag=True
    while email_flag:
        curr_email=custom_input(message)
        if is_valid_email(curr_email):
            email_flag=False
            return curr_email
        else :
            print('invalid email')
            
def is_valid_email(email):
    if not isinstance(email, str):
        return False
    
    # Check for exactly one @ symbol
    if email.count("@") != 1:
        return False
    
    # Split the email into local and domain parts
    local_part, domain = email.split("@")
    
    # Validate local part
    if len(local_part) == 0 or len(local_part) > 64:
        return False
    
    if local_part[0] == "." or local_part[-1] == ".":
        return False
    
    valid_special_chars = ["_", "-", "."]
    prev_char = ""
    for char in local_part:
        if prev_char == "." and char == ".":
            return False
        if not char.isalnum() and char not in valid_special_chars:
            return False
        prev_char = char
    
    # Validate domain
    if len(domain) == 0 or len(domain) > 255:
        return False
    
    if domain.count(".") < 1:
        return False
    
    if domain[0] == "-" or domain[-1] == "-":
        return False
    
    # Check for consecutive dots in domain
    prev_char = ""
    for char in domain:
        if prev_char == "." and char == ".":
            return False
        if not char.isalnum() and char not in ["-", "."]:
            return False
        prev_char = char
    
    # Check TLD length (last part after dot)
    if len(domain.split('.')[-1]) < 2:
        return False
    
    return True

def address_input(message):
    # here the user has to input entire thing every time improve it
    print(message)
    print('Enter the following :')
    house_or_locality=custom_input('Enter your house or locality : ')
    street_name_or_landmark=custom_input('Enter street name or landmark : ')
    city=custom_input('Enter city(village block city) : ')
    pin_code=custom_input('Enter pin code : ')
    state=custom_input('Enter state : ')
    
    address={'house_or_locality':house_or_locality,'street_name_or_landmark':street_name_or_landmark,'city':city,'pin_code':pin_code,'state':state}
    address_str=house_or_locality+' '+street_name_or_landmark+' '+city+' '+pin_code+' '+state
    return address,address_str
    #try returning dictionary for each field for individual corrections
    
def year_input(today):
    year=0
    year_flag=True
    while year_flag:
        year=int_input('Enter year : \n-1 for current year : \n0 to exit : ')
        if year==0:
            return '0'
        elif year==-1:
            year=today.year
            break
        elif year<today.year:
            print('it cannot be a year from past')
        elif year>2100:
            print('year too much in future (limit is 2100)')
        else:
            year_flag=False
    return year

def month_input(today,year):
    
    month=0
    month_flag=True        
        
    while month_flag:
        month=int_input('Enter month : \n-1 for current month : \n0 to exit : ')
        if month==0:
            return '0'
        elif month==-1:
            month=today.month
            break
        elif 0<month<today.month and year==today.year:
            print('it cannot be a month from past')
        elif not (13>month>0):
            print('month can only be from 1 to 12')
        else :
            month_flag=False
    return month
    
def date_input(today,month,year):
    date=0
       
    date_flag=True    
    while date_flag:
        date=int_input('Enter date : \n-1 for current date : \n0 to exit : ')
        if date==0:
            return '0'
        if date==-1:
            date=today.day
            break
        elif 0<date<today.day and month==today.month and year==today.year:
            print('it cannot be a date from past')
        elif not is_valid_date(date,month,year):
            print('please enter a valid date')
        else:
            date_flag=False
    return date
    
def hour_input(today,date,month,year):
    hour=0
        
    hour_flag=True  
    while hour_flag:
        hour=int_input('Enter hour(24 hour) : \n-1 for current hour : \n-2 to exit : ')
        if hour==-2:
            return '0'
        elif hour==-1:
            hour=today.hour
            break
        elif not (24>hour>=0) :
            print('Invalid hour input(keep hour between 0 and 23)')
        elif hour<today.hour and date==today.date and month==today.month and year==today.year:
            print('it cannot be a hour from past')
        else:
            hour_flag=False
    return hour
    
def minute_input(today,hour,date,month,year):
    minute=0
    minute_flag=True  
    while minute_flag:
        minute=int_input('Enter minute : \n-1 for current minute : \n-2 to exit : ')
        if minute==-2:
            return '0'
        elif minute==-1:
            minute=today.minute
            break
        elif not (60>minute>=0) :
            print('Invalid minute input(keep minutes between 0 and 59)')
        elif minute<today.minute and hour==today.hour and date==today.date and month==today.month and year==today.year:
            print('it cannot be a minute from past')
        else:
            minute_flag=False
    return minute

def time_input(message):
    
    today = datetime.now()
    print(message)

    year=year_input(today)
    if year=='0':
        return year
    
    month=month_input(today,year)
    if month=='0':
        return month
    
    date=date_input(today,month,year)
    if date=='0':
        return date
    
    hour=hour_input(today,date,month,year)
    if hour=='0':
        return hour
    
    minute=minute_input(today,hour,date,month,year)
    if minute=='0':
        return minute
    
    return  datetime(year, month, date, hour, minute)
        
def is_valid_date(date,month,year):
    if month in [1,3,5,7,8,10,12]:
        return 0<date <32
    elif month in [4,6,9,11]:
        return 0<date<31
    elif month==2:
        if is_leap_year(year):
            return 0<date<30
        else :
            return 0<date<29
    else:
        return False

def is_leap_year(year):
    if year%4==0:
        if year%400!=0:
            return False
        return True
    return False

def task_name_input():
    task_name=''
    task_name_choice=''
    while task_name_choice!='1':
        task_name=custom_input('Please enter new task name : ')
        #make task name unique
        task_name_choice=custom_input(f'Provided task name : {task_name} \nEnter 1 to confirm : \n0 to exit : \nelse to go again: ')
        if task_name_choice=='0':
            return '0'
    return task_name

def task_description_input():
    task_description=''
    task_description_choice=''
    while task_description_choice!='1':
        task_description=custom_input('Please new task description : ')

        task_description_choice=custom_input(f'Provided task description : {task_description} \nEnter 1 to confirm : \n0 to exit : \nelse to go again : ')
        if task_description_choice=='0':
            return '0'
    return task_description

def task_start_time_input():
    task_start_time=''
    task_start_time_choice=''
    while task_start_time_choice!='1':
        task_start_time=time_input('Please enter new task start time : ')
        if task_start_time=='0':
            return '0'
        task_start_time_choice=custom_input(f'Provided task start time : {task_start_time} \nEnter 1 to confirm : \n0 to exit : \nelse to go again: ')
        if task_start_time_choice=='0':
            return '0'
    return task_start_time

def task_end_time_input(task_start_time):
    task_end_time=''
    task_end_time_choice=''
    while task_end_time_choice!='1':
        task_end_time=time_input('Please enter new task end time : ')
        if task_end_time=='0':
            return '0'
        elif task_end_time<task_start_time:
            print('end time cannot be before start time')
        else:
            task_end_time_choice=custom_input(f'Provided task end time : {task_end_time} \nEnter 1 to confirm : \n0 to exit : \nelse to go again : ')
        if task_end_time_choice=='0':
            return  '0'
    return task_end_time

def task_priority_input():
    task_priority=0
    task_priority_choice=''
    task_priority_flag=True
    while task_priority_choice!='1':
        if task_priority_flag: 
            print('Task priority should be in range 1 to 10(10 being highest priority)')
            task_priority_flag=False
        task_priority=int_input('Please enter new task priority : ')
        if not (0<task_priority<11):
            print('Enter valid priority ')
        else:
            task_priority_choice=custom_input(f'Provided task priority : {task_priority} \nEnter 1 to confirm : \n0 to exit : \nelse to go again : ')
            if task_priority_choice=='0':
                return '0'
    return task_priority

def task_team_input():
    task_team=''
    task_team_flag=True
    while task_team_flag:
        task_team=custom_input('Please enter new task name : ')
        task_team_choice=custom_input(f'Provided task team : {task_team} \nEnter 1 to confirm : \n0 to exit : \nelse to go again: ')
        if task_team_choice=='1':
            task_team_flag=False
        elif task_team_choice=='0':
            return task_team_choice
        
    return task_team

def edit_task_input(key):
    match key:
        case 'task_name':
            return task_name_input() 
        case 'task_description':
            return task_description_input()
        case 'task_start_time':
            return task_start_time_input()
        case 'task_end_time':
            return task_end_time_input()
        case 'task_priority':
            return task_priority_input()