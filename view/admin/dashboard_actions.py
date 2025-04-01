from utils import custom_input
from utils import password_input
from utils import get_admin_credential_data
from constants import ConstantStringEnum as cons

def admin_login():
    admin_credential_data=get_admin_credential_data()
    if len(admin_credential_data.keys())==0:
        print(cons.NO_ADMIN_EXISTS.value)
        return '0'
    
    admin_name=admin_credential_data['admin_name']
    
    admin_name_flag=True
    while admin_name_flag:
        admin_name_input=custom_input("Please enter admin name : (Enter 0 to exit)")
        if admin_name_input == admin_name:
            admin_name_flag=False
        elif admin_name_input=='0':
            print(cons.LOGIN_FAILED.value)
            return '0'
        else:
            print(cons.ADMIN_NAME_NOT_EXISTS.value)
    
    pass_flag=True
    password=admin_credential_data['admin_password']
    while pass_flag:
            admin_password_input=password_input('Please enter password for admin : (Enter 0 to exit)')
            if admin_password_input==password:
                print(cons.ADMIN_LOGIN_SUCCESS.value)
                break
            elif password=='0':
                print(cons.LOGIN_FAILED.value)
                return '0'
            else:
                print(cons.INVALID_PASSWORD.value)
            
                
    return admin_name