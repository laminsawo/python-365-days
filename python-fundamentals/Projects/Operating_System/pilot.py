import os


os_name = os.name
sys_path = os.path
cpu_count = os.cpu_count()
process_id = os.getpid()
logged_user = os.getlogin()

details = [os_name, sys_path, cpu_count, process_id, logged_user]

for detail in details:
    if detail == os_name:
        print("The OS name is: %s" % detail)
    elif detail == sys_path:
        print('The system path is: %s' % detail)
    elif detail == cpu_count:
        print('Number of CPUs is: %s' % detail)
    elif detail == process_id:
        print('The Process ID is: %s' % detail)
    elif detail == logged_user:
        print('Current user: is %s' % detail)
