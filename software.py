# Type software names that are okay to be inputted into. Make sure to include the .exe extension.
# For example, notepad will be "notepad.exe" in the list
# If not sure what the process name is, check Task Manager
# For your safety, only include software you intend for users to interact with.
ApprovedExeProcesses = []

# Type user names that should not be allowed to input commands
# Useful for banning bots or trolls from inputting commands, either by accident or on purpose
BannedUsers = []

UseMode = 1 # 0 for false, 1 for true

# Enter as many names as you wish to here, as these are essentially different profiles for your Twitch Plays, so you can jump between different games or software.
# This will require you to also program in the logic in which games or software reacts to the chat commands in the main.py file yourself. The names must match the names in this list.
# I recommend adding the .lower() function to the names in the list, so that the names are not case sensitive.
SoftwareFormats = []
