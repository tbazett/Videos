from manim import *
from manim_chess.chess_board import ChessBoard
from circle_board import CircleBoard #delete later
import random

#knight_type
a=2
b=4

def create_circle(x,y,color):
    circle = Circle(0.25, stroke_width=0, fill_color=color, fill_opacity=1)
    circle.shift(UP*y+RIGHT*x)
    circle.z_index=0
    return circle

def add_knight_arrow_circle(i,j, dx, dy, width=15):
    #For 8x8 board use stroek_width 15. For 16x16 use 7. 
    graphical_segment = Line((RIGHT * i + UP * j), (RIGHT * (i + dx) + UP * j), color=BLUE, stroke_width=width)
    square=Circle(radius=(width/32)*21/135, fill_color=BLUE, fill_opacity=1, stroke_opacity=0).shift(RIGHT*(i+dx)+UP*j)
    graphical_arrow = Arrow((RIGHT * (i+dx) + UP * j), (RIGHT * (i + dx) + UP * (j + dy)), color=BLUE, stroke_width=width, max_stroke_width_to_length_ratio=125, max_tip_length_to_length_ratio=0.5, buff=0)
  
    group = VGroup(graphical_segment, graphical_arrow, square)
    group.z_index=-2
    #group=graphical_arrow
    return group


class Chess_small(Scene):
    def construct(self):
        smaller_board_king = ChessBoard("5/5/2K2/5/5 w - - 0 1")
        smaller_board_knight = ChessBoard("5/5/2N2/5/5 w - - 0 1").next_to(smaller_board_king, 2*LEFT)
        #big_board= ChessBoard("9/9/9/9/4K4/9/9/9/9 w KQkq - 0 1")


        arrows=[]
        for m in range(-1, 2):
            for n in range(-1, 2):
                if (m, n) == (0, 0):
                    continue  # Skip this iteration
                arrows.append((2,2,m,n))
                smaller_board_king.add_text(m+2, n+2, "1")

        for arrow in arrows:
            smaller_board_king.add_arrow(*arrow)

        for m in range(-2, 3):
            for n in range(-2, 3):
                if max(abs(m),abs(n)) <= 1:
                    continue
                smaller_board_king.add_text(m+2, n+2, "2")


        self.add(Group(smaller_board_king, smaller_board_knight).move_to(ORIGIN))

        #self.play(Transform(smaller_board,new_smaller_board))

        print("moves:", Chess.get_knight_moves([3,3],2))
 

class Chess_fill_in_numbers(Scene):
    def construct(self):

        for count in range(1,30):

            m=random.randint(0,7)
            n=random.randint(0,7)

            #m=0
            #n=2
            piece ="N"

            fen = Super_Board.generate_big_fen(m,n, piece,8,8)
            board=ChessBoard(fen)
            point=(m,n)
            board.add_highlight(n, m, GREEN)

            #board= ChessBoard("8/8/8/8/4N3/8/8/8 w KQkq - 0 1")

            if piece=="N":
                type= [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]
            if piece=="K":
                type=[(1, 0),(1, -1), (0, -1),(-1, -1), (-1, 0),(-1, 1), (0, 1),(1, 1)]

            moves_one=Chess_fill_in_numbers.get_knight_moves(point,1,type)
            for move in moves_one:
                board.add_text(move[0], move[1], "1", RED)

            moves_two=Chess_fill_in_numbers.get_knight_moves(point,2,type)
            for move in moves_two:
                board.add_text(move[0], move[1], "2", BLUE)

           

            moves_three=Chess_fill_in_numbers.get_knight_moves(point,3,type)
            for move in moves_three:
                board.add_text(move[0], move[1], "3", YELLOW)

            moves_four=Chess_fill_in_numbers.get_knight_moves(point,4,type)
            for move in moves_four:
                board.add_text(move[0], move[1], "4", PINK)

            moves_five=Chess_fill_in_numbers.get_knight_moves(point,5,type)
            for move in moves_five:
                board.add_text(move[0], move[1], "5", GREEN)

            moves_six=Chess_fill_in_numbers.get_knight_moves(point,6,type)
            for move in moves_six:
                board.add_text(move[0], move[1], "6", ORANGE)

            moves_seven=Chess_fill_in_numbers.get_knight_moves(point,7,type)
            for move in moves_seven:
                board.add_text(move[0], move[1], "7", TEAL)

            board.move_to(ORIGIN)
            self.add(board)

            # avg=(len(moves_one)+2*len(moves_two)+3*len(moves_three)+4*len(moves_four)+5*len(moves_five)+6*len(moves_six)+7*len(moves_seven))/63
            # text = Text(f"Average # of Moves: {avg:.2f}")
            # text.to_edge(UP + LEFT).scale(0.8)
            # self.add(text)


            self.wait()
            self.remove(board)
            #self.remove(text)

    @staticmethod
    def get_knight_moves(point, jumps,type):
        locations = [(m, n) for m in range(8) for n in range(8)]
        knight_moves = type
        #[(1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 1)]
        #knight_moves = [(3, 2), (3, 3), (-2, 3), (-3, 2), (-3, -2), (-2, -3), (2, -3), (3, -2)]


        step_one =[]
        step_two =[]
        step_three=[]
        step_four=[]
        step_five=[]
        step_six=[]
        step_seven=[]

        for location in locations:
            for move in type:
                new_location = (location[0] + move[0], location[1] + move[1])
                if new_location == point: 
                    step_one.append(location)

        for location in step_one:
            step_two.extend([(location[0] + dx, location[1] + dy) for dx, dy in type if 0 <= location[0] + dx < 8 and 0 <= location[1] + dy < 8] )
        step_two = list(filter(lambda item: item not in step_one and item != point, step_two))
        step_two = list(set(step_two))
        
        for location in step_two:
            step_three.extend([(location[0] + dx, location[1] + dy) for dx, dy in type if 0 <= location[0] + dx < 8 and 0 <= location[1] + dy < 8] )
        step_three = list(filter(lambda item: item not in step_one and item not in step_two, step_three))
        step_three = list(set(step_three))

        for location in step_three:
            step_four.extend([(location[0] + dx, location[1] + dy) for dx, dy in type if 0 <= location[0] + dx < 8 and 0 <= location[1] + dy < 8] )
        step_four = list(filter(lambda item: item not in step_one and item not in step_two and item not in step_three, step_four))
        step_four = list(set(step_four))

        for location in step_four:
            step_five.extend([(location[0] + dx, location[1] + dy) for dx, dy in type if 0 <= location[0] + dx < 8 and 0 <= location[1] + dy < 8] )
        step_five = list(filter(lambda item: item not in step_three and item not in step_one and item not in step_two and item not in step_four, step_five))
        step_five = list(set(step_five))

        for location in step_five:
            step_six.extend([(location[0] + dx, location[1] + dy) for dx, dy in type if 0 <= location[0] + dx < 8 and 0 <= location[1] + dy < 8] )
        step_six = list(filter(lambda item: item not in step_two and item not in step_four and item not in step_one and item not in step_three and item not in step_five, step_six))
        step_six = list(set(step_six))

        for location in step_six:
            step_seven.extend([(location[0] + dx, location[1] + dy) for dx, dy in type if 0 <= location[0] + dx < 8 and 0 <= location[1] + dy < 8])
        step_seven = list(filter(lambda item: item not in step_two and item not in step_four and item not in step_one and item not in step_three and item not in step_five and item not in step_six, step_seven))
        step_seven = list(set(step_seven))
       
        if jumps==1:
            return step_one
        if jumps==2:
            return step_two
        if jumps==3:
            return step_three
        if jumps==4:
            return step_four
        if jumps==5:
            return step_five
        if jumps==6:
            return step_six
        if jumps==7:
            return step_seven
        else:
            return []
            print("too long a length")
        

class Chess_to_points(Scene):
    def construct(self):

        m=2
        n=2

        fen="9/9/9/9/4N4/9/9/9/9 w KQkq - 0 1"

        #fen = Chess_fill_in_numbers.generate_fen(m,n, piece)
        pieces=ChessBoard(fen)
        size=9
        background=CircleBoard(size)
        point=(m,n)
        
        pieces.move_to(ORIGIN) 
        #background=background.convert_to_circles(size)
        background.move_to(ORIGIN)

        ax = Axes(tips=False, y_range=[-4,4,1], x_range=[-4,4,1], y_length=8, x_length=8)
        self.add(ax)

        self.add(background,pieces)

        #self.play(background.animate_to_circles(size))

        self.play(AnimationGroup(background.animate_to_circles(size), FadeOut(pieces)), run_time=2)
        self.wait()

