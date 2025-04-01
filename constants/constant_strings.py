from enum import Enum
class ConstantStringEnum(Enum):
    
    ZERO:str='0'
    ONE:str='1'
    TWO:str='2'
    THREE:str='3'
    FOUR:str='4'
    FIVE:str='5'
    SIX:str='6'
    SEVEN:str='7'
    EIGHT:str='8'
    NINE:str='9'
    TEN:str='10'
    ELEVEN:str='11'
    EXIT:str='exit'

    WELCOME_STRING:str='''
    Welcome to CALENDAR SCHEDULING SYSTEM
    please follow the guide to perform the actions
    '''

    DASHBOARD_GUIDE:str='''
    Please enter :
    1 for user dashboard 
    2 for admin dashboard
    0 to end the program
    '''
    USER_DASHBOARD_GUIDE:str='''
    Please enter :
    1 for user login using user_id and password
    2 for registering as a new user
    3 for viewing your pending requests
    0 for returning to main menu
    '''
    ADMIN_DASHBOARD_GUIDE:str='''
    Please enter : 
    1 for admin login
    0 for returning to main menu
    '''


    INVALID_USER_ID:str='Entered user id is invalid. please try again'
    ZERO_TO_BACK:str='Enter 0 to return back to menu'
    
    ADMIN_NAME_INPUT:str="Please enter admin name : "
    ADMIN_PASSWORD_INPUT:str='Please enter password for admin : '
    ADMIN_NAME_NOT_EXISTS:str='Entered admin name does not exists'
    ADMIN_LOGIN_SUCCESS:str='Admin login successful'
    NO_ADMIN_EXISTS:str='No admin exists in the system'

    INVALID_PASSWORD:str='Entered password is invalid'

    USER_ID_INVALID_FORMAT:str='Entered user id is invalid, user id should always be a positive integer'

    USER_LOGIN_SUCCESS:str='user login was successful'
    
    LOGIN_FAILED:str='login failed'
    
    LOGIN_SUCCESS:str='user login successfully login id :'
    
   
    
    ENTER_USER_NAME:str='Please enter users username : '
    ENTER_CONFIRM_PASSWORD:str='Please enter password again to confirm : \n'
    ENTER_USER_ID:str='Please enter userid :\n'
    ENTER_USER_PASSWORD:str='Please enter password :\n'
    
    PENDING_REQUEST_EMPTY:str='There are no pending requests'
    USER_NAME_NOT_EXISTS:str='Entered user name does not exists in pending requests'
    
    NEW_REGISTRATION_WELCOME:str='''
    Welcome to registration of a new user
    in the registration process user has to file a request for approval by admin
    after entering the user name and password you wish to assign, it goes to pending approvals and after
    the approval by admin you become a user for this system.
    '''
    
    CONFIRM_REGISTRATION:str='''
    Do you wish to register as a new user with the provided name and password
    Please enter 
    'yes' to confirm 
    'cancel' to cancel the request process
    anything else for going again
    your provided name is : '''
    
    REGISTRATION_REQUEST_ADDED:str='The registration request for the following name is recorded kindly wait for the admins approval.'
    
    YES:str='yes'
    NO:str='no'
    CANCEL:str='cancel'
    
    USER_REGISTER_SUCCESS:str='user registration successful'
    USER_REGISTER_FAIL:str='user registration failed'
    PASSWORD_NOT_MATCH:str='password and confirm password dont match'
    
    CONFIRM_USER_NAME:str='''
    Do you wish to continue with the entered user name 
    Please Enter 
    'yes' for yes 
    'cancel' for canceling request
    anything else for going again
    your entered user name is : 
    '''
    
    NAME_EXISTS_PENDING_LIST:str='user name already exists in pending requests data, please pick some other name'
    
    USER_LOGGED_IN_DASHBOARD:str='''
    Please enter 
    1 to work with personal tasks
    2 to work with professional tasks
    3 to change password
    4 to show personal information
    5 to edit personal info
    6 to send someone message
    7 to view messages
    0 to logout
    '''
    
    ADMIN_LOGGED_IN_DASHBOARD:str='''
    Please enter
    1 to show pending registration requests
    2 to show user data
    3 to show today's tasks
    4 to create new task
    5 to change password
    6 to create new user
    7 to show all user ids
    8 to show calendar
    9 to show all teams
    10 to send messages
    11 to show message
    0 to log out
    '''
    
    
    