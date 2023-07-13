define pareto_task1 = "Выбор лучшей альтернативы из множества Парето"

label b2kadr1:
    $ screens = ["check_exp_eval", "butforwardback", "ev_al_task2_input"]
    $ allow_forward = False
    $ xy_ev_al_table = [100, 225]
    $ xsize_ev_al_table = 800
    $ ysize_ev_al_table = 600
    show screen relevance_definition(pareto_task1)
    show screen butforwardback
    pause


init python:
    req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true&key={TOKEN}")
    # TODO дергает ручку с гугл таблицы
    google_sheet_data = json.loads(req.text)["sheets"][1]["data"][row_number]["rowData"][0]["values"]
    second_row_data = json.loads(req.text)["sheets"][1]["data"][0]["rowData"][1]["values"]
    third_row_data = json.loads(req.text)["sheets"][1]["data"][0]["rowData"][2]["values"]
    second_sheet_data= json.loads(req.text)["sheets"][1]["data"]
    method1_task1_alternatives = list(map(str.strip, google_sheet_data[0]["userEnteredValue"]["stringValue"].split(";")))
    method1_task1_valid_alternatives = list(map(str.strip, google_sheet_data[1]["userEnteredValue"]["stringValue"].split(";")))
    criteries = list(map(str.strip, second_row_data[2]["userEnteredValue"]["stringValue"].split(";")))
    min_maxing_criteries = list(map(int,map(str.strip, third_row_data[2]["userEnteredValue"]["stringValue"].split(";"))))
    pareto_table=[]
    criteries_txt = ""
    alts_txt = ""
    for i in range(len(criteries)):
        criteries_txt += f"{'максимизация' if min_maxing_criteries[i] else 'минимизация'} K{i+1} - {criteries[i]}\n"
    for i in range(len(method1_task1_alternatives)):
        alts_txt += f"A{i+1} - {method1_task1_alternatives[i]}\n"
    alts_txt = alts_txt + "\n" + criteries_txt
    for i in range(len(method1_task1_alternatives)):
        pareto_table.append(list())
        for j in range(len(criteries)):
            cell_data = second_sheet_data[0]["rowData"][3+i]["values"][j]["userEnteredValue"]["numberValue"]
            if not cell_data:
                raise Exception()
            pareto_table[i].append(cell_data)
    pareto_table_line_status = []
    for i in range(len(method1_task1_alternatives)):
        pareto_table_line_status.append(0)
    def kadrb2():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b2kadr{nkadr}"):
            renpy.call("startgame")
            return
        renpy.call(f"b2kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()
    def strikeout(number):
        global pareto_table_line_status
        if pareto_table_line_status[number]:
            pareto_table_line_status[number]= 0
        else:
            pareto_table_line_status[number] = 1
        renpy.restart_interaction()
        return


screen relevance_definition(task):
    text "Метод скаляризации" color "#000000" xpos 40 ypos 10 xsize 1920 ysize 50 size 80
    text "[task]"  color "#000000" xpos 40 ypos 100 xsize 1000 ysize 900
    text "[alts_txt]" color "#000000" xpos 1100 ypos xy_ev_al_table[1] xsize 800 ysize 50*(len(criteries) + len(method1_task1_alternatives))
    zorder 100
    for i in range(len(method1_task1_alternatives)):
        frame:
            textbutton _("A" + str(i+1)) xalign 0.5 yalign 0.5 action Function(strikeout, int(i)) 
            xpos xy_ev_al_table[0] 
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(method1_task1_alternatives) + 1))
    for i in range(len(criteries)):
        frame:
            text "k" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0]  + (i+1)*(xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))
            ypos int(xy_ev_al_table[1])
            xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(method1_task1_alternatives) + 1))
    for i in range(len(method1_task1_alternatives)):
        for j in range(len(criteries)):
            frame:
                if pareto_table_line_status[i] == 1:
                    image "kadr b14v" xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1)) ypos 0.2
                else:
                    text str(pareto_table[i][j]) color "#000000" xalign 0.5 yalign 0.5 #pareto_table[i][j]
                xpos int(xy_ev_al_table[0]  + (j+1)*(xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                ypos int(xy_ev_al_table[1] + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(method1_task1_alternatives) + 1))
    
