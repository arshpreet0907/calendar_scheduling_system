

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