from utils import show_calendar
from .user_task_actions import show_all_scheduled_user_tasks
from .user_task_actions import show_user_tasks_for_particular_date_month_year
from .user_task_actions import show_todays_user_tasks
from .user_task_actions import create_new_user_task
from .user_task_actions import remove_past_user_tasks
from .user_task_actions import edit_user_task

PERSONAL_TASKS='personal_tasks'
PERSONAL='PERSONAL'

def show_all_scheduled_personal_tasks(logged_in_id):
    show_all_scheduled_user_tasks(logged_in_id,PERSONAL_TASKS)


def show_todays_personal_tasks(logged_in_id):
    show_todays_user_tasks(logged_in_id,PERSONAL_TASKS)
            
def show_personal_tasks_for_particular_date_month_year(logged_in_id):
    show_user_tasks_for_particular_date_month_year(logged_in_id,PERSONAL_TASKS)

def show_personal_calendar(logged_in_id):
    show_calendar(logged_in_id,PERSONAL)
    
def create_new_personal_task(logged_in_id):

    create_new_user_task(logged_in_id,PERSONAL_TASKS)

def edit_personal_task(logged_in_id):
    edit_user_task(logged_in_id,PERSONAL_TASKS)


def remove_past_personal_tasks(logged_in_id):
    remove_past_user_tasks(logged_in_id,PERSONAL_TASKS)