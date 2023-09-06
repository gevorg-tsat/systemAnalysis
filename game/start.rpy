label task:
    $ global screens
    $ screens = ["task", "butforwardback"]
    scene white
    hide screen main_menu
    $ b1_done = b2_done = b3_done = b4_done = b5_done = False
    show screen task(task_text1)
    $ vkadr = "start"
    show screen butforwardback
    pause

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
        text "{size=+10}{cps=10}Итак, ты — в Игре!\nЭтот путь будет только твоим. Качай задания, смотри подсказки, следи за волшебными кнопкам, стань лучшим!\nУдачи!{/cps}{/size}" xpos 50 ypos 50 xsize 830 ysize 400 color "#000000"



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

label startb8:
    hide screen start
    scene white with dissolve
    $ vkadr = "b8"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb8()
    scene black with fade
    return

label startb9:
    hide screen start
    scene white with dissolve
    $ vkadr = "b9"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb9()
    scene black with fade
    return

label startb10:
    hide screen start
    scene white with dissolve
    $ vkadr = "b10"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb10()
    scene black with fade
    return

label startb11:
    hide screen start
    scene white with dissolve
    $ vkadr = "b11"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb11()
    scene black with fade
    return

label startb12:
    hide screen start
    scene white with dissolve
    $ vkadr = "b12"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb12()
    scene black with fade
    return

label startb13:
    hide screen start
    scene white with dissolve
    $ vkadr = "b13"
    $ nkadr = 1
    $ renpy.show_screen("butforwardback")
    #$ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    #$ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb13()
    scene black with fade
    return



screen stkadr1text:
    text "{size=+10}{cps=10}Итак, ты — в Игре!\nЭтот путь будет только твоим. Качай задания, смотри подсказки, следи за волшебными кнопкам, стань лучшим!\nУдачи!{/cps}{/size}" xpos 930 ypos 580 xsize 830 ysize 400 color "#ffffff"
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
    "Итак, ты — в Игре! Этот путь будет только твоим.\nВыполняй задания в каждом блоке, смотри подсказки, следи за волшебными кнопками, стань лучшим! Удачи!"
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