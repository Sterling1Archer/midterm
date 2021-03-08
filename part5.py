from guizero import App, Text, TextBox, Box, PushButton, Drawing
from gpiozero import AngularServo, Servo
from threading import Thread
from queue import Queue
import time, math, serial

Arduino_serial_transmit = serial.Serial('/dev/ttyACM0',9600,timeout=2)
Arduino_serial_transmit.flush()

def thread1(threadname,q):
    run_update = q.get()
    print("Starting " + threadname)
    while(run_update):
        print("Updating textboxes")
        update_textboxes()

def secondfunc():
    global pin8_flag, pin9_flag, pin10_flag, pin11_flag,d0_value,d1_value,d2_value,d3_value,a0_value,a1_value,a2_value,a3_value
    global a0_textbox,a1_textbox,a2_textbox,a3_textbox,run_update,circle_2,circle_3,circle_4,circle_5
    pin8_flag = "0"
    pin9_flag = "0"
    pin10_flag = "0"
    pin11_flag = "0"
    a0_value = "0"
    a1_value = "0"
    a2_value = "0"
    a3_value = "0"
    d0_value = "0"
    d1_value = "0"
    d2_value = "0"
    d3_value = "0"
    
    app.bg = "#00cc99"
    app.width = 400
    app.height= 300
    wanted_text = Text(app, "IO data acquisition system GUI")
    wanted_text.text_size = 12
    wanted_text.font = "Times New Roman"
    wanted_text.text_color = "#000000"
    
    Box_input_digital = Box(app, layout="grid",border=1)
    digital_text = Text(Box_input_digital, "Input digital",grid=[0,0])
    circle_2 = Drawing(Box_input_digital, height = 11, width = 11, grid=[0,1])
    circle_3 = Drawing(Box_input_digital, height = 11, width = 11, grid=[1,1])
    circle_4 = Drawing(Box_input_digital, height = 11, width = 11, grid=[2,1])
    circle_5 = Drawing(Box_input_digital, height = 11, width = 11, grid=[3,1])
    
    box_output = Box(app, layout="grid", border=1)
    pin8_button = PushButton(box_output,text="pin8", command=pin8_out, grid=[0,0])
    pin9_button = PushButton(box_output,text="pin9",command=pin9_out, grid=[1,0])
    pin10_button = PushButton(box_output,text="pin10",command=pin10_out, grid=[0,1])
    pin11_button = PushButton(box_output,text="pin11",command=pin11_out, grid=[1,1])
    circle_2.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    circle_3.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    circle_4.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    circle_5.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    circle_2_text = Text(Box_input_digital, "2", grid=[0,2])
    circle_2_text = Text(Box_input_digital, "3", grid=[1,2])
    circle_2_text = Text(Box_input_digital, "4", grid=[2,2])
    circle_2_text = Text(Box_input_digital, "5", grid=[3,2])
    
    box_input_analog = Box(app, layout="grid", border=1)
    a0_text = Text(box_input_analog, "A0", grid=[0,0])
    a1_text = Text(box_input_analog, "A1", grid=[0,1])
    a2_text = Text(box_input_analog, "A2", grid=[0,2])
    a3_text = Text(box_input_analog, "A3", grid=[0,3])
    a0_textbox = TextBox(box_input_analog, text=a0_value, grid=[1,0])
    a1_textbox = TextBox(box_input_analog, text=a1_value, grid=[1,1])
    a2_textbox = TextBox(box_input_analog, text=a2_value, grid=[1,2])
    a3_textbox = TextBox(box_input_analog, text=a3_value, grid=[1,3])
    
    button_exit = PushButton(app,text="Exit",command=exit_program)
  
    return app
