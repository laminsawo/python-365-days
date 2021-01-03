import socket


def get_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    print("host name is: \t %s " % host_name)
    print("This machines IP address is: \t %s" % ip_address)


get_machine_info()
