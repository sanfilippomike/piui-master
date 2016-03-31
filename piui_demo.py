import functools
import os
import random
import time
from piui import PiUi



current_dir = os.path.dirname(os.path.abspath(__file__))


class DemoPiUi(object):

    def __init__(self):
        self.title = None
        self.txt = None
        self.img = None
        self.ui = PiUi(img_dir=os.path.join(current_dir, 'imgs'))
        self.src = "sunset.png"

    def page_static(self):
        self.page = self.ui.new_ui_page(title="Static Content", prev_text="Back",
            onprevclick=self.main_menu)
        self.page.add_textbox("Add a mobile UI to your Raspberry Pi project", "h1")
        self.page.add_element("hr")
        self.page.add_textbox("You can use any static HTML element " + 
            "in your UI and <b>regular</b> <i>HTML</i> <u>formatting</u>.", "p")
        self.page.add_element("hr")
        self.page.add_textbox("Your python code can update page contents at any time.", "p")
        update = self.page.add_textbox("Like this...", "h2")
        time.sleep(2)
        for a in range(1, 10):
            update.set_text(str(a))
            time.sleep(1)


    def page_smalltalk(self):
        self.page = self.ui.new_ui_page(title="Small Talk", prev_text="Back", onprevclick=self.main_menu)

        self.title = self.page.add_textbox("Small Talk Questions", "h1")
        bq1 = self.page.add_button("HowAreYou", self.q1)
        bq2 = self.page.add_button("TellMe", self.q2)
        bq3 = self.page.add_button("Brothers/Sisters", self.q3)
        bq4 = self.page.add_button("Pets", self.q4)
        bq5 = self.page.add_button("Birthday", self.q5)
        bq6 = self.page.add_button("Grade", self.q6)
        bq7 = self.page.add_button("Breakfast", self.q7)
        bq8 = self.page.add_button("School", self.q8)
        self.title = self.page.add_textbox("Small Talk Answers", "h1")
        b1 = self.page.add_button("HowAreYou", self.m1)
        b2 = self.page.add_button("ImGood", self.m2)
        b3 = self.page.add_button("ImOkay", self.m3)
        b4 = self.page.add_button("NotGreat", self.m4)
        b5 = self.page.add_button("AboutMe", self.m5)
        b6 = self.page.add_button("Brothers/Sisters", self.m6)
        b7 = self.page.add_button("ImGood", self.m7)
        b8 = self.page.add_button("ImOkay", self.m8)
        b9 = self.page.add_button("NotGreat", self.m9)
        b10 = self.page.add_button("AboutMe", self.m10)
        b11 = self.page.add_button("Brothers/Sisters", self.m11)
        self.title = self.page.add_textbox("Output String", "h1")

    def page_buttons(self):
        self.page = self.ui.new_ui_page(title="Buttons", prev_text="Back", onprevclick=self.main_menu)
        self.title = self.page.add_textbox("Buttons!", "h1")
        plus = self.page.add_button("Up Button &uarr;", self.onupclick)
        minus = self.page.add_button("Down Button &darr;", self.ondownclick)

    def page_input(self):
        self.page = self.ui.new_ui_page(title="Input", prev_text="Back", onprevclick=self.main_menu)
        self.title = self.page.add_textbox("Input", "h1")
        self.txt = self.page.add_input("text", "Name")
        button = self.page.add_button("Say Hello", self.onhelloclick)

    def page_images(self):
        self.page = self.ui.new_ui_page(title="Images", prev_text="Back", onprevclick=self.main_menu)
        self.img = self.page.add_image("sunset.png")
        self.page.add_element('br')
        button = self.page.add_button("Change The Picture", self.onpicclick)

    def page_toggles(self):
        self.page = self.ui.new_ui_page(title="Toggles", prev_text="Back", onprevclick=self.main_menu)
        self.list = self.page.add_list()
        self.list.add_item("Lights", chevron=False, toggle=True, ontoggle=functools.partial(self.ontoggle, "lights"))
        self.list.add_item("TV", chevron=False, toggle=True, ontoggle=functools.partial(self.ontoggle, "tv"))
        self.list.add_item("Microwave", chevron=False, toggle=True, ontoggle=functools.partial(self.ontoggle, "microwave"))
        self.page.add_element("hr")
        self.title = self.page.add_textbox("Home Appliance Control", "h1")
        

    def page_console(self):
        con = self.ui.console(title="Console", prev_text="Back", onprevclick=self.main_menu)
        con.print_line("Hello Console!")

    def main_menu(self):
        self.page = self.ui.new_ui_page(title="PiUi")
        self.list = self.page.add_list()
        self.list.add_item("Buttons", chevron=True, onclick=self.page_buttons)
        self.list.add_item("Small Talk", chevron=True, onclick=self.page_smalltalk)
        self.list.add_item("Input", chevron=True, onclick=self.page_input)
        self.list.add_item("Images", chevron=True, onclick=self.page_images)
        self.list.add_item("Toggles", chevron=True, onclick=self.page_toggles)
        self.list.add_item("Console!", chevron=True, onclick=self.page_console)
        self.ui.done()


    def main(self):
        self.main_menu()
        self.ui.done()

    def onupclick(self):
        self.title.set_text("Up ")
        print "Up"

    def m1(self):
        self.title.set_text("How are you")
        print "How are you"

    def m2(self):
        self.title.set_text("I'm good")
        print "I'm good"

    def m3(self):
        self.title.set_text("I'm okay")
        print "I'm okay"

    def m4(self):
        self.title.set_text("Not great. I'm having trouble figuring out some math problems I was assigned")
        print "Not great.  I'm having trouble figuring out some math problems I was assigned"

    def m5(self):
        self.title.set_text("How are you")
        print "How are you"

    def m6(self):
        self.title.set_text("I'm good")
        print "I'm good"

    def q1(self):
        self.title.set_text("How are you")
        print "How are you"

    def q2(self):
        self.title.set_text("Tell me about yourself")
        print "Tell me about yourself"

    def q3(self):
        self.title.set_text("Do you have any brothers or sisters?")
        print "Do you have any brothers or sisters?"

    def q4(self):
        self.title.set_text("Do you have any pets")
        print "Do you have any pets"

    def q5(self):
        self.title.set_text("When is your birthday?")
        print "When is your birthday?"

    def q6(self):
        self.title.set_text("What grade are you in?")
        print "What grade are you in?"

    def q7(self):
        self.title.set_text("What did you have for breakfast today?")
        print "What did you have for breakfast today?"

    def q8(self):
        self.title.set_text("What did you do in school today?")
        print "What did you do in school today?"
        

    def ondownclick(self):
        self.title.set_text("Down")
        print "Down"

    def onhelloclick(self):
        print "onstartclick"
        self.title.set_text("Hello " + self.txt.get_text())
        print "Start"

    def onpicclick(self):
        if self.src == "sunset.png":
          self.img.set_src("sunset2.png")
          self.src = "sunset2.png"
        else:
          self.img.set_src("sunset.png")
          self.src = "sunset.png"

    def ontoggle(self, what, value):
        self.title.set_text("Toggled " + what + " " + str(value))

def main():
  piui = DemoPiUi()
  piui.main()

if __name__ == '__main__':
    main()