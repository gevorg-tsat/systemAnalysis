label b4kadr1:
    $ screens = ["ranging_method", "butforwardback", "method4_input", "pearson_table_image", "final_go_to_next_method4"]
    $ allow_forward = False
    $ xy_ev_al_table = [50, 300]
    $ xsize_ev_al_table = 500
    $ ysize_ev_al_table = 500
    $ alts_methods4_txt += ", ΣRi - сумма рангов, r - общий ранг альтерантивы, W - коэффициента конкордации Кенделла, P = 90%"
    show screen ranging_method(alts_methods4_txt)
    show screen method4_input
    show screen butforwardback
    pause



init python:
    req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true&key={TOKEN}")
    ranging_method4_google_data = json.loads(req.text)["sheets"][3]["data"][0]["rowData"]
    EXPERTS_COUNT_METHOD4 = 3
    show_error = False
    alts_methods4 = method1_task1_alternatives
    ranging_method4_table = list()
    sum_R_index_method4 = 1
    r_index_method4 = 1
    W_data = -1
    sum_R_values = list()
    r_values = list()
    method4_sogl = 0 # 0 == None, 1 == weak, 2 == medium, 3 == strong
    pearson_data = -1

    for i in range(len(alts_methods4)):
        ranging_method4_table.append(list())
        for j in range(EXPERTS_COUNT_METHOD4):
            ranging_method4_table[i].append(int(ranging_method4_google_data[i]["values"][j]["userEnteredValue"]["numberValue"]))
    alts_methods4_txt = "Задача состоит в сопоставлении оцениваемой альтернативе ранга: чем меньше ранг, тем альтернатива приоритетнее по мнению эксперта. "
    for i in range(len(alts_methods4)):
        alts_methods4_txt += f"A{i+1} - {alts_methods4[i]}, "
    alts_methods4_txt = alts_methods4_txt[:-2]
    def write_sum_R(inp):
        global show_error
        global sum_R_index_method4
        global allow_forward
        global table_input
        if not inp:
            return
        value = int(inp)
        table_input = ''
        global sum_R_values
        global ranging_method4_table
        if round(sum(ranging_method4_table[sum_R_index_method4-1]), 2) != round(value,2):
            show_error = True
            return
        sum_R_values.append(value)
        sum_R_index_method4+=1
        show_error = False
        renpy.restart_interaction()
    def write_r(inp):
        global show_error
        global r_index_method4
        global allow_forward
        global table_input
        if not inp:
            return
        value = int(inp)
        table_input = ''
        global r_values
        show_error = False
        r_values.append(value)
        r_index_method4 += 1
        renpy.restart_interaction()
    def write_W(inp):
        global show_error
        global sum_R_values
        global allow_forward
        global EXPERTS_COUNT_METHOD4
        global W_data
        if not inp:
            return
        value = float(inp)
        sum_sq = 0
        for i in range(len(sum_R_values)):
            sum_sq += ((sum_R_values[i] - 0.5 * (len(sum_R_values) + 1) * EXPERTS_COUNT_METHOD4) ** 2)
        W_corr = 12*sum_sq/((EXPERTS_COUNT_METHOD4 ** 2) * (len(sum_R_values)**3 - len(sum_R_values)))
        if round(value,2) != round(W_corr, 2):
            show_error = True
            return
        W_data = value
        show_error = False
        renpy.restart_interaction()
    def write_Pearson(inp):
        global show_error
        global table_input
        global sum_R_values
        global allow_forward
        global EXPERTS_COUNT_METHOD4
        global W_data
        global pearson_data
        if not inp:
            return
        value = float(inp)
        table_input = ''
        Pearson_corr = W_data * EXPERTS_COUNT_METHOD4 * (len(sum_R_values) - 1)
        if round(value,2) != round(Pearson_corr, 2):
            show_error = True
            return
        pearson_data = value
        show_error = False
        renpy.show_screen("pearson_table_image")
        renpy.restart_interaction()
    def pearson_90_table(n_m1):
        table=[2.71, 4.61, 6.25, 7.78, 9.24, 10.64, 12.02, 13.36, 14.68, 50.99]
        return table[n_m1-1]
    def write_sogl(inp):
        global method4_sogl
        method4_sogl = inp
    def check_correctness(signif):
        global allow_forward
        global pearson_data
        global b4_done
        pearson_from_table = pearson_90_table(len(sum_R_values) - 2)
        if (signif and pearson_data > pearson_from_table) or (signif == False and pearson_data <= pearson_from_table):
            text = "Верно! Поздравляю! переходи вперед, в меню"
        else:
            text = "К сожалению ты ошибься. переходи вперед, в меню"
        allow_forward = True
        b4_done = True
        renpy.hide_screen("method4_input")
        renpy.show_screen("final_go_to_next_method4", text)
        renpy.restart_interaction()

    def kadrb4():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b4kadr{nkadr}"):
            renpy.call("startgame")
            return
        renpy.call(f"b4kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()

screen ranging_method(text):
    text "Ранжирование" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 150 xsize 1800 ysize 900

    zorder 100
    for i in range(len(alts_methods4)):
        frame:
            text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos xy_ev_al_table[0] 
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(alts_methods4) + 1)))
            xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
            ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
    for i in range(EXPERTS_COUNT_METHOD4):
        frame:
            text "E" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0]  + (i+1)*(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4)))
            ypos int(xy_ev_al_table[1])
            xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
            ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
    for i in range(len(alts_methods4)):
        for j in range(EXPERTS_COUNT_METHOD4):
            frame:
                text str(ranging_method4_table[i][j]) color "#000000" xalign 0.5 yalign 0.5
                xpos int(xy_ev_al_table[0]  + (j+1)*(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4)))
                ypos int(xy_ev_al_table[1] + (i+1)*(ysize_ev_al_table/(len(alts_methods4) + 1)))
                xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
                ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
    frame:
        text "ΣRi" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0]  + (EXPERTS_COUNT_METHOD4 + 1)*(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4)))
        ypos xy_ev_al_table[1]
        xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
        ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))

    for i in range(len(sum_R_values)):
        frame:
            text str(sum_R_values[i]) color "#000000" xalign 0.5 yalign 0.5 size 25
            xpos int(xy_ev_al_table[0]  + (EXPERTS_COUNT_METHOD4 + 1)*(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4)))
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(alts_methods4) + 1)))
            xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
            ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
    
    if sum_R_index_method4 == len(alts_methods4) + 1:
        frame:
            text "r" color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0]  + (EXPERTS_COUNT_METHOD4 + 2)*(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4)))
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
            ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
        for i in range(len(r_values)):
            frame:
                text str(r_values[i]) color "#000000" xalign 0.5 yalign 0.5 size 25
                xpos int(xy_ev_al_table[0]  + (EXPERTS_COUNT_METHOD4 + 2)*(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4)))
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(alts_methods4) + 1)))
                xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
                ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
    if W_data != -1:
        frame:
            text "W = " + str(round(W_data,2)) color "#000000" xalign 0.5 yalign 0.5 size 25
            xpos int(xy_ev_al_table[0])
            ypos xy_ev_al_table[1] + int(ysize_ev_al_table) + 20
            xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
            ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
    if pearson_data != -1:
        frame:
            text "X2_расч = " + str(round(pearson_data,2)) color "#000000" xalign 0.5 yalign 0.5 size 25
            xpos int(xy_ev_al_table[0])
            ypos xy_ev_al_table[1] + int(ysize_ev_al_table) + int(ysize_ev_al_table/(len(alts_methods4) + 1)) + 20
            xsize int(xsize_ev_al_table/(EXPERTS_COUNT_METHOD4))
            ysize int(ysize_ev_al_table/(len(alts_methods4) + 1))
    
