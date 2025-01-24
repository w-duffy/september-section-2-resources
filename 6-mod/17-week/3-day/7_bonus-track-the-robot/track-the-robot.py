# A robot has been given a list of movement instructions. Each instruction is
# either _left_, _right_, _up_ or _down_, followed by a distance to move. The
# robot starts at [0, 0]. You want to calculate where the robot will end up and
# return its final position as a list. For example, if the robot is given the
# instructions `["right 10", "up 50", "left 30", "down 10"]`, it will end up 20
# left and 40 up from where it started, so you should return `[-20, 40]`.


def track_robot(moves: list[str]):
    position = {"x": 0, "y": 0}
    mod = {"right": ("x", 1), "up": ("y", 1), "left": ("x", -1), "down": ("y", -1)}

    for move in moves:
        direction, val = move.split()
        pos, multi = mod[direction]

        position[pos] += int(val) * multi

    return list(position.values())

# #! a/A's less convoluted solution
# def track_robot(instructions):
#     totals = {"left": 0, "right": 0, "up": 0, "down": 0}
#     for step in instructions:
#         step = step.split()
#         totals[step[0]] += int(step[1])
#     return [totals["right"] - totals["left"], totals["up"] - totals["down"]]


print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]
