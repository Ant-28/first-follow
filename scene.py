from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars
from typing import Tuple
import copy
class FirstFollow(Scene):
    def construct(self):
        width = 60
        height = width*9//16


        self.rendered_code = Code('grammar.bnf', tab_width=4, language='Bnf',background="window", font="Monospace")
        self.rendered_code.width = 25//2
        self.rectangle = False
        self.lines = self.rendered_code.code_string.split('\n')
        self.rendered_code.code = remove_invisible_chars(self.rendered_code.code)
        self.play(Create(self.rendered_code))
        self.play(self.rendered_code.
                  animate.move_to([-5, 0, 1]))
        self.curr_rect = None
       

        self.first_set = Code('first_set.bnf', tab_width=4, language='python',background="window", font="Monospace")
        self.first_set.height = self.rendered_code.height

        self.follow_set =  Code('follow_set.bnf', tab_width=4, language='python',background="window", font="Monospace")
        self.follow_set.height = self.rendered_code.height
        self.first_set.move_to(self.rendered_code.get_right() + 5*RIGHT )
        
        self.play(Create(self.first_set))
        # self.play(Create(self.follow_set))
        self.fslines = self.first_set.code_string.split('\n')
        self.foslines = self.follow_set.code_string.split('\n')
        # print("fslines: ", self.fslines)
        self.highlight_block(6, 'Op') 
        
        # I could make this a function but this makes more sense

        self.highlight_block(7, None, 1, 4) 
        self.emphasize()
        self.first_update(7,"{   *   }" )

        self.highlight_block(6, None, 5, 8)
        self.emphasize()
        self.first_update(6, "{   +   }" )
        
        self.highlight_block(4, "Unit")

        self.highlight_block(5, None,1, 3)
        self.emphasize()
        self.first_update(5,"{  ID   }" )

        self.highlight_block(4, None,7, 10)
        self.emphasize()
        self.first_update(4,"{   (   }" )

        self.highlight_block(2, "Expr2")
        
        self.highlight_block(3, None,1,3)
        self.emphasize()
        self.first_update(3,'{  ""   }' )

        self.highlight_block(2, None, 8, 10)
        self.emphasize()
        self.highlight_block(6, 'Op')
        self.emphasize()
        self.emphasize()

        self.highlight_block(6, None, 5, 8)
        self.highlight_block(7, None, 1, 4)
        
        self.highlight_block(2, None, 8, 10)
        self.highlight_fix()
        self.first_update(2,"{  +,*  }" )

        self.highlight_block(1, "Expr")
        self.highlight_block(1, None, 7, 11)
        self.emphasize()
        
        self.highlight_block(4, "Unit")
        self.emphasize()
        self.emphasize()

        self.highlight_block(4, None,7, 10)
        self.highlight_block(5, None,1, 3)
        
        self.highlight_block(1, None, 7, 11) # why is this so inconsistent manim goddamn it
        self.highlight_fix()


        self.first_update(1, "{  (,ID }")

        first_text = Text("The First Set")
        first_text.move_to(self.first_set.get_bottom() + DOWN)
        self.play(Create(first_text))
        self.play(FadeOut(self.curr_rect))
        self.curr_rect = None
        # follow set
        self.play(self.rendered_code.
                  animate.move_to([-width // 6 + 0.3, 0, 1]))
        # self.first_set.move_to(self.rendered_code.get_right() + 5*RIGHT)
        first_set_and_text = VGroup(self.first_set, first_text)
        self.play(first_set_and_text.animate.move_to(self.rendered_code.get_right() + 5*RIGHT + 0.6*DOWN))

        self.follow_set.move_to(self.rendered_code.get_right() + 14*RIGHT )
        self.play(Create(self.follow_set))

        for i in range(1,8):
            if i != 3:
                self.follow_update(i, "     NA     ")
        


        self.highlight_block(3, None,1,3)
        self.highlight_block(2, None, 14, 19)
        self.block_shake()
        self.follow_update(3, "{ None     }")

        self.highlight_block(2, "Expr2")
        self.highlight_block(1, None, 11, 16)
        
        self.highlight_block(1, "Expr")
        self.emphasize()
        self.highlight_block(4, None, 10, 14)
        self.emphasize()
        
        self.highlight_block(4, None, 14, 17)
        self.emphasize()

        self.follow_update(3, "{ None, )  }")
        self.play(FadeOut(self.curr_rect))

        follow_text = Text("The Follow Set")
        follow_text.move_to(self.follow_set.get_bottom() + DOWN)
        self.play(Create(follow_text))


        self.play(Wait(2))
        
        merge = Text("Now merge both!")

        merge.move_to(self.first_set.get_top() + UP)
        self.play(Create(merge))

        self.first_update(3, "{None,) }")
        self.play(Wait(1))
        follow_set_text = VGroup(self.follow_set, follow_text, merge)
        self.play(FadeOut(follow_set_text))
    
        newcode = self.rendered_code.copy()
        newcode.move_to([-5, 0, 1])

        self.play(first_set_and_text.animate.move_to(newcode.get_right() + 5*RIGHT + 0.6*DOWN))
        self.play(self.rendered_code.
                  animate.move_to([-5, 0, 1]))
        
      
        newtext = Text("The First+ Set")
        newtext.move_to(first_text.get_center())


        self.play(ReplacementTransform(first_text, newtext))



        self.play(Wait(5))
        
        # selected_code = self.rendered_code.code[0][0:4]
        # new_code = self.first_set.code[0][1:5]
        # path_rect = SurroundingRectangle(selected_code,fill_color=YELLOW, fill_opacity=0)
        # destination_rect = SurroundingRectangle(new_code,fill_color=YELLOW, fill_opacity=0)
        # test_code = Text('Expr', font = "Monospace", font_size=DEFAULT_FONT_SIZE*1.05).align_to(path_rect.get_left())
        # test_code.move_to(destination_rect.get_center())
        # # self.highlight_block(3, None, 0, 4)
        # self.move_down()
        # self.play(Wait(2))
        # self.play(Create(test_code))

    def first_update(self, line: int, newstr: str):
        self.fslines[line-1] = newstr
        newcode = Code(code="\n".join(self.fslines), tab_width=4, language='python',background="window", font="Monospace")
        newcode.height = self.rendered_code.height
        newcode.move_to(self.rendered_code.get_right() + 5*RIGHT )
        self.play(ReplacementTransform(self.first_set, newcode))
        self.first_set = newcode

    def follow_update(self, line: int, newstr: str):
        self.foslines[line-1] = newstr
        newcode = Code(code="\n".join(self.foslines), tab_width=4, language='python',background="window", font="Monospace")
        newcode.height = self.rendered_code.height
        newcode.move_to(self.rendered_code.get_right() + 14*RIGHT )
        self.play(ReplacementTransform(self.follow_set, newcode))
        self.follow_set = newcode

    
    def move_down(self):
        assert self.curr_rect
        l1 = Line(self.curr_rect.get_center(), self.curr_rect.get_center()+0.87*DOWN)
        self.play(MoveAlongPath(self.curr_rect, l1), rate_func=smooth)
       
    def highlight_block(self, line: int, code_str: str, start: int = None, end: int = None):
        ind = line - 1

        
        
        if not start and not end:
            assert code_str in self.lines[ind]
            start, end = self.get_code_str(self.lines[ind], code_str)
        
        selected_code = self.rendered_code.code[ind][start:end]
        if not self.curr_rect:
            self.curr_rect = SurroundingRectangle(selected_code,fill_color=YELLOW, fill_opacity=0.3)
            self.play(FadeIn(self.curr_rect))
        else:
            newrect = SurroundingRectangle(selected_code,fill_color=YELLOW, fill_opacity=0.3)
            self.play(Transform(self.curr_rect, newrect))
            self.remove(self.curr_rect)
            self.curr_rect = newrect

    def highlight_fix(self):
        self.play(Create(self.curr_rect))



    def get_code_str(self, string: str, substr: str) -> Tuple[int, int]:
        start = string.find(substr)
        end = start + len(substr) 
        return start, end
    

    def emphasize(self):
        oldrect = self.curr_rect.copy()
        newrect = self.curr_rect.copy()

        newrect.scale(1.1)
        newrect.set_color(RED)
        self.play(ReplacementTransform(self.curr_rect, newrect), run_time = 0.15)
        self.play(ReplacementTransform(newrect, oldrect), run_time = 0.15)
        self.curr_rect = oldrect

    def block_shake(self):
        oldrect = self.curr_rect.copy()
        oldrect2 = self.curr_rect.copy()
        leftrect = self.curr_rect.copy()
        rightrect = self.curr_rect.copy()
        leftrect.set_color(RED)
        rightrect.set_color(RED)
        leftrect.move_to(oldrect.get_center() + 0.1*LEFT)
        rightrect.move_to(oldrect.get_center() + 0.1*RIGHT)
        self.play(ReplacementTransform(self.curr_rect, rightrect), run_time = 0.10)
        self.play(ReplacementTransform(rightrect, oldrect), run_time = 0.10)
        self.play(ReplacementTransform(oldrect, leftrect), run_time = 0.10)
        self.play(ReplacementTransform(leftrect, oldrect2), run_time = 0.10)
        self.curr_rect = oldrect2
      