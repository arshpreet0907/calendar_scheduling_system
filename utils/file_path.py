import os

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))# Get the directory of the current file
    project_folder=os.path.dirname(current_dir)
    file_path = os.path.join(project_folder,'model','json', filename)
    return file_path

def get_user_credential_file_path():
    return get_file_path('user_credentials.json')
    
def get_pending_request_file_path():
    return get_file_path('pending_requests.json')

def get_admin_credential_file_path():
    return get_file_path('admin_credentials.json')

def get_user_data_file_path(user_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_folder=os.path.dirname(current_dir)
    
    file_path = os.path.join(project_folder,'model','users',  f'{user_id}.json')
    return file_path