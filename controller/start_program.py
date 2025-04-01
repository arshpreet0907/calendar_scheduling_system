from constants import ConstantStringEnum as cons
from controller import user_dashboard 
from utils import custom_input 
from controller import admin_dashboard

def program_start():
 
    print(cons.WELCOME_STRING.value)
    dashboard_guide_choice=''
    while dashboard_guide_choice!=cons.ZERO.value:
        dashboard_guide_choice=custom_input(cons.DASHBOARD_GUIDE.value)
        match dashboard_guide_choice:
            case cons.ONE.value:
                    user_dashboard()
            case cons.TWO.value:
                    admin_dashboard()
                


