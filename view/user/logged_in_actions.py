import datetime

from utils import get_user_credential_data
from utils import password_input
from utils import put_user_credential_data
from utils import get_specific_user_data
from utils import custom_input
from utils import put_specific_user_data
from utils import get_admin_credential_data
from utils import put_admin_credential_data
from utils import phone_number_input
from utils import email_address_input
from utils import address_input
from .personal_task_actions import create_new_personal_task
from .personal_task_actions import show_todays_personal_tasks
from .personal_task_actions import show_all_scheduled_personal_tasks
from .personal_task_actions import show_personal_tasks_for_particular_date_month_year
from .personal_task_actions import edit_personal_task
from .personal_task_actions import remove_past_personal_tasks
from .personal_task_actions import show_personal_calendar
from .professional_task_actions import show_all_scheduled_professional_tasks
from .professional_task_actions import show_todays_professional_tasks
from .professional_task_actions import show_professional_tasks_for_particular_date_month_year
from .professional_task_actions import create_new_professional_task
from .professional_task_actions import show_professional_calendar
from .professional_task_actions import edit_professional_task
from .professional_task_actions import remove_past_professional_tasks
from utils import int_input


TASK_CHOICE='''
    Please Enter : 
    1 to show all scheduled tasks
    2 to show today's tasks
    3 to show for particular date,month,year
    4 to show calendar
    5 to create new task
    6 to edit task
    7 to remove tasks
    0 to exit
            '''

def work_with_personal_tasks(logged_in_user_id):
    personal_task_choice=''
    print('Working With Personal Tasks')
    while(personal_task_choice)!='0':
        personal_task_choice=custom_input(TASK_CHOICE)
        match personal_task_choice:
            case '1':
                show_all_scheduled_personal_tasks(logged_in_user_id)
            case '2':
                show_todays_personal_tasks(logged_in_user_id)
            case '3':
                show_personal_tasks_for_particular_date_month_year(logged_in_user_id)
            case '4':
                show_personal_calendar(logged_in_user_id)
            case '5':
                create_new_personal_task(logged_in_user_id)
            case '6':
                edit_personal_task(logged_in_user_id)
            case '7':
                remove_past_personal_tasks(logged_in_user_id)
            

def work_with_professional_tasks(logged_in_user_id):
    personal_task_choice=''
    print('Working With Professional Tasks')
    while(personal_task_choice)!='0':
        personal_task_choice=custom_input(TASK_CHOICE)
        match personal_task_choice:
            case '1':
                show_all_scheduled_professional_tasks(logged_in_user_id)
            case '2':
                show_todays_professional_tasks(logged_in_user_id)
            case '3':
                show_professional_tasks_for_particular_date_month_year(logged_in_user_id)
            case '4':
                show_professional_calendar(logged_in_user_id)
            case '5':
                create_new_professional_task(logged_in_user_id)
            case '6':
                edit_professional_task(logged_in_user_id)
            case '7':
                remove_past_professional_tasks(logged_in_user_id)

def change_password_user(logged_in_user_id):
    print('User logged in with user id : ',logged_in_user_id)
    user_credential_data=get_user_credential_data()
    
    for user in user_credential_data:
        if user['user_id']==logged_in_user_id:
            pass_flag=True
            while pass_flag:    
                current_password=password_input('Enter current password : (0 to go to menu)')
                if current_password==user['password']:
                    pass_confirm_flag=True
                    while pass_confirm_flag:
                        
                        new_password=password_input('Enter new password : (0 to go to menu)',True)
                        if new_password=='0':
                            return
                        confirm_new_password=password_input('Enter new password again to confirm : ')
                        if new_password==confirm_new_password:
                            user.update({'user_id':logged_in_user_id,'user_name':user['user_name'],'password':new_password})
                          
                            password_success=put_user_credential_data(user_credential_data)
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
    

