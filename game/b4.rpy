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
    sum_R_values = list()
    r_values = list()
    for i in range(len(alts_methods4)):
        ranging_method4_table.append(list())
        for j in range(EXPERTS_COUNT_METHOD4):
            ranging_method4_table[i].append(int(ranging_method4_google_data[i]["values"][j]["userEnteredValue"]["numberValue"]))
    alts_methods4_txt = ""
    for i in range(len(alts_methods4)):
        alts_methods4_txt += f"A{i+1} - {alts_methods4[i]}, "
    alts_methods4_txt = alts_methods4_txt[:-2]

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
            else:
                label _("W"):
                    style "confirm_prompt"
                    xalign 0.5
            input:
                default "None"
                color "#000000"
                value VariableInputValue("table_input", returnable=True)
                xalign 0.5
                length 8
                if r_index_method4 != len(alts_methods4) + 1 and sum_R_index_method4 == len(alts_methods4) + 1:
                    allow "123456789"
                else:
                    allow "0123456789."
                size 24
                        
            hbox:

                xalign 0.5
                spacing 100
                if C_index_method3 != len(method1_task1_valid_alternatives) + 1:
                    textbutton _("ввод") action Function(rewrite_table_method3_C, table_input)
                elif V_index_method3 != len(method1_task1_valid_alternatives) + 1:
                    textbutton _("ввод") action Function(rewrite_table_method3_V, table_input)
                else:
                    textbutton _("ввод") action Function(rewrite_table_method3_R, table_input)