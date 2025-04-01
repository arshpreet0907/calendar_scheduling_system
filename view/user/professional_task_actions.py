from .user_task_actions import show_all_scheduled_user_tasks
from .user_task_actions import show_user_tasks_for_particular_date_month_year
from .user_task_actions import show_todays_user_tasks
from .user_task_actions import create_new_user_task
from utils import show_calendar
from .user_task_actions import edit_user_task
from .user_task_actions import remove_past_user_tasks


PROFESSIONAL_TASKS='professional_tasks'
PROFESSIONAL='PROFESSIONAL'

def show_all_scheduled_professional_tasks(logged_in_user_id):
    show_all_scheduled_user_tasks(logged_in_user_id,PROFESSIONAL_TASKS)

def show_todays_professional_tasks(logged_in_user_id):
    show_todays_user_tasks(logged_in_user_id,PROFESSIONAL_TASKS)

def show_professional_tasks_for_particular_date_month_year(logged_in_user_id):
    show_user_tasks_for_particular_date_month_year(logged_in_user_id,PROFESSIONAL_TASKS)

def create_new_professional_task(logged_in_user_id):
    create_new_user_task(logged_in_user_id,PROFESSIONAL_TASKS)

def show_professional_calendar(logged_in_user_id):
    show_calendar(logged_in_user_id,PROFESSIONAL)

def edit_professional_task(logged_in_user_id):
    edit_user_task(logged_in_user_id,PROFESSIONAL_TASKS)

def remove_past_professional_tasks(logged_in_user_id):
    remove_past_user_tasks(logged_in_user_id,PROFESSIONAL_TASKS)