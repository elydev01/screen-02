from kivy.lang import Builder
from kivy import properties as P
from kivy.animation import Animation

from kivymd.uix.card import MDCard
from kivymd.app import MDApp as App


KV = """
<AnimatedCard>:
    size_hint_y: None
    orientation: 'vertical'
    height: self.width * 1.2
    radius: [dp(5)]
    padding: dp(10), dp(10)
    pos_hint: {'center_x': .5}
    on_release: self.active = not self.active
    canvas.before:
        PushMatrix
        Rotate:
            angle: -20 * root._variation
            origin: self.center
        Color:
            rgb: .95,.95,.95
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        Color:
            rgb: .8,.8,.8
        Line:
            rounded_rectangle: self.pos + self.size + [dp(10)]
        PopMatrix
        PushMatrix
        Rotate:
            angle: -10 * root._variation
            origin: self.center
        Color:
            rgb: .95,.95,.95
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        Color:
            rgb: .8,.8,.8
        Line:
            rounded_rectangle: self.pos + self.size + root.radius
        PopMatrix
        Color:
            rgba: root.md_bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        Color:
            rgb: .8,.8,.8
        Line:
            rounded_rectangle: self.pos + self.size + root.radius
    MDBoxLayout:
        id: info_box
        padding: 0, dp(5)
        spacing: dp(5)
        adaptive_height: True
        radius: root.radius
        orientation: 'vertical'
        pos_hint: {'center_x': .5, 'y': 0}
        MDLabel:
            bold: True
            halign: "center"
            shorten: True
            shorten_from: "right"
            text: root.title.upper()
            font_style: "H6"
            adaptive_height: True
            color: .2,.1,.3
        MDLabel:
            text: str(root.subtitle).upper()
            halign: "center"
            font_style: "Subtitle1"
            adaptive_height: True
            color: 1,.2,.4
    MDFloatLayout:
        height: 0
        size_hint_y: None
        FitImage:
            id: image
            source: root.source
            radius: root.radius
            y: info_box.y
            size_hint_y: None
            pos_hint: {'center_x': .5}
            height: (root.height - (dp(20) + (info_box.height * root._variation)))

MDScreen:
    anim_width: self.width * .5
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1
        ScrollView:
            always_overscroll: False
            MDBoxLayout:
                adaptive_height: True
                padding: dp(30), dp(40)
                orientation: 'vertical'
                spacing: dp(50)
                AnimatedCard:
                    size_hint_x: None
                    width: root.anim_width
                    source: "assets/i01.jpeg"
                    subtitle: "Director"
                AnimatedCard:
                    size_hint_x: None
                    width: root.anim_width
                    source: "assets/i02.jpeg"
                    subtitle: "Producer"
                AnimatedCard:
                    size_hint_x: None
                    width: root.anim_width
                    source: "assets/i03.jpeg"
                    subtitle: "Actor"
"""


class AnimatedCard(MDCard):
    active = P.BooleanProperty(False)
    source = P.StringProperty("assets/i01.jpeg")
    title = P.StringProperty("Someone Famous")
    subtitle = P.StringProperty("-")
    _variation = P.NumericProperty(0)

    def on_active(self, *args):
        if self.active:
            _variation = 1
            y = self.ids.info_box.top
        else:
            _variation = 0
            y = self.ids.info_box.y
        Animation(_variation=_variation, duration=0.2).start(self)
        Animation(y=y, duration=0.2).start(self.ids.image)


class HomeScreenApp(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    HomeScreenApp().run()
