label b3kadr1:
    $ screens = ["eval_alternative", "butforwardback", "ev_al_task1_input", "task1_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [50, 200]
    $ xsize_ev_al_table = 400
    $ ysize_ev_al_table = 400
    show screen goal_defenition(alts_methods3_txt)
    show screen butforwardback
    pause


init python:
    alts_methods3_txt = ""
    for i in range(len(method1_task1_valid_alternatives)):
        alts_methods3_txt += f"A{i+1} - {method1_task1_valid_alternatives[i]}, "
    alts_methods3_txt = alts_methods3_txt[:-2]
    experts_evals_google_data = json.loads(req.text)["sheets"][2]["data"][0]["rowData"]
    EXPERTS_COUNT = 3
    experts_evals = [[[0] * len(method1_task1_valid_alternatives)] * len(method1_task1_valid_alternatives)]*EXPERTS_COUNT

    for i in range(EXPERTS_COUNT):
        for j in range(len(method1_task1_valid_alternatives)):
            for k in range(len(method1_task1_valid_alternatives)):
                experts_evals[i][j][k] = float(experts_evals_google_data[j]["values"][i*EXPERTS_COUNT + j]["userEnteredValue"]["stringValue"])
    def kadrb3():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b3kadr{nkadr}"):
            return
        renpy.call(f"b3kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()


screen goal_defenition(text):
    text "Алгоритм парных сравнений для группы экспертов" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 150 xsize 1000 ysize 900

    #text "[alts_methods3_txt]" color "#000000" xpos 1100 ypos xy_ev_al_table[1] xsize 800 ysize 50*(len(criteries) + len(method1_task1_alternatives))
    for exp in range(EXPERTS_COUNT):
        for i in range(len(ev_al_task1_alternatives)):
            frame:
                text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
                xpos int(xy_ev_al_table[0] + (exp*(xsize_ev_al_table) + exp*30) + (i+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                ypos xy_ev_al_table[1]
                xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            frame:
                text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
                xpos xy_ev_al_table[0] + (exp*(xsize_ev_al_table) + exp*30)
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    # frame:
    #     text "Ci" color "#000000" xalign 0.5 yalign 0.5 
    #     xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 1))
    #     ypos xy_ev_al_table[1]
    #     xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    #     ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    # if C_index == len(ev_al_task1_alternatives) + 1:
    #     frame:
    #         text "Vi" color "#000000" xalign 0.5 yalign 0.5 
    #         xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 2))
    #         ypos xy_ev_al_table[1]
    #         xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    #         ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    # for i in range(len(ev_al_task1_alternatives)):
    #     for j in range(len(ev_al_task1_alternatives)):
    #         frame:
    #             xpos int(xy_ev_al_table[0] + (j+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
    #             ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
    #             xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    #             ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    #             if ev_al_task1_table_data[i][j] != 0:
    #                 text str(round(ev_al_task1_table_data[i][j], 2)) color "#000000" xalign 0.5 yalign 0.5
    #             elif i == j:
    #                 text "1" color "#000000" xalign 0.5 yalign 0.5