def show_personal_information(logged_in_user_id,personal=True):
    
    user_data=get_specific_user_data(logged_in_user_id)
    
    user_personal_info(user_data)
    
    if personal:
        personal_tasks=user_data.get('personal_tasks')
        if len(personal_tasks)>0:
            print('All the personal tasks of user are :')
            for task in personal_tasks:
                print('   ',task['task_name'])
        else:
            print('No personal tasks scheduled')
        
    professional_tasks=user_data.get('professional_tasks')
    if len(professional_tasks)>0:
        print('All the professional tasks of user are :')
        for task in professional_tasks:
            print('   ',task['task_name'])
    else:
        print('No professional tasks scheduled')
        
    teams=user_data.get('teams')
    if len(teams)>0:
        print('All the teams user is in are :')
        for team in teams:
            print('   ',team)
    else :
        print('You have no team')
    

def user_personal_info(user_data):
    print('Your personal information is as follows : ')
    print(f'''
    User ID : {user_data['user_id']}
    User Name : {user_data['user_name']}
    Phone number : {user_data['phone_number']}
    Email address : {user_data['email_id']}
    Address : {user_data['address']}
    ''')
    return user_data

def edit_personal_info(logged_in_user_id):
    
    user_data=get_specific_user_data(logged_in_user_id)
    user_personal_info(user_data)
    
    did_edit=False
    
    new_phone_number=user_data['phone_number']
    new_email_address=user_data['email_id']
    new_address=user_data['address']
    
    
    edit_choice=''
    while edit_choice!='Y' or edit_choice!='0':
        edit_choice=custom_input('Wish to edit (Y for yes, 0 for no)')
        if edit_choice=='Y':
            
            while edit_choice!='0':
                edit_choice=custom_input('''
    Please Enter :
    1 to update phone number
    2 to update email address
    3 to edit address
    0 to exit
    
                  ''')
                if edit_choice=='1':
                    print('your current phone number is : ',user_data['phone_number'])
                    phone_number_flag=True
                    while phone_number_flag:
                        new_phone_number=phone_number_input('Enter new phone number : ')
                        
                        print('Your new phone number would be : ',new_phone_number)
                        confirm_choice=custom_input('Enter \n1 to confirm \n2 to edit something else\n0 to exit\nelse to go again')
                        if confirm_choice=='1':
                            phone_number_flag=False
                            did_edit=True
                        elif confirm_choice=='2':
                            new_phone_number=user_data['phone_number']
                            phone_number_flag=False
                        elif confirm_choice=='0':
                            edit_choice='0'
                            did_edit=True
                        
                elif edit_choice=='2':
                    print('your current email address is : ',user_data['email_id'])
                    email_address_flag=True
                    
                    while email_address_flag:
                        new_email_address=email_address_input('Enter new email address : ')
                        
                        print('Your new email address would be : ',new_email_address)
                        confirm_choice=custom_input('Enter \n1 to confirm \n2 to edit something else\n0 to exit\nelse to go again')
                        if confirm_choice=='1':
                            email_address_flag=False
                        elif confirm_choice=='2':
                            new_email_address=user_data['email_id']
                            email_address_flag=False
                        elif confirm_choice=='0':
                            did_edit=True
                            edit_choice='0'
                            
                elif edit_choice=='3':
                    print('your current address is : ',user_data['email_id'])
                    address_flag=True
                    
                    while address_flag:
                        address_dict,new_address=address_input('Enter new address : ')
                        
                        print('Your new address would be : ',new_address)
                        confirm_choice=custom_input('Enter \n1 to confirm \n2 to edit something else\n0 to exit\nelse to go again')
                        
                        if confirm_choice=='1':
                            address_flag=False
                        elif confirm_choice=='2':
                            
                            address_edit,new_address=edit_address(address_dict)
                            if address_edit:
                                print('Edit successful')
                            else:
                                print('Edit failed')
                            address_flag=False
                        elif confirm_choice=='0':
                            did_edit=True
                            edit_choice='0'
                            
                else:
                    print('Enter valid input (0 to exit)')
        else:
            print('Please enter valid input')
        if edit_choice=='0':
            break
    
    if did_edit:
        user_data.update({'phone_number':new_phone_number,'email_id':new_email_address,'address':new_address})
        update_response=put_specific_user_data(user_data)
        if update_response:
            print('Information updated successfully')
        else:
            print('Information update failed')
            
