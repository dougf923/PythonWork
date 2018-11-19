# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, desc, link, pubdate):
        '''
        Initializes a NewsStory object


        a NewsStory object has five attributes:
            self.guid (string, determined by input guid)
            self.title (string, determined by input title)
            self.description (string, determined by input desc)
            self.link (string, determined by input link)
            self.pubdate (datetime, determined by input pudbate)
            




        '''
        self.guid = guid
        self.title = title
        self.description = desc
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid

    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title   

    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description   

    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link   

    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate       

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
	def __init__(self,phrase):
		#Initializes a Phrase Trigger object


        #    a Phrase Trigger object has one attribute:
        #    self.phrase (string, determined by input phrase)
		self.phrase = phrase        


	def is_phrase_in(self, text):

		numeral = ["1","2","3","4","5","6","7","8","9","0"];

		# Make list of each word in the phrase and make all elements lowercase
		phrase_list = [];
		phrase_list_count = 0;
		new_word = True;

		for s in range(len(self.phrase)):
			if self.phrase[s] == " " or self.phrase[s] in string.punctuation:
				if s < len(self.phrase)-1:
					if self.phrase[s+1] in string.ascii_lowercase or self.phrase[s+1] in string.ascii_uppercase or self.phrase[s+1] in numeral:
						if phrase_list_count < len(phrase_list):
							phrase_list[phrase_list_count] = phrase_list[phrase_list_count].lower();
						phrase_list_count += 1;
						new_word = True;
			elif new_word:
				phrase_list.append(self.phrase[s]);
				new_word = False;
			else:
				phrase_list[phrase_list_count] = phrase_list[phrase_list_count]+self.phrase[s]


		if phrase_list_count < len(phrase_list):		
			phrase_list[phrase_list_count] = phrase_list[phrase_list_count].lower();
		len_phrase_list = len(phrase_list);

		# Make list of each word in the text and make all elements lowercase
		text_list = [];
		text_list_count = 0;
		new_word = True;


		for s in range(len(text)):
			if text[s] == " " or text[s] in string.punctuation:
				if s < len(text)-1:
					if text[s+1] in string.ascii_lowercase or text[s+1] in string.ascii_uppercase or text[s+1] in numeral:
						if text_list_count < len(text_list):	
							text_list[text_list_count] = text_list[text_list_count].lower();
						text_list_count += 1;
						new_word = True;
			elif new_word:
				text_list.append(text[s]);
				new_word = False;
			else:
				if text_list_count < len(text_list):
					text_list[text_list_count] = text_list[text_list_count]+text[s]

		if text_list_count < len(text_list):
			text_list[text_list_count] = text_list[text_list_count].lower();

			

		# Check if the phrase list appears in order at any point in the text list
		
		match_count = 0;
		for elem in range(len(text_list)):
			if text_list[elem] == phrase_list[0]:
				match_count = 1;
				for i in range(len_phrase_list-1):
					if elem+i+1 < len(text_list):
						if text_list[elem+i+1] == phrase_list[i+1]:
							match_count += 1;

				
		if match_count == len_phrase_list:
			return True
		else:
			return False
		



# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
	def __init__(self,phrase):
		#Initializes a Title Trigger object


        #    a Title Trigger object has one attribute:
        #    self.phrase (string, determined by input phrase)

		PhraseTrigger.__init__(self,phrase)

	def evaluate(self, story):
		title = story.get_title()
		return PhraseTrigger(self.phrase).is_phrase_in(title)



# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
	def __init__(self,phrase):
		#Initializes a Description Trigger object


        #    a Description Trigger object has one attribute:
        #    self.phrase (string, determined by input phrase)

		PhraseTrigger.__init__(self,phrase)

	def evaluate(self, story):
		desc = story.get_description()
		return PhraseTrigger(self.phrase).is_phrase_in(desc)

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
	def __init__(self,time):

		#Initializes a Time Trigger object

        #    a Time Trigger object has one attribute:
        #    self.time (datetime, determined by input string time)
		
		struct_time = datetime.strptime(time, "%d %b %Y %H:%M:%S");
		struct_time = struct_time.replace(tzinfo=pytz.timezone("EST"))

		self.time = struct_time



