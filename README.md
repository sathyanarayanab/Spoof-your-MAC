# Spoof-your-MAC
Spoof your MAC address with this simple Python tool easily.
## Why This tool?
This is a simple tool but just added a `profiles.csv` file to use MAC address from the particular profile name.
## Installation Guide
Download the zip file of the project or clone this project.
#### Downloading Zip file
Go to the downloads folder and enter the following commands
```
unzip Spoof-your-MAC-main.zip
cd Spoof-your-MAC
```
#### Cloning the Project
```
git clone https://github.com/Sathya-Narayana2001/Spoof-your-MAC.git
cd Spoof-your-MAC
```
## Usage
This python tool is very simple and basic. This has very few flags.
- Open the help option either by `-h` or by `--help` flag.
- Specify the interface by `-i` or `--interface` flag.
- Specify the MAC address manually by using `-m` or `--mac` flag.
- Randomize the new MAC address by using the `-r` or `--random` flag.
- Use the MAC address saved in `profiles.csv` by `-p` or `--profile` flag and profile name.
- Save the New MAC to the `profiles.csv` by `-n` or `--new` flag.
- List all the saved names and MAC from `profiles.csv` by `-l` or `--list` flag.
## Examples
- To manually Spoof MAC ` python3 spoofer.py -i [interface] -m [manual mac address]`
- To manually Spoof MAC and create a new profile ` python3 spoofer.py -i [interface] -m [manual mac address] -n [new_name]`
- To randomize the MAC and Spoof ` python3 spoofer.py -i [interface] -r `
- To use MAC from saved profile ` python3 spoofer.py -i [interface] -p [profile_name]`
## Note
This tool works only on Linux in which python has been installed. It works both in python2 and python3. Open and edit `profiles.csv` and configure as required or create a profile while spoofing the MAC.
## Additional info
I know this is very basic tool yet managed to implement randomizing MAC and profiling MAC and I'm new to coding. So I am very open to learn from others. Please correct me if I'm wrong or help me to use the variables or functions efficently without any hesitation. Happy to learn always :)
