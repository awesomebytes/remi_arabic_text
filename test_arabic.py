#!/usr/bin/env python
import remi.gui as gui
from remi import start, App


class MyApp(App):

    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self, name='world'):
        # the arguments are	width - height - layoutOrientationOrizontal
        wid = gui.Widget(800, 1000, False, 10)

        self.title = gui.Label(400, 20, "Testing arabic in TextInput")

        # Open a UTF-8 file with arabic in it
        with open('./arabic.txt', 'r') as f:
            self.contents = f.read()

        # If we do this nothing works
        # self.contents = self.contents.decode('UTF-8')
        # The error is:
        #   File "/usr/local/lib/python2.7/dist-packages/remi/server.py", line 550, in process_all
        #     self.wfile.write(encodeIfPyGT3(html))
        #   File "/usr/lib/python2.7/socket.py", line 316, in write
        #     data = str(data) # XXX Should really reject non-string non-buffers
        # UnicodeEncodeError: 'ascii' codec can't encode characters in position 544-550: ordinal not in range(128)


        self.text_in = gui.TextInput(700, 300, single_line=False)
        # Here setting the text works fine...
        self.text_in.set_text(self.contents)
        # But if we set the text dynamically with this button... its shown all wrong
        self.killer_button = gui.Button(100, 20, "Reload text")
        self.killer_button.set_on_click_listener(self, 'button_that_kills_arabic_cb')

        # appending a widget to another, the first argument is a string key
        wid.append('0', self.title)
        wid.append('1', self.text_in)
        wid.append('2', self.killer_button)


        # returning the root widget
        return wid

    def button_that_kills_arabic_cb(self):
        # Same contents but one char less so it actually does something
        self.text_in.set_text(self.contents[:-1])

if __name__ == "__main__":
    # setting up remi debug level 
    #       2=all debug messages   1=error messages   0=no messages
    import remi.server
    remi.server.DEBUG_MODE = 2 

    # starts the webserver
    # optional parameters   
    #       start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(MyApp)
