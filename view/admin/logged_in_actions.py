from datetime import datetime,date

from utils import get_pending_request_data
from utils import custom_input
from utils import int_input
from constants import ConstantStringEnum as cons
from utils import put_new_user_credential_data
from utils import update_pending_request_data
from utils import get_admin_credential_data
from utils import password_input
from utils import put_admin_credential_data
from utils import update_user_json_file
from utils import update_user_json_file
from utils import get_user_credential_data
from utils import get_specific_user_data
from utils import task_string
from utils import json_to_datetime
from utils import show_calendar

from ..user.user_task_actions import create_new_user_task

def pending_requests():
    user_pending_request_data=get_pending_request_data()
    
    choice_flag=True
    while choice_flag:
        choice=custom_input(
            '''
    Please enter
    1 to show all pending request
    2 to work with specific request
    0 to return to menu
    ''')
        if len(user_pending_request_data)==0:
                    print('No pending requests')
                    return
        match choice:
            case cons.ONE.value:
                for index,user in enumerate(user_pending_request_data,1):
                    print(f'',index,' user name : ',user['user_name'],' status : ',user['status'])
                    
            case cons.TWO.value:
                name_choice_flag=True
                while name_choice_flag:
                    specific_name_choice=custom_input('Enter specific user name : (all to go one by one, 0 to exit)')
                    
                    all_name_list=[user['user_name'] for user in user_pending_request_data]
                    
                    
                    if specific_name_choice in all_name_list:
                        all_name_list=[user['user_name'] for user in user_pending_request_data]
                        index=all_name_list.index(specific_name_choice)
                        work_with_specific_user_request(user_pending_request_data,index)
                        name_choice_flag=False
                        update_pending_request_data(user_pending_request_data)
                        
                    elif specific_name_choice=='all':
                        #new_list=user_pending_request_data.copy()
                            
                        index=0
                        for _ in range(len(user_pending_request_data)):
                            index+=work_with_specific_user_request(user_pending_request_data,index)
                        # instead of working with index if wish to work with user directly traversing on list
                        # for this purpose use enumerate to get index and value together
                            
                        name_choice_flag=False
                        update_pending_request_data(user_pending_request_data)
                        update_user_json_file()
                    
                    elif specific_name_choice==cons.ZERO.value:
                        return
                    else :
                        print('Invalid input')
                    
                        
            case cons.ZERO.value:
                return
    
    
#      
def work_with_specific_user_request(user_pending_request_data,index):
        print('user name : ',user_pending_request_data[index]['user_name'],
              '\nstatus : ',user_pending_request_data[index]['status'])
                
        
        approve_choice=custom_input('Wish to approve registration request?(Y for yes, anything else for no)')
        user=user_pending_request_data[index]
        if approve_choice=='Y':   
            user_pending_request_data.remove(user)
            new_user=put_new_user_credential_data(user)
            print('Registration request approved')
            print('New user id : ',new_user['user_id'],
                    'New user name : ',new_user['user_name'])
            update_user_json_file()
            print()
            return 0
        else:
            user.update({'user_name':user['user_name'],'password':user['password'],'status':'viewed'})
            return 1
                    

def show_all_user_data():
    user_credential_data=get_user_credential_data()
    show_user_data_choice=''
    while show_user_data_choice!='0':
        show_user_data_choice=custom_input('''
    Please Enter :
    1 to show specific user data 
    2 to show all user data
    0 to exit
    ''')
        match show_user_data_choice:
            case '1':
                specific_user_id=''
                while specific_user_id!=0:
                    specific_user_id=int_input('Please enter specific user id : (Enter 0 to exit)')
                    user_ids=[user['user_id'] for user in user_credential_data]
                    if specific_user_id in user_ids:
                        show_specific_user_data(specific_user_id)
                        
                    elif specific_user_id=='0':
                        return                  
                    else:
                        print('User id not found')
                
                
            case '2':
                for user in user_credential_data:
                    show_specific_user_data(user['user_id'])
                    print()

