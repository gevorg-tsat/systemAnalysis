# Вы можете расположить сценарий своей игры в этом файле.


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

define nkadr = 0
define vkadr = ""
define backkadr = ""
define b1kadr4a1 = ""
define b1kadr4a2 = ""
define b1kadr4a3 = ""
define b1kadr4a4 = ""
default b1kadr4rez = -1
default b1kadr6rez = 0
default b1kadr8rez = 0
define b1kadr8a1 = ""
define b1kadr8a2 = ""
define b1kadr8a3 = ""
define b1kadr8back = False
image white = "#ffffff"
define b1aqcor = 0
define b1zcor = 0
define b1xcor = 0
define b1gcor = 0
define b1tabcor = 0
define b1aqn = 0
define b1zn = 0
define b1xn = 0
define b1gn = 0
define b1tabn = 0
define b1amcor = 0
define b1mtcor = 0
define b1naccor = 0
define b1amn = 0
define allow_forward = True
define b1nc = False

define b1tab = False

define task_text1 = "Пример задачи.\n Процесс подготовки требований неразрывно связан с проектированием. Например, погружаясь в требования и разбирая их, специалист проектирует сценарии использования системы, то есть то, как она должна вести себя и отвечать на действия пользователя, разрабатывает пользовательские интерфейсы (как правило, в связке с дизайнером) и пр. Он является носителем знаний о предметной области. Это позволяет ему проектировать какую-либо концептуальную модель данных. Затем системный аналитик передает информацию разработчикам, чтобы они могли написать правильный код, корректно спроектировать базу данных и пр. Конечно, системный аналитик не полностью заменяет стейкхолдера, однако является одним из специалистов, наиболее погруженных в проект. Но тем не менее системный аналитик — связующее звено между клиентом, пользователями и командой разработки, способный либо самостоятельно ответить на возникающие вопросы с обеих сторон, либо передать их ответственным лицам."
define symptom1 = "Что-то допольнительное про задание"
define relevance_task1 = "Разузнай актуально ли это вообще??"
define winner_text = "Поздравляю. Верно. Можешь двигаться дальше"
define loser_text = "Неверно. Можешь попытаться еще раз"
define loser_no_tries_text = "Неверно. Попытки закончилось, повезет в следующий раз"

init python:
    def play1():
        Rollback()
    
define but = Character("", color="#ffcc77", window_left_padding=100, image="gui/frame1.png", left_margin = 0)
image kadr1 = "images/splashscreen 1.png"
define n = Character(None, kind=nvl, what_bold=True, what_color="#0000ff")
#centered "{cps=5}Test Typewrite Effect"

screen butforwardback:
    zorder 99
    modal True
    if True:
        frame:
            #background "gui/frame1.png"
            xalign 0.5 yalign 1.0
            xsize 400 ysize 100
            if vkadr == "rez" or vkadr == "ha" or allow_forward:
                imagebutton:
                    xalign 0.7 yalign 0.8
                    idle "butforward.png"
                    hover "butforward_.png"
                    action Call("KadrForward")
            # if vkadr == "ha" or (vkadr != "rez"):
            imagebutton:
                xalign 0.3 yalign 0.8
                idle "butback.png"
                hover "butback_.png"
                action Call("KadrBack")
