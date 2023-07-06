define ldac = ["Центр виртуальных миров — это уникальное пространство 6+ для развлечений, мероприятий, дней рождений, частного и корпоративного активного отдыха.", "Клиентам Центра предлагается огромный выбор популярных лицензионных игр для разных возрастных категорий.", "Центр виртуальных миров создавался на базе самых современных технологий, позволяющих участникам приключений не просто видеть, но и чувствовать вновь открываемый мир.", "3D и 4D реальность имитируют подвижные полы, жилеты, передающие физические ощущения, портативные компьютеры, генераторы запахов. Эти объекты учитываются как основные средства.", "Каждая из двух площадок Центра располагается в отдельном зале и имеет свой набор оборудования. Площадки находятся в арендованном на длительный срок помещении, за которое вносятся платежи.", "В Центре виртуальных миров есть мобильная игровая арена, которая включает генераторы, кондиционеры, игровое оборудование, систему транспортировки. Все объекты учитывается в составе основных средств.", "Для регулярной дезинфекции оборудования и помещений приобретены соответствующие пульверизаторы и закупаются расходные материалы (жидкости, салфетки).", "Посетителям Центра предоставляются необходимые удобства, включая санитарно-техническое оборудование. Для санузлов регулярно приобретаются расходные материалы.", "Билеты на игровые площадки можно купить в кассах за наличный или безналичный расчет. Предварительная продажа есть на сайте Центра. Выпущены подарочные карты. Выписываются счета для предприятий.", "Одна из постоянных статей расходов Центра – затраты на рекламу. Создаются рекламные ролики, выпускаются футболки, объемные открытки, гостей приглашают веселые игровые персонажи.", "Сотрудники Центра работают по трудовым контрактам или гражданско-правовым договорам.  Персонал принимает посетителей, обеспечивает уборку Центра, текущее обслуживание оборудования, иные работы."]

init python:
    def kadrac():
        global nkadr
        if nkadr == 12: 
            renpy.hide("kadr ac12")
            renpy.hide_screen("butforwardback")
            vkadr = ""
            return
        if nkadr == 4 or nkadr == 8 or nkadr == 11:
            renpy.hide_screen(f"kadrac{nkadr-1}")
        if nkadr == 2 or nkadr == 6 or nkadr == 9:
            renpy.hide_screen(f"kadrac{nkadr+1}")
        renpy.show(f"kadr ac{nkadr}",at_list=[top])
        renpy.with_statement(fade)
        if nkadr == 3 or nkadr == 7 or nkadr == 10:
            renpy.show_screen(f"kadrac{nkadr}")
        renpy.say(None,ldac[nkadr-1])
        #nkadr += 1
        #kadrrg() 

screen hello_lup:
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        $ renpy.movie_cutscene("kadr 16.ogv")

screen kadrac3:
    imagebutton:
        xalign 0.28 yalign 0.8
        idle "butopen.png"
        hover "butopen_.png"
        action Call("kadrac3")
        #action [Function(renpy.movie_cutscene,"videok5.ogv"), Function(Rollback)]#Call("showvideok5")
screen kadrac7:
    imagebutton:
        xalign 0.28 yalign 0.8
        idle "butopen.png"
        hover "butopen_.png"
        action Call("kadrac7")
screen kadrac10:
    imagebutton:
        xalign 0.33 yalign 0.796
        idle "butopenr.png"
        hover "butopenr_.png"
        action Call("kadrac10")

label kadrac3:
    $ renpy.movie_cutscene("kadr ac3.ogv")
    $ kadrac()
    return
label kadrac7:
    $ renpy.movie_cutscene("kadr ac7.ogv")
    $ kadrac()
    return
label kadrac10:
    $ renpy.movie_cutscene("kadr ac10.ogv")
    $ kadrac()
    return

label AboutCompany:
    hide screen main_menu
    scene white
    $ renpy.show_screen("butforwardback")
    $ vkadr = "ac"
    $ nkadr = 1
    $ kadrac()
    scene black with fade
    return