class points(Scene):
    def construct(self):
        size=15
        board=CircleBoard(size)
        smallboard=CircleBoard(9)
        smallboard.move_to(ORIGIN)
        board.move_to(ORIGIN)
        #board.add_circle(1,2,RED)
        self.add(smallboard)
        self.wait()
        ax = Axes(tips=False, y_range=[-4,4,1], x_range=[-size//2+0.5,size//2+0.5,1], y_length=8, x_length=size)
        self.play(smallboard.animate_to_circles(9), FadeIn(ax))
        self.wait()
        board=board.convert_to_circles(size)
        self.play(FadeIn(board))
        self.wait()
     
        #Generate Initial Labels


        tex1 = MathTex("(1,1)")
        tex1.set_color(GREEN).scale(1)
        tex1.move_to(RIGHT * 1 + UP* (1+0.5))    
        

        tex2 = MathTex("(3,2)")
        tex2.set_color(RED).scale(1)
        tex2.move_to(RIGHT * 3 + UP* (2+0.5)) 
        
        self.play(FadeIn(create_circle(1,1,GREEN)),Write(tex1), run_time=0.75)
        self.play(FadeIn(create_circle(3,2,RED)),Write(tex2), run_time=0.75)
        self.wait()

        tex3 = MathTex("(2,1)")
        tex3.set_color(BLUE).scale(1)
        tex3.move_to(RIGHT * 2.5 + UP* (.5))

        arrow=add_knight_arrow_circle(1,1,2,1)
        self.play(Create(arrow),Write(tex3))
        self.wait()


        



        plus = MathTex("+").scale(1)
        equals = MathTex("=").scale(1)

        full_expr = MathTex("{{(1,1)}}", "+", "{{(2,1)}}", "=", "{{(3,2)}}")
        full_expr.move_to(UP*3.45 + RIGHT*2.5)
        full_expr[0].set_color(GREEN)     # Color (1,1) red
        full_expr[2].set_color(BLUE)    # Color (2,1) blue
        full_expr[4].set_color(RED)   # Color (3,2) green

        box = Rectangle(
            width=full_expr.width + 0.25,  # Add some padding around the expression
            height=full_expr.height + 0.25,  # Add some padding around the expression
            stroke_color=YELLOW,  # Yellow stroke
            fill_color=BLACK,  # No fill (you can keep it BLACK or make it transparent)
            fill_opacity=0  # Make the fill fully transparent
        )
        box.move_to(full_expr.get_center())

       
        self.wait()

        # self.play(
        #     Transform(tex1, full_expr[0]),
        #     Transform(tex2, full_expr[4]),
        #     Transform(tex3, full_expr[2]),
        #     FadeIn(full_expr[1], full_expr[3])
        # )
        texgroup=VGroup(tex1,tex2,tex3)
        self.play(TransformMatchingTex(texgroup,full_expr))
        self.play(Create(box))
        self.wait()

class point_triangle(Scene):
    def construct(self):
        size=15
        board=CircleBoard(size)
        board=board.convert_to_circles(size)
        board.move_to(ORIGIN)
        point=[[0,0,0], [8,4,0], [8,0,0]]
        point2=[[0,0,0], [8,8,0], [8,4,0]]
    
        ax = Axes(tips=False, y_range=[-4,4,1], x_range=[-size//2+0.5,size//2+0.5,1], y_length=8, x_length=size)
        self.add(board, ax)
        triangle=Polygon(*point, color=TEAL, stroke_width=5, fill_color=TEAL, fill_opacity=0.9)
      
        triangle2=Polygon(*point2, color=BLUE_E, stroke_width=5, fill_color=BLUE_E, fill_opacity=0.9)
    
        
        #tex2=MathTex(r"N_{(a,b)}(x,y)}\leq \frac{x}{b} +O(b)")

     

       


        tex2 = MathTex(
            r"N_{(a,b)}(x,y)", 
            r"\leq", 
            r"\frac{x}{b}", 
            r"+", 
            r"O(b)"
        )
        tex6=MathTex(r"\frac{x+y}{a+b}+O(b)")
        tex6.set_color(YELLOW)
        tex6.move_to((5.25*RIGHT+3.35*UP))

        # Arrange the components to look like a single equation
        tex2.arrange(RIGHT, buff=0.2)
        tex2.move_to(RIGHT*4.25+UP*0.6)
        tex2.set_color(YELLOW)

        # Select the "O(b)" part explicitly
        ob_part = tex2[-1]  # Index of the last component ("O(b)")

        # Create a rectangle around the "O(b)" part
        highlight = SurroundingRectangle(ob_part, color=RED, buff=0.1)


    

       

        tex3=Tex("$N_{(a,b)}(x,y)$ is  \# of moves")
        tex4=Tex(" for an $(a,b)$-superknight ")
        tex5=Tex("to get from $(0,0)$ to $(x,y)$")

        group = VGroup(tex3, tex4, tex5).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        # Move the group to the top-left corner
        group.to_corner(UP + LEFT, buff=0.2)

        background = Rectangle(
            width=group.width + 0.2,  # Add padding
            height=group.height + 0.2,  # Add padding
            color=YELLOW,  # Outline color
            fill_color=BLACK,  # Fill color
            stroke_width=0,
            fill_opacity=1,  # Solid background
        )
        background.move_to(group.get_center())

        self.add(triangle, triangle2)
        self.wait()
        triangles=VGroup()
        for i in range(1,8):
            rotated_triangle=triangle.copy().rotate(i*TAU/8,about_point=ORIGIN)
            triangles.add(rotated_triangle)
        for i in range(8):
            rotated_triangle=triangle2.copy().rotate(i*TAU/8,about_point=ORIGIN)
            triangles.add(rotated_triangle)
        self.play(Create(triangles))
        self.wait()


        # self.add( background, group)
        # self.wait()
        # self.play(Create(triangle))
        # self.play(Write(tex2))
        # self.wait(3)
        # self.play(Create(highlight))
        # self.wait(0.25)
        # self.play(Uncreate(highlight))
        # self.wait()
        # self.play(Create(triangle2))
        # self.play(Write(tex6))
        # self.wait()
       

     
        #Generate Initial Labels



class superknight(Scene):
    def construct(self):
        fen = Super_Board.generate_big_fen(0,3,"S",8,8)
        print(fen)
        point=(3,0)
        board=ChessBoard(fen)
        board.add_highlight(3, 0, GREEN)
        board.add_highlight(3, 2, RED)
       
        tex=MathTex("?")
        tex.scale(1.25)
        tex.move_to(LEFT*1.5+0.5*UP)
        tex.z_index=2
        brace=BraceBetweenPoints(RIGHT*2.5+2.5*UP, LEFT*3.5+2.5*UP)
        brace.set_stroke(width=7)
        brace.set_color(PINK)
        tex2=MathTex("2b")
        tex2.scale(1.25)
        tex2.move_to(LEFT*0.5+3.5*UP)
        tex2.set_color(PINK)
        background = BackgroundRectangle(tex2, color=BLACK, fill_opacity=1, buff=0.1)


        brace3=BraceBetweenPoints(RIGHT*2.5+.75*UP, LEFT*1.5+.75*UP)
        brace3.set_stroke(width=7)
        brace3.set_color(PINK)
        tex3=MathTex("2a")
        tex3.scale(1.25)
        tex3.move_to(RIGHT*0.5+1.7*UP)
        tex3.set_color(PINK)
        background3 = BackgroundRectangle(tex3, color=BLACK, fill_opacity=1, buff=0.1)

 
        



        center=board.get_center()

        board.move_to(ORIGIN)
        self.add(board,tex)
        self.wait()
        board1=board.copy()
        


        board.move_to(center)
        board.add_knight_arrow(3,0, -2,3)
        board.move_to(ORIGIN)
        self.add(board)
        self.wait()
        board.move_to(center)
        board.add_knight_arrow(1,3, 2,3)
        board.move_to(ORIGIN)
        self.add(board)
        self.wait()
        board.move_to(center)
        board.add_highlight(3,6,PINK)
        board.move_to(ORIGIN)
        self.add(board)
        self.wait()
        self.play(Create(brace), Create(background), Write(tex2))
        self.wait()
        board.move_to(center)

        self.remove(board)
        board1.move_to(ORIGIN)
        self.add(board1,brace,background,tex2)

        board1.add_highlight(3,6,PINK)
        self.wait()
        board1.move_to(center)
        board2=board1.copy()


        board1.add_knight_arrow(3,6, 3,-2)
        board1.move_to(ORIGIN)
        self.add(board1, brace, background,tex2)
        self.wait()
        board1.move_to(center)
        board1.add_knight_arrow(6,4, -3,-2)
        board1.move_to(ORIGIN)
        self.add(board1, brace, background,tex2)
        self.wait()
        self.play(Create(brace3), Create(background3), Write(tex3))
        self.wait()
        self.remove(board1)
        board2.move_to(ORIGIN)
        
        group=Group(board2, brace, brace3, background, background3, tex, tex2, tex3)
        self.add(group)
        self.play(group.animate.scale(0.85).shift(DOWN*0.4))
        self.wait()
        tex4=MathTex("Move\ Right: 2(ax+by)")
        tex4.to_edge(UP, buff=0.1)
        tex4[0][10:].set_color(PINK)
        tex5=MathTex("=2")
        tex5.next_to(tex4, RIGHT, buff=0.1)
        self.play(Write(tex4))
        self.wait()
        self.play(Write(tex5))
        texgroup=Group(tex4,tex5)
        tex6=MathTex("gcd(a,b)=1")
        tex6.to_edge(UP, buff=0.1)
        self.play(TransformMatchingTex(texgroup, tex6))
        self.wait()






      





        type1= [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]

     
        # for type in type1:
        #     board.move_to(center)
        #     board.add_knight_arrow(point[0], point[1],type[0], type[1])
        #     board.add_highlight(point[0]+type[0], point[1]+type[1],RED)
        #     board.move_to(ORIGIN)
        #     self.add(board)
        #     self.wait(0.5)




        # locationN=(4,4)

        # for t in range(10):
        #     while True:
        #         p=random.randint(0,7)
        #         if 0<=locationN[0]+type1[p][0]<=7 and 0<=locationN[1]+type1[p][1]<=7 and Random_Walk.check_knight_move(locationK,(locationN[0]+type1[p][0], locationN[1]+type1[p][1])):
        #             break
        #     fade_out, movement = board.move_piece(locationN[0], locationN[1], locationN[0]+type1[p][0], locationN[1]+type1[p][1])
        #     locationN =(locationN[0]+type1[p][0],locationN[1]+type1[p][1])
        #     self.play(movement)
        #     #self.wait(0.5)


class sumset(Scene):
    def construct(self):
        size=21
        board=CircleBoard(size)
        board=board.convert_to_circles(size)
        board.move_to(ORIGIN)
        #ax = Axes(tips=False, y_range=[-6,6,1], x_range=[-10,10,1], y_length=8, x_length=13.333) #size=21
        #ax = Axes(tips=False, y_range=[-5,5,1], x_range=[-9,9,1], y_length=8, x_length=14.4) #size=17 and 4/5 everywhere else. 
        ax = Axes(tips=False, y_range=[-4,4,1], x_range=[-7,7,1], y_length=8, x_length=14) #size=17 and 4/5 everywhere else. 
        #general formula for x_length is y_length/2 * x_max/y_max *2

        #a=2
        #b=2
        baseset=[(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]
        #baseset=[(2,1),(-1,-1)]
        #baseset=[(2,2),(-2,2),(2,-2),(-2,-2)]

        static=True

        sumsets=[baseset]
        for t in range(5):
            new_level=[]
            for pair in sumsets[t]:
                for basepair in baseset:
                    new_level.append((pair[0]+basepair[0], pair[1]+basepair[1]))
            new_level=list(set(new_level))
            lower_levels = set().union(*sumsets[0:t])
            new_level = [item for item in new_level if item not in lower_levels]
            sumsets.append(new_level)
    


        colors=[GREEN,RED,BLUE,MAROON_E,ORANGE, PURPLE]
        numbers=Group()
        dots=VGroup()
        arrows=VGroup()
        board.scale(4/4) #make 4/6 or 4/5
        self.add(board,ax)


        text_size=56

      

        ax = Axes(tips=False, y_range=[-6,6,1], x_range=[-10,10,1], y_length=8, x_length=13.333) #size=21
        
        board.scale(4/6)
   
        numbers=VGroup()
        dots=VGroup()
        dot=VGroup()

           ##ALL AT ONCE

        dot.add(create_circle(2,3,colors[0]))
        dot.scale(4/6,about_point=ORIGIN)#make 4/6
        tex=MathTex("(a,b)", )
        tex.move_to((2,3.5,0))
        tex.set_color(GREEN)
        tex.scale(4/6,about_point=ORIGIN)#make 4/6
        


        self.play(FadeIn(dot), Write(tex))
        self.wait(2)


        for t in range(5):
            for pair in sumsets[t]:
                dots.add(create_circle(pair[0],pair[1],colors[t]))
                # tex=MathTex(str(t+1))
                # tex.move_to((pair[0],pair[1],0))
                # tex.z_index=1
                # numbers.add(tex)
            dots.scale(4/6,about_point=ORIGIN)#make 4/6
            numbers.scale(4/6, about_point=ORIGIN) #make 4/6
            self.play(FadeIn(dots))
            self.wait(0.5)
            dots.scale(6/4,about_point=ORIGIN)#make 4/6
            numbers.scale(6/4, about_point=ORIGIN)#make 4/6
        dots.scale(4/6,about_point=ORIGIN)#make 4/6
        numbers.scale(4/6, about_point=ORIGIN)#make 4/6



        # Ah=MathTex(r"hA=\{a_1+\cdots+a_h\ |\ a_1,\cdots a_h\in A\}",font_size=text_size)
        # #self.add(index_labels(Ah[0]))
        # Ah[0][1:2].set_color(GREEN)
        # Ah[0][23].set_color(GREEN)
        # Ah[0][0].set_color(YELLOW)
        # Ah[0][12].set_color(YELLOW)
        # Ah[0][21].set_color(YELLOW)

        # group=VGroup(Ah).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # background = Rectangle(
        #     width=group.width + 0.2,  # Add padding
        #     height=group.height + 0.2,  # Add padding
        #     color=YELLOW,  # Outline color
        #     fill_color=BLACK,  # Fill color
        #     stroke_width=3,
        #     fill_opacity=1,  # Solid background
        # )
        # Ah.z_index=3
        # background.z_index=2
        # group.to_corner(UL, buff=0.5)
        # group.z_index=3
        # background.move_to(group.get_center())
        # self.play(Create(background))
        # self.bring_to_front(Ah)
        # self.play(Write(Ah))
        # self.add(Ah)
        # self.wait()


        #region SUMSET 2 POINT ANIMATION
        # self.wait()
        # for pair in sumsets[0]:
        #     dots.add(create_circle(pair[0],pair[1],colors[0]))
        #     tex=MathTex(str(0+1))
        #     tex.move_to((pair[0],pair[1],0))
        #     tex.z_index=2
        #     numbers.add(tex)

        # dots.scale(4/4,about_point=ORIGIN)#make 4/6
        # numbers.scale(4/4, about_point=ORIGIN)#make 4/6

        # tex1=MathTex("(2,1)").set_color(GREEN).scale(0.8)
        # tex2=MathTex("(-1,-1)").set_color(GREEN).scale(0.8)
        # tex1.move_to((2,1.5,0))
        # tex2.move_to((-1,-.5,0))
        # #FadeIn(numbers)
        # self.play(FadeIn(dots),  Write(tex1), Write(tex2))
        # self.wait()

        # text_size=44

        # A=MathTex(r"A=\{ {{(2,1)}}, {{(-1,-1)}}\}",font_size=text_size)
        # A.z_index=2
        # A2=MathTex(r"2A=\{ {{(4,2)}}, {{(-2,-2)}}, {{(1,0)}}\}",font_size=text_size)
        # A3=MathTex(r"3A=\{ {{(6,3)}}, {{(-3,-3)}}, {{(-1,0)}}, {{(3,1)}}\}",font_size=text_size)
        # Adot=MathTex(r"\quad\quad\quad \vdots",font_size=text_size)
        # Ah=MathTex(r"hA=\{a_1+\cdots+a_h\ |\ a_1,\cdots a_h\in A\}",font_size=text_size)
        # #self.add(index_labels(Ah[0]))
        # Ah[0][1:2].set_color(GREEN)
        # Ah[0][23].set_color(GREEN)
        # Ah[0][0].set_color(YELLOW)
        # Ah[0][12].set_color(YELLOW)
        # Ah[0][21].set_color(YELLOW)

        # A.set_color(GREEN)
        # A2.set_color(RED)
        # A3.set_color(BLUE)
        # group=VGroup(A).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
      
       

        # background = Rectangle(
        #     width=group.width + 0.2,  # Add padding
        #     height=group.height + 0.2,  # Add padding
        #     color=YELLOW,  # Outline color
        #     fill_color=BLACK,  # Fill color
        #     stroke_width=3,
        #     fill_opacity=1,  # Solid background
        # )

        # texgroup=VGroup(tex1,tex2)
        # group.to_corner(UL, buff=0.5)
        # background.move_to(group.get_center())
        # self.play(Create(background))
        # self.play(TransformMatchingTex(texgroup,A))
        # self.wait()
        # self.play(FadeIn(numbers))
        # self.wait()
    
       
               
        # self.wait()
        # dots2=VGroup()
        # numbers2=VGroup()

        # for pair in sumsets[1]:
        #     dots2.add(create_circle(pair[0],pair[1],colors[1]))
        #     tex=MathTex(str(1+1))
        #     tex.move_to((pair[0],pair[1],0))
        #     tex.z_index=2
        #     numbers2.add(tex)

        # tex1=MathTex("(4,2)").set_color(RED).scale(0.8)
        # tex2=MathTex("(-2,-2)").set_color(RED).scale(0.8)
        # tex3=MathTex("(1,0)").set_color(RED).scale(0.8)
        # tex1.move_to((4,2.5,0))
        # tex2.move_to((-2,-1.5,0))
        # tex3.move_to((1,0.5,0))

        # self.play(FadeIn(dots2), FadeIn(numbers2), Write(tex1), Write(tex2), Write(tex3))
        # self.wait()


        # tex_group2=VGroup(A,A2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        # background2 = Rectangle(
        #     width=tex_group2.width + 0.2,  # Add padding
        #     height=tex_group2.height + 0.2,  # Add padding
        #     color=YELLOW,  # Outline color
        #     fill_color=BLACK,  # Fill color
        #     stroke_width=3,
        #     fill_opacity=1,  # Solid background
        # )
        # tex_group2.to_corner(UL, buff=0.25)
        # background2.move_to(tex_group2.get_center())
        # self.play(Transform(background, background2), run_time=0.5)
        # texgroup2=VGroup(tex1,tex2,tex3)
        # self.play(TransformMatchingTex(texgroup2,A2))
        # self.wait()

        # arrow1=CurvedArrow((2,1,0), (4,2,0), radius=1.5)
        # arrow2=CurvedArrow((2,1,0), (4,2,0), radius=-1.5)
        # arrow1.z_index=-2
        # arrow1.submobjects[-1].z_index = -2
        # arrow2.z_index=-2
        # arrow2.submobjects[-1].z_index = -2
        # arrow3=CurvedArrow((-1,-1,0), (-2,-2,0), radius=1.5)
        # arrow4=CurvedArrow((-1,-1,0), (-2,-2,0), radius=-1.5)
        # arrow3.z_index=-2
        # arrow3.submobjects[-1].z_index = -2
        # arrow4.z_index=-2
        # arrow4.submobjects[-1].z_index = -2
        # arrow5=CurvedArrow((-1,-1,0), (1,0,0), radius=1.5)
        # arrow6=CurvedArrow((2,1,0), (1,0,0), radius=-1.5)
        # arrow5.z_index=-2
        # arrow5.submobjects[-1].z_index = -2
        # arrow6.z_index=-2
        # arrow6.submobjects[-1].z_index = -2
    
        # self.play(Create(arrow1), Create(arrow2), run_Time=1)
        # self.wait()
        # self.play(Create(arrow3), Create(arrow4), run_Time=1)
        # self.wait()
        # self.play(Create(arrow5), Create(arrow6), run_Time=1)
        # self.wait(3)
        # self.play(FadeOut(arrow1),FadeOut(arrow2),FadeOut(arrow3),FadeOut(arrow4),FadeOut(arrow5),FadeOut(arrow6))
        # self.wait()
        # dots3=VGroup()
        # numbers3=VGroup()

        # for pair in sumsets[2]:
        #     dots3.add(create_circle(pair[0],pair[1],colors[2]))
        #     tex=MathTex(str(2+1))
        #     tex.move_to((pair[0],pair[1],0))
        #     tex.z_index=2
        #     numbers3.add(tex)

        # tex1=MathTex("(6,3)").set_color(BLUE).scale(0.8)
        # tex2=MathTex("(-3,-3)").set_color(BLUE).scale(0.8)
        # tex3=MathTex("(-1,0)").set_color(BLUE).scale(0.8)
        # tex4=MathTex("(3,1)").set_color(BLUE).scale(0.8)
        # tex1.move_to((6,3.5,0))
        # tex2.move_to((-3,-2.5,0))
        # tex3.move_to((-1,0.5,0))
        # tex4.move_to((3,1.5,0))

        # #A3=MathTex(r"3A=\{ {{(6,3)}}, {{(-3,-3)}}, {{(-1,0)}}, {{(3,1)}}\}",font_size=text_size)


        # self.play(FadeIn(dots3), FadeIn(numbers3), Write(tex1), Write(tex2), Write(tex3), Write(tex4))
        # self.wait()
        
        # tex_group3=VGroup(A,A2,A3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        # background3 = Rectangle(
        #     width=tex_group3.width + 0.2,  # Add padding
        #     height=tex_group3.height + 0.2,  # Add padding
        #     color=YELLOW,  # Outline color
        #     fill_color=BLACK,  # Fill color
        #     stroke_width=3,
        #     fill_opacity=1,  # Solid background
        # )
        # tex_group3.to_corner(UL, buff=0.25)
        # texgroup3=VGroup(tex1,tex2,tex3,tex4)
        # background3.move_to(tex_group3.get_center())
        # self.play(Transform(background, background3), run_time=0.5)
        # self.play(TransformMatchingTex(texgroup3,A3))
        # self.wait()

        # arrow1=CurvedArrow((2,1,0), (6,3,0), radius=2.5)
        # arrow2=CurvedArrow((4,2,0), (6,3,0), radius=-1.5)
        # arrow1.z_index=-2
        # arrow1.submobjects[-1].z_index = -2
        # arrow2.z_index=-2
        # arrow2.submobjects[-1].z_index = -2
        # arrow3=CurvedArrow((-1,-1,0), (-3,-3,0), radius=2.5)
        # arrow4=CurvedArrow((-2,-2,0), (-3,-3,0), radius=-1.5)
        # arrow3.z_index=-2
        # arrow3.submobjects[-1].z_index = -2
        # arrow4.z_index=-2
        # arrow4.submobjects[-1].z_index = -2
        # arrow5=CurvedArrow((2,1,0), (3,1,0), radius=-1)
        # arrow6=CurvedArrow((1,0,0), (3,1,0), radius=1.5)
        # arrow5.z_index=-2
        # arrow5.submobjects[-1].z_index = -2
        # arrow6.z_index=-2
        # arrow6.submobjects[-1].z_index = -2
        # arrow7=CurvedArrow((-1,-1,0), (0,-1,0), radius=1)
        # arrow8=CurvedArrow((1,0,0), (0,-1,0), radius=-1)
        # arrow7.z_index=-2
        # arrow7.submobjects[-1].z_index = -2
        # arrow8.z_index=-2
        # arrow8.submobjects[-1].z_index = -2
    
        # self.play(Create(arrow1), Create(arrow2), run_Time=1)
        # self.wait()
        # self.play(Create(arrow3), Create(arrow4), run_Time=1)
        # self.wait()
        # self.play(Create(arrow5), Create(arrow6), run_Time=1)
        # self.wait()
        # self.play(Create(arrow7), Create(arrow8), run_Time=1)
        # self.wait(3)
        # self.play(FadeOut(arrow1),FadeOut(arrow2),FadeOut(arrow3),FadeOut(arrow4),FadeOut(arrow5),FadeOut(arrow6), FadeOut(arrow7), FadeOut(arrow8))
        # self.wait()

        # tex_group4=VGroup(A,A2,A3, Adot, Ah).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        # background4 = Rectangle(
        #     width=tex_group4.width + 0.2,  # Add padding
        #     height=tex_group4.height + 0.2,  # Add padding
        #     color=YELLOW,  # Outline color
        #     fill_color=BLACK,  # Fill color
        #     stroke_width=3,
        #     fill_opacity=1,  # Solid background
        # )
        # tex_group4.to_corner(UL, buff=0.25)
        # background4.move_to(tex_group4.get_center())
        # self.play(Transform(background, background4), run_time=0.5)
        # self.play(Write(Adot), Write(Ah))
        # self.wait()

        # dots4=VGroup()
        # numbers4=VGroup()

        # for pair in sumsets[3]:
        #     dots4.add(create_circle(pair[0],pair[1],colors[3]))
        #     tex=MathTex(str(3+1))
        #     tex.move_to((pair[0],pair[1],0))
        #     tex.z_index=2
        #     numbers4.add(tex)

        # self.play(FadeIn(dots4), FadeIn(numbers4))
        # self.wait()

        # dots5=VGroup()
        # numbers5=VGroup()

        # for pair in sumsets[4]:
        #     dots4.add(create_circle(pair[0],pair[1],colors[4]))
        #     tex=MathTex(str(4+1))
        #     tex.move_to((pair[0],pair[1],0))
        #     tex.z_index=2
        #     numbers5.add(tex)

        # self.play(FadeIn(dots5), FadeIn(numbers5))
        # self.wait()

        # dots6=VGroup()
        # numbers6=VGroup()

        # for pair in sumsets[5]:
        #     dots4.add(create_circle(pair[0],pair[1],colors[5]))
        #     tex=MathTex(str(5+1))
        #     tex.move_to((pair[0],pair[1],0))
        #     tex.z_index=2
        #     numbers5.add(tex)

        # self.play(FadeIn(dots6), FadeIn(numbers6))
        # self.wait(2)
        #endregion


        #region older animations
        ##Algorithmically draw arrows
        # down_starts=[(2,1),(-1,-1), (-1,-1)]
        # down_ends=[(4,2),(-2,-2),(1,0)]
        # up_starts=[(2,1),(-1,-1), (2,1)]
        # up_ends=[(4,2),(-2,-2),(1,0)]
        # for t in range(len(down_starts)):
        #     arrow=CurvedArrow((down_starts[t][0],down_starts[t][1],0), (down_ends[t][0],down_ends[t][1],0), radius=1.5)
        #     arrow.z_index=-2
        #     arrows.add(arrow)
        # for t in range(len(down_starts)):
        #     arrow=CurvedArrow((up_starts[t][0],up_starts[t][1],0), (up_ends[t][0],up_ends[t][1],0), radius=-1.5)
        #     arrow.z_index=-2
        #     arrows.add(arrow)





        
        # ##ALL AT ONCE
        # for t in range(len(sumsets)):
        #     for pair in sumsets[t]:
        #         dots.add(create_circle(pair[0],pair[1],colors[t]))
        #         tex=MathTex(str(t+1))
        #         tex.move_to((pair[0],pair[1],0))
        #         tex.z_index=2
        #         numbers.add(tex)
        #     if static==False:
        #         dots.scale(4/6,about_point=ORIGIN)#make 4/6
        #         numbers.scale(4/6, about_point=ORIGIN) #make 4/6
        #         self.add(dots, numbers)
        #         self.wait()
        #         dots.scale(6/4,about_point=ORIGIN)#make 4/6
        #         numbers.scale(6/4, about_point=ORIGIN)#make 4/6




       


                
        # #all at once
        # if static==True:
        #     dots.scale(4/5,about_point=ORIGIN)#make 4/6
        #     numbers.scale(4/5, about_point=ORIGIN)#make 4/6
        #     arrows.scale(4/5, about_point=ORIGIN)#make 4/6
        #     self.add(arrows)
        #     self.add(dots)
        #     self.add(numbers)
        
        # text_size=36

        # A=MathTex(r"A=\{(2,1), (-1,-1)\}",font_size=text_size)
        # A2=MathTex(r"2A=\{(4,2), (-2,-2), (1,0)\}",font_size=text_size)
        # A3=MathTex(r"3A=\{(6,3), (-3,-3), (-1,0), (3,1)\}",font_size=text_size)
        # Adot=MathTex(r"\quad\quad\quad \vdots",font_size=text_size)
        # Ah=MathTex(r"hA=\{a_1+\cdots+a_h\ |\ a_1,\cdots a_h\in A\}",font_size=text_size)
        # #self.add(index_labels(Ah[0]))
        # Ah[0][1:2].set_color(GREEN)
        # Ah[0][23].set_color(GREEN)
        # Ah[0][0].set_color(YELLOW)
        # Ah[0][12].set_color(YELLOW)
        # Ah[0][21].set_color(YELLOW)

        # A.set_color(GREEN)
        # A2.set_color(RED)
        # A3.set_color(BLUE)
        # group=VGroup(A,A2,A3,Adot,Ah).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
       

        # background = Rectangle(
        #     width=group.width + 0.2,  # Add padding
        #     height=group.height + 0.2,  # Add padding
        #     color=YELLOW,  # Outline color
        #     fill_color=BLACK,  # Fill color
        #     fill_opacity=1,  # Solid background
        # )

        # background.move_to(group.get_center())
        # textbox = VGroup(background, group)
        # textbox.to_corner(UL, buff=0.25)
        # self.add(textbox)
        #endregion

class Chess_moves_noanim(Scene):
    def construct(self):
             
        type1= [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]
        type2=[(1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 1)]

        #t=1
        totalK=0
        totalN=0

        

        maxi=100
        for t in range(1,maxi):
            point1=(random.randint(0,7),random.randint(0,7)) 
            while True:
                point2 = (random.randint(0, 7), random.randint(0, 7))
                if point2 != point1:
                    break
            # point1=(0,0)
            # point2=(1,2)
        
            fen = Super_Board.generate_big_fen(point1[1],point1[0],"1",8,8)
            board1=ChessBoard(fen)
            fen = Super_Board.generate_big_fen(point1[1],point1[0],"K",8,8)
            board2=ChessBoard(fen)

            board1.add_highlight(point1[0], point1[1], GREEN)
            board1.add_highlight(point2[0], point2[1], RED)

            board2.add_highlight(point1[0], point1[1], GREEN)
            board2.add_highlight(point2[0], point2[1], RED)
            
            movesN = Chess_moves.get_move_list(point1, point2,type1)


            point1_it=point1
            for move in movesN:
                board1.add_knight_arrow(point1_it[0], point1_it[1],move[0], move[1])
                point1_it=(point1_it[0]+move[0], point1_it[1]+move[1])



            point1_it=point1
            movesK = Chess_moves.get_move_list(point1, point2,type2)


            for move in movesK:
                board1.add_king_arrow(point1_it[0], point1_it[1],move[0], move[1])
                point1_it=(point1_it[0]+move[0], point1_it[1]+move[1])

            totalK=totalK+len(movesK)
            totalN=totalN+len(movesN)
            averageK=totalK/t
            averageN=totalN/t
            
        print(averageK, ",", averageN)
 

  
  
class Chess_moves(Scene):
    def construct(self):
             
        type1= [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]
        type2=[(1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 1)]

        #t=1
        totalK=0
        totalN=0

        #region Main Moves Animation
        # maxi=300
        # for t in range(1,maxi):
        #     point1=(random.randint(0,7),random.randint(0,7)) 
        #     while True:
        #         point2 = (random.randint(0, 7), random.randint(0, 7))
        #         if point2 != point1:
        #             break
        #     # point1=(0,0)
        #     # point2=(1,2)
        
        #     fen = Super_Board.generate_big_fen(point1[1],point1[0],"1",8,8)
        #     board1=ChessBoard(fen)
        #     fen = Super_Board.generate_big_fen(point1[1],point1[0],"K",8,8)
        #     board2=ChessBoard(fen)

        #     board1.add_highlight(point1[0], point1[1], GREEN)
        #     board1.add_highlight(point2[0], point2[1], RED)

        #     board2.add_highlight(point1[0], point1[1], GREEN)
        #     board2.add_highlight(point2[0], point2[1], RED)
            
        #     movesN = Chess_moves.get_move_list(point1, point2,type1)


        #     point1_it=point1
        #     for move in movesN:
        #         board1.add_knight_arrow(point1_it[0], point1_it[1],move[0], move[1])
        #         point1_it=(point1_it[0]+move[0], point1_it[1]+move[1])



        #     point1_it=point1
        #     movesK = Chess_moves.get_move_list(point1, point2,type2)


        #     for move in movesK:
        #         board1.add_king_arrow(point1_it[0], point1_it[1],move[0], move[1])
        #         point1_it=(point1_it[0]+move[0], point1_it[1]+move[1])

        #     totalK=totalK+len(movesK)
        #     totalN=totalN+len(movesN)
        #     averageK=totalK/t
        #     averageN=totalN/t

        #     board1.scale(0.9)
        #     board1.move_to(ORIGIN)
        #     board1.shift(DOWN*0.25)
        #     textK = Text(f"King Moves:").set_color(YELLOW).scale(0.75)
        #     textK.to_edge(UP+LEFT, buff=0.1)
        #     variable_textK = DecimalNumber(averageK, num_decimal_places=2).set_color(YELLOW).scale(.9)
        #     variable_textK.next_to(textK, RIGHT, buff=0.1)

        #     textN = Text(f"Knight Moves:").set_color(BLUE).scale(0.75)
        #     textN.to_edge(UP+RIGHT, buff=0.1)
        #     textN.shift(LEFT)
        #     variable_textN = DecimalNumber(averageN, num_decimal_places=2).set_color(BLUE).scale(.9)
        #     variable_textN.next_to(textN, RIGHT, buff=0.1)
            
        

        
        #     self.add(board1,textK,variable_textK,textN, variable_textN)
        #     timestep=max((maxi-5*t)/maxi, 1/30)
        #     self.wait(timestep)
        #     self.remove(board1,textK,variable_textK, textN, variable_textN)

        # variable_textK = DecimalNumber(3.75, num_decimal_places=2).set_color(YELLOW).scale(.9)
        # variable_textN = DecimalNumber(2.88, num_decimal_places=2).set_color(BLUE).scale(.9)
        # variable_textN.next_to(textN, RIGHT, buff=0.1)
        # variable_textK.next_to(textK, RIGHT, buff=0.1)
        # self.add(board1, textK, textN,variable_textK,variable_textN)
        # self.wait()
        # ratio=Text("Ratio: 1.3").set_color(RED).scale(.9)
        # ratio.to_edge(UP, buff=0.1)
        # self.play(Write(ratio))
        # self.wait()
        #endregion

        point1=(3,5)
        point2=(6,1)
        fen = Super_Board.generate_big_fen(point1[1],point1[0],"1",8,8)
        board1=ChessBoard(fen)
        center=board1.get_center()
        #board1.scale(0.9)
        board1.move_to(ORIGIN)
        #board1.shift(DOWN*0.25)
        self.add(board1)
        self.wait()
        board1.add_highlight(point1[0], point1[1], GREEN)
        self.add(board1)
        self.wait(0.25)
        board1.add_highlight(point2[0], point2[1], RED)
        

        self.add(board1)
        self.wait()
        movesN = Chess_moves.get_move_list(point1, point2,type1)
        point1_it=point1
        karrows=VGroup()
        for move in movesN:
            board1.move_to(center)
            board1.add_knight_arrow(point1_it[0], point1_it[1],move[0], move[1])
            point1_it=(point1_it[0]+move[0], point1_it[1]+move[1])
            board1.move_to(ORIGIN)
            self.add(board1)
            self.wait(0.5)

        point1_it=point1
        movesK = Chess_moves.get_move_list(point1, point2,type2)
        for move in movesK:
            board1.move_to(center)
            board1.add_king_arrow(point1_it[0], point1_it[1],move[0], move[1])
            point1_it=(point1_it[0]+move[0], point1_it[1]+move[1])
            board1.move_to(ORIGIN)
            self.add(board1)
            self.wait(0.5)

        totalK=totalK+len(movesK)
        totalN=totalN+len(movesN)
        averageK=totalK
        averageN=totalN

        self.wait()
        self.play(board1.animate.scale(0.9).shift(DOWN*0.25))
       

        
        textK = Text(f"King Moves:").set_color(YELLOW).scale(0.75)
        textK.to_edge(UP+LEFT, buff=0.1)
        variable_textK = DecimalNumber(averageK, num_decimal_places=2).set_color(YELLOW).scale(.9)
        variable_textK.next_to(textK, RIGHT, buff=0.1)

        textN = Text(f"Knight Moves:").set_color(BLUE).scale(0.75)
        textN.to_edge(UP+RIGHT, buff=0.1)
        textN.shift(LEFT)
        variable_textN = DecimalNumber(averageN, num_decimal_places=2).set_color(BLUE).scale(.9)
        variable_textN.next_to(textN, RIGHT, buff=0.1)

        self.play(Write(textN), Write(variable_textN))
        self.wait(0.5)
        self.play(Write(textK), Write(variable_textK))
        self.wait()
    
        #self.add(board1,textK,variable_textK,textN, variable_textN)






            # self.wait()
            # self.remove(board)

    @staticmethod
    def get_move_list(point1, point2,type):  
        type=type
        moves=[]      

        step_one=Chess_fill_in_numbers.get_knight_moves(point1,1,type)
        step_two=Chess_fill_in_numbers.get_knight_moves(point1,2,type)
        step_three=Chess_fill_in_numbers.get_knight_moves(point1,3,type)
        step_four=Chess_fill_in_numbers.get_knight_moves(point1,4,type)
        step_five=Chess_fill_in_numbers.get_knight_moves(point1,5,type)
        step_six=Chess_fill_in_numbers.get_knight_moves(point1,6,type)
        step_seven=Chess_fill_in_numbers.get_knight_moves(point1,7,type)
        found=False

        if point2 in step_seven:
            for step in step_six:
                for knight_move in type:
                    if (knight_move[0]+step[0], knight_move[1]+step[1])==point2:
                        moves.append(knight_move)
                        point2=step
                        found = True
                        break
                if found:
                    break 

        found=False
        if point2 in step_six:
            for step in step_five:
                for knight_move in type:
                    if (knight_move[0]+step[0], knight_move[1]+step[1])==point2:
                        moves.append(knight_move)
                        point2=step
                        found = True
                        break
                if found:
                    break 

        found=False
        if point2 in step_five:
            for step in step_four:
                for knight_move in type:
                    if (knight_move[0]+step[0], knight_move[1]+step[1])==point2:
                        moves.append(knight_move)
                        point2=step
                        found = True
                        break
                if found:
                    break 

        found=False


        if point2 in step_four:
            for step in step_three:
                for knight_move in type:
                    if (knight_move[0]+step[0], knight_move[1]+step[1])==point2:
                        moves.append(knight_move)
                        point2=step
                        found = True
                        break
                if found:
                    break 

        found=False

        if point2 in step_three:
            for step in step_two:
                for knight_move in type:
                    if (knight_move[0]+step[0], knight_move[1]+step[1])==point2:
                        moves.append(knight_move)
                        point2=step
                        found = True
                        break
                if found:
                    break 

        found=False
       
        #If in step_two
        if point2 in step_two:
            for step in step_one:
                for knight_move in type:
                    if (knight_move[0]+step[0], knight_move[1]+step[1])==point2:
                        moves.append(knight_move)
                        point2=step
                        found = True
                        break
                if found:
                    break  

        #If in step_one
        if point2 in step_one:
            for knight_move in type:
                if (knight_move[0]+point1[0], knight_move[1]+point1[1])==point2:
                    moves.append(knight_move)
                    break

        
        moves.reverse()
        return moves
    

class Chess_total_prob(Scene):
    def construct(self):
        total_king=0
        total_knight=0
        type1= [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]
        type2=[(1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 1)]
        for x_start in range(8):
            for y_start in range(8):
                for jumps in range(1,7):  
                    total_knight=total_knight+jumps*len(Chess_fill_in_numbers.get_knight_moves((x_start,y_start),jumps,type1))
        print("knight: ",total_knight/(64*63))

        for x_start in range(8):
            for y_start in range(8):
                for jumps in range(1,8):  
                    total_king=total_king+jumps*len(Chess_fill_in_numbers.get_knight_moves((x_start,y_start),jumps,type2))
        print("king: ",total_king/(64*63))
        print("ratio: ", total_king/total_knight)

class Chess_piece_moves(Scene):
    def construct(self):
        
        board= ChessBoard("8/8/8/8/4K3/8/8/8 w KQkq - 0 1")
        board.add_highlight(4, 4, GREEN)
          
        type1= [(-b, a),(b, a),(a, b), (a, -b), (b, -a), (-b, -a), (-a, -b),  (-a, b),]
        type2=[(1, 0),(1, -1), (0, -1),(-1, -1), (-1, 0),(-1, 1), (0, 1),(1, 1)]

        center=board.get_center()

        #King Opening
        # self.add(board.move_to(ORIGIN))
        # self.wait(2)
        # for type in type2:
        #     self.remove(board)
        #     board.move_to(center)
        #     board.add_highlight(4+type[0],4+type[1],RED)
        #     board.add_king_arrow(4,4,type[0],type[1])
        #     self.add(board.move_to(ORIGIN))
        #     if type==(1,0):
        #         self.wait(2)
        #     else:
        #         self.wait(0.5)

        # #Knight Opening
        # board0= ChessBoard("8/8/8/8/4N3/8/8/8 w KQkq - 0 1")
        # board0.add_highlight(4, 4, GREEN)

        # self.add(board0.move_to(ORIGIN))
        # self.wait(2)
        
        # for type in type1:
        #     self.remove(board0)
        #     board0.move_to(center)
        #     board0.add_highlight(4+type[0],4+type[1],RED)
        #     board0.add_knight_arrow(4,4,type[0],type[1])
        #     self.add(board0.move_to(ORIGIN))
        #     if type==(-b,a):
        #         self.wait(3)
        #     else:
        #         self.wait()

       
        # board= ChessBoard("8/8/8/8/4N3/8/8/8 w KQkq - 0 1")
        # board.add_highlight(4, 4, GREEN)
        # # for type in type1: 
        # #     board.add_highlight(4+type[0],4+type[1],GREEN)
            
        # for ty in type1: 
        #     board.add_text(4+ty[0],4+ty[1], "1", RED)

        # board.move_to(ORIGIN)
        # self.play(FadeIn(board))
        # self.wait()
        # self.remove(board)
        # board.add_highlight(2,3,GREEN)
        # self.add(board)
        # self.wait()
      

        # for type in type1:
        #     if type!=(2,1):
        #         self.remove(board)
        #         board.move_to(center)
        #         board.add_highlight(2+type[0],3+type[1],RED)
        #         board.add_knight_arrow(2,3,type[0],type[1])
                
        #         for ty in type1: 
        #             board.add_text(4+ty[0],4+ty[1], "1", RED)
        #         self.add(board.move_to(ORIGIN))
        #         self.wait(0.2)
        # self.wait()

        board2=ChessBoard("8/8/8/8/4N3/8/8/8 w KQkq - 0 1")
        board2.add_highlight(4, 4, GREEN)
        

        for ty in type1: 
            board2.add_text(4+ty[0],4+ty[1], "1", RED)
        for type in type1:
            if type!=(1,2):
                board2.add_text(3+type[0],2+type[1],"2", BLUE)

        board3=board2.copy()
        # board2.add_highlight(2,3,GREEN) 
        # board2.move_to(ORIGIN)



        # self.play(FadeIn(board2))
        # self.wait(2)

        self.add(board3)

        
        
        board3.move_to(center)
        moves_two=Chess_fill_in_numbers.get_knight_moves((4,4),2,type1)
        for move in moves_two:
            board3.add_text(move[0], move[1], "2", BLUE)
        board3.move_to(ORIGIN)

        # self.wait()
        # board3.move_to(center)
        # fade_in = board3.FadeIn_text(2, 3, "3", YELLOW)
        # board3.move_to(ORIGIN)
        # self.play(fade_in)

        self.wait()

        moves_three=Chess_fill_in_numbers.get_knight_moves((4,4),3,type1)
        board3.move_to(center)
        for move in moves_three:
            
            board3.add_text(move[0], move[1], "3", YELLOW)
        board3.move_to(ORIGIN)
        self.add(board3)
        self.wait()


        moves_four=Chess_fill_in_numbers.get_knight_moves((4,4),4,type1)
        board3.move_to(center)
        for move in moves_four:
            board3.add_text(move[0], move[1], "4", PINK)
        board3.move_to(ORIGIN)
        self.add(board3)
        self.wait()

        moves_five=Chess_fill_in_numbers.get_knight_moves((4,4),5,type1)
        board3.move_to(center)
        for move in moves_five:
            board3.add_text(move[0], move[1], "5", GREEN)
        board3.move_to(ORIGIN)
        self.add(board3)
        self.wait()

        # self.play(FadeIn(board3))
        # self.wait(3)

class Super_Board(Scene):
    def construct(self):
        
        fen0=Super_Board.generate_big_fen(0,0,"1", 8,8)
        fen=Super_Board.generate_big_fen(0,0,"1", 16,16)
        # fen2=Super_Board.generate_big_fen(0,0,"1", 32,32)
        #fen3=Super_Board.generate_big_fen(0,0,"1", 64,64)
        board=ChessBoard(fen)
        board0=ChessBoard(fen0)
        # board2=ChessBoard(fen2)
        # board3=ChessBoard(fen3)
        #board.scale(0.5)

        # self.add(board0.move_to(ORIGIN))
        # self.wait()
        # board3.move_to(ORIGIN)
        # self.play(FadeIn(board3))
        # #self.add(board3.move_to(ORIGIN))
        # self.wait()
        # self.play(board3.animate.scale(0.125*16/9), run_time=3)
        # self.wait()


        # board2.scale(0.25)
        # board3.scale(0.125)

        # self.add(board0.move_to(ORIGIN))
        # self.wait()
        # board.move_to(ORIGIN)
        # board2.move_to(ORIGIN)
        # board3.move_to(ORIGIN)
        # self.play(board0.animate.scale(0.5).shift(DOWN*2+LEFT*2))
        # self.play(FadeIn(board))
        # self.wait()
        # self.remove(board0)
        # self.play(board.animate.scale(0.5).shift(DOWN*2+LEFT*2))
        # self.play(FadeIn(board2))
        # self.wait()
        # self.remove(board)
        # self.play(board2.animate.scale(0.5).shift(DOWN*2+LEFT*2))
        # self.play(FadeIn(board3))
        # self.wait()
        
        center=board0.get_center()
        
        # board.add_highlight(15,0,GREEN)
        # board.add_highlight(0,15,RED)
        # board.scale(0.5)
        # self.add(board.move_to(ORIGIN))

       

        #Horizontal Paths

       
        

        board0.add_highlight(2,0,GREEN)
        board0.add_highlight(2,4,RED)
        self.add(board0.move_to(ORIGIN))
        self.wait()

        # for t in range(3):
        #     self.remove(board0)
        #     board0.move_to(center)

        #     board0.add_king_arrow(7-t,t,-1,1)
        #     if t % 2 == 0 and t<2:
        #         board0.add_knight_arrow(7-3*t/2,3*t/2,-1,2)
        #     if t % 2 !=0 and t<2:
        #         board0.add_knight_arrow(7-3*(t+1)/2+2,3*(t+1)/2-1,-2,1)

        #     board0.move_to(ORIGIN)
        #     self.add(board0)
        #     self.wait()
        # self.wait()

        for t in range(4):
            self.remove(board0)
            board0.move_to(center)
            board0.add_king_arrow(2,t,0,1,12)
            if t % 2 ==0 and t<2:
                board0.add_knight_arrow(2,2*t,-1,2)
            if t % 2 !=0 and t<2:
                board0.add_knight_arrow(1,2*t,1,2)
        
            board0.move_to(ORIGIN)
            self.add(board0)
            self.wait()
        self.wait()

        board0blank=ChessBoard(fen0)
        board0blank.add_highlight(2,0,GREEN)
        board0blank.move_to(ORIGIN)
        self.add(board0blank)
        self.play(FadeOut(board0), run_time=0.5)

        board.add_highlight(10,0,GREEN)
        board.add_highlight(9,14,RED)
        board.scale(0.5)
        board.z_index=-1
        center=board.get_center()
        board.move_to(ORIGIN)

        self.play(AnimationGroup(board0blank.animate.scale(0.5).shift(DOWN*2+LEFT*2), FadeIn(board), lag_ratio=0.5), run_time=1.5)

        # for obj in board0:
        #     if isinstance(obj, Arrow):  # Check if the object is an Arrow
        #         obj.set_opacity(0)

        self.wait()


      
        ## Diagonal Paths
        # for t in range(10):
        #     self.remove(board)
        #     board.move_to(center)
        #     board.scale(2)
        #     board.add_king_arrow(15-t,t,-1,1,7)
        #     if t % 2 == 0:
        #         board.add_knight_arrow(15-3*t/2,3*t/2,-1,2,7)
        #     if t % 2 !=0:
        #         board.add_knight_arrow(15-3*(t+1)/2+2,3*(t+1)/2-1,-2,1,7)
        #     board.scale(0.5)
        #     board.move_to(ORIGIN)
        #     self.add(board)
        #     self.wait()
        # self.wait()

        for t in range(7):
            self.remove(board)
            board.move_to(center)
            board.scale(2)
            board.add_king_arrow(10,t,0,1,7)
            if t % 2 == 0:
                board.add_knight_arrow(10,2*t,-1,2,7)
            if t % 2 !=0:
                board.add_knight_arrow(9,2*t,1,2,7)
            board.scale(0.5)
            board.move_to(ORIGIN)
            self.add(board)
            self.wait()
        self.wait()

    @staticmethod
    def generate_big_fen(n,m,piece, rows, cols):
        # Step 1: Generate random (m, n) coordinates
        m = m
        n = n

        # Step 2: Initialize the board (8 rows of 8 columns, filled with '1' for empty squares)
        board = [['1' for _ in range(rows)] for _ in range(cols)]

        # Step 3: Place the white knight at (m, n)
        board[m][n] = piece  # 'N' represents a white knight in FEN

        # Step 4: Convert the board to a FEN string
        fen = ''
        for row in board:
            empty_count = 0
            row_fen = ''
            for square in row:
                if square == '1':  # Count consecutive empty squares
                    empty_count += 1
                else:
                    if empty_count > 0:
                        row_fen += str(empty_count)  # Add number of empty squares
                        empty_count = 0
                    row_fen += square  # Add the piece (e.g., 'N' for knight)
            if empty_count > 0:  # If row ends with empty squares
                row_fen += str(empty_count)
            fen += row_fen + '/'

        return fen[:-1] + ' w KQkq - 0 1'  # Remove trailing slash and add standard FEN endOR
        
    
    
class Edges(Scene):
    def construct(self):   
        # fen = Super_Board.generate_big_fen(0,0,"N",8,8)
        # board=ChessBoard(fen)
        # board.add_highlight(0,0,GREEN)
        # center=board.get_center()
        # self.add(board.move_to(ORIGIN))
        # self.wait()
        # type1= [(b, a),(a, b),]
        # for type in type1:
        #     self.remove(board)
        #     board.move_to(center)
        #     board.add_highlight(0+type[0],type[1],RED)
        #     board.add_knight_arrow(0,0,type[0],type[1])
        #     self.add(board.move_to(ORIGIN))
        #     self.wait(0.25)
        # self.wait()
        # self.remove(board)
        
        # fen = Super_Board.generate_big_fen(0,4,"N",8,8)
        # board=ChessBoard(fen)
        # board.add_highlight(4,0,GREEN)
        # center=board.get_center()
        # self.add(board.move_to(ORIGIN))
        # self.wait()
        # type1= [(-a, b),(-b, a),(b, a),(a, b),]
        # for type in type1:
        #     self.remove(board)
        #     board.move_to(center)
        #     board.add_highlight(4+type[0],type[1],RED)
        #     board.add_knight_arrow(4,0,type[0],type[1])
        #     self.add(board.move_to(ORIGIN))
        #     self.wait(0.25)
        # self.wait()
        # self.remove(board)

        # fen = Super_Board.generate_big_fen(1,4,"N",8,8)
        # board=ChessBoard(fen)
        # board.add_highlight(4,1,GREEN)
        # center=board.get_center()
        # self.add(board.move_to(ORIGIN))
        # self.wait()
        # type1= [(-a,-b),(-a, b),(-b, a),(b, a),(a, b),(a,-b)]
        # for type in type1:
        #     self.remove(board)
        #     board.move_to(center)
        #     board.add_highlight(4+type[0],1+type[1],RED)
        #     board.add_knight_arrow(4,1,type[0],type[1])
        #     self.add(board.move_to(ORIGIN))
        #     self.wait(0.25)
        # self.wait()
        # self.remove(board)

        # fen = Super_Board.generate_big_fen(1,4,"1",8,8)
        # board=ChessBoard(fen)
        # boardblank=ChessBoard(fen)

        # self.add(boardblank.move_to(ORIGIN))

        # for m in range(8):
        #     for n in range(8):
        #         if m==0 or m==7 or n==0 or n==7:
        #             board.add_highlight(m,n,GREEN)

        # for m in range(1,7):
        #     for n in range(1,7):
        #         if m==1 or m==6 or n==1 or n==6:
        #             board.add_highlight(m,n,BLUE)

        # board.move_to(ORIGIN)

        # self.play(FadeIn(board))
        # self.wait(3)
        # self.play(FadeOut(board))


        fen = Super_Board.generate_big_fen(1,4,"1",8,8)
        fen_piece = Super_Board.generate_big_fen(4,4,"N",8,8)
        board=ChessBoard(fen_piece)
        blankboard=ChessBoard(fen)
        blankboard.move_to(ORIGIN)
        bigfen=Super_Board.generate_big_fen(0,0,"1", 16,16)
        bigboard=ChessBoard(bigfen)
        bigboard.z_index=-1
        blankbigboard=ChessBoard(bigfen)
        blankbigboard.move_to(ORIGIN)
        blankbigboard.scale(0.5)
        bigcenter=bigboard.get_center()



        # self.play(AnimationGroup(boardblank.animate.scale(0.5).shift(DOWN*2+LEFT*2), FadeIn(blankbigboard), lag_ratio=0.5), run_time=1.5)

        # self.wait()

        for m in range(16):
            for n in range(16):
                if m==0 or m==15 or n==0 or n==15:
                    bigboard.add_highlight(m,n,GREEN)

        for m in range(1,15):
            for n in range(1,15):
                if m==1 or m==14 or n==1 or n==14:
                    bigboard.add_highlight(m,n,BLUE)

        bigboard.move_to(ORIGIN).scale(0.5)
        self.add(bigboard)
        self.play(FadeIn(blankbigboard))
        self.remove(bigboard)
        self.add(blankboard.scale(0.5).shift(DOWN*2+LEFT*2))
        self.play(FadeOut(blankbigboard))
        self.play(blankboard.animate.scale(2).shift(UP*2+RIGHT*2))
        self.wait()
        self.remove(blankboard)
        board.add_highlight(4,4,GREEN)
        board.add_highlight(4,5,RED)
       
        center=board.get_center()
        self.add(board.move_to(ORIGIN))
        self.wait()
        self.remove(board)
        board.move_to(center)
        board.add_knight_arrow(4,4,-2,1)
        self.add(board.move_to(ORIGIN))
        self.wait(0.5)
        self.remove(board)
        board.move_to(center)
        board.add_knight_arrow(2,5,1,2)
        self.add(board.move_to(ORIGIN))
        self.wait(0.5)
        self.remove(board)
        board.move_to(center)
        board.add_knight_arrow(3,7,1,-2)
        self.add(board.move_to(ORIGIN))
        self.wait()

class Random_Walk(Scene):
    def construct(self): 
        board= ChessBoard("8/3N4/8/8/4k3/8/8/8 w KQkq - 0 1")
        type1= [(-b, a),(b, a),(a, b), (a, -b), (b, -a), (-b, -a), (-a, -b),  (-a, b),]
        type2=[(1, 0),(1, -1), (0, -1),(-1, -1), (-1, 0),(-1, 1), (0, 1),(1, 1)]

        self.add(board.move_to(ORIGIN))
        self.wait()
        locationN=(1,3)
        locationK=(4,4)
        # p=1

        # fade_out, movement = board.move_piece(location[0], location[1], location[0]+type1[p][0], location[1]+type1[p][1])
        # self.play(movement)
        # self.wait()
        # location =(location[0]+type1[p][0],location[1]+type1[p][1])
        # print(location)

        # p=3
        # fade_out, movement = board.move_piece(location[0], location[1], location[0]+type1[p][0], location[1]+type1[p][1])
        # self.play(movement)
        # self.wait()
        # location =(location[0]+type1[p][0],location[1]+type1[p][1])
        # print(location)
    


        for t in range(20):
            while True:
                p=random.randint(0,7)
                if 0<=locationN[0]+type1[p][0]<=7 and 0<=locationN[1]+type1[p][1]<=7 and Random_Walk.check_knight_move(locationK,(locationN[0]+type1[p][0], locationN[1]+type1[p][1])):
                    break
            fade_out, movement = board.move_piece(locationN[0], locationN[1], locationN[0]+type1[p][0], locationN[1]+type1[p][1])
            locationN =(locationN[0]+type1[p][0],locationN[1]+type1[p][1])
            self.play(movement)
            #self.wait(0.5)

            while True:
                p=random.randint(0,7)
                if 0<=locationK[0]+type2[p][0]<=7 and 0<=locationK[1]+type2[p][1]<=7 and Random_Walk.check_knight_move(locationN,(locationK[0]+type2[p][0], locationK[1]+type2[p][1])):
                    break
            fade_out, movement = board.move_piece(locationK[0], locationK[1], locationK[0]+type2[p][0], locationK[1]+type2[p][1])
            locationK =(locationK[0]+type2[p][0],locationK[1]+type2[p][1])
            self.play(movement)
            #self.wait(0.5)

    @staticmethod
    def check_king_move(knight_location, king_target):
        type1= [(-b, a),(b, a),(a, b), (a, -b), (b, -a), (-b, -a), (-a, -b),  (-a, b),]
        for type in type1:
            if (type[0]+king_target[0],type[1]+king_target[1])==knight_location:
                return False
        return True
    
    @staticmethod
    def check_knight_move(king_location, knight_target):
        type2=[(1, 0),(1, -1), (0, -1),(-1, -1), (-1, 0),(-1, 1), (0, 1),(1, 1)]
        for type in type2:
            if (type[0]+knight_target[0],type[1]+knight_target[1])==king_location:
                return False         
        return True
        

class Super_Random(Scene):
    def construct(self): 
        board= ChessBoard("8/3S4/8/8/8/8/8/8 w KQkq - 0 1")
        type1= [(-b, a),(b, a),(a, b), (a, -b), (b, -a), (-b, -a), (-a, -b),  (-a, b),]
        type2=[(1, 0),(1, -1), (0, -1),(-1, -1), (-1, 0),(-1, 1), (0, 1),(1, 1)]

        self.add(board.move_to(ORIGIN))
        self.wait()
        locationN=(1,3)
    
 


        for t in range(15):
            while True:
                p=random.randint(0,7)
                if 0<=locationN[0]+type1[p][0]<=7 and 0<=locationN[1]+type1[p][1]<=7:
                    break
            fade_out, movement = board.move_piece(locationN[0], locationN[1], locationN[0]+type1[p][0], locationN[1]+type1[p][1])
            locationN =(locationN[0]+type1[p][0],locationN[1]+type1[p][1])
            self.play(movement, run_time=0.5)
            self.wait(0.2)

class Formula(Scene):
    def construct(self): 
        tex=MathTex(r"velocity(N_{a,b})=\frac{2(a+b)b^2}{a^2+3b^2}")
        tex.scale(1.5)
        self.play(Write(tex))
        self.wait()

   





        

        



  
       
                            


        