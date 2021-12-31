from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget

Builder.load_file("widget_examples.kv")

class MyImageWidget(Widget):

    def __init__(self,**kwargs):
        super(MyImageWidget,self).__init__(**kwargs)
        self.image = Image(source='images/lab_logo.png')
        self.add_widget(self.image)
        #Clock.schedule_interval(self.update_pic,1)

    def update_pic(self,dt):
        self.image.reload()
        print("update")

    def on_size(self, *args):
        self.image.pos = self.pos
        self.image.size = self.size

class ImagesExample(GridLayout):

    def on_swap_click(self):
        print("click")

class WidgetsExample(GridLayout):
    my_text = StringProperty('1')
    count = 1
    count_enabled = BooleanProperty(False)
    text_input_str = StringProperty('Name')
    # slider_value_txt = StringProperty(str(50))

    def on_button_click(self):
        print('Button clicked')
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
        else:
            pass

    def on_toggle_button_state(self, widget):
        print('toggle state ' + widget.state)
        if widget.state == 'normal':
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    def on_slider_value(self, widget):
        print("Slider: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = "Your name is: " + widget.text
