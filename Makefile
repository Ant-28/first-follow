all:
	manim -pql scene.py FirstFollow

hq:
	manim -pqh scene.py FirstFollow

dummy:
	manim -pql dummy.py DummyScene
gpt:
	manim -pql GptScene.py CodeObject