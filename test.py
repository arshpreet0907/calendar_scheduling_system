# def show_calendar_user():
    
#     year=1996
#     month=11
    
#     width=78
#     month_names=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
#     month_dates=[  31,   28,   31,   30,   31,   30,   31,   31,   30,   31,   30,   31]

#     if is_leap_year(year):
#         month_dates[1]=29
#     #month name
#     print('-'*width)
#     print('|',end='')
#     month_year=f' {month_names[month-1]} {year}'
#     print(month_year,end='')
#     print(' '*(width-len(month_year)-2),end='')
#     print('|')
#     print('-'*width)
    
#     RED = '\033[91m'
#     RESET = '\033[0m'
#     #week names
#     week_names=['MO','TU','WE','TH','FR','ST','SU']
#     for day in week_names:
        
#         if day==week_names[-1] or day==week_names[-2]:
#             print('|   ',f'{RED}{day}{RESET}','   ',end='')
#         else :
#             print('|   ',day,'   ',end='')
#     print('|')
#     print('-'*width)
    
#     #dates
#     first_day = datetime(year, month, 1)
#     start= first_day.weekday()
#     date=1
#     max_dates=month_dates[month-1]
#     rest=42-start-max_dates+1
    
#     rows=no_of_rows(start,max_dates)
    
#     for _ in range(rows):
#         count=1
#         for _ in range(7):
#             if start>0:
#                 print('|'+' '*10,end='')
#                 start-=1
#             else:
                
#                 start_space=''
#                 if date<10:
#                     start_space+=' '
#                 if count%6==0 or count%7==0:
#                     date_block='|        '+start_space+f'{RED}{date}{RESET}'
#                 else:    
#                     date_block='|        '+start_space+str(date)
#                 date+=1
#                 if date>max_dates:
#                     start=rest
#                 print(date_block,end='')
#             count+=1
#         print('|')
#         print('-'*width)
        
#     print()


# def is_leap_year(year):
#     if year%4==0:
#         if year%400!=0:
#             return False
#         return True
#     return False

# def no_of_rows(start,max_dates):
#     rows=0
#     if max_dates==31:
#         if start>4:
#             rows=6
#         else:
#             rows=5
#     elif max_dates==30:
#         if start>5:
#             rows=6
#         else:
#             rows=5
#     elif max_dates==29:
#         rows=5
#     else :
#         if start==0:
#             rows=4
#         else:
#             rows=5
#     return rows

# #show_calendar_user()










# import json
# from datetime import datetime

# my_datetime = datetime(2023, 10, 27, 10, 30, 0)

# # Serialize using isoformat()
# datetime_str = my_datetime.isoformat()
# print(datetime_str) #Example: 2023-10-27T10:30:00

# # Serialize using strftime() (custom format)
# custom_datetime_str = my_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(custom_datetime_str) # Example: 2023-10-27 10:30:00

# data = {"timestamp": datetime_str} # Or custom_datetime_str
# json_data = json.dumps(data)
# print(json_data)


# import json
# from datetime import datetime, timedelta

# def json_to_datetime(json_data):
#     """Converts datetime strings in JSON to datetime objects."""
#     data = json.loads(json_data)
#     if "start_time" in data:
#         data["start_time"] = datetime.fromisoformat(data["start_time"])
#     if "end_time" in data:
#         data["end_time"] = datetime.fromisoformat(data["end_time"])
#     return data

# # Sample JSON data with datetime strings
# json_data = '{"start_time": "2023-10-27T10:30:00", "end_time": "2023-10-28T12:45:00"}'

# # Deserialize and convert to datetime objects
# data = json_to_datetime(json_data)

# # Perform actions on the datetime objects
# start_time = data["start_time"]
# end_time = data["end_time"]

# time_difference = end_time - start_time
# print(f"Time difference: {time_difference}")

# new_time = start_time + timedelta(hours=3)
# print(f"Start time + 3 hours: {new_time}")

# if start_time < end_time:
#     print("Start time is before end time")
    
    
# time_difference = timedelta(days=2, hours=65, minutes=30, seconds=45)

# # Extract individual components
# days = time_difference.days
# print(time_difference.days)
# print(time_difference.seconds)
# hours = time_difference.seconds // 3600  # Integer division to get hours
# minutes = (time_difference.seconds % 3600) // 60  # Remainder and integer division for minutes
# seconds = time_difference.seconds % 60  # Remainder for seconds

# print(f'''
#     days : {days}
#     hours : {hours}
#     minutes : {minutes}
#     seconds : {seconds}
#     ''')



d={1:'1'}
var=d.get(2,None)
if not var:
    print(1)
else:
    print(2)