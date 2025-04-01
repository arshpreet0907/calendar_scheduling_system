
from .user.dashboard_actions import user_registration
from .user.dashboard_actions import user_log_in
from .user.dashboard_actions import view_pending_request

from .admin.dashboard_actions import admin_login

from .admin.logged_in_actions import pending_requests
from .admin.logged_in_actions import change_password_admin
from .admin.logged_in_actions import show_all_user_data
from .admin.logged_in_actions import show_all_user_ids
from .admin.logged_in_actions import show_todays_tasks
from .admin.logged_in_actions import create_new_user
from .admin.logged_in_actions import create_new_task
from .admin.logged_in_actions import show_admin_calendar
from .admin.logged_in_actions import show_all_teams

from .user.logged_in_actions import change_password_user
from .user.logged_in_actions import edit_personal_info
from .user.logged_in_actions import work_with_personal_tasks
from .user.logged_in_actions import work_with_professional_tasks
from .user.logged_in_actions import show_personal_information
from .user.logged_in_actions import send_message
from .user.logged_in_actions import show_message