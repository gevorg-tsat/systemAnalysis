label b5kadr1:
    $ screens = ["processing_of_eval", "butforwardback", "method5_input", "student_table_image", "task2_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [50, 400]
    $ xsize_ev_al_table = 700
    $ ysize_ev_al_table = 300
    show screen processing_of_eval(method5_text)
    show screen method5_input
    show screen student_table_image
    show screen butforwardback
    pause


init python:
    import math
    req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true&key={TOKEN}")
    method5_google_data = json.loads(req.text)["sheets"][4]["data"][0]["rowData"]
    EXPERTS_COUNT_METHOD5 = method5_google_data[0]["values"][1]["userEnteredValue"]["numberValue"]
    method5_text = "Задача состоит в сопоставлении оцениваемой альтернативе одного числа. N экспертов изолированы; обратная связь отсутствует. Найти интервал, в который оцениваемая величина попадет с вероятностью P = 90%"
    x_data = []
    alpha_data = []
    mean_exps = None
    despersion_exps = -1
    delta_exps = None
    left_diaposon = None
    right_diaposon = None
    for i in range(EXPERTS_COUNT_METHOD5):
        x_data.append(method5_google_data[1]["values"][i+1]["userEnteredValue"]["numberValue"])
    for i in range(EXPERTS_COUNT_METHOD5):
        alpha_data.append(method5_google_data[2]["values"][i+1]["userEnteredValue"]["numberValue"])
    def kadrb5():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b5kadr{nkadr}"):
            return
        renpy.call(f"b5kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()
    def check_mean(inp):
        global x_data
        global table_input
        global alpha_data
        global EXPERTS_COUNT_METHOD5
        global mean_exps
        if not inp:
            return
        value = float(inp)
        table_input = ''
        mean_corr = sum([x_data[i] * alpha_data[i] for i in range(len(x_data))])/sum(alpha_data)
        if abs(value - mean_corr) > 0.1:
            return
        mean_exps = value
        renpy.restart_interaction()

    def check_desp(inp):
        global x_data
        global alpha_data
        global EXPERTS_COUNT_METHOD5
        global mean_exps
        global table_input
        global despersion_exps
        if not inp:
            return
        value = float(inp)
        table_input = ''
        despersion_corr = sum([((x_data[i] - mean_exps)**2) * alpha_data[i] for i in range(len(x_data))])/sum(alpha_data)
        if abs(value - despersion_corr) > 0.1:
            return
        despersion_exps = value
        renpy.restart_interaction()
    
    def check_delta(inp):
        student_coef = [6.3137, 2.9199, 2.3533, 2.1318, 2.01504, 1.94318, 1.8945, 1.8595, 1.83311]
        global x_data
        global alpha_data
        global despersion_exps
        global delta_exps
        global table_input
        global EXPERTS_COUNT_METHOD5
        if not inp:
            return
        value = float(inp)
        table_input = ''
        delta_corr = student_coef[EXPERTS_COUNT_METHOD5 - 2] * math.sqrt(despersion_exps)/ math.sqrt(EXPERTS_COUNT_METHOD5)
        if abs(value - delta_corr) > 0.1:
            return
        delta_exps = value
        renpy.restart_interaction()
    
    def check_left_diap(inp):
        global x_data
        global alpha_data
        global despersion_exps
        global delta_exps
        global mean_exps
        global table_input
        global EXPERTS_COUNT_METHOD5
        global left_diaposon
        if not inp:
            return
        value = float(inp)
        table_input = ''
        left_corr = mean_exps - delta_exps
        if abs(value - left_corr) > 0.1:
            return
        left_diaposon = value
        renpy.restart_interaction()
    
    def check_right_diap(inp):
        global x_data
        global alpha_data
        global despersion_exps
        global delta_exps
        global mean_exps
        global EXPERTS_COUNT_METHOD5
        global right_diaposon
        global allow_forward
        global table_input
        if not inp:
            return
        value = float(inp)
        table_input = ''
        right_corr = mean_exps + delta_exps
        if abs(value - right_corr) > 0.1:
            return
        right_diaposon = value
        text = "Верно! Поздравляю! переходи вперед, в меню"
        allow_forward = True
        renpy.hide_screen("method5_input")
        renpy.show_screen("final_go_to_next_method4", text)
        renpy.restart_interaction()
    
screen processing_of_eval(text):
    text "Обработка числовых экспертных значений" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 150 xsize 1000 ysize 900

    frame:
        text "xi" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0])
        ypos int(xy_ev_al_table[1])
        xsize int(xsize_ev_al_table/(len(x_data) + 1))
        ysize int(ysize_ev_al_table/(len(x_data) + 1))
    
    frame:
        text "alpha" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0])
        ypos int(xy_ev_al_table[1]) + int(ysize_ev_al_table/(len(x_data) + 1))
        xsize int(xsize_ev_al_table/(len(x_data) + 1))
        ysize int(ysize_ev_al_table/(len(x_data) + 1))
    
    for i in range(len(x_data)):
        frame:
            text str(x_data[i]) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0]) + (i+1) * int(xsize_ev_al_table/(len(x_data) + 1))
            ypos int(xy_ev_al_table[1])
            xsize int(xsize_ev_al_table/(len(x_data) + 1))
            ysize int(ysize_ev_al_table/(len(x_data) + 1))
    for i in range(len(alpha_data)):
        frame:
            text str(alpha_data[i]) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0]) + (i+1) * int(xsize_ev_al_table/(len(x_data) + 1))
            ypos int(xy_ev_al_table[1]) + int(ysize_ev_al_table/(len(x_data) + 1))
            xsize int(xsize_ev_al_table/(len(x_data) + 1))
            ysize int(ysize_ev_al_table/(len(x_data) + 1))
    if mean_exps:
        frame:
            text "матожидание = " + str(mean_exps) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0])
            ypos (int(xy_ev_al_table[1]) + int(ysize_ev_al_table/(len(x_data) + 1)) * 2)
            xsize int(xsize_ev_al_table)
            ysize int(ysize_ev_al_table/(len(x_data) + 1))
    if despersion_exps != -1:
        frame:
            text "дисперсия = " + str(despersion_exps) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0])
            ypos (int(xy_ev_al_table[1]) + int(ysize_ev_al_table/(len(x_data) + 1)) * 3)
            xsize int(xsize_ev_al_table)
            ysize int(ysize_ev_al_table/(len(x_data) + 1))
    if delta_exps:
        frame:
            text "delta = " + str(delta_exps) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0])
            ypos (int(xy_ev_al_table[1]) + int(ysize_ev_al_table/(len(x_data) + 1)) * 4)
            xsize int(xsize_ev_al_table)
            ysize int(ysize_ev_al_table/(len(x_data) + 1))

