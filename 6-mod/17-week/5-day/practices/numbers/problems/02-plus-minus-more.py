# Now it's time to explore numbers in Python: int and float. Follow the
# directions provided in the starting code. In total, you should add 14 print
# commands to complete this activity.

# DO NOT EDIT - Setup for exploration
# tiny number
int1 = 5
float1 = 5.0
# small number
int2 = 135
float2 = 135.246
# huge number known as `googol`
int3 = 10**100
float3 = 10.0**100

# STEP 1: Print and compare tiny numbers
print('** FIVE **')

# 1A: Print int1
#!!START SILENT
print(int1)
#!!END

# 1B: Print float1
#!!START SILENT
print(float1)
#!!END

# 1C: Print equality comparison (==) between int1 and float1
#!!START SILENT
print(int1 == float1)
#!!END

# STEP 2: Print and compare huge numbers
print('\n** GOOGOL **')

# 2A: Print int3
#!!START SILENT
print(int3)
#!!END

# 2B: Print float3
#!!START SILENT
print(float3)
#!!END

# 2C: Print equality comparison (==) between int1 and float3
#!!START SILENT
print(int3 == float3)
#!!END

# STEP 3: Compare results of integer division in all 4 possible combinations
print('\n** INTEGER DIVISION **')

# 3A: Print int2 divided by int1 (//)
#!!START SILENT
print(int2 // int1)
#!!END

# 3B: Print float2 divided by float1 (//)
#!!START SILENT
print(float2 // float1)
#!!END

# 3C: Print float2 divided by int1
#!!START SILENT
print(float2 // int1)
#!!END

# 3D: Print int2 divided by float1
#!!START SILENT
print(int2 // float1)
#!!END

# STEP 4: Compare results of mod in all 4 possible combinations
print('\n** MOD **')
# Copy/paste 4 statements from STEP 3 and switch operator to mod (from // to %)

# 4A: Print int2 mod int1 (%)
#!!START SILENT
print(int2 % int1)
#!!END

# 4B: Switch both numbers to float
#!!START SILENT
print(float2 % float1)
#!!END

# 4C: Float divided by int
#!!START SILENT
print(float2 % int1)
#!!END

# 4D: Int divided by float
#!!START SILENT
print(int2 % float1)
#!!END
