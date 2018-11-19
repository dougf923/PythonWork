
import string

# test_string = "I am a rock"
# split_test = test_string.split()
# print(split_test)

shift = 2
shift_dict = {}

alph_lower = string.ascii_lowercase 
alph_upper = string.ascii_uppercase


for i in range(26):
    if i+shift < 26:
        shift_dict[alph_lower[i]] = alph_lower[i+shift]
        shift_dict[alph_upper[i]] = alph_upper[i+shift]
    else:
        overlap_shift = i+shift-26
        shift_dict[alph_lower[i]] = alph_lower[overlap_shift]     
        shift_dict[alph_upper[i]] = alph_upper[overlap_shift]  

print(shift_dict['z'])