label KadrForward:
    if vkadr == "rg":
        $ nkadr += 1
        $ kadrrg()
    elif vkadr == "ac":
        $ nkadr += 1
        $ kadrac()
    elif vkadr == "b1":
        # if b1kadr8back:
        #     $ nkadr = 7
        #     $ b1kadr8back = False
        # #if nkadr == 8:
        # #    if (b1kadr6rez == 0) and (6 - (b1amcor + b1mtcor + b1naccor) == 0):
        # #        $ store.b1scores0 = True
        # #    else:
        # #        $ store.b1scores0 = False
        # if nkadr == 4 and (b1bt or b1kadr4rez == 0):
        #     $ nkadr = 9
        # else:
        $ nkadr += 1
        $ kadrb1()
    elif vkadr == "b2":
        $ nkadr += 1
        $ kadrb2()
    elif vkadr == "b3":
        $ nkadr += 1
        $ kadrb3()
    elif vkadr == "b4":
        $ nkadr += 1
        $ kadrb4()
    elif vkadr == "b5":
        $ nkadr += 1
        $ kadrb5()
    elif vkadr == "b6":
        $ nkadr += 1
        $ kadrb6()
    elif vkadr == "b7":
        $ nkadr += 1
        $ kadrb7()
    elif vkadr == "b7":
        $ nkadr += 1
        $ kadrb7()
    elif vkadr == "b8":
        $ nkadr += 1
        $ kadrb8()
    elif vkadr == "b9":
        $ nkadr += 1
        $ kadrb9()
    elif vkadr == "b10":
        $ nkadr += 1
        $ kadrb10()
    elif vkadr == "b11":
        $ nkadr += 1
        $ kadr11()
    elif vkadr == "b12":
        $ nkadr += 1
        $ kadrb12()
    elif vkadr == "b13":
        $ nkadr += 1
        $ kadrb13()
    elif vkadr == "start":
        hide screen butforwardback
        call startgame
    elif vkadr == "ha":
        hide kadr ha3 at top with dissolve
        $ vkadr = ""
        if backkadr == "":
            show black
            return
        elif backkadr == "b1":
            $ backkadr = ""
            $ b1nc = False
            $ vkadr = "b1"
            #$ kadrb1()
            $ renpy.show(f"kadr b1{nkadr}")
            $ renpy.hide_screen(f"b1kadr{nkadr}")
            $ renpy.show_screen(f"b1kadr{nkadr}")
            $ renpy.with_statement(fade)
            if nkadr == 8:
                $ for i in range(3): renpy.hide_screen(f"b1kadr8v{i+1}")
                $ for i in range(3): renpy.show_screen(f"b1kadr8v{i+1}")
            pause
    elif vkadr == "rez":
        $ vkadr = ""
        if backkadr == "":
            hide screen butforwardback
            hide screen rez with fade
            #hide kadr rez at top with dissolve
            #show black with fade
            return
        elif backkadr == "b1":
            $ backkadr = ""
            #$ b1nc = False
            $ vkadr = "b1"
            #$ kadrb1()
            if nkadr == 0:
                $ renpy.hide_screen("butforwardback")
            hide screen rez with fade
            #hide kadr rez at top with dissolve
            #$ renpy.show(f"kadr b1{nkadr}")
            #$ renpy.hide_screen(f"b1kadr{nkadr}")
            #$ renpy.show_screen(f"b1kadr{nkadr}")
            #$ renpy.with_statement(fade)
            pause
    return
label KadrBack:
    if vkadr == "rg":
        $ nkadr -= 1
        $ kadrrg()
    elif vkadr == "ac":
        $ nkadr -= 1
        $ kadrac()
    elif vkadr == "b1":
        if nkadr == 9 and (b1bt or b1amcor == 0):
            $ nkadr = 4
        else:
            $ nkadr -= 1
        $ kadrb1()
    elif vkadr == "ha":
        hide screen butforwardback
        call hakadr2 from _call_hakadr2
    return


# Игра начинается здесь:





label splashscreen:
    #call startgame3 from _call_startgame3
    scene white
    show splashscreen at top with fade
    show screen splashscreen_frame
    pause(3)
    hide screen splashscreen_frame
    #jump start


screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu
    
    imagemap:
        ground "gui/main_menu.jpeg"
        idle "gui/main_menu_button.png"
        hover "gui/main_menu_button_.png"
        hotspot(1457,59,430,75) action Call("AboutCompany")
        hotspot(1457,169,430,75) action Call("RulesGame")#[Hide("main_menu"),SetVariable("nkadr",0),Function(kadr)]#Call("RulesGame")
        hotspot(1457,289,430,75) action Call("ha")
        hotspot(1457,404,430,75) action Call("rez")
        hotspot(1457,524,430,75) action Call("sg")
        hotspot(1457,639,430,75) action Quit(confirm=True)
        hotspot(1495,850,355,205) action Call("task")

    text "{size=+5}Текст {b}Текст ТекстТекст{/b} Текст Текст Текст{/size}" xpos 40 ypos 950 xsize 800 ysize 50 color "#000000"
    
label start:
    return