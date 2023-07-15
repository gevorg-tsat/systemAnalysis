label b4kadr1:
    # TODO
    $ screens = ["goal_defenition", "butforwardback", "method3_input", "method3_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [50, 300]
    $ xsize_ev_al_table = 500
    $ ysize_ev_al_table = 500
    show screen ranging_method(alts_methods4_txt)
    show screen method4_input
    show screen butforwardback
    pause



init python:
    req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true&key={TOKEN}")
    ranging_method4_google_data = json.loads(req.text)["sheets"][3]["data"][0]["rowData"]
    EXPERTS_COUNT_METHOD4 = 3
    alts_methods4 = method1_task1_alternatives
    ranging_method4_table = list()
    sum_R_index_method4 = 1
    r_index_method4 = 1
    W_data = -1
    sum_R_values = list()
    r_values = list()
    method4_sogl = 0 # 0 == None, 1 == weak, 2 == medium, 3 == strong
    for i in range(len(alts_methods4)):
        ranging_method4_table.append(list())
        for j in range(EXPERTS_COUNT_METHOD4):
            ranging_method4_table[i].append(int(ranging_method4_google_data[i]["values"][j]["userEnteredValue"]["numberValue"]))
    alts_methods4_txt = ""
    for i in range(len(alts_methods4)):
        alts_methods4_txt += f"A{i+1} - {alts_methods4[i]}, "
    alts_methods4_txt = alts_methods4_txt[:-2]
    def write_sum_R(inp):
        global sum_R_index_method4
        global allow_forward
        if not inp:
            return
        value = int(inp)
        global sum_R_values
        global ranging_method4_table
        if abs(sum(ranging_method4_table[sum_R_index_method4-1]) - value) > 1:
            return
        sum_R_values.append(value)
        sum_R_index_method4+=1
        renpy.restart_interaction()
    def write_r(inp):
        global r_index_method4
        global allow_forward
        if not inp:
            return
        value = int(inp)
        global r_values
        r_values.append(value)
        r_index_method4 += 1
        renpy.restart_interaction()
    def write_W(inp):
        global sum_R_values
        global allow_forward
        global EXPERTS_COUNT_METHOD4
        if not inp:
            return
        value = float(inp)
        sum_sq = 0
        for i in range(len(sum_R_values)):
            sum_sq += ((sum_R_values[i] - 0.5 * (len(sum_R_values) + 1) * EXPERTS_COUNT_METHOD4) ** 2)
        W_corr = 12*sum_sq/((EXPERTS_COUNT_METHOD4 ** 2) * (len(sum_R_values)**3 - len(sum_R_values)))
        if abs(value - W_corr) > 0.1:
            return
        W_data = value
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
            return
        renpy.call(f"b4kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()

screen ranging_method(text):
    text "Алгоритм парных сравнений для группы экспертов" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 150 xsize 1000 ysize 900

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

screen method4_input:
    zorder 100
    frame:
        xpos 1450 ypos 810
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 30
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
            else:
                label _("Критерий Пирсона. Расчетный"):
                    style "confirm_prompt"
                    xalign 0.5
            if W_data == -1:
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
                        
            hbox:

                xalign 0.5
                spacing 100
                if sum_R_index_method4 != len(alts_methods4) + 1:
                    textbutton _("ввод") action Function(write_sum_R, table_input)
                elif r_index_method4 != len(alts_methods4) + 1:
                    textbutton _("ввод") action Function(write_r, table_input)
                elif W_data == -1:
                    textbutton _("ввод") action Function(write_W, table_input)
                elif not method4_sogl:
                    textbutton _("слабая") action VariableInputValue(method4_sogl, 1)
                    textbutton _("средняя") action VariableInputValue(method4_sogl, 2)
                    textbutton _("сильная") action VariableInputValue(method4_sogl, 3)
                else:
                    textbutton _("ввод") action Function(write_W, table_input)