def update_textboxes():
    global a0_value,a1_value,a2_value,a3_value,a0_textbox,a1_textbox,a2_textbox,a3_textbox
    input_stream = ""
    intput_stream_tokenized = ""
    Arduino_serial_transmit.write(bytes(("4,0,").encode('utf-8')))
    input_stream = Arduino_serial_transmit.readline().decode('utf-8')
    print(input_stream)
    intput_stream_tokenized = input_stream.split(",")
    print(intput_stream_tokenized)
    if intput_stream_tokenized[0] == "4":
        a0_value = intput_stream_tokenized[1]
        a1_value = intput_stream_tokenized[3]
        a2_value = intput_stream_tokenized[5]
        a3_value = intput_stream_tokenized[7]
    a0_textbox.value = a0_value
    a1_textbox.value = a1_value
    a2_textbox.value = a2_value
    a3_textbox.value = a3_value
    print(a0_value)
    print(a1_value)
    print(a2_value)
    print(a3_value)
    
def exit_program():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        
def pin8_out():
    global pin8_flag, d0_value, run_update,queue,circle_2
    run_update=0
    queue.put(run_update)
    time.sleep(1)
    if pin8_flag == "0":
        pin8_flag = "1"
    elif pin8_flag == "1":
        pin8_flag = "0"
    Arduino_serial_transmit.write(bytes(("0").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((pin8_flag).encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    d0_value = Arduino_serial_transmit.readline().decode('utf-8')
    if d0_value == "1":
        circle_2.oval(0,0,10,10, color="red", outline=True, outline_color = "black")
    elif d0_value == "0":
        circle_2.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    print(d0_value)
    run_update=1
    queue.put(run_update)
    
def pin9_out():
    global pin9_flag, d1_value,queue,circle_3
    run_update=0
    queue.put(run_update)
    time.sleep(1)
    if pin9_flag == "0":
        pin9_flag = "1"
    elif pin9_flag == "1":
        pin9_flag = "0"
    Arduino_serial_transmit.write(bytes(("1").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((pin9_flag).encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    d1_value = Arduino_serial_transmit.readline().decode('utf-8')
    if d0_value == "1":
        circle_3.oval(0,0,10,10, color="red", outline=True, outline_color = "black")
    elif d0_value == "0":
        circle_3.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    run_update=1
    queue.put(run_update)
    
def pin10_out():
    global pin10_flag, d2_value,queue,circle_4
    run_update=0
    queue.put(run_update)
    time.sleep(1)
    if pin10_flag == "0":
        pin10_flag = "1"
    elif pin10_flag == "1":
        pin10_flag = "0"
    Arduino_serial_transmit.write(bytes(("2").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((pin10_flag).encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    d2_value = Arduino_serial_transmit.readline().decode('utf-8')
    if d0_value == "1":
        circle_4.oval(0,0,10,10, color="red", outline=True, outline_color = "black")
    elif d0_value == "0":
        circle_4.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    run_update=1
    queue.put(run_update)
    
def pin11_out():
    global pin11_flag, d3_value,queue,circle_5
    run_update=0
    queue.put(run_update)
    time.sleep(1)
    if pin11_flag == "0":
        pin11_flag = "1"
    elif pin11_flag == "1":
        pin11_flag = "0"
    Arduino_serial_transmit.write(bytes(("3").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    Arduino_serial_transmit.write(bytes((pin11_flag).encode('utf-8')))
    Arduino_serial_transmit.write(bytes((",").encode('utf-8')))
    d3_value = Arduino_serial_transmit.readline().decode('utf-8')
    if d0_value == "1":
        circle_5.oval(0,0,10,10, color="red", outline=True, outline_color = "black")
    elif d0_value == "0":
        circle_5.oval(0,0,10,10, color="black", outline=True, outline_color = "black")
    run_update=1
    queue.put(run_update)

if __name__ == '__main__':
    global queue
    queue = Queue()
    run_update=1
    queue.put(run_update)
    thread1 = Thread(target=thread1, args=("Thread-1",queue))
    thread1.daemon = True
    thread1.start()
    
    app = App("IO data acquisition system GUI")
    app2 = secondfunc()
    app.display()
    thread1.join()
    Arduino_serial_transmit.close()