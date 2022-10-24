import itertools

# Get message string
message = input()

# Convert message to binary
bin_msg = ''.join(bin(ord(char)).replace('0b','').zfill(7) for char in message)

# Seperate bin_msg into groups
bin_grp = [''.join(grp) for _, grp in itertools.groupby(bin_msg)]

# Apply binary to unary rules
uni_msg = ''.join(('00 ', '0 ')["1" in grp] + len(grp) * '0' + ' ' for grp in bin_grp)[:-1]

# Print result
print(uni_msg)
