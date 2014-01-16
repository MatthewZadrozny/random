#!/usr/bin/python
# -*- coding: latin-1 -*
#pocketParser.py
#Author: m.zadrozny@gmail.com
#Date: 2014-01-16
#Requests getpocket.com html data export and dumps it into a 
#  ` -delimitted text file
#Data should be marked as UTF-8 when imported into spreadsheet

import datetime, re, Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()
file_path = tkFileDialog.askopenfilename() 
s = tkFileDialog.askopenfilename() 

pat_url = re.compile('<a href=".+?"')
pat_tags = re.compile('tags=".+?"')
pat_title = re.compile('<.*?>') #('>.+</a>')
pat_time = re.compile('time_added=".+?"')
status = 'Unread'

with open(s) as i, open('pocket_output.txt', 'w') as o: 
	for line in i: 
		if '<h1>Read Archive</h1>' in line: status = 'Read'
		elif '<li>' in line: 
			url = pat_url.findall(line)[0][9:-1]
			time = pat_time.findall(line)[0][12:-1]
			title = pat_title.sub('', line).strip().strip('\n')
			try: tags = pat_tags.findall(line)[0][6:-1]
			except: tags = 'no_tag' #older untagged articles seem to have been saved as ''

			time = (datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S'))

			entry = '`'.join([title, time, tags, url, status, '\n'])

			o.write(entry)