#!/user/bin/env python
import subprocess
import optparse
import re
import random
import csv


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def change_mac(interface, new_mac, c_mac):
    print(bcolors.OKGREEN +
          bcolors.BOLD + "\n----------> Changing the MAC address of " + interface + " from " + str(
        c_mac) + " to " + new_mac + bcolors.ENDC)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def check_same(mac, new_mac):
    if mac == new_mac:
        print(bcolors.OKCYAN + "\n\n\nAlready having the given MAC address " + mac + "\n\n\n" + bcolors.ENDC)
        exit()


def fetch_arguments():
    parse_arguments = optparse.OptionParser()
    parse_arguments.add_option("-i", "--interface", dest="interface",
                               help=bcolors.OKBLUE + "Interface which MAC has to be changed." + bcolors.ENDC)
    parse_arguments.add_option("-l", "--list", action="store_true", dest="list_all",
                               help=bcolors.OKBLUE + "List all the profile and assigned MAC from profiles.csv" + bcolors.ENDC)
    parse_arguments.add_option("-m", "--mac", dest="new_mac",
                               help=bcolors.OKBLUE + "Manually enter the New MAC address." + bcolors.ENDC + "\n\n\n")
    parse_arguments.add_option("-n", "--new", dest="new_name",
                               help=bcolors.OKBLUE + "Creates a new profile and saves in profiles.csv in the given name" + bcolors.ENDC)
    parse_arguments.add_option("-p", "--profile", dest="profile_name",
                               help=bcolors.OKBLUE + "Assigns MAC of given name from profiles.csv\n\n\n" + bcolors.ENDC)
    parse_arguments.add_option("-r", "--random", action="store_true", dest="is_random",
                               help=bcolors.OKBLUE + "Automatically Generates a random MAC." + bcolors.ENDC + "\n\n\n")

    (options, arguments) = parse_arguments.parse_args()
    if options.list_all:
        list_all_prof()
        exit()
    if options.is_random:
        options.new_mac = fetch_rand(options.interface)
    if options.new_name:
        f = open('profiles.csv', 'a')
        results = fetch_from_file()
        if options.new_name in results:
            print(bcolors.FAIL + "\n\n\nProfile already exists\n\n\n" + bcolors.ENDC)
            exit()
        else:
            f.write(options.new_name + "," + options.new_mac)
            f.write("\n")
            f.close()
            print(
                bcolors.BOLD + bcolors.OKGREEN + "\n\n\n---------->New profile " + options.new_name + " has been created\n\n\n" + bcolors.ENDC)
    if options.profile_name:
        results = fetch_from_file()
        try:
            options.new_mac = results[options.profile_name]['MAC']
        except:
            print(bcolors.FAIL + "No Such profile name found\n\n\n" + bcolors.ENDC)
            exit()
    if not options.interface:
        parse_arguments.error(
            bcolors.FAIL + "Please Specify an Interface to change MAC, use -h or --help for more info.\n\n\n" + bcolors.ENDC)
    elif not options.new_mac:
        parse_arguments.error(
            bcolors.FAIL + "Please specify a new MAC to be changed, use -h or --help for more info.\n\n\n" + bcolors.ENDC)
    return options


def fetch_from_file():
    f = open('profiles.csv', 'r')
    reader = csv.reader(f)
    profiles = {}
    for row in reader:
        profiles[row[0]] = {'MAC': row[1]}
    return profiles


def fetch_rand(iface):
    if "eth" in iface:
        mac = "02:%02x:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    else:
        mac = "%02x:%02x:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    return mac


def find_current_mac(interface):
    try:
        result = subprocess.check_output(["ifconfig", interface])
        refined_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
        if refined_result:
            return refined_result.group(0)
        else:
            print(bcolors.FAIL + "\nCould not read MAC address\n\n\n" + bcolors.ENDC)
    except subprocess.CalledProcessError:
        print(bcolors.FAIL + "\n\n\nNo such Device found\n\n\n" + bcolors.ENDC)
        exit()


def list_all_prof():
    results = fetch_from_file()
    print(bcolors.BOLD + bcolors.OKCYAN + str(results) + bcolors.ENDC)


def print_banner():
    print(bcolors.BOLD + """\n\n\n .oooooo..o                                 .o88o. 
d8P'    `Y8                                 888 `" 
Y88bo.      oo.ooooo.   .ooooo.   .ooooo.  o888oo  
 `"Y8888o.   888' `88b d88' `88b d88' `88b  888    
     `"Y88b  888   888 888   888 888   888  888    
oo     .d8P  888   888 888   888 888   888  888    
8""88888P'   888bod8P' `Y8bod8P' `Y8bod8P' o888o   
             888                                   
            o888o                                  
                                                   
oooooo   oooo                                      
 `888.   .8'                                       
  `888. .8'    .ooooo.  oooo  oooo  oooo d8b       
   `888.8'    d88' `88b `888  `888  `888""8P       
    `888'     888   888  888   888   888           
     888      888   888  888   888   888           
    o888o     `Y8bod8P'  `V88V"V8P' d888b          
                                                   
                                                   
                                                   
ooo        ooooo                                   
`88.       .888'                                   
 888b     d'888   .oooo.    .ooooo.                
 8 Y88. .P  888  `P  )88b  d88' `"Y8               
 8  `888'   888   .oP"888  888                     
 8    Y     888  d8(  888  888   .o8               
o8o        o888o `Y888""8o `Y8bod8P'               
                                                   
                                                   
                                                   """ + bcolors.BOLD + bcolors.WARNING + """By Sathya Narayana\n\n\n""" + bcolors.ENDC)


def print_error():
    print(
        bcolors.WARNING + "\nPlease make sure that the following conditions are satisfying\n1)You have specified the correct interface name\n2)You are running it as sudo\n3)The given MAC is unicast address ( First byte is even).\n4)The given address has Six groups of two hexadecimal digits.\n\n\n" + bcolors.ENDC)


def verify_op(new_mac, new_op):
    if new_mac == new_op:
        print(bcolors.OKGREEN +
              bcolors.BOLD + "\n----------> Success: The MAC address of " + option.interface + " has been changed to " + str(
            new_mac) + '\n\n\n' + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Error: Failed to change MAC to " + str(
            new_mac) + bcolors.ENDC)
        print_error()


print_banner()
option = fetch_arguments()
current_mac = find_current_mac(option.interface)
check_same(current_mac, option.new_mac)
change_mac(option.interface, option.new_mac, current_mac)
after_op = find_current_mac(option.interface)
verify_op(option.new_mac, after_op)
