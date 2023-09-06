label b3kadr1:
    $ screens = ["goal_defenition", "butforwardback", "method3_input", "method3_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [50, 400]
    $ xsize_ev_al_table = 400
    $ ysize_ev_al_table = 400
    show screen goal_defenition(alts_methods3_txt)
    show screen method3_input
    show screen butforwardback
    pause


init python:
    req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true&key={TOKEN}")
    alts_methods3_txt = ""
    show_error = False
    for i in range(len(method1_task1_valid_alternatives)):
        alts_methods3_txt += f"A{i+1} - {method1_task1_valid_alternatives[i]}, "
    alts_methods3_txt = alts_methods3_txt[:-2] + ". Каждый эксперт независимо от других заполнил все ячейки матрицы попарных сравнений в соответствии с правилами сравнения. Определить обобщенные оценки предпочтения альтернатив над другими, вес каждой альтернативы и ранжировать в зависимости от полученных значений весов."
    experts_evals_google_data = json.loads(req.text)["sheets"][2]["data"][0]["rowData"]
    EXPERTS_COUNT = 3
    experts_evals = list()
    C_index_method3 = 1
    V_index_method3 = 1
    C_values_method3 = list()
    V_values_method3 = list()
    R_method3 = 1
    R_values_method3 = list()
    for i in range(EXPERTS_COUNT):
        experts_evals.append(list())
        for j in range(len(method1_task1_valid_alternatives)):
            experts_evals[i].append(list())
            for k in range(len(method1_task1_valid_alternatives)):
                experts_evals[i][j].append(float(experts_evals_google_data[j]["values"][i*EXPERTS_COUNT + k]["userEnteredValue"]["stringValue"]))
    def kadrb3():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b3kadr{nkadr}"):
            renpy.call("startgame")
            return
        renpy.call(f"b3kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()
    def sum_all_exps(C_index_method3):
        global experts_evals
        global EXPERTS_COUNT
        res = 0
        for exp in range(EXPERTS_COUNT):
            for i in range(len(experts_evals[exp][C_index_method3-1])):
                res += experts_evals[exp][C_index_method3-1][i]
        return res

    def rewrite_table_method3_C(inp):
        global show_error
        global C_index_method3
        global allow_forward
        global table_input
        if not inp:
            return
        value = float(inp)
        table_input = ''
        global C_values_method3
        global experts_evals
        if abs(sum_all_exps(C_index_method3) - value) > 0.1:
            show_error = True
            return
        C_values_method3.append(value)
        C_index_method3+=1
        show_error = False
            # renpy.show_screen("task1_go_to_next")
        renpy.restart_interaction()
    
    def rewrite_table_method3_V(inp):
        global show_error
        global V_index_method3
        global allow_forward
        global table_input
        if not inp:
            return
        value = float(inp)
        table_input = ''
        global C_values_method3
        global V_values_method3
        if abs(C_values_method3[V_index_method3-1]/sum(C_values_method3) - value) > 0.05:
            show_error = True
            return
        V_values_method3.append(value)
        show_error = False
        V_index_method3 += 1
        renpy.restart_interaction()

    def rewrite_table_method3_R(inp):
        global show_error
        global R_values_method3
        global R_method3
        global allow_forward
        global table_input
        if not inp:
            return
        try:
            value = int(inp)
        except:
            show_error = True
            return
        table_input = ''
        if value == 0:
            show_error = True
            return
        R_values_method3.append(value)
        R_method3 += 1
        show_error = False
        if R_method3 == len(method1_task1_valid_alternatives) + 1:
            allow_forward = True
            renpy.hide_screen("method3_input")
            renpy.show_screen("method3_go_to_next")
        renpy.restart_interaction()


screen goal_defenition(text):
    text "Алгоритм парных сравнений для группы экспертов" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 150 xsize 1000 ysize 900

    #text "[alts_methods3_txt]" color "#000000" xpos 1100 ypos xy_ev_al_table[1] xsize 800 ysize 50*(len(criteries) + len(method1_task1_alternatives))
    for exp in range(EXPERTS_COUNT):
        for i in range(len(method1_task1_valid_alternatives)):
            frame:
                text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
                xpos int(xy_ev_al_table[0] + (exp*(xsize_ev_al_table) + exp*30) + (i+1)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1)))
                ypos xy_ev_al_table[1]
                xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
            frame:
                text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
                xpos xy_ev_al_table[0] + (exp*(xsize_ev_al_table) + exp*30)
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
    for exp in range(EXPERTS_COUNT):
        for i in range(len(method1_task1_valid_alternatives)):
            for j in range(len(method1_task1_valid_alternatives)):
                frame:
                    text str(experts_evals[exp][i][j]) color "#000000" xalign 0.5 yalign 0.5 size 25
                    xpos int(xy_ev_al_table[0] + (exp*(xsize_ev_al_table) + exp*30) + (j+1)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1)))
                    ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1)))
                    xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
                    ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
    frame:
        text "Ci" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0] + ((EXPERTS_COUNT-1)*(xsize_ev_al_table) + (EXPERTS_COUNT-1)*30) + (len(method1_task1_valid_alternatives)+1)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))) + 30
        ypos xy_ev_al_table[1]
        xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
        ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
    for i in range(len(C_values_method3)):
        frame:
            text str(C_values_method3[i]) color "#000000" xalign 0.5 yalign 0.5 size 25
            xpos int(xy_ev_al_table[0] + ((EXPERTS_COUNT-1)*(xsize_ev_al_table) + (EXPERTS_COUNT-1)*30) + (len(method1_task1_valid_alternatives)+1)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))) + 30
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
    if C_index_method3 == len(method1_task1_valid_alternatives) + 1:
        frame:
            text "Vi" color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + ((EXPERTS_COUNT-1)*(xsize_ev_al_table) + (EXPERTS_COUNT-1)*30) + (len(method1_task1_valid_alternatives)+2)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))) + 30
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
        for i in range(len(V_values_method3)):
            frame:
                text str(V_values_method3[i]) color "#000000" xalign 0.5 yalign 0.5 size 25
                xpos int(xy_ev_al_table[0] + ((EXPERTS_COUNT-1)*(xsize_ev_al_table) + (EXPERTS_COUNT-1)*30) + (len(method1_task1_valid_alternatives)+2)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))) + 30
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
    if V_index_method3 == len(method1_task1_valid_alternatives) + 1:
        frame:
            text "Ri" color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + ((EXPERTS_COUNT-1)*(xsize_ev_al_table) + (EXPERTS_COUNT-1)*30) + (len(method1_task1_valid_alternatives)+3)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))) + 30
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
        for i in range(len(R_values_method3)):
            frame:
                text str(R_values_method3[i]) color "#000000" xalign 0.5 yalign 0.5 size 25
                xpos int(xy_ev_al_table[0] + ((EXPERTS_COUNT-1)*(xsize_ev_al_table) + (EXPERTS_COUNT-1)*30) + (len(method1_task1_valid_alternatives)+3)*(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))) + 30
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(method1_task1_valid_alternatives) + 1))




screen method3_input:
    zorder 100
    frame:
        xpos 1450 ypos 810
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 30
            if C_index_method3 != len(method1_task1_valid_alternatives) + 1:
                label _("C{size=-10}[C_index_method3]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            elif V_index_method3 != len(method1_task1_valid_alternatives) + 1:
                label _("V{size=-10}[V_index_method3]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            else:
                label _("R{size=-10}[R_method3]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5

            input:
                default "None"
                color "#000000"
                value VariableInputValue("table_input", returnable=True)
                xalign 0.5
                length 8
                if V_index_method3 == len(method1_task1_valid_alternatives) + 1 and C_index_method3 == len(method1_task1_valid_alternatives) + 1:
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
    if show_error:
        text "Ошибка" xpos 1560 ypos 1030  color '#000000'

screen method3_go_to_next:
    frame:
        xpos 1450 ypos 810
        xsize 400 ysize 200
        text "Ты заполнил(-а) таблицу, можешь двигаться дальше ->"color "#000000" 