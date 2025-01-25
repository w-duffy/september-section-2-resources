# A robot has been given a list of movement instructions. Each instruction is
# either _left_, _right_, _up_ or _down_, followed by a distance to move. The
# robot starts at [0, 0]. You want to calculate where the robot will end up and
# return its final position as a list. For example, if the robot is given the
# instructions `["right 10", "up 50", "left 30", "down 10"]`, it will end up 20
# left and 40 up from where it started, so you should return `[-20, 40]`.

# Write your function here.
#!!START SILENT
def track_robot(instructions):
    totals = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
    for step in instructions:
        step = step.split()
        totals[step[0]] += int(step[1])
    return [totals['right'] - totals['left'], totals['up'] - totals['down']]
#!!END

print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]