from datetime import datetime,date

from utils import get_specific_user_data
from utils import custom_input
from utils import json_to_datetime
from utils import task_string
from utils import year_input
from utils import month_input
from utils import date_input
from utils import is_task_in_month
from utils import task_name_input
from utils import task_description_input
from utils import task_start_time_input
from utils import task_end_time_input
from utils import task_priority_input
#from utils import task_assignee_input
from utils import put_new_user_task
from utils import put_user_tasks
from utils import edit_task_input
from utils import task_team_input

def show_all_scheduled_user_tasks(logged_in_id,task_type):
    
    tasks=get_specific_user_data(logged_in_id)[task_type]
    for task in tasks:
        task=json_to_datetime(task)
        print(task_string(task))
        
def show_todays_user_tasks(logged_in_id,task_type):
    
    tasks=get_specific_user_data(logged_in_id)[task_type]
    today=datetime.now().date()
    
    for task in tasks:
        task=json_to_datetime(task)
        start=task['task_start_time'].date()
        end=task['task_end_time'].date()
        
        if today>=start and today<=end:
            print(task_string(task))

def show_user_tasks_for_particular_date_month_year(logged_in_id,task_type):
    show_task_choice=''
    while show_task_choice!='0':
        tasks=get_specific_user_data(logged_in_id)[task_type]
        show_task_choice=custom_input(
            '''
    Please Enter 
    1 to show tasks for particular year
    2 to show tasks for particular month
    3 to show tasks for particular date
    0 to exit
                                      ''')
        today=datetime.now()
        match show_task_choice:
            case '1':
                year=year_input(today)
                for task in tasks:
                    task=json_to_datetime(task)
                    start=task['task_start_time']
                    end=task['task_end_time']
                    if year>=start.year and year<=end.year:
                        print(task_string(task))
                
            case '2':
                year=year_input(today)
                month=month_input(today,year)
                
                for task in tasks:
                    if is_task_in_month(month,year,task):
                        print(task_string(task))
            case '3':
                year=year_input(today)
                month=month_input(today,year)
                day=date_input(today,month,year)
                
                date_to_check=date(year,month,day)
                for task in tasks:
                    task=json_to_datetime(task)
                    start=task['task_start_time'].date()
                    end=task['task_end_time'].date()
                    
                    if start<=date_to_check<=end:
                        print(task_string(task))
                        
def create_new_user_task(logged_in_id,task_type):
    task_name=task_name_input()
    if task_name=='0':
        return
    
    task_description=task_description_input()
    if task_description=='0':
        return
    
    task_start_time=task_start_time_input()
    if task_start_time=='0':
        return
    
    task_end_time=task_end_time_input(task_start_time)
    if task_end_time=='0':
        return
    
    task_priority=task_priority_input()
    if task_priority=='0':
        return
 
    new_task={
        'task_name':task_name,
        'task_description':task_description,
        'task_start_time':task_start_time.isoformat(),
        'task_end_time':task_end_time.isoformat(),
        'task_priority':task_priority,
        'task_duration':str(task_end_time-task_start_time)
    }
    if task_type=='professional_tasks':
        
        # here if user is creating a task he himself is assignee 
        # when admin will create root will be assignee

        new_task['assignee']=logged_in_id
        task_team=''
        if logged_in_id=='root':
            task_team=task_team_input()
            if task_priority=='0':
                return
        if task_team=='':
            new_task['team']=logged_in_id
        else:
            new_task['team']=task_team
            
    new_task_creation_output=put_new_user_task(logged_in_id,new_task,task_type)
    if new_task_creation_output:
        print('Task created successfully')
    else:
        print('Task creation failed')

def edit_user_task(logged_in_id,task_type):
    edit_task_choice=''

    while edit_task_choice!='0':

        tasks=get_specific_user_data(logged_in_id)[task_type]
        edit_task_choice=custom_input('''
    Wish to  or ?
    Please Enter 
    1 to edit specific task
    2 to go one by one
    0 to exit
    ''' )
        match edit_task_choice:
            case '1':
                specific_task_name=''
                while specific_task_name!='0':
                    specific_task_name=custom_input('Please enter specific task name : (Enter 0 to exit)')
                    task_names=[task['task_name'] for task in tasks]
                    if specific_task_name in task_names:
                        task=tasks[task_names.index(task_name)]
                        assignee=task.get('assignee',None)
                        if assignee !=None and assignee!=logged_in_id :                    
                            print('You cannot edit the task assigned by admin')
                            break
                        task=edit_task(task)
                        if task=='0':
                            return
                        tasks[task_names.index(specific_task_name)]=task
                        break
                    elif specific_task_name=='0':
                        return                  
                    else:
                        print('Task name not found')
            case '2': 
                for task in tasks:
                    task=json_to_datetime(task)
                    assignee=task.get('assignee',None)
                    if assignee !=None and assignee!=logged_in_id :   
                        continue
                    task_name=task['task_name']
                    print(f'Name of task is : {task_name}')
                    edit_task_choice=custom_input('Wish to edit this task (Y for yes 0 to exit else to move ahead)')
                    if edit_task_choice=='Y':
                        task=edit_task(task)    
                    elif edit_task_choice=='0':
                        return
        put_task_output=put_user_tasks(logged_in_id,tasks,task_type)
        if put_task_output:
            print('Task updated successfully.')
        else :
            print('Task update failed.')        
                               
def edit_task(task):
    
    
    for key in task.keys():
        if key=='assignee' or key=='team':
            continue
        edit_task_choice=custom_input(f'Do you wish to edit {key}, enter Y for yes, 0 to exit, else to move ahead')
        if edit_task_choice=='Y':
            task[key]=edit_task_input(key)
        elif edit_task_choice=='0':
            return '0'
    return task

def remove_past_user_tasks(logged_in_user_id,task_type):
    
    remove_task_choice=''
    tasks=get_specific_user_data(logged_in_user_id)[task_type]
    while remove_task_choice!='0':
        remove_task_choice=custom_input('''
    Wish to  or ?
    Please Enter 
    1 to remove specific task
    2 to go one by one
    0 to exit
    ''' )
        match remove_task_choice:
            case '1':
                specific_task_name=''
                while specific_task_name!='0':
                    specific_task_name=custom_input('Please enter specific task name : (Enter 0 to exit)')
                    task_names=[task['task_name'] for task in tasks]
                    if specific_task_name in task_names:
                        index=task_names.index(specific_task_name)
                        if tasks[index]['assignee']!=logged_in_user_id:
                            print('You cannot remove the task assigned by admin')
                            break
                        delete_choice=custom_input(f'task name provided : {specific_task_name}, do you wish to remove this task?\nEnter\nY for yes\n0 to exit')
                        if delete_choice=='Y':
                            index=task_names.index(specific_task_name)
                            tasks.pop(index)
                    elif specific_task_name=='0':
                        return                  
                    else:
                        print('Task name not found')
            case '2':
                for task in tasks:
                    task=json_to_datetime(task)
                    task_name=task['task_name']
                    if task['assignee']!=logged_in_user_id:
                            #print('You cannot remove the task assigned by admin')
                            continue
                    print(f'Name of task is : {task_name}')
                    remove_task_choice=custom_input('Wish to remove this task (Y for yes 0 to exit else to move ahead)')
                    if remove_task_choice=='Y':
                        tasks.remove(task)
                    elif remove_task_choice=='0':
                        return
    
        put_task_output=put_user_tasks(logged_in_user_id,tasks,task_type)
        if put_task_output:
            print('Task deleted successfully.')
        else :
                print('Task delete failed.')    
       