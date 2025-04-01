from controller import start_program as start
from utils import update_user_json_file
def main():
    update_user_json_file()
    start.program_start()

main()

