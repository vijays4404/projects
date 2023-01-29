#importing the library
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput  import TextInput
from kivy.uix.boxlayout import BoxLayout
import socket
import threading

#creating the class with App class 
class TextMessageApp(App):
    #creating the constructor to received the message
    def build(self):
        #creating the label
        self.label=Label(text='No messages received yet.')
        self.textinput=TextInput(text='Enter message to send')
        self.textinput.bind(on_text_validate=self.send_message)
        layout=BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(self.textinput)
        return layout

        #returning the label
        return self.label
    def start_server(self):
        HOST='127.0.0.1'
        PORT=65432
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind((HOST,PORT))
            s.listen()
            conn,addr=s.accept()
            with conn:
                print('Connected by','addr')
                with True:
                    data=conn.recv(1024)
                    #if not data:
                        #break
                self.on_message_received(data.decode())
                conn.sendall(data)
    def on_message_received(self,message):
        self.label.text=message
    
    def send_message(self,instance):
        message=self.textinput.text
        self.conn.sendall(message.encode())
        self.textinput.text=""


    def on_start(self):
        self.server_thread=threading.Thread(target=self.start_server)
        self.server_thread.daemon=True
        self.server_thread.start()
    def on_message_received(self,message):
        self.label.text=message

if __name__=='__main__':
    TextMessageApp().run()