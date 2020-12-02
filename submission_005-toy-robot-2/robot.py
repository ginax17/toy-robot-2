#valid commands = [off','help']
current_direction_index = 0
position_x = 0
position_y = 0
degrees = 0

def ask_robot_name():
    """ Ask the user to name the robot and we return the newly created robot name"""
    return input("What do you want to name your robot? ") 

def robot_greeting(robot_name):
    """Prints the user's robot name along with a hello message"""
    print(robot_name +": Hello kiddo!")

def get_commands(robot_name):
    """Gets an input of a commands """
    correct = False
    while not correct:
        commands = input(f"{robot_name}: What must I do next? ")
        command = split_command(commands.lower())
        number_steps = 0
        # print(command[1].isdigit())

        if not validate_commands(command[0].lower(),number_steps) \
        or (not command[1].isdigit() and command[0].lower() == 'forward'):

            print(f"{robot_name}: Sorry, I did not understand '{commands}'.")
            continue
            
        if command[0] == 'forward' and command[1].isdigit():
            number_steps = int(command[1])
        
        if command[0] == 'back' and command[1].isdigit():
            number_steps = int(command[1])

        if command[0] == 'sprint' and command[1].isdigit():
            number_steps = int(command[1])        

        correct = commands_perform_tasks(robot_name,command[0].lower(),number_steps)


def split_command(command):
    command = command.split()
    if len(command) == 1:
        return command[0], ''
    else:
        return command[0], command[1]

def validate_commands(command,number_steps = None):
    """A list of commands are checked and a bool in returned after """
    commands_list = ['off','help','forward','back','right','left','sprint']
    if command not in commands_list:
        return False
    else:
        return True

def commands_perform_tasks(robot_name,command,number_steps):
    """Commands are checked then their respective functions are then called to perform the command's tasks """
    correct = False
    if command == 'off':
        turn_robot_off(robot_name,command)
        correct = True
    elif command == 'help':
        print(robot_help_command(robot_name,number_steps,command))
    elif command == 'forward':
        
        print(tracking_robot_position(robot_name,number_steps,command))
    elif command == 'back':
        
        print(tracking_robot_position(robot_name,number_steps,command))
    elif command == 'right':
        print(robot_turn_right_command(robot_name))
        print(tracking_robot_position(robot_name,number_steps,command))
    elif command == 'left':
        print(robot_turn_left_command(robot_name))
        print(tracking_robot_position(robot_name,number_steps,command))
    elif command == 'sprint':
        sprint(robot_name,number_steps)
        print(tracking_robot_position(robot_name,0,command))
    return correct

def turn_robot_off(robot_name,command):
    """output displays to the user once user types 'off' """ 
    print(f"{robot_name}: Shutting down..")

def robot_help_command(robot_name,number_steps,command):
    """Output returned when the user types 'help' as a command """

    return "I can understand these commands:\n\
OFF  - Shut down robot\n\
HELP - provide information about commands\n\
FORWARD - robot moves in the forward direction\n\
POSITION - robot moves in x,y positions\n\
BACK - robot moves in the backward direction\n\
RIGHT - robot turns right by number of degrees\n\
LEFT - robot turns left by number of degrees"

def robot_forward_command(robot_name,number_steps):
    """Returns the number of steps for the forward command"""
    global position_x
    global position_y

    # if position_x - number_steps <= -100 or position_x + number_steps >= 100:
    #     print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
    # elif position_y - number_steps <= -200 or position_y + number_steps >= 200:
    #     f"{robot_name}: Sorry, I cannot go outside my safe zone."

    return f" > {robot_name} moved forward by {number_steps} steps."

def tracking_robot_position(robot_name,number_steps,command):
    """Function that tracks a robot's x,y position"""
    #Eposition_y += number_steps
    global position_x
    global position_y
    new_position_y = position_y
    global degrees

    if position_x - number_steps <= -100 or position_x + number_steps >= 100:
        print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
    elif position_y <= -200 or position_y >= 200:
        print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")

    else:
        if degrees == 0:
            if command == 'forward':
                position_y += number_steps
                
            elif command == 'back':
                position_y -= number_steps
        elif degrees == 90:
            if command == 'forward':
                position_x += number_steps
            elif command == 'back':
                position_x -= number_steps
        elif degrees == 180:
            if command == 'forward':
                position_y -= number_steps
            elif command == 'back':
                position_y += number_steps
        elif degrees == 270:
            if command == 'forward':
                position_x -= number_steps
                
            elif command == 'back':
                position_x += number_steps
        elif degrees > 270:
            degrees = 0
            return tracking_robot_position(robot_name, number_steps)
        else:
            degrees += 360
            return tracking_robot_position(robot_name,number_steps,command)
        
        if command == 'forward':
            print(robot_forward_command(robot_name, number_steps))
        if command == 'back':
            print(robot_moves_backwards(robot_name,number_steps))

    return f" > {robot_name} now at position ({position_x},{position_y})."

# def tracking_robot_negative_position(robot_name,number_steps):
#     """Function that tracks the robot's negative position in different directions """
#     position_x = 0
#     position_y = 0
#     return f"> {robot_name} now at position (0,-{number_steps})."

def robot_moves_backwards(robot_name,number_steps):
    """Function to process instructions when the robot moves backwards"""
    global position_y
    return f" > {robot_name} moved back by {number_steps} steps."

def robot_turn_right_command(robot_name):
    """Returns output of turn right command"""
    global degrees
    if degrees == 270:
        degrees = 0
    else:
        degrees += 90
    return f" > {robot_name} turned right."

def robot_turn_left_command(robot_name):
    """Returns output of the turn left command"""
    global degrees
    if degrees == 0:
        degrees = 270
    else:
        degrees -= 90
    return f" > {robot_name} turned left."

def sprint(robot_name,number_steps):
    global position_x
    global position_y
    if degrees == 0:
        position_y += number_steps
    elif degrees == 90:
        position_x += number_steps
    elif degrees == 180:
        position_y -= number_steps
    elif degrees == 270:
        position_x -= number_steps
    # elif degrees > 270:
    #     degrees = 0
    #     return tracking_robot_position(robot_name, number_steps)
    # else:
    #     degrees += 360
    #     return tracking_robot_position(robot_name,number_steps)
    if number_steps <= 0:
        return number_steps
    else:
        print(f" > {robot_name} moved forward by {number_steps} steps.")
        return sprint(robot_name,number_steps - 1)

def robot_start():
    """This is the entry function, do not change"""
    global position_x
    global position_y
    global current_direction_index
    global degrees
    current_direction_index = 0
    position_x = 0
    position_y = 0
    degrees = 0
    robot_name = ask_robot_name()
    robot_greeting(robot_name)
    command = get_commands(robot_name)

if __name__ == "__main__":
    robot_start()
