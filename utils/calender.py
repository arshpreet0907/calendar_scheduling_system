from datetime import date,datetime,timedelta
from .data_json import json_to_datetime
from .data_json import get_specific_user_data
from .user_input import month_input
from .user_input import year_input
from .data_json import get_user_credential_data

def last_day_of_month(month,year):
    if month == 12:
        return  date(year+1, 1, 1) - timedelta(days=1)
    else:
        return  date(year, month+1, 1) - timedelta(days=1)

def is_task_in_month(month,year,task):
    task=json_to_datetime(task)
    start=task['task_start_time'].date()
    end=task['task_end_time'].date()

    first_day= date(year, month, 1)
    last_day=last_day_of_month(month,year)
                
    if start <= last_day and first_day <= end:
        return True,start,end
    else :
        return False,start,end

def dates_in_month_year_with_tasks_user(logged_in_id,month,year,task_type):
    dates_in_month_year=set({}) 
    user_data=get_specific_user_data(logged_in_id)
    if task_type=='PERSONAL':
        tasks=user_data['personal_tasks']
    else:
        tasks=user_data['professional_tasks']

    for task in tasks:
        
        task_in_month,start,end=is_task_in_month(month,year,task)
        if task_in_month:
            
            if start.month==month and start.year==year:
                current_date = start
            else:
                date(year,month,1)
            
            if end.month==month and end.year==year:
                end_date=end
            else:
                end_date= last_day_of_month(month,year)  
                
            while current_date <=end_date :
                dates_in_month_year.add(current_date.day)
                current_date=current_date+timedelta(days=1)
    
    return  dates_in_month_year

def dates_in_month_year_with_tasks(logged_in_id,month,year,task_type)->list[int]:
    dates_in_month_year=set({}) #use dictionary to store key and count also need to change add as well as making it blue in calendar
    if logged_in_id!='root':
        dates_in_month_year=dates_in_month_year_with_tasks_user(logged_in_id,month,year,task_type)
        
    else:
        users=get_user_credential_data()
        for user in users:
            dates_in_month_year.add(dates_in_month_year_with_tasks_user(user['user_id'],month,year,'professional_tasks'))
        return dates_in_month_year

def show_calendar(logged_in_id,task_type):
    print(f'\nCALENDER TO SHOW DATES WITH {task_type} TASKS\n')
    today=datetime.now()
    year=year_input(today)
    month=month_input(today,year)

    dates_with_tasks=dates_in_month_year_with_tasks(logged_in_id,month,year,task_type)
    print(f'{task_type} calender for {logged_in_id}')
    width=78
    #month name
    print('-'*width)
    print('|',end='')
    month_year=f' {month_names(month)} {year}'
    print(month_year,end='')
    print(' '*(width-len(month_year)-2),end='')
    print('|')
    print('-'*width)
    
    RED = '\033[91m'
    RESET = '\033[0m'
    
    T_in_W='\033[94m'  #BLUE
    T_in_H='\033[95m'  #MAGENTA
    
    
    #week names
    week_names=['MO','TU','WE','TH','FR','ST','SU']
    for day in week_names:
        
        if day==week_names[-1] or day==week_names[-2]:
            print('|   ',f'{RED}{day}{RESET}','   ',end='')
        else :
            print('|   ',day,'   ',end='')
    print('|')
    print('-'*width)
    
    #dates
    first_day = datetime(year, month, 1)
    start= first_day.weekday()
    date=1
    max_dates=month_dates(month,year)
    rest=42-start-max_dates+1
    
    rows=no_of_rows(start,max_dates)
    
    for _ in range(rows):
        count=1
        for _ in range(7):
            if start>0:
                print('|'+' '*10,end='')
                start-=1
            else:
                start_space=''
                if date<10:
                    start_space+=' '
                if count%6==0 or count%7==0:
                    if date in dates_with_tasks:
                        date_block='|        '+start_space+f'{T_in_H}{date}{RESET}'
                    else:
                        date_block='|        '+start_space+f'{RED}{date}{RESET}'
                else:
                    if date in dates_with_tasks:
                        date_block='|        '+start_space+f'{T_in_W}{date}{RESET}'
                    else:        
                        date_block='|        '+start_space+str(date)
                date+=1
                if date>max_dates:
                    start=rest
                print(date_block,end='')
            count+=1
        print('|')
        print('-'*width)
        
    print()

def month_names(month):
    match month:
        case 1:
            return 'JAN'
        case 2:
            return 'FEB'
        case 3:
            return 'MAR'
        case 4:
            return 'APR'
        case 5:
            return 'MAY'
        case 6:
            return 'JUN'
        case 7:
            return 'JUL'
        case 8:
            return 'AUG'
        case 9:
            return 'SEP'
        case 10:
            return 'OCT'
        case 11:
            return 'NOV'
        case 12:
            return 'DEC'

def month_dates(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month==2:
        if is_leap_year(year):
            return 29
        else:
            return 28

def is_leap_year(year):
    if year%4==0:
        if year%400!=0:
            return False
        return True
    return False

def no_of_rows(start,max_dates):
    rows=0
    if max_dates==31:
        if start>4:
            rows=6
        else:
            rows=5
    elif max_dates==30:
        if start>5:
            rows=6
        else:
            rows=5
    elif max_dates==29:
        rows=5
    else :
        if start==0:
            rows=4
        else:
            rows=5
    return rows


# RED = '\033[91m'
# GREEN = '\033[92m'
# YELLOW = '\033[93m'
# BLUE = '\033[94m'
# MAGENTA = '\033[95m'
# CYAN = '\033[96m'
# RESET = '\033[0m'  # Resets color to default
# # Example usage
# print(f"{RED}This text is red!{RESET}")
# print(f"{GREEN}This text is green!{RESET}")
# print(f"{BLUE}This text is blue!{RESET}")

# from colorama import init, Fore, Back, Style

# # Initialize colorama
# init()

# # Print colored text
# print(Fore.RED + "This text is red!")
# print(Fore.GREEN + "This text is green!")
# print(Back.BLUE + "This has a blue background!")
# print(Style.BRIGHT + "This text is bright!")

# # Reset all colors/styles
# print(Style.RESET_ALL + "Back to normal text")