from constants import ConstantStringEnum as cons
from utils import get_user_credential_data
from utils import get_pending_request_data
from utils import put_pending_request_data
from utils import password_input
from utils import custom_input 
from utils import int_input

def is_valid_user_name(user_name):
    pending_request_data=get_pending_request_data()
    for user in pending_request_data:
        if user['user_name']==user_name:
            return False
    return True

def user_registration():
    print(cons.NEW_REGISTRATION_WELCOME.value) 
    confirm_flag=cons.NO.value
    while confirm_flag==cons.NO.value:
               
        new_user_name=custom_input(cons.ENTER_USER_NAME.value)
        
        is_valid_name=is_valid_user_name(new_user_name)
        if not is_valid_name:
            print(cons.NAME_EXISTS_PENDING_LIST.value)
        else:
            confirm_name_str=cons.CONFIRM_USER_NAME.value+new_user_name+'\n'
            confirm_flag=custom_input(confirm_name_str)
            if confirm_flag==cons.YES.value:
            
                pass_match_flag=False
                while not pass_match_flag:
                    new_user_password=password_input(cons.ENTER_USER_PASSWORD.value,True)
                    confirm_password=password_input(cons.ENTER_CONFIRM_PASSWORD.value)
                
                    if new_user_password==confirm_password:
                        confirm_str=cons.CONFIRM_REGISTRATION.value+new_user_name+'\n'
                        confirm_flag=custom_input(confirm_str)
                        
                        if confirm_flag == cons.YES.value:
                            pass_match_flag=True
                            data_tuple=tuple([new_user_name,new_user_password])
                            registration_confirmation=put_pending_request_data(data_tuple)
                            if registration_confirmation:
                                print(cons.USER_REGISTER_SUCCESS.value)
                            else:
                                print(cons.USER_REGISTER_FAIL.value)
                            
                    else:
                        print(cons.PASSWORD_NOT_MATCH.value)
                    
                    if confirm_flag==cons.CANCEL.value:
                        return
            elif confirm_flag==cons.EXIT.value:
                return
def user_log_in():
 
    user_credential_data=get_user_credential_data()
    if not len(user_credential_data):
        return "No "
    user_id=0
    user_id_list=[user['user_id'] for user in user_credential_data]
    
    while user_id not in user_id_list:
        
        user_id=int_input('Please enter user id (Enter 0 to exit):\n')
        if user_id  in user_id_list:
            break
        elif user_id==0:
            print(cons.LOGIN_FAILED.value)
            return '0'
        else :
            print(cons.INVALID_USER_ID.value)
        
        
    if user_id!=0:
        id_index=user_id_list.index(user_id)
        pass_flag=True
        while pass_flag:
            password=password_input('Please enter password (Enter 0 to exit):\n')
            if password==user_credential_data[id_index]['password']:
                print(cons.LOGIN_SUCCESS.value,user_id)
                pass_flag=False
                break
            elif password=='0':
                print(cons.LOGIN_FAILED.value)
                return '0'
            else:
                print(cons.INVALID_PASSWORD.value)
            
    return user_id      

def view_pending_request():
    pending_request_data=get_pending_request_data()
    pending_users=[user['user_name'] for user in pending_request_data]
    #print(pending_request_data)
    if len(pending_users)==0:
        print(cons.PENDING_REQUEST_EMPTY.value)
        return 
    
    user__name_flag=True
    while user__name_flag:
            user_name=custom_input(cons.ENTER_USER_NAME.value)
            if user_name in pending_users:
                user__name_flag=False
                break
            print(cons.USER_NAME_NOT_EXISTS.value)
    
    name_index=pending_users.index(user_name)
    pass_flag=True
    while pass_flag:
        password=password_input(cons.ENTER_USER_PASSWORD.value)
        if password==pending_request_data[name_index]['password']:
            print_pending_request_data(pending_request_data,name_index)
            pass_flag=False
            break
        else:
            print(user_name,'\n',cons.INVALID_PASSWORD.value)
        print(cons.ZERO_TO_BACK.value)
        if password==cons.ZERO.value:
            return 
    
    
def print_pending_request_data(pending_request_data,id_index): 
    
    user_data=pending_request_data[id_index]
    print('Name of user : ',user_data['user_name'])
    print('status of request : ',user_data['status'])
    
        
        