screen method4_input:
    zorder 100
    frame:
        xpos 1450 ypos 810
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 10
            if sum_R_index_method4 != len(alts_methods4) + 1:
                label _("ΣR{size=-10}[sum_R_index_method4]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            elif r_index_method4 != len(alts_methods4) + 1:
                label _("r{size=-10}[r_index_method4]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            elif W_data == -1:
                label _("W"):
                    style "confirm_prompt"
                    xalign 0.5
            elif method4_sogl == 0:
                label _("Согласованность"):
                    style "confirm_prompt"
                    xalign 0.5
            elif pearson_data == -1:
                label _("Критерий Пирсона. Расчетный"):
                    style "confirm_prompt"
                    xalign 0.5
            else:
                label _("W - статистически"):
                    style "confirm_prompt"
                    xalign 0.5
            if W_data == -1 or (method4_sogl != 0 and pearson_data == -1):
                input:
                    default "None"
                    color "#000000"
                    value VariableInputValue("table_input", returnable=True)
                    xalign 0.5
                    length 8
                    if r_index_method4 != len(alts_methods4) + 1 or sum_R_index_method4 != len(alts_methods4) + 1:
                        allow "1234567890"
                    else:
                        allow "0123456789."
                    size 24
            
            if not method4_sogl and W_data != -1:
                vbox:
                    xalign 0.5
                    spacing 5
                    textbutton _("слабая") action Function(write_sogl, 1)
                    textbutton _("средняя") action Function(write_sogl, 2)
                    textbutton _("сильная") action Function(write_sogl, 3)        
            else:    
                hbox:
                    xalign 0.5
                    spacing 100
                    if sum_R_index_method4 != len(alts_methods4) + 1:
                        textbutton _("ввод") action Function(write_sum_R, table_input)
                    elif r_index_method4 != len(alts_methods4) + 1:
                        textbutton _("ввод") action Function(write_r, table_input)
                    elif W_data == -1:
                        textbutton _("ввод") action Function(write_W, table_input)
                    elif pearson_data == -1:
                        textbutton _("ввод") action Function(write_Pearson, table_input)
                    else:
                        textbutton _("значим") action Function(check_correctness, True)
                        textbutton _("не значим") action Function(check_correctness, False)
    if show_error:
        text "Ошибка" xpos 1560 ypos 1030  color '#000000'
screen final_go_to_next_method4(text):
    frame:
        xpos 1450 ypos 810
        xsize 400 ysize 200
        text "[text]" color "#000000" 

screen pearson_table_image:
    image "pearson_table.png":
        xpos 1400 ypos 300 xsize 500 ysize 500