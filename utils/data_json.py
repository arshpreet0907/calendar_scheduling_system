import json
import os
from datetime import timedelta,datetime
from .file_path import get_user_credential_file_path
from .file_path import get_pending_request_file_path
from .file_path import get_admin_credential_file_path
from .file_path import get_user_data_file_path

def fetch_file_data(file_path):
    """Loads user data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data if data else {}  # Return the dictionary or an empty one
    except Exception as e:
        print(e)
        return {}

def update_file_data(file_path,new_data):
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        data.append(new_data)

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        print(e)
        return False
    else :
        return True
        
def overwrite_file_data(file_path,new_data):
    
    try:
        with open(file_path, 'w') as f:
            json.dump(new_data, f, indent=4)

    except Exception as e:
        print(e)
        return False
    else :
        return True        

def get_user_credential_data():
    file_path=get_user_credential_file_path()
    return fetch_file_data(file_path)

def get_pending_request_data():
    file_path=get_pending_request_file_path()
    return fetch_file_data(file_path)

def put_pending_request_data(data:tuple[str,str]):
    file_path=get_pending_request_file_path()
    new_data={'user_name':data[0],'password':data[1],'status':'requested'}
    return update_file_data(file_path,new_data)
    
def update_pending_request_data(user_credential_data):
    file_path=get_pending_request_file_path()
    return overwrite_file_data(file_path,user_credential_data)
    
def get_admin_credential_data():
    file_path=get_admin_credential_file_path()
    return fetch_file_data(file_path)

def put_new_user_credential_data(user):
    user_credential_data=get_user_credential_data()
    new_user_id=user_credential_data[-1]['user_id']+1
    user_credential_data.append({'user_id':new_user_id,'user_name':user['user_name'],'password':user['password']})
    file_path=get_user_credential_file_path()
    overwrite_file_data(file_path,user_credential_data)
    return user_credential_data[-1]

def put_admin_credential_data(admin_credential_data):
    file_path=get_admin_credential_file_path()
    return overwrite_file_data(file_path,admin_credential_data)
    
def put_user_credential_data(user_credential_data):
    file_path=get_user_credential_file_path()
    return overwrite_file_data(file_path,user_credential_data)

def update_user_json_file(user_data={},user_id_given=0):
    user_credential_data=get_user_credential_data()
    
    if user_id_given==0 and user_data=={}:
        for user in user_credential_data:
            user_id=user['user_id']
            file_path=get_user_data_file_path(user_id)
            if not os.path.exists(file_path):
                user_data = {
                    'user_id': user_id,
                    'user_name': user['user_name'],
                    'personal_tasks': [],
                    'professional_tasks': [],
                    'phone_number': 0,
                    'email_id': '',
                    'address': '',
                    'teams': [],
                    "messages":[]
                }
            else:
                user_data=get_specific_user_data(user_id)
            return overwrite_file_data(file_path,user_data)
    elif  user_id_given!=0 and user_data!={}:
        return overwrite_file_data(get_user_data_file_path(user_id_given),user_data)
    else:
        print('Please provide valid user data')
            
def get_specific_user_data(logged_in_user_id):
    file_path= get_user_data_file_path(logged_in_user_id)
    return fetch_file_data(file_path)

def put_specific_user_data(user_data):
    user_id=user_data['user_id']
    file_path=get_user_data_file_path(user_id)
    
    return overwrite_file_data(file_path,user_data)

def json_to_datetime(task):
    if "task_start_time" in task:
        task["task_start_time"] = datetime.fromisoformat(task["task_start_time"])
    if "task_end_time" in task:
        task["task_end_time"] = datetime.fromisoformat(task["task_end_time"])
    return task

def string_to_timedelta(timedelta_str):
    """Converts a string back to a timedelta object."""

    parts = timedelta_str.split(":")
    days_part = parts[0].split(" days, ") if "days" in parts[0] else ["0",parts[0]]
    days = int(days_part[0])
    hours = int(days_part[1])
    minutes = int(parts[1])
    seconds_parts = parts[2].split(".")
    seconds = int(seconds_parts[0])
    
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def time_delta_to_day_hr_min_sec(timedelta_obj):
    days = timedelta_obj.days
    hours = timedelta_obj.seconds // 3600  
    minutes = (timedelta_obj.seconds % 3600) // 60  
    seconds = timedelta_obj.seconds % 60  
    
    return days,hours,minutes,seconds
    
def task_string(task):
    key_value=list(task.items())
    required_string=''
    for item in key_value:
        required_string+=f'{item[0]} : {item[1]} \n'
        
    return required_string

def put_new_user_task(logged_in_id,new_task,task_type):
    
    user_data=get_specific_user_data(logged_in_id)
    user_data[task_type].append(new_task)
    file_path=get_user_data_file_path(logged_in_id)
    return overwrite_file_data(file_path,user_data)

def put_user_tasks(logged_in_id,tasks,task_type):
    file_path=get_user_data_file_path(logged_in_id)
    
    user_data=get_specific_user_data(logged_in_id)
    
    user_data[task_type]=tasks
    
    return overwrite_file_data(file_path,user_data)