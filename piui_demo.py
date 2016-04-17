import functools
import os
import random
import time
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from piui import PiUi
from sklearn.decomposition import RandomizedPCA
import glob
import math
import os.path
import string

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')
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
        b1 = self.page.add_button("ImGood", self.a1)
        b2 = self.page.add_button("ImOkay", self.a2)
        b3 = self.page.add_button("NotGreat", self.a3)
        b4 = self.page.add_button("AboutMe", self.a4)
        b5 = self.page.add_button("Brothers/Sisters", self.a5)
        b6 = self.page.add_button("Pets", self.a6)
        b7 = self.page.add_button("Birthday", self.a7)
        b8 = self.page.add_button("Grade", self.a8)
        b9 = self.page.add_button("Breakfast", self.a9)
        b10 = self.page.add_button("School", self.a10)
        self.title = self.page.add_textbox("Output String", "h1")


    def page_introexitgeneric(self):
        self.page = self.ui.new_ui_page(title="Intro Exit Generic", prev_text="Back", onprevclick=self.main_menu)

        self.title = self.page.add_textbox("Intro", "h1")
        inb1 = self.page.add_button("Hello", self.in1)
        inb2 = self.page.add_button("Intro", self.in2)
        self.title = self.page.add_textbox("Exit", "h1")
        exb1 = self.page.add_button("Bye", self.ex1)
        exb2 = self.page.add_button("See you", self.ex2)
        self.title = self.page.add_textbox("Generic", "h1")
        geb1 = self.page.add_button("Don'tKnow", self.ge1)
        geb2 = self.page.add_button("Yes", self.ge2)
        geb3 = self.page.add_button("No", self.ge3)
        geb4 = self.page.add_button("Sorry", self.ge4)
        geb5 = self.page.add_button("HowAbout", self.ge5)
        geb6 = self.page.add_button("MeToo", self.ge6)
        geb7 = self.page.add_button("Why?", self.ge7)
        geb8 = self.page.add_button("Maybe", self.ge8)
        self.title = self.page.add_textbox("Output String", "h1")



    def page_buttons(self):
        img = cv2.imread('imgs/lena.jpg',0)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
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
        self.img = self.page.add_image("lena.jpg")
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


    #function to get ID from filename
    def ID_from_filename(filename):
        part = string.split(filename, '/')
        return part[1].replace("s", "")
     
    #function to convert image to right format
    def prepare_image(filename):
        img_color = cv2.imread(filename)
        img_gray = cv2.cvtColor(img_color, cv2.cv.CV_RGB2GRAY)
        img_gray = cv2.equalizeHist(img_gray)
        return img_gray.flat

    def page_video(self):
        self.page = self.ui.new_ui_page(title="Video", prev_text="Back", onprevclick=self.main_menu)
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (320, 240)
        camera.framerate = 5
        rawCapture = PiRGBArray(camera, size=(320, 240))
         
        # allow the camera to warmup
        time.sleep(0.1)
         
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
         
            # show the frame
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    test_val = ex 
            cv2.imshow("Frame", image)


            count = 0
            if (count < 10 and ex != null):
                resized_image = cv2.resize(image, (92, 112)) 
                cv2.imwrite("face-" + str(count) + ".jpg", resized_image)
                #take photos here
                

            key = cv2.waitKey(1) & 0xFF
         
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)
         
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break

    # positive feedback, uhoh i didn't say
    #intro, exit generic responses


    def page_simonsays(self):
        self.page = self.ui.new_ui_page(title="Simon Says", prev_text="Back", onprevclick=self.main_menu)
        self.title = self.page.add_textbox("Simon Says", "h1")
        ssq1 = self.page.add_button("Hands/head", self.ss1)
        ssq2 = self.page.add_button("Touch Nose", self.ss2)
        ssq3 = self.page.add_button("Spin", self.ss3)
        ssq4 = self.page.add_button("Hands/hip", self.ss4)
        ssq5 = self.page.add_button("Touch/knees", self.ss5)
        ssq6 = self.page.add_button("Jump", self.ss6)
        ssq7 = self.page.add_button("Hands/high", self.ss7)
        ssq8 = self.page.add_button("Touch/toes", self.ss8)
        ssq9 = self.page.add_button("Rub/tum", self.ss9)
        ssq10 = self.page.add_button("Clap", self.ss10)
        ssq11 = self.page.add_button("Run", self.ss11)
        ssq12 = self.page.add_button("Stomp", self.ss12)
        self.title = self.page.add_textbox("Simon Didn't Say", "h1")
        sdsq1 = self.page.add_button("Hands/head", self.sds1)
        sdsq2 = self.page.add_button("Touch Nose", self.sds2)
        sdsq3 = self.page.add_button("Spin", self.sds3)
        sdsq4 = self.page.add_button("Hands/hip", self.sds4)
        sdsq5 = self.page.add_button("Touch/knees", self.sds5)
        sdsq6 = self.page.add_button("Jump", self.sds6)
        sdsq7 = self.page.add_button("Hands/high", self.sds7)
        sdsq8 = self.page.add_button("Touch/toes", self.sds8)
        sdsq9 = self.page.add_button("Rub/tum", self.sds9)
        sdsq10 = self.page.add_button("Clap", self.sds10)
        sdsq11 = self.page.add_button("Run", self.sds11)
        sdsq12 = self.page.add_button("Stomp", self.sds12)
        self.title = self.page.add_textbox("Output String", "h1")

    def page_feedback(self):
        self.page = self.ui.new_ui_page(title="Feedback", prev_text="Back", onprevclick=self.main_menu)
        self.title = self.page.add_textbox("Uh-oh...I didn't say", "h1")

        fnb1 = self.page.add_button("Uh-oh", self.fn1)
        fnb2 = self.page.add_button("Sorry", self.fn2)
        fnb3 = self.page.add_button("Too bad", self.fn3)
        fnb4 = self.page.add_button("Got you!", self.fn4)
        fnb5 = self.page.add_button("No, no", self.fn5)
        fnb6 = self.page.add_button("I saw you!", self.fn6)
        fnb7 = self.page.add_button("Didn't say", self.fn7)
        fnb8 = self.page.add_button("Oh no", self.fn8)

        self.title = self.page.add_textbox("Positive Feedback", "h1")
        fpb1 = self.page.add_button("Way to go!", self.fp1)
        fpb2 = self.page.add_button("Awesome", self.fp2)
        fpb3 = self.page.add_button("You did it!", self.fp3)
        fpb4 = self.page.add_button("Excellent!", self.fp4)
        fpb5 = self.page.add_button("Smart!", self.fp5)
        fpb6 = self.page.add_button("Terrfic!", self.fp6)
        fpb7 = self.page.add_button("The best!", self.fp7)
        fpb8 = self.page.add_button("Great!", self.fp8)

        self.title = self.page.add_textbox("Output String", "h1")

    def page_headeyes(self):
        self.page = self.ui.new_ui_page(title="Head Eyes", prev_text="Back", onprevclick=self.main_menu)
        heq1 = self.page.add_button("Blink", self.he1)
        heq2 = self.page.add_button("Wink", self.he2)
        heq3 = self.page.add_button("Head Right", self.he3)
        heq4 = self.page.add_button("Head Left", self.he4)
        heq5 = self.page.add_button("Center", self.he5)
        self.title = self.page.add_textbox("Output Action", "h1")

    def main_menu(self):
        self.page = self.ui.new_ui_page(title="PiUi")
        self.list = self.page.add_list()
        #self.list.add_item("Buttons", chevron=True, onclick=self.page_buttons)
        self.list.add_item("Small Talk", chevron=True, onclick=self.page_smalltalk)
        self.list.add_item("Head Eyes", chevron=True, onclick=self.page_headeyes)
        self.list.add_item("Simon Says", chevron=True, onclick=self.page_simonsays)
        self.list.add_item("Feedback", chevron=True, onclick=self.page_feedback)
        self.list.add_item("Intro Exit Generic", chevron=True, onclick=self.page_introexitgeneric)
        #self.list.add_item("Input", chevron=True, onclick=self.page_input)
        #self.list.add_item("Images", chevron=True, onclick=self.page_images)
        #self.list.add_item("Toggles", chevron=True, onclick=self.page_toggles)
        self.list.add_item("Console!", chevron=True, onclick=self.page_console)
        self.list.add_item("Video", chevron=True, onclick=self.page_video)
        self.ui.done()


    def main(self):
        self.main_menu()
        self.ui.done()

    def onupclick(self):
        self.title.set_text("Up ")
        print "Up"


        inb1 = self.page.add_button("Hello", self.in1)
        inb2 = self.page.add_button("Intro", self.in2)
        self.title = self.page.add_textbox("Exit", "h1")
        exb1 = self.page.add_button("Bye", self.ex1)
        exb2 = self.page.add_button("See you", self.ex2)
        self.title = self.page.add_textbox("Generic", "h1")
        geb1 = self.page.add_button("Don'tKnow", self.ge1)
        geb2 = self.page.add_button("Yes", self.ge2)
        geb3 = self.page.add_button("No", self.ge3)
        geb4 = self.page.add_button("Sorry", self.ge4)
        geb5 = self.page.add_button("HowAbout", self.ge5)
        geb6 = self.page.add_button("MeToo", self.ge6)
        geb7 = self.page.add_button("Why?", self.ge7)
        geb8 = self.page.add_button("Maybe", self.ge8)

    def in1(self):
        self.title.set_text("Hi!  My name is L-E and I love to play Simon Says.  Would you like to play with me?")
        print "Hi!  My name is L-E and I love to play Simon Says.  Would you like to play with me?"

    def in2(self):
        self.title.set_text("Ok great!  I'll be Simon!  When I say Simon Says, you do what I say.  But if I don't say Simon Says, then you shouldn't do it.  Ok?")
        print "Ok great!  I'll be Simon!  When I say Simon Says, you do what I say.  But if I don't say Simon Says, then you shouldn't do it.  Ok?"

    def ex1(self):
        self.title.set_text("Bye addNameVar. That was fun!")
        print "Bye addNameVar. That was fun!"

    def ex2(self):
        self.title.set_text("Bye addNameVar. That was fun!")
        print "See you next time addNameVar."

    def ge1(self):
        self.title.set_text("I don't know")
        print "I don't know"

    def ge2(self):
        self.title.set_text("Yes")
        print "Yes"

    def ge3(self):
        self.title.set_text("No")
        print "No"

    def ge4(self):
        self.title.set_text("Sorry")
        print "Sorry"

    def ge5(self):
        self.title.set_text("How about you?")
        print "How about you?"

    def ge6(self):
        self.title.set_text("Me too")
        print "Me too"

    def ge7(self):
        self.title.set_text("Why")
        print "Why"

    def ge8(self):
        self.title.set_text("Maybe")
        print "Maybe"

    def fn1(self):
        self.title.set_text("Uh-Oh... I didn't say Simon Says!")
        print "Uh-Oh... I didn't say Simon Says!"

    def fn2(self):
        self.title.set_text("I'm sorry but I didn't say Simon Says!... make sure you listen closely!")
        print "I'm sorry but I didn't say Simon Says!... make sure you listen closely!"

    def fn3(self):
        self.title.set_text("Oh no!... you moved but I never said Simon Says!  Ok, here we go again...")
        print "Oh no!... you moved but I never said Simon Says!  Ok, here we go again..."

    def fn4(self):
        self.title.set_text("I got you!  I didn't say Simon Says this time...  this is fun!  Let's keep going!")
        print "I got you!  I didn't say Simon Says this time...  this is fun!  Let's keep going!"

    def fn5(self):
        self.title.set_text("No-No-No, I didn't say it!  That's ok though, you are doing great!  Let's play again!")
        print "No-No-No, I didn't say it!  That's ok though, you are doing great!  Let's play again!"

    def fn6(self):
        self.title.set_text("HA-ha-ha! I saw you! You moved but I didn't say Simon Says!, This is so much fun! Let's play again!")
        print "HA-ha-ha! I saw you! You moved but I didn't say Simon Says!, This is so much fun! Let's play again!"
        
    def fn7(self):
        self.title.set_text("OOPS! I think you moved but I didn't say Simon Says! Ok, let's keep going!")
        print "OOPS! I think you moved but I didn't say Simon Says! Ok, let's keep going!"

    def fn8(self):
        self.title.set_text("Oh-oh-oh! Too bad, so sad. I got you!! Next time, wait until I say Simon Says before you move!")
        print "Oh-oh-oh! Too bad, so sad. I got you!! Next time, wait until I say Simon Says before you move!"

    def fp1(self):
        self.title.set_text("Way to go! That was perfect! Let's play again!")
        print "Way to go! That was perfect! Let's play again!"

    def fp2(self):
        self.title.set_text("You are awesome! Great listening! Let's keep going!")
        print "You are awesome! Great listening! Let's keep going!"

    def fp3(self):
        self.title.set_text("You did it! Fabulous! Should we keep playing?")
        print "You did it! Fabulous! Should we keep playing?"

    def fp4(self):
        self.title.set_text("Excellent! You are listening so well and did it perfectly! Let's keep playing!")
        print "Excellent! You are listening so well and did it perfectly! Let's keep playing!"

    def fp5(self):
        self.title.set_text("You are very smart! I couldn't trick you once! Let's play again!")
        print "You are very smart! I couldn't trick you once! Let's play again!"

    def fp6(self):
        self.title.set_text("That was terrific! Another amazing performance! Do you want to keep playing with me?")
        print "That was terrific! Another amazing performance! Do you want to keep playing with me?"
        
    def fp7(self):
        self.title.set_text("You are the best! Incredible! Let's do it again!")
        print "You are the best! Incredible! Let's do it again!"

    def fp8(self):
        self.title.set_text("Great! You are truly awesome. Here we go again! Are you ready?")
        print "Great! You are truly awesome. Here we go again! Are you ready?"

    def ss1(self):
        self.title.set_text("Simon says, put your hands on your head!")
        print "Simon says, put your hands on your head!"

    def ss2(self):
        self.title.set_text("Simon says, Touch your nose!")
        print "Simon says, Touch your nose!"

    def ss3(self):
        self.title.set_text("Simon says, turn all the way around!")
        print "Simon says, turn all the way around!"

    def ss4(self):
        self.title.set_text("Simon says, place your hands on your hips!")
        print "Simon says, place your hands on your hips!"

    def ss5(self):
        self.title.set_text("Now Simon says, Touch your knees!")
        print "Now Simon says, Touch your knees!"

    def ss6(self):
        self.title.set_text("Simon says, jump three times!")
        print "Simon says, jump three times!"

    def ss7(self):
        self.title.set_text("Ok, Simon says, Hold your hands up high!")
        print "Ok, Simon says, Hold your hands up high!"

    def ss8(self):
        self.title.set_text("Simon says, touch your toes!")
        print "Simon says, touch your toes!"

    def ss9(self):
        self.title.set_text("Simon says, rub your tummy!")
        print "Simon says, rub your tummy!"

    def ss10(self):
        self.title.set_text("Simon says, Clap your hands!")
        print "Simon says, Clap your hands!"

    def ss11(self):
        self.title.set_text("And Simon says, run in place!")
        print "And Simon says, run in place!"

    def ss12(self):
        self.title.set_text("Simon says, stomp your feet!")
        print "Simon says, stomp your feet!"

    #simon didn't say...
    def sds1(self):
        self.title.set_text("Put your hands on your head!")
        print "Put your hands on your head!"

    def sds2(self):
        self.title.set_text("Touch your nose!")
        print "Touch your nose!"

    def sds3(self):
        self.title.set_text("Turn all the way around!")
        print "Turn all the way around!"

    def sds4(self):
        self.title.set_text("Put your hands on your hips!")
        print "Put your hands on your hips!"

    def sds5(self):
        self.title.set_text("Touch your knees!")
        print "Touch your knees!"

    def sds6(self):
        self.title.set_text("Now, jump three times!")
        print "Now, jump three times!"

    def sds7(self):
        self.title.set_text("Hold your hands up high!")
        print "Hold your hands up high!"

    def sds8(self):
        self.title.set_text("Now, touch your toes!")
        print "Now, touch your toes!"

    def sds9(self):
        self.title.set_text("Everyone rub your tummy!")
        print "Everyone rub your tummy!"

    def sds10(self):
        self.title.set_text("Clap your hands!")
        print "Clap your hands!"

    def sds11(self):
        self.title.set_text("Ok, run in place!")
        print "Ok, run in place!"

    def sds12(self):
        self.title.set_text("Let's stomp your feet!")
        print "Let's stomp your feet!"


    def he1(self):
        self.title.set_text("Blink")
        print "Blink"
        
    def he2(self):
        self.title.set_text("Wink")
        print "Wink"

    def he3(self):
        self.title.set_text("Head Right")
        print "Head Right"

    def he4(self):
        self.title.set_text("Head Left")
        print "Head Left"

    def he5(self):
        self.title.set_text("Center")
        print "Center"

    def a1(self):
        self.title.set_text("I'm good")
        print "I'm good"

    def a2(self):
        self.title.set_text("I'm okay")
        print "I'm okay"

    def a3(self):
        self.title.set_text("Not great. I'm having trouble figuring out some math problems I was assigned")
        print "Not great.  I'm having trouble figuring out some math problems I was assigned"

    def a4(self):
        self.title.set_text("Well, I love reading and watching TV.  I can't do everything humans can do because I'm a robot, but I love playing wit humans like you!")
        print "Well, I love reading and watching TV.  I can't do everything humans can do because I'm a robot, but I love playing wit humans like you!"

    def a5(self):
        self.title.set_text("Robots don't really have brothers and sisters, but there are others like me out there! I like to think of them as my brothers and sisters.")
        print "Robots don't really have brothers and sisters, but there are others like me out there! I like to think of them as my brothers and sisters."

    def a6(self):
        self.title.set_text("I wish! I think dogs are really fun.")
        print "I wish! I think dogs are really fun."

    def a7(self):
        self.title.set_text("I was created on May 15")
        print "I was created on May 15"

    def a8(self):
        self.title.set_text("Robots can go to school with kids from all different grades, but I'm eight!")
        print "Robots can go to school with kids from all different grades, but I'm eight!"

    def a9(self):
        self.title.set_text("I didn't have breakfast today, but I love doughnuts!")
        print "I didn't have breakfast today, but I love doughnuts!"

    def a10(self):
        self.title.set_text("Today, I learned about the sea.  Did you know that a shark is the only known fish that can blink with both eyes?")
        print "Today, I learned about the sea.  Did you know that a shark is the only known fish that can blink with both eyes?"

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