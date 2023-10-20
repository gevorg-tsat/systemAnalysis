label task:
    $ global screens
    $ screens = ["task", "butforwardback"]
    scene white
    hide screen main_menu
    $ b1_done = b2_done = b3_done = b4_done = b5_done = False
    show screen task("")
    $ your_name = ""
    $ your_name = renpy.input("Введите свое ФИО:")
    $ vkadr = "start"
    show screen butforwardback
    pause

init -2 python:
    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)

screen start:
    modal True
    imagemap:
        ground "kadr start_blocked.png"
        idle "kadr start_nopick.png"
        hover "kadr start_picked.png"
        if not b1_done:
            hotspot(1016,364,253,150) action Call("startb2")
        if not b2_done:
            hotspot(1325,364,253,150) action Call("startb7")
        if not b3_done:
            hotspot(1636,364,253,150) action Call("startb3")
        if not b4_done:
            hotspot(1016,575,253,150) action Call("startb4")
        if not b5_done:
            hotspot(1325,575,253,150) action Call("startb5")
        text "{size=+10}{cps=10}Необходимо последовательно решить по 1 задаче на 6 методов принятия решений: формирование множества Парето и формирование обобщающего критерия (скаляризация аддитивным методом неоднородных критериев) (блок 1), метод парных сравнений (блок 2), метод парных сравнений группы экспертов (блок 3), ранжирование (блок 4), обработка числовых значений экспертов (блок 5).\nОкругление осуществляйте до 2-х знаков после запятой. В расчетах используйте значения, которые есть на экране, т.е. округленные.\nУдачи!{/cps}{/size}" xpos 50 ypos 50 xsize 830 ysize 400 color "#000000"



label startgame:
    hide screen task
    #jump b1kadr9scores0bt
    scene white
    #show kadr start at center with fade
    show screen start
    #"Итак, ты — в Игре! Этот путь будет только твоим.\nВыполняй задания в каждом блоке, смотри подсказки, следи за волшебными кнопками, стань лучшим! Удачи!"
    pause
    return

label startb1:
    hide screen start
    scene white with dissolve
    $ vkadr = "b1"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb1()
    scene black with fade
    return

label startb2:
    hide screen start
    scene white with dissolve
    $ vkadr = "b2"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb2()
    scene black with fade
    return

label startb3:
    hide screen start
    scene white with dissolve
    $ vkadr = "b3"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb3()
    scene black with fade
    return

label startb4:
    hide screen start
    scene white with dissolve
    $ vkadr = "b4"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb4()
    scene black with fade
    return

label startb5:
    hide screen start
    scene white with dissolve
    $ vkadr = "b5"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb5()
    scene black with fade
    return

label startb6:
    hide screen start
    scene white with dissolve
    $ vkadr = "b6"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb6()
    scene black with fade
    return

label startb7:
    hide screen start
    scene white with dissolve
    $ vkadr = "b7"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb7()
    scene black with fade
    return



screen stkadr1text:
    text "{size=+10}{cps=10}Необходимо последовательно решить по 1 задаче на 6 методов принятия решений: формирование множества Парето и формирование обобщающего критерия (скаляризация аддитивным методом неоднородных критериев) (блок 1), метод парных сравнений (блок 2), метод парных сравнений группы экспертов (блок 3), ранжирование (блок 4), обработка числовых значений экспертов (блок 5).\nОкругление осуществляйте до 2-х знаков после запятой. В расчетах используйте значения, которые есть на экране, т.е. округленные.\nУдачи!{/cps}{/size}" xpos 930 ypos 580 xsize 830 ysize 400 color "#ffffff"
screen stkadr1but:
    #tag stbuttg
    modal True
    imagebutton:
        xalign 0.8 yalign 0.95
        idle "stkadr1but.png"
        hover "stkadr1but_.png"
        action Call("startgame2")
screen stkadr2but:
    #tag stbuttg
    modal True
    imagebutton:
        xalign 0.494 yalign 0.18
        idle "stkadr2but.png"
        hover "stkadr2but_.png"
        action Jump("startgame3")#[Hide("stkadr2but"), Hide("stkadr2")]#Call("startgame3"), MainMenu(), Hide("window")
label startgame0:
    hide screen main_menu
    scene black
    return
    show stkadr1 at center with fade
    pause(1)
    show screen stkadr1text
    pause(2)
    show screen stkadr1but
    pause
    return

label startgame2:
    hide screen stkadr1but with dissolve
    hide screen stkadr1text with dissolve
    scene white
    show stkadr2 at top with fade
    show screen stkadr2but
    "Необходимо последовательно решить по 1 задаче на 6 методов принятия решений: формирование множества Парето и формирование обобщающего критерия (скаляризация аддитивным методом неоднородных критериев) (блок 1), метод парных сравнений (блок 2), метод парных сравнений группы экспертов (блок 3), ранжирование (блок 4), обработка числовых значений экспертов (блок 5).\nОкругление осуществляйте до 2-х знаков после запятой. В расчетах используйте значения, которые есть на экране, т.е. округленные."
    pause
    return

label startgame3:
    hide screen main_menu
    hide screen stkadr2but
    scene white
    $ vkadr = "b1"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    $ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    $ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb1()
    scene black with fade
    return