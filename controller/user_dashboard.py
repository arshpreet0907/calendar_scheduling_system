from constants import ConstantStringEnum as cons 

from view import user_log_in
from view import view_pending_request
from view import user_registration
from utils import custom_input 
from view import change_password_user
from view import edit_personal_info
from view import work_with_personal_tasks
from view import show_personal_information
from view import work_with_professional_tasks
from view import send_message
from view import show_message

def user_dashboard():
    user_dashboard_choice=''
    while user_dashboard_choice!='0':
        user_dashboard_choice=custom_input(cons.USER_DASHBOARD_GUIDE.value)
        match user_dashboard_choice:
            case cons.ONE.value:
                user_logged_in_id=user_log_in()
                if user_logged_in_id!='0':
                    user_logged_in_dashboard(user_logged_in_id)
                    
            case cons.TWO.value: 
                user_registration()
                
            case cons.THREE.value: 
                view_pending_request()
                # here the status for the request can be requested, viewed, approval_pending
            
def user_logged_in_dashboard(logged_in_user_id):

    user_logged_in_dashboard_choice=''
    
    while user_logged_in_dashboard_choice!=cons.ZERO.value:
        
        user_logged_in_dashboard_choice=custom_input(cons.USER_LOGGED_IN_DASHBOARD.value)
        
        match user_logged_in_dashboard_choice:
            case cons.ONE.value: 
                work_with_personal_tasks(logged_in_user_id)
            case cons.TWO.value: 
                work_with_professional_tasks(logged_in_user_id)
            case cons.THREE.value:
                change_password_user(logged_in_user_id)
            case cons.FOUR.value: 
                show_personal_information(logged_in_user_id)
            case cons.FIVE.value: 
                edit_personal_info(logged_in_user_id)
            case cons.SIX.value: 
                send_message(logged_in_user_id)
            case cons.SEVEN.value: 
                show_message(logged_in_user_id)