def edit_address(address_dict):
    
    did_edit=False
    
    # house_or_locality
    house_or_locality=address_dict['house_or_locality']
    house_or_locality_choice=custom_input(f'your current house_or_locality is {house_or_locality} \nDo you wish to edit \nEnter \n1 for yes \n0 to exit \nelse for no : ')
    if house_or_locality_choice=='1':
        house_or_locality_flag=True
        while house_or_locality_flag:
            new_house_or_locality=custom_input('Enter new house_or_locality')
            house_or_locality_choice=custom_input(f'Provided house_or_locality is {new_house_or_locality} \nDo you wish to confirm \nEnter\n1 for yes \n2 for no\n0 to exit \nelse to again : ')
            if house_or_locality_choice=='1':
                address_dict['house_or_locality']=new_house_or_locality
                did_edit=True
                house_or_locality_flag=False
                
            elif house_or_locality_choice=='0':
                return did_edit,address_dict_str(address_dict)
            elif pin_code_choice=='2':
                break
            
    elif house_or_locality_choice=='0':
       return did_edit,address_dict_str(address_dict)
    
    # street_name_or_landmark
    
    street_name_or_landmark=address_dict['street_name_or_landmark']
    street_name_or_landmark_choice=custom_input(f'your current street_name_or_landmark is {street_name_or_landmark} \nDo you wish to edit \nEnter \n1 for yes \n0 to exit \nelse for no : ')
    if street_name_or_landmark_choice=='1':
        street_name_or_landmark_flag=True
        while street_name_or_landmark_flag:
            new_street_name_or_landmark=custom_input('Enter new street_name_or_landmark')
            street_name_or_landmark_choice=custom_input(f'Provided street_name_or_landmark is {new_street_name_or_landmark} \nDo you wish to confirm \nEnter\n1 for yes \n2 for no\n0 to exit \nelse to again : ')
            if street_name_or_landmark_choice=='1':
                address_dict['street_name_or_landmark']=new_street_name_or_landmark
                did_edit=True
                street_name_or_landmark_flag=False
                
            elif street_name_or_landmark_choice=='0':
                return did_edit,address_dict_str(address_dict)
            elif pin_code_choice=='2':
                break
            
    elif street_name_or_landmark_choice=='0':
       return did_edit,address_dict_str(address_dict)
    
    # city
   
    city=address_dict['city']
    city_choice=custom_input(f'your current city is {city} \nDo you wish to edit \nEnter \n1 for yes \n0 to exit \nelse for no : ')
    if city_choice=='1':
        city_flag=True
        while city_flag:
            new_city=custom_input('Enter new city')
            city_choice=custom_input(f'Provided city is {new_city} \nDo you wish to confirm \nEnter\n1 for yes \n2 for no\n0 to exit \nelse to again : ')
            if city_choice=='1':
                address_dict['city']=new_city
                did_edit=True
                city_flag=False
                
            elif city_choice=='0':
                return did_edit,address_dict_str(address_dict)
            elif pin_code_choice=='2':
                break
            
    elif city_choice=='0':
       return did_edit,address_dict_str(address_dict)
   
    # pin_code
    
    pin_code=address_dict['pin_code']
    pin_code_choice=custom_input(f'your current pin_code is {pin_code} \nDo you wish to edit \nEnter \n1 for yes \n0 to exit \nelse for no : ')
    if pin_code_choice=='1':
        pin_code_flag=True
        while pin_code_flag:
            new_pin_code=int_input('Enter new pin_code')
            pin_code_choice=custom_input(f'Provided pin_code is {new_pin_code} \nDo you wish to confirm \nEnter\n1 for yes \n2 for no\n0 to exit \nelse to again : ')
            if pin_code_choice=='1':
                address_dict['pin_code']=new_pin_code
                did_edit=True
                city_flag=False
                
            elif pin_code_choice=='0':
                return did_edit,address_dict_str(address_dict)
            elif pin_code_choice=='2':
                break
            
    elif pin_code_choice=='0':
       return did_edit,address_dict_str(address_dict)
   
    # state
    state=address_dict['state']
    state_choice=custom_input(f'your current state is {state} \nDo you wish to edit \nEnter \n1 for yes \n0 to exit \nelse for no : ')
    if state_choice=='1':
        state_flag=True
        while state_flag:
            new_state=custom_input('Enter new state')
            state_choice=custom_input(f'Provided state is {new_pin_code} \nDo you wish to confirm \nEnter\n1 for yes \n2 for no\n0 to exit \nelse to again : ')
            if state_choice=='1':
                address_dict['state']=new_state
                did_edit=True
                city_flag=False
                
            elif state_choice=='0':
                return did_edit,address_dict_str(address_dict)
            elif pin_code_choice=='2':
                break
            
    elif state_choice=='0':
       return did_edit,address_dict_str(address_dict)
   
    
    return did_edit,address_dict_str(address_dict)
    
