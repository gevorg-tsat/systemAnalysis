transform mmove(x0, x1):
    xpos x0[0] ypos x0[1]
    #xpos 1500 ypos 175 zoom 0.03
    linear 1 xpos x1[0] ypos x1[1]
    
init python:
    import random
    b1a = renpy.random.randint(150000,180000)
    b1d = renpy.random.randint(4000,8000)
    b1b = renpy.random.randint(5000,8000)
    b1aq0 = "0"
    b1z0 = "0"
    b1x0 = "0"
    b1g0 = "0"
    b1am0 = "0"
    b1mt0 = "0"
    b1nac0 = "0"
    b1i = 0
    b1nsh = [0, 1, 2, 3]
    b1quest = ""
    b1aq = round((b1a + b1d + b1b) / 1.2)
    b1z = round(b1aq / 48)
    b1x = b1z * 2
    b1g = b1aq - b1x
    b1am = b1z + 36
    b1mt = 287088 + b1g - 36
    b1nac = round(4410 + b1aq * 0.2)
    b1tabvq = [["Расчетный счет", "Амортизация основных средств", "Основное производство", "Расчеты с персоналом по оплате труда", "Товары", "Основные средства"],
            ["Расчеты с покупателями и заказчиками", "Материалы", "Общехозяйственные расходы", "Прибыли и убытки", "Добавочный капитал", "Выручка"],
            [str(b1z), str(b1x), str(b1z * 3), str((b1aq + 100000)//48), str(b1aq//4), str(b1z * 4)]]
    debet0 = ""
    kredit0 = ""
    summa0 = ""    
    debet = None
    kredit = None
    summa = None
    b1quebt = ["Остаточная стоимость амортизируемых активов - это:", "Амортизация основных средств начисляется в течение:", "Первоначальная стоимость объектов основных средств, внесенных в счет вклада в уставный капитал, определяется по:", "Что НЕ относится к факторам, влияющим на определение срока полезного использования основных средств:"]
    b1ansbt = [["их рыночная стоимость", "сумма, на которую активы должны быть застрахованы", "их «недоамортизированная» стоимость", "разница между их первоначальной стоимостью и расходами на амортизацию за последний отчетный период"], ["всего срока их нахождения в организации", "всего срока их полезной службы", "установленного руководством организации срока полезной службы, но не более 20 лет", "от 2 до 12 лет полезной службы в зависимости от принадлежности объекта к амортизационной группе"] ,["чистой рыночной стоимости", "согласованной стоимости", "справедливой стоимости", "остаточной стоимости"], ["ожидаемый физический износ, зависящий от режима эксплуатации, климатических условий", "нормативно-правовые ограничения", "ожидаемый срок производительного использования", "величина первоначальной стоимости – чем дороже, тем дольше эксплуатируется"]]
    b1bt = False
    mXY0 = (1300,290)
    #lim = [Image(f"m{i+1}.png", pos=mXY0) for i in range(2)]
    b1immy = 0
    b1imyet = 0

    def kadrb1():
        global nkadr
        global vkadr
        if nkadr == 8 or nkadr == 10 or (nkadr == 4 and (b1bt or b1amcor == 0)):
            renpy.hide("b1kadr9")
        if nkadr == 10:
            renpy.hide("kadr b19")
            renpy.hide_screen("butforwardback")
            for i in range(3,10): renpy.hide_screen(f"b1kadr{i}")
            for i in range(1,5): renpy.hide_screen(f"b1kadr4v{i}")
            for i in range(1,4): renpy.hide_screen(f"b1kadr8v{i}")
            #scene black with fade
            #renpy.show(black)
            #renpy.with_statement(fade)
            vkadr = ""
            nkadr = 0
            renpy.jump("b1end")
            return
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        renpy.call(f"b1kadr{nkadr}")
        #renpy.with_statement(fade)
        if nkadr == 6:
            #renpy.hide_screen("butforwardback")
            #renpy.show_screen("butforwardback")
            renpy.hide_screen("b1kadr6")
            renpy.show_screen("b1kadr6")
        if nkadr == 8:
            renpy.hide_screen("b1kadr8")
            renpy.show_screen("b1kadr8")
            for i in range(1,4): renpy.hide_screen(f"b1kadr8v{i}")
            for i in range(1,4): renpy.show_screen(f"b1kadr8v{i}")
        if nkadr == 9:
            renpy.hide_screen("b1kadr9")
            renpy.show_screen("b1kadr9")
            if not b1bt and b1amcor == 0:# and b1scores0
                renpy.show("b1kadr9")
        #renpy.show("window")
        renpy.pause()
        #nkadr += 1
        #kadrb1()
    def monetmove():
        global b1immy
        global b1imyet
        for i in range(b1kadr8rez):
            renpy.show(f"m{i+1}", at_list=[mmove(mXY0, [900-48*i, 740])])
            renpy.pause(1)
            b1immy += 1
        for i in range(b1kadr8rez, 18):
            renpy.show(f"m{i+1}", at_list=[mmove(mXY0, [1780-48*(i-b1kadr8rez), 740])])
            renpy.pause(1)
            b1imyet += 1
    
    def clearlup():
        renpy.hide("b1kadrnclup")
        
    def drag_placed(drags, drop):
        #global debet
        #global kredit
        #global summa
        #global b1tab
        #global nnn
        #nnn = store.nnn
        #store.nextstep1 = False
        store.draggable = drags[0].drag_name
        if not drop:
            if draggable == debet:
                store.debet = None
                store.debetXY = None
            if draggable == kredit:
                store.kredit = None
                store.kreditXY = None
            if draggable == summa:
                store.summa = None
                store.summaXY = None
        else:
            store.droppable = drop.drag_name
            if ((draggable in b1tabvq[2]) and (droppable != 'summa')) or ((draggable not in b1tabvq[2]) and (droppable == 'summa')) or ((debet is not None) and (droppable == "debet")) or ((kredit is not None) and (droppable == "kredit")) or ((summa is not None) and (draggable in b1tabvq[2])) or ((droppable == "debet") and (debet is not None) and (kredit is not None) and (kredit == draggable)) or ((droppable == "kredit") and (kredit is not None) and (debet is not None) and (debet == draggable)):
                if (droppable == "debet") and (debet is not None) and (kredit is not None) and (kredit == draggable):
                    drags[0].snap(kreditXY[0], kreditXY[1], 0.25)
                elif (droppable == "kredit") and (kredit is not None) and (debet is not None) and (debet == draggable):
                    drags[0].snap(debetXY[0], debetXY[1], 0.25)
                elif (draggable in b1tabvq[2]) and (summa is not None) and (summa == draggable):
                    drags[0].snap(summaXY[0], summaXY[1], 0.25)
                elif (droppable == "debet") and (debet == draggable):
                    drags[0].snap(debetXY[0], debetXY[1], 0.25)
                elif (droppable == "kredit") and (kredit == draggable):
                    drags[0].snap(kreditXY[0], kreditXY[1], 0.25)
                else:
                    drags[0].snap(int(drags[0].start_x-drags[0].w//2), int(drags[0].start_y-drags[0].h//2), 0.25)
            else:
                drags[0].snap(drop.x + 5, drop.y + 17, 0.25)
                if (droppable == "debet") and (draggable == kredit):
                    store.kredit = None
                if (droppable == "kredit") and (draggable == debet):
                    store.debet = None
                if droppable == "debet":
                    store.debet = draggable
                    store.debetXY = [drop.x + 5, drop.y + 17]
                elif droppable == "kredit":
                    store.kredit = draggable
                    store.kreditXY = [drop.x + 5, drop.y + 17]
                elif droppable == "summa":
                    store.summa = draggable
                    store.summaXY = [drop.x + 5, drop.y + 17]
        if (debet is not None) and (kredit is not None) and (summa is not None):
            store.b1tab = True
        else:
            store.b1tab = False
        renpy.restart_interaction()
        return
        #return True

image b1kadrnclup = Movie(play="b1kadrnc.ogv", pos=(50,1000),side_mask=False) #, anchor=(50,1000) 
image b1kadr9 = Movie(play="b1kadr9.ogv", pos=(730,740), side_mask=False)
image b1endes = Movie(play="b1endes.ogv", pos=(1600,650),side_mask=False)
image b1endp = Image("b1endp.png", pos=(1300,700))#, zoom=0.133)
image b1ende = Image("b1ende.png", pos=(1700,800))#, zoom=0.114)
image b1endl = Image("b1endl.png", pos=(200, 500))
image m1 = Image("m1.png", pos=mXY0)
image m2 = Image("m1.png", pos=mXY0)
image m3 = Image("m1.png", pos=mXY0)
image m4 = Image("m1.png", pos=mXY0)
image m5 = Image("m1.png", pos=mXY0)
image m6 = Image("m1.png", pos=mXY0)
image m7 = Image("m1.png", pos=mXY0)
image m8 = Image("m1.png", pos=mXY0)
image m9 = Image("m1.png", pos=mXY0)
image m10 = Image("m1.png", pos=mXY0)
image m11 = Image("m1.png", pos=mXY0)
image m12 = Image("m1.png", pos=mXY0)
image m13 = Image("m1.png", pos=mXY0)
image m14 = Image("m1.png", pos=mXY0)
image m15 = Image("m1.png", pos=mXY0)
image m16 = Image("m1.png", pos=mXY0)
image m17 = Image("m1.png", pos=mXY0)
image m18 = Image("m1.png", pos=mXY0)
screen b1kadr3:
    $ s = '''
В составе основных средств Центра учитываются игровые жилеты для передвижных и стационарных площадок.

Срок полезного использования жилетов варьируется от 3-х до 5-ти лет в зависимости от модели.

{color=#ff00ff}Без знаний по начислению амортизации не обойтись!{/color} 
    '''
    if vkadr == "b1" and nkadr == 3:
        frame:
            background "gui/frame1.png"
            text "{size=+0}[s]{/size}" xpos 20 ypos 450 xsize 600 ysize 400 color "#000000" line_spacing 4

label b1kadr1:
    # $ global task_text1
    show screen task(task_text1)
    show screen butforwardback
    pause

screen b1kadr4:
    zorder 100
    $ s = f'''
- \u007bb\u007d23 октября 2022 года\u007b/b\u007d Центр приобрел три жилета для мобильной игровой площадки на общую сумму {b1a} рублей (в т.ч. НДС 20%).
- Данное оборудование было введено в эксплуатацию \u007bb\u007d29 октября 2022 года\u007b/b\u007d.
- Расходы на доставку и установку соответственно составили: {b1d} рублей и {b1b} рублей (в т.ч. НДС 20%).
- Ожидаемый срок полезной службы \u007bb\u007d4 года\u007b/b\u007d. 
- Центр использует \u007bb\u007dлинейный метод\u007b/b\u007d начисления амортизации.
- Бухгалтер начисляет амортизацию ежемесячно.

    \u007bb\u007dЗадание:\u007b/b\u007d
    Рассчитайте следующие величины для приобретенных жилетов \u007bb\u007d(округлите ответы до целых рублей)\u007b/b\u007d:
    '''
    if vkadr == "b1" and nkadr == 4: 
        text "{size=+10}{b}Задание 1.1{/b}{/size}" xpos 80 ypos 34 xsize 1000 ysize 10 color "#ffffff"
        if not b1nc:
            frame:
                background "gui/frame1.png"
                text "{size=+3}[s]{/size}" xpos 80 ypos 100 xsize 1600 ysize 800 color "#000000" line_spacing 4
                text "{size=+3}- первоначальную стоимость на 29.10.2022:{/size}" xpos 80 ypos 675 xsize 1720 ysize 800 color "#000000" #момент ввода в эксплуатацию
                text "{size=+3}- расходы на амортизацию за декабрь 2022 года:{/size}" xpos 80 ypos 750 xsize 1720 ysize 800 color "#000000"
                text "{size=+3}- начисленную амортизацию на 31.12.2022:{/size}" xpos 80 ypos 825 xsize 1720 ysize 800 color "#000000"
                text "{size=+3}- остаточную стоимость на 31.12.2022:{/size}" xpos 80 ypos 900 xsize 1720 ysize 800 color "#000000"
                add "intern.jpg" xpos 1680 ypos 120
                if b1aqcor == 1:
                    add "b1cor.png" xpos 1210 ypos 674
                elif b1aq0 == b1kadr4a1:
                    add "b1ncor.png" xpos 1210 ypos 674
                if b1zcor == 1:
                    add "b1cor.png" xpos 1210 ypos 749
                elif b1z0 == b1kadr4a2:
                    add "b1ncor.png" xpos 1210 ypos 749
                if b1xcor == 1:
                    add "b1cor.png" xpos 1210 ypos 824
                elif b1x0 == b1kadr4a3:
                    add "b1ncor.png" xpos 1210 ypos 824    
                if b1gcor == 1:
                    add "b1cor.png" xpos 1210 ypos 899
                elif b1g0 == b1kadr4a4:
                    add "b1ncor.png" xpos 1210 ypos 899
                if b1kadr4a1 != "" and b1aqcor != 1 and b1aqn != 2 and b1kadr4a1 != b1aq0:
                    imagebutton:
                        xpos 1270 ypos 668
                        idle "b1butch.png"
                        hover "b1butch_.png"
                        action Call("b1kadr4nc")
                if b1kadr4a2 != "" and b1zcor != 1 and b1zn != 2 and b1kadr4a2 != b1z0:
                    imagebutton:
                        xpos 1270 ypos 743
                        idle "b1butch.png"
                        hover "b1butch_.png"
                        action Call("b1kadr4nc")
                if b1kadr4a3 != "" and b1xcor != 1 and b1xn != 2 and b1kadr4a3 != b1x0:
                    imagebutton:
                        xpos 1270 ypos 818
                        idle "b1butch.png"
                        hover "b1butch_.png"
                        action Call("b1kadr4nc")
                if b1kadr4a4 != "" and b1gcor != 1 and b1gn != 2 and b1kadr4a4 != b1g0:
                    imagebutton:
                        xpos 1270 ypos 893
                        idle "b1butch.png"
                        hover "b1butch_.png"
                        action Call("b1kadr4nc")
            frame:
                background "kadr b14v.png"
                xpos 1000 ypos 675
                xsize 200 ysize 50
                if b1aqcor != 1 and b1aqn != 2:
                    input default "":
                        xpos 20 ypos 6
                        xsize 200 ysize 50
                        color "#ffffff"
                        value VariableInputValue("b1kadr4a1")
                        length 8
                        allow "0123456789"
                else:
                    text "[b1kadr4a1]" xpos 20 ypos 6 color "#ffffff"
            frame:
                background "kadr b14v.png"
                xpos 1000 ypos 750
                xsize 200 ysize 50
                if  b1zcor != 1 and b1zn != 2:
                    input default "":
                        xpos 20 ypos 6
                        #xalign 0.5 yalign 0.3
                        xsize 200 ysize 50
                        color "#ffffff"
                        value VariableInputValue("b1kadr4a2")
                        length 8
                        allow "0123456789"
                else:
                    text "[b1kadr4a2]" xpos 20 ypos 6 color "#ffffff"
            frame:
                background "kadr b14v.png"
                xpos 1000 ypos 825
                xsize 200 ysize 50
                if  b1xcor != 1 and b1xn != 2 and b1kadr4rez == -1:
                    input default "":
                        xpos 20 ypos 6
                        xsize 200 ysize 50
                        color "#ffffff"
                        value VariableInputValue("b1kadr4a3")
                        length 8
                        allow "0123456789"
                else:
                    text "[b1kadr4a3]" xpos 20 ypos 6 color "#ffffff"   
            frame:
                background "kadr b14v.png"
                xpos 1000 ypos 900
                xsize 200 ysize 50
                if  b1gcor != 1 and b1gn != 2 and b1kadr4rez == -1:
                    input default "":
                        xpos 20 ypos 6
                        xsize 200 ysize 50
                        color "#ffffff"
                        value VariableInputValue("b1kadr4a4")
                        length 8
                        allow "0123456789"
                else:
                    text "[b1kadr4a4]" xpos 20 ypos 6 color "#ffffff"
label b1kadr4nc:
    if b1kadr4a1 == "": 
        return
    if b1kadr4a2 == "":
        if b1aq == int(b1kadr4a1):
            $ b1aqcor = 1
        else:
            $ b1aq0 = b1kadr4a1
            $ b1aqcor = 2
            $ b1aqn += 1
            if b1aqn < 2:
                $ b1nc = True
                hide screen butforwardback
                show b1kadrnclup at left with fade:
                    xpos 50 ypos 850
                pause(2)
                show screen b1kadr4nc
    elif b1kadr4a3 == "":
        if b1z == int(b1kadr4a2):
            $ b1zcor = 1
        else:
            $ b1z0 = b1kadr4a2
            $ b1zcor = 2
            $ b1zn += 1
            if b1zn < 2:
                $ b1nc = True
                hide screen butforwardback
                show b1kadrnclup at left with fade:
                    xpos 50 ypos 850
                pause(2)
                show screen b1kadr4nc
            elif b1aqcor == 2:
                $ store.b1kadr6rez = 0
                $ store.b1kadr4rez = 0
                $ nkadr = 9
                $ kadrb1()
                #"К сожалению, Вы неверно ответили на 2 вопроса, поэтому продолжать выполнять задание 1.1, а также 1.2 и 1.3 нет смысла. Но есть еще одна возможность показать себя.\nПредлагаю не огорчаться окончательно и ответить на вопросы блиц-теста. Можно заработать две золотые монеты. Это лучше, чем уходить отсюда с «пустым кошельком»." 
    elif b1kadr4a4 == "":
        if b1x == int(b1kadr4a3):
            $ b1xcor = 1
        else:
            $ b1x0 = b1kadr4a3
            $ b1xcor = 2
            $ b1xn += 1
            if b1xn < 2:
                $ b1nc = True
                hide screen butforwardback
                show b1kadrnclup at left with fade:
                    xpos 50 ypos 850
                pause(2)
                show screen b1kadr4nc
    else:
        if b1g == int(b1kadr4a4):
            $ b1gcor = 1
        else:
            $ b1g0 = b1kadr4a4
            $ b1gcor = 2
            $ b1gn += 1
            if b1gn < 2:
                $ b1nc = True
                hide screen butforwardback
                show b1kadrnclup at left with fade:
                    xpos 50 ypos 850
                pause(2)
                show screen b1kadr4nc                
    pause
    return
label b1kadr4ncback:
    $ b1nc = False
    $ clearlup()
    hide screen b1kadr4nc
    show screen butforwardback
    hide screen b1kadr4
    show screen b1kadr4 with fade
    pause
    return

screen b1kadr4nc:
    modal True
    text "{size=+5}Введенный ответ неверный!\nПредлагаю не вешать нос и попробовать снова.{/size}" xpos 800 ypos 150 xsize 1000 ysize 800 color "#000000"
    imagebutton:
        xpos 1000 ypos 250
        idle "b1ncbut1.png"
        hover "b1ncbut1_.png"
        action Call("b1kadr4ncback")  
    text "{size=+5}Если немного забыл материал, то можно обратиться за помощью к опытному бухгалтеру.{/size}" xpos 800 ypos 450 xsize 1000 ysize 800 color "#000000"
    imagebutton:
        xpos 1000 ypos 550
        idle "b1ncbut2.png"
        hover "b1ncbut2_.png"
        action [Function(clearlup), Hide("b1kadr4nc"), SetVariable("backkadr", "b1"), Call("ha")]      

screen b1kadr5:
    if vkadr == "b1" and nkadr == 5:
        $ store.b1kadr4rez = 3 * (8 - (b1aqcor + b1zcor + b1xcor + b1gcor))
        if b1kadr4rez > 0:        
            $ s = f'''
Молодец!
Ты заработал {b1kadr4rez} золотых монет.
 
Переходи к выполнению Задания 1.2.
                    '''
        else:
            $ s = f'''
К сожалению, в задании 1.1 не удалось заработать золотых монет.
 
Переходи к выполнению Задания 1.2.
                    '''
        text "{size=+20}[s]{/size}" xpos 950 ypos 270 xsize 833 ysize 800 color "#000000"

screen b1kadr6:
    zorder 100
    if vkadr == "b1" and nkadr == 6:
        $ s = f'''
Составьте бухгалтерскую проводку по начислению амортизации на приобретенные жилеты (задание 1.1) за декабрь 2022 года, перетащив 3 блока в таблицу ответа.
Блоки для выбора и перетаскивания:
    '''
        text "{size=+10}{b}Задание 1.2{/b}{/size}" xpos 80 ypos 34 xsize 1000 ysize 10 color "#ffffff"
        if not b1nc:
            frame:
                background "gui/frame1.png"    
                text "{size=+3}[s]{/size}" xpos 80 ypos 80 xsize 1600 ysize 800 color "#000000" line_spacing 4
                text "{size=+3}{b}Ответ:{/b}{/size}" xpos 80 ypos 700 xsize 1720 ysize 800 color "#000000" line_spacing 4
                add "intern.jpg" xpos 1680 ypos 120
                if b1tabcor == 1:
                    add "b1cor.png" xpos 1525 ypos 835
                elif (debet == debet0 and kredit == kredit0 and summa == summa0):
                    add "b1ncor.png" xpos 1525 ypos 835
                if b1tab and b1tabcor != 1 and b1tabn != 2 and not (debet == debet0 and kredit == kredit0 and summa == summa0):
                    imagebutton:
                        xpos 1590 ypos 830
                        idle "b1butch.png"
                        hover "b1butch_.png"
                        action Call("b1kadr6nc")
                frame:
                    background Frame([ "gui/confirm_frame.png", "gui/frameyel.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
                    #background im.Scale("gui/frameyel.png", 120, 28)
                    xpos 80 ypos 750
                    xsize 175 ysize 60
                    text "Дата" color "#000000" size 28 xalign 0.5 yalign 0.5
                frame:
                    xpos 80 ypos 806
                    xsize 175 ysize 100
                    frame:
                        background Frame([ "gui/confirm_frame.png", "gui/framegrey.png"], gui.frame_borders, tile=gui.frame_tile)
                        xpos 1 ypos 11 xsize 163 ysize 65
                    text "31.12.2022" color "#000000" size 24 xalign 0.5 yalign 0.5
                frame:
                    background Frame([ "gui/confirm_frame.png", "gui/frameyel.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
                    xpos 251 ypos 750
                    xsize 560 ysize 60
                    text "Дебет" color "#000000" size 28 xalign 0.5 yalign 0.5
                frame:
                    background Frame([ "gui/confirm_frame.png", "gui/frameyel.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
                    xpos 807 ypos 750
                    xsize 560 ysize 60
                    text "Кредит" color "#000000" size 28 xalign 0.5 yalign 0.5
                frame:
                    background Frame([ "gui/confirm_frame.png", "gui/frameyel.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
                    xpos 1363 ypos 750
                    xsize 160 ysize 60
                    text "Сумма" color "#000000" size 28 xalign 0.5 yalign 0.5                 
            draggroup:
                drag:
                    drag_name "debet"
                    xpos 257 ypos 812
                    draggable False
                    xysize(560, 100)
                    frame:
                        xsize 560 ysize 100
                drag:
                    drag_name "kredit"
                    xpos 813 ypos 812
                    draggable False
                    xysize(560, 100)
                    frame:
                        xsize 560 ysize 100
                drag:
                    drag_name "summa"
                    xpos 1369 ypos 812
                    frame:
                        xsize 160 ysize 100
                    draggable False
                    xysize(160, 100)            
                for i in range(6):
                    drag:
                        drag_name b1tabvq[0][i]
                        if debet is not None and debet == b1tabvq[0][i]:
                            xpos debetXY[0] ypos debetXY[1]
                        elif kredit is not None and kredit == b1tabvq[0][i]:
                            xpos kreditXY[0] ypos kreditXY[1]
                        else:
                            xpos 80 ypos 275 + i*70
                        droppable False
                        draggable not (b1tabcor == 1 or b1tabn == 2)
                        dragged drag_placed
                        frame:
                            background Frame([ "gui/confirm_frame.png", "gui/framegrey.png"], gui.frame_borders, tile=gui.frame_tile)
                            xsize 550 ysize 65
                            xpadding 5
                            ypadding 5
                            text b1tabvq[0][i] color "#000000" size 24 xalign 0.5 yalign 0.5
                for i in range(6):
                    drag:
                        drag_name b1tabvq[1][i]
                        if debet is not None and debet == b1tabvq[1][i]:
                            xpos debetXY[0] ypos debetXY[1]
                        elif kredit is not None and kredit == b1tabvq[1][i]:
                            xpos kreditXY[0] ypos kreditXY[1]
                        else:
                            xpos 700 ypos 275 + i*70
                        droppable False
                        draggable not (b1tabcor == 1 or b1tabn == 2)
                        dragged drag_placed
                        frame:
                            background Frame([ "gui/confirm_frame.png", "gui/framegrey.png"], gui.frame_borders, tile=gui.frame_tile)
                            xsize 550 ysize 65
                            xpadding 5
                            ypadding 5
                            text b1tabvq[1][i] color "#000000" size 24 xalign 0.5 yalign 0.5
                for i in range(6):
                    drag:
                        drag_name b1tabvq[2][i]
                        if summa is not None and summa == b1tabvq[2][i]:
                            xpos summaXY[0] ypos summaXY[1]
                        else:
                            xpos 1320 ypos 275 + i*70
                        droppable False
                        draggable not (b1tabcor == 1 or b1tabn == 2)
                        #mouse_drop False
                        #drag_raise False
                        dragged drag_placed
                        frame:
                            background Frame([ "gui/confirm_frame.png", "gui/framegrey.png"], gui.frame_borders, tile=gui.frame_tile)
                            xsize 150 ysize 65
                            xpadding 5
                            ypadding 5
                            text str(b1tabvq[2][i]) color "#000000" size 24 xalign 0.5 yalign 0.5

label b1kadr6nc:
    if debet == b1tabvq[1][2] and kredit == b1tabvq[0][1] and summa == b1tabvq[2][0]:
        $ b1tabcor = 1
    else:
        $ debet0 = debet
        $ kredit0 = kredit
        $ summa0 = summa
        $ b1tabcor = 2
        $ b1tabn += 1
        if b1tabn < 2:
            $ b1nc = True
            hide screen butforwardback
            show b1kadrnclup at left with fade:
                xpos 50 ypos 850
            pause(2)
            show screen b1kadr6nc     
    pause
    return
label b1kadr6ncback:
    $ b1nc = False
    $ clearlup()
    hide screen b1kadr6nc
    show screen butforwardback
    hide screen b1kadr6
    show screen b1kadr6 with fade
    pause
    return

screen b1kadr6nc:
    modal True
    text "{size=+5}Введенный ответ неверный!\nПредлагаю не вешать нос и попробовать снова.{/size}" xpos 800 ypos 150 xsize 1000 ysize 800 color "#000000"
    imagebutton:
        xpos 1000 ypos 250
        idle "b1ncbut1.png"
        hover "b1ncbut1_.png"
        action Call("b1kadr6ncback")#[SetVariable("b1nc", False), Function(clearlup), Hide("b1kadrnc")] #Show("butforwardback"),  
    text "{size=+5}Если немного забыл материал, то можно обратиться за помощью к опытному бухгалтеру.{/size}" xpos 800 ypos 450 xsize 1000 ysize 800 color "#000000"
    imagebutton:
        xpos 1000 ypos 550
        idle "b1ncbut2.png"
        hover "b1ncbut2_.png"
        action [Function(clearlup), Hide("b1kadr6nc"), SetVariable("backkadr", "b1"), Call("ha")]

screen b1kadr7:
    if vkadr == "b1" and nkadr == 7:
        $ store.b1kadr6rez = b1kadr4rez + 3 * (2 - b1tabcor)
        if b1kadr6rez > b1kadr4rez:
            $ s = f'''
Молодец!
Ты заработал 3 золотые монеты и теперь у тебя {b1kadr6rez} золотых монет.
 
Переходи к выполнению Задания 1.3.
                    '''
        elif b1kadr6rez == b1kadr4rez and b1kadr6rez != 0:
            $ s = f'''
К сожалению, задание 1.2 не удалось выполнить и у тебя по прежнему {b1kadr6rez} золотых монет.
 
Переходи к выполнению Задания 1.3.
                    '''
        else:
            $ s = f'''
К сожалению, задание 1.2 не удалось выполнить и у тебя пока нет золотых монет.
 
Переходи к выполнению Задания 1.3.
                    '''
        text "{size=+20}[s]{/size}" xpos 950 ypos 270 xsize 800 ysize 800 color "#000000"

screen b1kadr8:
    zorder 100
    if vkadr == "b1" and nkadr == 8:
        text "{size=+10}{b}Задание 1.3{/b}{/size}" xpos 80 ypos 34 xsize 1000 ysize 10 color "#ffffff"
        $ s = f'''
Внесите соответствующие суммы в отчет о финансовых результатах и баланс. Примите также в расчет ежемесячных расходов на амортизацию остальные виды основных средств на общую сумму 36 тыс. руб. Для расчетов используйте кнопки начального баланса и задания 1.1.
    '''
        if not b1nc:
            frame:
                background "gui/frame1.png"
                text "{size=+0}[s]{/size}" xpos 80 ypos 80 xsize 1600 ysize 800 color "#000000" line_spacing 2
                add "kadr b18t1" xpos 80 ypos 230 zoom 0.9
                add "kadr b18t2" xpos 880 ypos 230 zoom 0.78
                add "intern.jpg" xpos 1680 ypos 120
                imagebutton:
                    xalign 0.93 yalign 0.5
                    idle "b1kadr8but1.png"
                    hover "b1kadr8but1_.png"
                    action [SetVariable("nkadr", 3), SetVariable("b1kadr8back", True), Call("KadrBack")]
                imagebutton:
                    xalign 0.93 yalign 0.7
                    idle "b1kadr8but2.png"
                    hover "b1kadr8but2_.png"
                    action [SetVariable("nkadr", 5), SetVariable("b1kadr8back", True), Call("KadrBack")]
                if b1amcor == 1:
                    add "b1cor.png" xpos 737 ypos 468
                elif b1am0 == b1kadr8a1:
                    add "b1ncor.png" xpos 737 ypos 468
                if b1mtcor == 1:
                    add "b1cor.png" xpos 1453 ypos 375
                elif b1mt0 == b1kadr8a2:
                    add "b1ncor.png" xpos 1453 ypos 375
                if b1naccor == 1:
                    add "b1cor.png" xpos 1453 ypos 470
                elif b1nac0 == b1kadr8a3:
                    add "b1ncor.png" xpos 1453 ypos 470
                if (b1kadr8a1 != "" and b1kadr8a2 != "" and b1kadr8a3 != "") and b1amn != 2 and ((b1amcor == 1 or b1kadr8a1 != b1am0) and (b1mtcor == 1 or b1kadr8a2 != b1mt0) and (b1naccor == 1 or b1kadr8a3 != b1nac0)) and not (b1amcor == 1 and b1mtcor == 1 and b1naccor == 1):
                    imagebutton:
                        xalign 0.91 yalign 0.9
                        idle "b1butch.png"
                        hover "b1butch_.png"
                        action Call("b1kadr8nc")                
screen b1kadr8v1:
    zorder 100
    if vkadr == "b1" and nkadr == 8 and not b1nc:
        frame:
            background "gui/frame1.png"
            xpos 580 ypos 475
            xsize 150 ysize 36
            if b1amcor != 1 and b1amn != 2:
                imagebutton:
                    idle im.Scale("gui/frame1.png", 150, 36)
                    action [Hide("b1kadr8v1"),Hide("b1kadr8v2"),Hide("b1kadr8v3"),Show("b1kadr8v1"),Show("b1kadr8v2"),Show("b1kadr8v3")] 
                input default "":
                    color "#000000"
                    value VariableInputValue("b1kadr8a1")
                    length 8
                    allow "0123456789"
                    size 24
            else:
                text "[b1kadr8a1]" size 24 color "#000000"#"#ffffff"
                   
screen b1kadr8v2:
    zorder 100
    if vkadr == "b1" and nkadr == 8 and not b1nc:
        frame:
            background "gui/frame1.png"
            xpos 1335 ypos 384
            xsize 120 ysize 28
            if  b1mtcor != 1 and b1amn != 2:
                imagebutton:
                    idle im.Scale("gui/frame1.png", 120, 28)
                    action [Hide("b1kadr8v1"),Hide("b1kadr8v2"),Hide("b1kadr8v3"),Show("b1kadr8v2"),Show("b1kadr8v1"),Show("b1kadr8v3")]
                input default "":
                    color "#000000"
                    value VariableInputValue("b1kadr8a2")
                    length 8
                    allow "0123456789"
                    size 20
            else:
                text "[b1kadr8a2]" size 20 color "#000000"#"#ffffff"                    
screen b1kadr8v3:
    zorder 100
    if vkadr == "b1" and nkadr == 8 and not b1nc:
        frame:
            background "gui/frame1.png"
            xpos 1335 ypos 480
            xsize 120 ysize 28
            if  b1naccor != 1 and b1amn != 2:
                imagebutton:
                    idle im.Scale("gui/frame1.png", 120, 28)
                    action [Hide("b1kadr8v1"),Hide("b1kadr8v2"),Hide("b1kadr8v3"),Show("b1kadr8v3"),Show("b1kadr8v2"),Show("b1kadr8v1")]
                input default "":
                    color "#000000"
                    value VariableInputValue("b1kadr8a3")
                    length 8
                    allow "0123456789"
                    size 20
            else:
                text "[b1kadr8a3]" size 20 color "#000000"#"#ffffff"                    

label b1kadr8nc:
        $ b1amcor = 1 if b1am == int(b1kadr8a1) else 2
        $ b1mtcor = 1 if b1mt == int(b1kadr8a2) else 2
        $ b1naccor = 1 if b1nac == int(b1kadr8a3) else 2
        if b1amcor != 1 or b1mtcor != 1 or b1naccor != 1:
            $ b1am0 = b1kadr8a1
            $ b1mt0 = b1kadr8a2
            $ b1nac0 = b1kadr8a3
            $ b1amn += 1
            if b1amn < 2:
                $ b1nc = True
                hide screen butforwardback
                show b1kadrnclup at left with fade:
                    xpos 50 ypos 850
                pause(2)
                show screen b1kadr8nc          
        pause
        return

label b1kadr8ncback:
    $ b1nc = False
    $ clearlup()
    hide screen b1kadr8nc
    show screen butforwardback
    hide screen b1kadr8
    show screen b1kadr8 with fade
    hide screen b1kadr8v1
    hide screen b1kadr8v2
    hide screen b1kadr8v3    
    show screen b1kadr8v1
    show screen b1kadr8v2
    show screen b1kadr8v3
    pause
    return

screen b1kadr8nc:
    modal True
    text "{size=+5}Введенный ответ неверный!\nПредлагаю не вешать нос и попробовать снова.{/size}" xpos 800 ypos 150 xsize 1000 ysize 800 color "#000000"
    imagebutton:
        xpos 1000 ypos 250
        idle "b1ncbut1.png"
        hover "b1ncbut1_.png"
        action Call("b1kadr8ncback")
    text "{size=+5}Если немного забыл материал, то можно обратиться за помощью к опытному бухгалтеру.{/size}" xpos 800 ypos 450 xsize 1000 ysize 800 color "#000000"
    imagebutton:
        xpos 1000 ypos 550
        idle "b1ncbut2.png"
        hover "b1ncbut2_.png"
        action [Function(clearlup), Hide("b1kadr8nc"), SetVariable("backkadr", "b1"), Call("ha")]
                
screen b1kadr9:
    zorder 100
    if vkadr == "b1" and nkadr == 9:
        if not b1bt and b1amcor == 0:
            $ s = 'У тебя этот блок сегодня не получился, но есть еще одна возможность показать себя.\nПредлагаю не огорчаться окончательно и ответить на вопросы блиц-теста. Можно заработать две золотые монеты. Это лучше, чем уходить отсюда с «пустым кошельком».'
            text "{size=+10}[s]{/size}" xpos 850 ypos 100 xsize 900 ysize 800 color "#000000"
            imagebutton:
                xpos 1010 ypos 690
                idle "b1kadr9butbt.png"
                hover "b1kadr9butbt_.png"
                action Call("b1kadr9bt")
        else:
            imagebutton:
                xpos 1280 ypos 50
                idle "b1butrez.png"
                hover "b1butrez_.png"
                action [SetVariable("backkadr", "b1"), Call("rez")]
            if not b1bt:
                $ store.b1kadr8rez = b1kadr6rez + (6 - (b1amcor + b1mtcor + b1naccor))
                $ persistent.scores = b1kadr8rez
                #$ renpy.save_persistent()
                #$ print(b1kadr6rez, b1kadr8rez)
                if b1kadr8rez == 18:
                    $ s = f'''
Молодец!
Ты выполнил все три задания в этом блоке и заработал {b1kadr8rez} золотых монет.
 
А еще ты получаешь веселый бейджик «ХРАНИТЕЛЬ БОГАТСТВ»!
                '''
                    text "{size=+20}[s]{/size}" xpos 950 ypos 270 xsize 800 ysize 800 color "#000000"
                    add "badgekt.png" xpos 1550 ypos 700
                elif b1kadr8rez != b1kadr6rez and b1kadr8rez > 0:
                    $ s = f'''
Молодец!
Ты выполнил все три задания в этом блоке и заработал {b1kadr8rez} золотых монет.
                '''
                    text "{size=+20}[s]{/size}" xpos 950 ypos 270 xsize 800 ysize 800 color "#000000"
                elif b1kadr8rez == b1kadr6rez and b1kadr8rez > 0:
                    $ s = f'''
К сожалению, в задании 1.3 не удалось заработать золотых монет и у тебя по прежнему {b1kadr8rez} золотых монет.
                        '''
                    text "{size=+20}[s]{/size}" xpos 950 ypos 270 xsize 835 ysize 800 color "#000000"
            else:
                $ s = f'''
В блиц-тестировании ты заработал {b1kadr8rez} золотых монет.
                    '''
                text "{size=+20}[s]{/size}" xpos 950 ypos 270 xsize 835 ysize 800 color "#000000"
            
                
#label b1kadr9scores0:
#    show b1kadrnclup at left with fade:
#        xpos 50 ypos 850
#    pause(2)
#    return
screen b1kadr9bt:
    text "{size=+2}Вопрос №[b1i]. [b1quest]{/size}" xpos 400 ypos 300 xsize 1200 ysize 200 #color "#ff00cc"

label b1kadr9bt:
    hide screen butforwardback
    hide b1kadr9
    hide screen b1kadr9
    show kadr b19bt   
    $ b1i = 1
    $ b1nv = 0
    $ renpy.random.shuffle(b1nsh)
label cicbt:
    $ b1ansbtsh = b1ansbt[b1nsh[b1i-1]].copy()
    $ renpy.random.shuffle(b1ansbtsh)
    $ b1quest = b1quebt[b1nsh[b1i-1]]
    $ ans1 = b1ansbtsh[b1nsh[0]]
    $ ans2 = b1ansbtsh[b1nsh[1]]
    $ ans3 = b1ansbtsh[b1nsh[2]]
    $ ans4 = b1ansbtsh[b1nsh[3]]
    show screen b1kadr9bt
    menu:
        "1. [ans1]":
            if ans1 == b1ansbt[b1nsh[b1i-1]][0]:
                jump corbt
            else:
                jump ncorbt
        "2. [ans2]":
            if ans2 == b1ansbt[b1nsh[b1i-1]][0]:
                jump corbt
            else:
                jump ncorbt
        "3. [ans3]":
            if ans3 == b1ansbt[b1nsh[b1i-1]][0]:
                jump corbt
            else:
                jump ncorbt
        "4. [ans4]":
            if ans4 == b1ansbt[b1nsh[b1i-1]][0]:
                jump corbt
            else:
                jump ncorbt
label corbt:
    $ b1nv += 1
label ncorbt:
    $ b1i += 1
    if b1i <= 4:
        jump cicbt
    hide screen b1kadr9bt
    $ store.b1kadr8rez = 0 if b1nv == 0 else 1 if b1nv <= 2 else 2
    $ persistent.scores = b1kadr8rez
    $ b1bt = True
    #$ kadrb1()
    scene white
    show kadr b19
    show screen butforwardback
    show screen b1kadr9
    pause
    return

screen b1endt:
    if b1kadr8rez == 18:
        $ s = '''
{color=#cf0f0f}Блок 1 пройден! Поздравляю! Давай подведем итоги!{/color}
 
Всего можно было заработать в этом блоке {b}18 монет{/b}. Тебе удалось решить правильно все задания.

Я предупреждал, что кое-кто будет внимательно следить за тобой, чтобы забрать монеты в случае ошибок. Но сегодня эти наблюдатели остались без монет.
    '''    
    elif b1kadr8rez == 0:
        $ s = '''
{color=#cf0f0f}Блок 1 пройден! Давай подведем итоги!{/color}
 
Я огорчен. Тебе не удалось верно решить задания в этом блоке, и блиц-тест не получился. Кое-кто внимательно следил за тобой и сейчас забирает все твои монеты.

Не вешать нос! Соберись! \nДокажи, что ты можешь побеждать. Я верю в тебя!
    '''    
    else:
        $ s = '''
{color=#cf0f0f}Блок 1 пройден! Поздравляю! Давай подведем итоги!{/color}
 
Всего можно было заработать в этом блоке {b}18 монет{/b}. Не все задания тебе удалось решить правильно.

Я предупреждал, что кое-кто будет внимательно следить за тобой, чтобы забрать монеты в случае ошибок. 
    '''
    text "{size=+2}[s]{/size}" xpos 400 ypos 100 xsize 700 ysize 1000 color "#000000"

screen b1endm:
    frame:
        background Frame([ "gui/confirm_frame.png", "gui/frameyel.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xpos 80 ypos 800 xsize 880 ysize 60
        text "Твой результат:" color "#000000" size 28 xalign 0.5 yalign 0.5
    frame:
        background Frame([ "gui/confirm_frame.png", "gui/frameyel.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xpos 956 ypos 800 xsize 880 ysize 60
        text "Результат твоих наблюдателей - Йети и К:" color "#000000" size 28 xalign 0.5 yalign 0.5
    frame:
        xpos 80 ypos 856 xsize 880 ysize 60
        background Frame([ "gui/confirm_frame.png", "gui/framegrey.png"], gui.frame_borders, tile=gui.frame_tile)
        text "[b1immy] золотых монет" color "#000000" size 28 xalign 0.5 yalign 0.5    
    frame:
        background Frame([ "gui/confirm_frame.png", "gui/framegrey.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xpos 956 ypos 856 xsize 880 ysize 60
        text "[b1imyet] золотых монет" color "#000000" size 28 xalign 0.5 yalign 0.5

screen b1endb:        
    modal True
    imagebutton:
        xpos 1280 ypos 50
        idle "b1butrez.png"
        hover "b1butrez_.png"
        action [SetVariable("backkadr", "b1"), Call("rez")]
        #add "b1kadr10p.png" xpos 1200 ypos 175 zoom 0.133#xsize 400 ysize 486 #3008 3660
        #add "b1kadr10e.png" xpos 1500 ypos 175 zoom 0.114#xsize 400 ysize 565 #3508 4961
    imagebutton:
        xalign 0.5 yalign 0.97
        idle "b1butb2.png"
        hover "b1butb2_.png"
        action Jump("startb2")

label b1end:
    scene white
    show b1endl with dissolve
    pause(1)
    show screen b1endt
    show screen b1endm
    show b1ende#kadr b1ende #xpos 1500 ypos 175 zoom 0.114
    pause(3)
    show b1endp #zoom 0.1#kadr b1endp xpos 1200 #ysize 175 size 0.133#xsize 400 ysize 486 
    pause(2)
    $ monetmove()
    pause(2)
    hide b1endp
    pause(2)
    if b1kadr8rez == 0:
        hide b1ende
        show b1endes
        pause(2)
    show screen b1endb
    pause
    return