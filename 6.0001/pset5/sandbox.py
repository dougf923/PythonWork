import string
import time
from datetime import datetime
from datetime import timedelta

# phrase = "I@$%#went to tHe Store"
# text = "One@@day!! I WENT to THE store."


# phrase_list = [];
# phrase_list_count = 0;
# new_word = True;

# for s in range(len(phrase)):
# 	if phrase[s] == " " or phrase[s] in string.punctuation:
# 		if s < len(phrase)-1:
# 			if phrase[s+1] in string.ascii_lowercase or phrase[s+1] in string.ascii_uppercase:

# 				phrase_list[phrase_list_count] = phrase_list[phrase_list_count].lower();
# 				phrase_list_count += 1;
# 				new_word = True;
# 	elif new_word:
# 		phrase_list.append(phrase[s]);
# 		new_word = False;
# 	else:
# 		phrase_list[phrase_list_count] = phrase_list[phrase_list_count]+phrase[s]

# phrase_list[phrase_list_count] = phrase_list[phrase_list_count].lower();


# len_phrase_list = len(phrase_list);

# text_list = [];
# text_list_count = 0;
# new_word = True;


# for s in range(len(text)):
# 	if text[s] == " " or text[s] in string.punctuation:
# 		if s < len(text)-1:
# 			if text[s+1] in string.ascii_lowercase or text[s+1] in string.ascii_uppercase:

# 				text_list[text_list_count] = text_list[text_list_count].lower();
# 				text_list_count += 1;
# 				new_word = True;
# 	elif new_word:
# 		text_list.append(text[s]);
# 		new_word = False;
# 	else:
# 		text_list[text_list_count] = text_list[text_list_count]+text[s]


# text_list[text_list_count] = text_list[text_list_count].lower();

# print(phrase_list)
# print(text_list)

# for elem in range(len(text_list)):
# 	if text_list[elem] == phrase_list[0]:
# 		count = 1;
# 		for i in range(len_phrase_list):
# 			if count == len_phrase_list:
# 				return_var = True;
# 				print(return_var)
# 			if elem+i+1 < len(text_list) and text_list[elem+i+1] == phrase_list[i+1]:
# 				count += 1;
		


# return_var  = False;
# print(return_var)

from ps5 import *

# sam_time = "3 Oct 2016 17:00:10";
# sam_time2 = "4 Oct 2016 17:00:10";

# struct_time = datetime.strptime(sam_time, "%d %b %Y %H:%M:%S");

# future_time = datetime(2087, 10, 15)



# print(future_time.minute)
# future_time = future_time.replace(tzinfo=pytz.timezone("EST"))
# future = NewsStory('', '', '', '', future_time)


# struct_time = datetime.strptime(sam_time, "%d %b %Y %H:%M:%S");
# struct_time = struct_time.replace(tzinfo=pytz.timezone("EST"))
# struct = NewsStory('','','','',struct_time)



# print (struct.get_pubdate()> future.get_pubdate())

# lines = ['ADD,t1','t1,TITLE,TIT'];

# for l in range(len(lines)):
# 	a = lines[l].split(',')
# 	print(a)
# 	print(lines[l].split(',') )

# for l in a:
# 	print(l)	


# current_line = ["a","b","c","d"]
# print( current_line[2:len(current_line)])

t =  TitleTrigger("doug")
print(t)
print(type(t))
plural    = NewsStory('', '', 'Purple cows are cool!', '', datetime.now())

print(t.evaluate(plural))

print(string.punctuation)