def address_dict_str(address_dict):
    house_or_locality=address_dict['house_or_locality']
    street_name_or_landmark=address_dict['street_name_or_landmark']
    city=address_dict['city']
    pin_code=address_dict['pin_code']
    state=address_dict['state']
    
    return house_or_locality+' '+street_name_or_landmark+' '+city+' '+pin_code+' '+state

def show_message(logged_in_user_id='root'):
    if logged_in_user_id=='root':
        admin_data=get_admin_credential_data()
        messages=admin_data['messages']
    else:
        user_data=get_specific_user_data(logged_in_user_id)
        messages=user_data['messages']
    if len(messages)==0:
        print('You dont have any messages ')
        return
    else:
        messages_copy=messages.copy()
        for message in messages:
            print(f'Sender  : {message[0]}')
            print(f'Message is : \n {message[1]} \n')
            delete_choice=custom_input('Do you wish to delete this message?Enter \n1 for \n0 to exit \nelse to continue :')
            if delete_choice=='1':
                messages_copy.remove(message)
            elif delete_choice=='0':
                return
        
    if messages!=messages_copy:
        if logged_in_user_id=='root':    
            admin_data['messages']=messages_copy
            put_data_output=put_admin_credential_data(admin_data)
            
        else:
            user_data['messages']=messages_copy
            put_data_output=put_specific_user_data(user_data)
            
        if put_data_output:
            print('Messages updated successfully')
        else :
            print('Message update failed')
    
def send_message(logged_in_user_id='root'):
    
    receiver_choice_flag=True
    users=get_user_credential_data()
    user_ids=[user['user_id'] for user in users]
    
    while receiver_choice_flag:
        receiver=custom_input('Please enter receiver id (enter root for admin) (enter 0 to exit) : ')
        
        if str(logged_in_user_id)==receiver:
            print('sender and receiver cannot be same')
            continue    
        elif receiver==0:
            return
        elif (receiver=='root')  :

            receiver_choice=custom_input(f'You entered receiver {receiver} \nenter 1 for yes\n0 to exit \nelse to go again : ')
            if receiver_choice=='1':
                receiver_choice_flag=False
            elif receiver_choice=='0':
                return 
            
        elif (receiver.isdigit() and int(receiver) in user_ids):
            receiver=int(receiver)
            index=user_ids.index(receiver)
            user_name=users[index]['user_name']
            receiver_choice=custom_input(f'You entered receiver id : {receiver}, name : {user_name} \nenter 1 for yes\n0 to exit \nelse to go again : ')
            if receiver_choice=='1':
                
                receiver_choice_flag=False
            elif receiver_choice_flag=='0':
                return 
        else:
            print('Invalid input')
    message_flag=True
    
    while message_flag:
        message=custom_input('Enter your message to be sent : (enter 0 exit) :')
        if message=='0':
            return
        message_choice=custom_input(f'your entered message is : {message} \nEnter \n1 to confirm \0 to exit \nelse to go again : ')
        if message_choice=='1':
            message_flag=False
        elif message_choice=='0':
            return
    if logged_in_user_id=='root':
        final_message=('root',message)
    else:
        user_data=get_specific_user_data(logged_in_user_id)
        final_message=(str(logged_in_user_id)+' '+user_data['user_name'],message)
    if receiver=='root':
        admin_data=get_admin_credential_data()
        admin_data['messages'].append(final_message)
        send_message_output=put_admin_credential_data(admin_data)
    else:
        receiver_user_data=get_specific_user_data(receiver)
        receiver_user_data['messages'].append(final_message)
        send_message_output=put_specific_user_data(receiver_user_data)
    if send_message_output:
        print('Message sent successfully')
    else:
        print('Message failed')