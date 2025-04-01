from constants import ConstantStringEnum as cons
from utils import custom_input
from view import admin_login
from view import pending_requests
from view import change_password_admin
from view import show_all_user_data
from view import show_all_user_ids
from view import show_todays_tasks
from view import create_new_user
from view import create_new_task
from view import show_admin_calendar
from view import show_all_teams
from view import send_message
from view import show_message

def admin_dashboard():
    
    admin_login_status=admin_login()
       
    if admin_login_status==cons.ZERO.value:
        return
    admin_logged_in_dashboard()   

def admin_logged_in_dashboard():
    
    admin_logged_in_dashboard_choice=''
    while admin_logged_in_dashboard_choice!='0':
        admin_logged_in_dashboard_choice=custom_input(cons.ADMIN_LOGGED_IN_DASHBOARD.value)
        match admin_logged_in_dashboard_choice:
            case cons.ONE.value: 
                pending_requests()
            case cons.TWO.value: 
                show_all_user_data()
            case cons.THREE.value:
                show_todays_tasks()
            case cons.FOUR.value: 
                create_new_task()
            case cons.FIVE.value: 
                change_password_admin()
            case cons.SIX.value: 
                create_new_user()
            case cons.SEVEN.value: 
                show_all_user_ids()
            case cons.EIGHT.value:
                show_admin_calendar()
            case cons.NINE.value:
                show_all_teams()
            case cons.TEN.value:
                send_message()
            case cons.ELEVEN.value:
                show_message()
                
         
            