screen method5_input:
    zorder 100
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 15
            if mean_exps is None:
                label _("Мат ожидание"):
                    style "confirm_prompt"
                    xalign 0.5
            elif despersion_exps == -1:
                label _("Дисперсия"):
                    style "confirm_prompt"
                    xalign 0.5
            elif delta_exps is None:
                label _("Дельта"):
                    style "confirm_prompt"
                    xalign 0.5
            elif left_diaposon is None:
                label _("Левая граница интервала"):
                    style "confirm_prompt"
                    xalign 0.5
            elif right_diaposon is None:
                label _("Правая граница интервала"):
                    style "confirm_prompt"
                    xalign 0.5

            input:
                default "None"
                color "#000000"
                value VariableInputValue("table_input", returnable=True)
                xalign 0.5
                length 8
                allow "0123456789."
                size 24
                        
            hbox:

                xalign 0.5
                spacing 100
                if mean_exps is None:
                    textbutton _("ввод") action Function(check_mean, table_input)
                elif despersion_exps == -1:
                    textbutton _("ввод") action Function(check_desp, table_input)
                elif delta_exps is None:
                    textbutton _("ввод") action Function(check_delta, table_input)
                elif left_diaposon is None:
                    textbutton _("ввод") action Function(check_left_diap, table_input)
                elif right_diaposon is None:
                    textbutton _("ввод") action Function(check_right_diap, table_input)

screen student_table_image:
    image "student-table.png":
        xpos 1200 ypos 50 xsize 600 ysize 700