# Problem 6
# TODO: BeforeTrigger and AfterTrigger


class BeforeTrigger(TimeTrigger):
	def __init__(self,time):

		TimeTrigger.__init__(self,time)

	def evaluate(self,story):

		publish_time = story.get_pubdate()
		publish_time = publish_time.replace(tzinfo=pytz.timezone("EST"))


		if publish_time < self.time:
			return True
		else:
			return False	

class AfterTrigger(TimeTrigger):
	def __init__(self,time):

		TimeTrigger.__init__(self,time)

	def evaluate(self,story):

		publish_time = story.get_pubdate()
		publish_time = publish_time.replace(tzinfo=pytz.timezone("EST"))


		if publish_time > self.time:
			return True
		else:
			return False




# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
	def __init__(self,other):

		self.InputTrigger = other;

	def evaluate(self, story):
		a = self.InputTrigger.evaluate(story)

		if a:
			return False
		else:
			return True		

# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
	def __init__(self,other1,other2):

		self.InputTrigger1 = other1;
		self.InputTrigger2 = other2;

	def get_input1(self):
		return self.InputTrigger1	


	def get_input2(self):
		return self.InputTrigger2	

	def evaluate(self, story):
		a = self.get_input1()
		b = self.get_input2()
		c = a.evaluate(story)
		d = b.evaluate(story)

		if c and d:
			return True
		else:
			return False		




# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
	def __init__(self,other1,other2):

		self.InputTrigger1 = other1;
		self.InputTrigger2 = other2;

	def evaluate(self, story):
		a = self.InputTrigger1.evaluate(story)
		b = self.InputTrigger2.evaluate(story)

		if a or b:
			return True
		else:
			return False


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    sorted_stories_list = [];

    for s in stories:
    	trig = False;
    	for tr in triggerlist:
    		if tr.evaluate(s):
    			trig = True;
    	if trig:		
    		sorted_stories_list.append(s)
    				



    return sorted_stories_list



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    trigger_options = {};
    trigger_list = [];
    for l in lines:
    	current_line = l.split(',') 

    	if current_line[0] != "ADD":
    		trigger_options[current_line[0]] = create_trigger_instance(current_line[1], current_line[2:len(current_line)], trigger_options);
    		#print(trigger_options)
    	else:
    		for i in range(len(current_line)-1):
    			trigger_list.append(trigger_options[current_line[i+1]])	
    return trigger_list


    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll



def create_trigger_instance(trigger_type,arg_list, trigger_dict):
	type1 = ["TITLE", "DESCRIPTION", "AFTER", "BEFORE", "NOT"];
	type2 = ["AND", "OR"];

	if trigger_type in type1:
		if len(arg_list) != 1:
			error("Configuration Error: Wrong number of input arguments")

	if trigger_type in type2:
		if len(arg_list) != 2:
			error("Configuration Error: Wrong number of input arguments")	

	if trigger_type == "TITLE":
		return TitleTrigger(arg_list[0]);
	elif trigger_type == "DESCRIPTION":
		return  DescriptionTrigger(arg_list[0]) 	
	elif trigger_type == "AFTER":			
		return AfterTrigger(arg_list[0])
	elif trigger_type == "BEFORE":			
		return  BeforeTrigger(arg_list[0])	
	elif trigger_type == "NOT":		
		return  NotTrigger(trigger_dict[arg_list[0]])
	elif trigger_type == "AND":			
		return AndTrigger(trigger_dict[arg_list[0]],trigger_dict[arg_list[1]])
	elif trigger_type == "OR":			
		return OrTrigger(trigger_dict[arg_list[0]],trigger_dict[arg_list[1]])		
	else:			
		error("Configuration Error: Trigger type not recognized")










def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
				        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")
            
            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))
           
            stories = filter_stories(stories, triggerlist)
            
            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