#
def show_specific_user_data(user_id):
    
    user_data=get_specific_user_data(user_id)
    
    print('Your personal information is as follows : ')
    print(f'''
    User ID : {user_data['user_id']}
    User Name : {user_data['user_name']}
    Phone number : {user_data['phone_number']}
    Email address : {user_data['email_id']}
    Address : {user_data['address']}
    ''')
    
    professional_tasks=user_data.get('professional_tasks')
    if len(professional_tasks)>0:
        print('All the professional tasks of user are :')
        for task in professional_tasks:
            print(task_string(task))
    else:
        print('No professional tasks scheduled')
        
    teams=user_data.get('teams')
    if len(teams)>0:
        print('All the teams user is in are :')
        for team in teams:
            print('   ',team)
    else :
        print('User has no team')
    
def show_all_user_ids():
    user_credential_data=get_user_credential_data()
    print('All user id and their user names are as follows :')
    for user in user_credential_data:
        user_id=user['user_id']
        user_name=user['user_name']
        print(f'    User id : {user_id}')
        print(f'    User name : {user_name}')
        print()

def show_todays_tasks():
    
    today=datetime.now().date()
    user_ids=[ user['user_id'] for user in get_user_credential_data()]
    print('Todays date : ',today,'\n')
    for user_id in user_ids:
        tasks=get_specific_user_data(user_id)['professional_tasks']
        print('Todays tasks for user id : ',user_id,' are as follows : ')
        for task in tasks:
            task=json_to_datetime(task)
            start=task['task_start_time'].date()
            end=task['task_end_time'].date()
            
            if today>=start and today<=end:
                print(task_string(task))
    

def create_new_user():
    
    new_user_name_flag=True
    while new_user_name_flag:
        user_name=custom_input('Enter new user name : ')
        user_name_choice=custom_input(f'provided name is {user_name} wish to continue?\nEnter 1 for yes \n0 to exit \nelse to go again')
        if user_name_choice=='1':
            new_user_name_flag=False
        elif user_name_choice=='0':
            return
    new_user_pass_flag=True
    while new_user_pass_flag:
        user_password=password_input('Enter new user password (Enter 0 to exit) :',True)
        if user_password=='0':
            return
        confirm_user_password=password_input('Enter password again to confirm (Enter 0 to exit) : ')
        if confirm_user_password=='0':
            return
        if user_password==confirm_user_password:
            new_user_pass_flag=False
        else:
            print('passwords do not match')
    user={'user_name':user_name,'password':user_password}
    
    credential_flag=put_new_user_credential_data(user) 
    update_json_flag=update_user_json_file()

    if len(credential_flag.keys())!=0  and update_json_flag :
        print('User created successfully')
    else:
        print('User creation failed')
    
        
    
    
def create_new_task():
    create_task_flag=True
    user_ids=[user['user_id'] for user in get_user_credential_data()]
    while create_task_flag:
        
        new_task_user_id=int_input('Enter user id to create a task : (Enter 0 to exit)')
        if new_task_user_id in user_ids:
            create_task_output=create_new_user_task('root','professional_tasks')
            if create_task_output=='0':
                return 
            create_task_flag=False
            
        elif new_task_user_id==0:
            return
        else:
            print('user id does not exists')
            

def show_admin_calendar():
    show_calendar('root','professional_tasks')
    

def change_password_admin(logged_in_admin_name):
    print('Admin logged in as : ',logged_in_admin_name)
    
    admin=get_admin_credential_data()   

    pass_flag=True
    while pass_flag:    
        current_password=password_input('Enter current password : (0 to go to menu)')
        if current_password==admin['admin_password']:
            pass_confirm_flag=True
            while pass_confirm_flag:
                
                new_password=password_input('Enter new password : (0 to go to menu)',True)
                if new_password=='0':   
                    return
                confirm_new_password=password_input('Enter new password again to confirm : ')
                if new_password==confirm_new_password:
                    admin.update({'admin_name':admin['admin_name'],'admin_password':new_password})
                    
                    password_success=put_admin_credential_data(admin)
                    if password_success:    
                        print('Password updated successfully')
                    else :
                        print('Password update failed')
                    pass_confirm_flag=False
                else:
                    print('password do not match')
            
            
            pass_flag=False
        elif current_password=='0':
            return
        else :
            print('Invalid password')


def show_all_teams():
    
    users=get_user_credential_data()
    teams={}
    for user in users:
        team=user['team']
        user=(user['user_id'],user['user_name'])
        teams.setdefault(team, []).append(user)
        
    print('all the available teams are as follows : ')
    for team in teams:
        print(team)
        user_list=teams[team]
        for user in user_list:
            print(f'   {user[0]} : {user[1]}')
        
    
   