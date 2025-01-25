#  Stacks

# Create a function named stack that keeps the scores of a game with specific
# rules. At the beginning of the game, you start with an empty record. You are
# given a list of strings, some strings have a special rule applied to the
# record.

# An integer n.
# Record a new score of n.

# The symbol '+'.
# Records a new score that is the sum of the previous two scores.

# 'T'.
# Record a new score that is the Triple of the previous score.

# 'P'.
# Removes the previous score from the record.

#!!START
def stack(lst):
    stack = []

    for x in lst:
        if x == "+" and len(stack) >= 2:
            add = stack[-2] + stack[-1]
            stack.append(add)
        elif x == "T" and len(stack) >= 1:
            triple = stack[-1]*3
            stack.append(triple)
        elif x == "P":
            stack.pop()
        else:
            stack.append(int(x))
    return sum(stack)
#!!END

lst = ["10","5","P","T","+"]

print(stack(lst)) # 80
