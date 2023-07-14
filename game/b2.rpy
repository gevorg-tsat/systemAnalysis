define pareto_task1 = "Выбор лучшей альтернативы из множества Парето"

label b2kadr1:
    $ screens = ["check_pareto_table_answer", "butforwardback", "relevance_definition"]
    $ allow_forward = False
    $ xy_ev_al_table = [100, 225]
    $ xsize_ev_al_table = 800
    $ ysize_ev_al_table = 600
    show screen relevance_definition(pareto_task1)
    show screen check_pareto_table_answer
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
    method1_task1_valid_alternatives = list() #list(map(str.strip, google_sheet_data[1]["userEnteredValue"]["stringValue"].split(";")))
    criteries = list(map(str.strip, second_row_data[2]["userEnteredValue"]["stringValue"].split(";")))
    min_maxing_criteries = list(map(int,map(str.strip, third_row_data[2]["userEnteredValue"]["stringValue"].split(";"))))
    pareto_table=[]
    criteries_txt = ""
    alts_txt = ""
    is_correct_pareto_table_answer = None
    lbl_txt = ""
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
    
    def compare_line(line1, line2, min_maxing_criteries):
        # True - line1 if absolutely worser then line2
        is_better = False
        for k in range(len(line1)):
            if (line1[k] <= line2[k] and min_maxing_criteries[k]) or (line1[k] >= line2[k] and not min_maxing_criteries[k]):
                if (line1[k] < line2[k] and min_maxing_criteries[k]) or (line1[k] > line2[k] and not min_maxing_criteries[k]):
                    is_better = True
            else:
                return False
        return is_better


    def get_valid_alernatives(parreto_table, alternative, min_maxing_criteries):
        result = []
        for i in range(len(alternative)):
            is_valid = True
            for j in range(len(alternative)):
                if compare_line(parreto_table[i], parreto_table[j], min_maxing_criteries):
                    is_valid = False
            if is_valid:
                result.append(alternative[i])
        return result
                
    method1_task1_valid_alternatives = get_valid_alernatives(pareto_table, method1_task1_alternatives, min_maxing_criteries)
    
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
    
    def check_pareto_answ():
        global is_correct_pareto_table_answer
        global pareto_table_line_status
        global pareto_table
        global method1_task1_alternatives
        global method1_task1_valid_alternatives
        global allow_forward
        user_answer = []
        for i in range(len(pareto_table_line_status)):
            if not pareto_table_line_status[i]:
                user_answer.append(method1_task1_alternatives[i])
        if len(user_answer) == len(method1_task1_valid_alternatives) and set(user_answer) == set(method1_task1_valid_alternatives):
            is_correct_pareto_table_answer = True
            allow_forward = True
        else:
            is_correct_pareto_table_answer = False
        renpy.restart_interaction()
                



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

screen check_pareto_table_answer:
    zorder 100
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        vbox:
            spacing 30
            xalign .5
            yalign .5
            
            if is_correct_pareto_table_answer is not None:
                if is_correct_pareto_table_answer:
                    label _("[winner_text]"):
                        style "confirm_prompt"
                        xalign 0.5
                else:
                    label _("[loser_text]"):
                        style "confirm_prompt"
                        xalign 0.5
            if not allow_forward:
                textbutton _("Проверить") xalign 0.5 action Function(check_pareto_answ)
            
