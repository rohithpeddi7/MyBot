from tkinter import *
from textwrap3 import wrap
from AppOpener import run

from io import StringIO # Python3 use: from io import StringIO
import sys

# GUI
root = Tk()
root.title("MyBot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

import os
import openai

openai.api_key = "sk-LfURf8m7mqGQZ9PIR1Y2T3BlbkFJD4poErFSUfCvn4EhV"# add X2m at end
os.environ["OPENAI_API_KEY"] = openai.api_key
# openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt(query):
	response = openai.Completion.create(
	model="text-davinci-003",
	prompt=query,
	temperature=0.9,
	max_tokens=500,
	top_p=1,
	frequency_penalty=0.0,
	presence_penalty=0.6,
	stop=[" Human:", " AI:"]
	)
	return response["choices"][0]["text"].strip()

def all_commands():
	cmds = {"-h or help":"Open manual",
			"<no option> query": "Use gpt-3 to answer your query",
			"-o <AppName>":"Open Application",
			"-o ls":"List All Applications",
			"-o find <AppName>":"Find Application",
			"-o update -m <AppName>":"Update Application Manually",
			}
	count=0
	ans="The following are the options::\n"
	for cmd,func in cmds.items():
		count+=1
		ans+=str(count)+". "+cmd+" : "+func+"\n"
	return ans

# Send function
def send():
	send_this = "You : " + e.get()
	txt.insert(END, "\n" + send_this)
	user = e.get().lower().strip()
	try:
		if user[0:2]=="-o":
			app = user[2:].strip()
			sys.stdout = mystdout = StringIO()
			old_stdout = sys.stdout
			run(app)
			answer = mystdout.getvalue()
		else:
			try:
				if str(user)=="-h" or str(user)=="help":
					answer=all_commands()
				else:
					answer = gpt(user)
			except Exception as er:
				answer =gpt(user)
	except Exception as er:
		print(user)
		print(type(er).__name__)
		answer="Enter valid input! or report an error."
	txt.insert(END, "\n" + "Bot : "+answer)
	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="AI assistant", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=50)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

txt.insert(END, "\n" + "Welcome to the next generation AI assistant!\nCreated by Rohith Peddi and Gaurav Mahendraker.\nAll rights reserved.\n\nPlease enter your query/command below.\nEnter help or -h for list of options.\n")

root.mainloop()