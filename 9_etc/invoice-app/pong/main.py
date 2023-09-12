from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongGame(Widget):
	pass

class PongApp(App):
	def build(self):
		return PongGame()

class PongBall(Widget):
	#velocity od the ball on the x and y axis
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)

	#referencelist property so we can use ball.velocity as 
	#a shorthand, just like e.g. w.pos for w.x and w.y
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	def move(self):
		self.pos = Vector(*self.velocity) + self.pos

if __name__ == '__main__':
	PongApp().run()