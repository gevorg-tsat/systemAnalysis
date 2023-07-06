screen start:
    modal True
    imagemap:
        ground "#FFFFFF"
        idle "kadr start.png"
        hover "kadr start_.png"
        hotspot(783,312,327,288) action Call("startb1")
        hotspot(1164,312,327,288) action Call("startb1")
        hotspot(1546,312,327,288) action Call("startb1")
        hotspot(783,572,327,288) action Call("startb1")
        hotspot(1164,572,327,288) action Call("startb1")
        hotspot(1546,572,327,288) action Call("startb1")
        hotspot(783,824,327,288) action Call("startb1")
        text "{size=+10}{cps=10}Итак, ты — в Игре!\nЭтот путь будет только твоим. Качай задания, смотри подсказки, следи за волшебными кнопкам, стань лучшим!\nУдачи!{/cps}{/size}" xpos 50 ypos 50 xsize 830 ysize 400 color "#000000"

label startgame:
    hide screen main_menu
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
    $ for i in range(3,10): renpy.show_screen(f"b1kadr{i}")
    #$ for i in range(1,5): renpy.show_screen(f"b1kadr4v{i}")
    $ for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
    $ kadrb1()
    scene black with fade
    return

label startb2:
    $ vkadr = "b2"
    $ nkadr = 1
    hide screen b1endt
    hide screen b1endm
    hide screen b1endb
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