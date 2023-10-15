define pareto_task1 = "Выбор лучшей альтернативы из множества Парето. Чтобы исключить альтернативу, нажми на номер строки"
define answer_input = VariableInputValue("table_input", returnable=True)
label b2kadr1:
    $ screens = ["check_pareto_table_answer", "butforwardback", "relevance_definition"]
    $ allow_forward = False
    $ xy_ev_al_table = [100, 225]
    $ xsize_ev_al_table = 800
    $ ysize_ev_al_table = 600
    if is_correct_pareto_table_answer:
        $ allow_forward = True
    show screen relevance_definition(pareto_task1)
    show screen check_pareto_table_answer
    show screen butforwardback
    pause

label b2kadr2:
    $ screens = ["scolar_method_input", "butforwardback", "scolar_method", "task2_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [100, 225]
    $ xsize_ev_al_table = 800
    $ ysize_ev_al_table = 600
    show screen scolar_method(pareto_task2)
    show screen scolar_method_input
    show screen butforwardback
    pause

init python:
    pareto_task2 = "Формирование обобщающего критерия Ki. Весовые коэффициенты i-о критерия: "
    # req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true&key={TOKEN}")
    table_input = ''
    show_error = False
    google_sheet_data = json.loads(req.text)["sheets"][1]["data"][row_number]["rowData"][1]["values"]
    second_row_data = json.loads(req.text)["sheets"][1]["data"][0]["rowData"][2]["values"]
    third_row_data = json.loads(req.text)["sheets"][1]["data"][0]["rowData"][3]["values"]
    second_sheet_data= json.loads(req.text)["sheets"][1]["data"]
    with open("/Users/gevorgtsaturyan/Downloads/system_analysis/game/log.txt","w") as fw:
        fw.write(str(google_sheet_data[0]))
    VARIANTS_AMOUNT = json.loads(req.text)["sheets"][1]["data"][row_number]["rowData"][0]["values"][0]["userEnteredValue"]["numberValue"]
    method1_task1_alternatives = list(map(str.strip, google_sheet_data[0]["userEnteredValue"]["stringValue"].split(";")))
    method1_task1_valid_alternatives = list() #list(map(str.strip, google_sheet_data[1]["userEnteredValue"]["stringValue"].split(";")))
    criteries = list(map(str.strip, second_row_data[2]["userEnteredValue"]["stringValue"].split(";")))
    min_maxing_criteries = list(map(int,map(str.strip, third_row_data[2]["userEnteredValue"]["stringValue"].split(";"))))
    alphas_task2 = list(map(float,map(str.strip, third_row_data[3]["userEnteredValue"]["stringValue"].split(";"))))
    for i in range(len(alphas_task2)):
        pareto_task2 += f"a{i+1} = {alphas_task2[i]}, "
    pareto_task2 = pareto_task2[:-2]
    pareto_table=[]
    criteries_txt = ""
    alts_txt = ""
    is_correct_pareto_table_answer = None
    K_index = 1
    R_index = 1
    rangs_method1 = [0] * len(method1_task1_alternatives)
    for i in range(len(criteries)):
        criteries_txt += f"{'максимизация' if min_maxing_criteries[i] else 'минимизация'} K{i+1} - {criteries[i]}\n"
    for i in range(len(method1_task1_alternatives)):
        alts_txt += f"A{i+1} - {method1_task1_alternatives[i]}\n"
    alts_txt = alts_txt + "\n" + criteries_txt
    for i in range(len(method1_task1_alternatives)):
        pareto_table.append(list())
        for j in range(len(criteries)):
            cell_data = second_sheet_data[0]["rowData"][4+i]["values"][j]["userEnteredValue"]["numberValue"]
            if not cell_data:
                raise Exception()
            pareto_table[i].append(cell_data)
    pareto_table_line_status = []
    for i in range(len(method1_task1_alternatives)):
        pareto_table_line_status.append(0)
    K_index_data = [-1] * len(method1_task1_alternatives)
    def init_K_index():
        global pareto_table_line_status
        global K_index
        global R_index
        K_index = 1
        while K_index - 1 < len(pareto_table_line_status) and pareto_table_line_status[K_index-1]:
            K_index+=1
        R_index = K_index
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

    def ranging(inp):
        global rangs_method1
        global R_index
        global allow_forward
        global table_input
        global b1_done
        global show_error
        K_sorted = K_index_data[:]
        K_sorted.sort(reverse=True)
        if not inp:
            return
        value = int(inp)
        table_input = ''
        if value != K_sorted.index(K_index_data[R_index-1]) + 1:
            show_error = True
            return
        show_error = False
        rangs_method1[R_index-1] = value
        R_index += 1
        while R_index - 1 < len(pareto_table_line_status) and pareto_table_line_status[R_index-1]:
            R_index+=1
        if R_index > len(pareto_table_line_status):
            allow_forward = True
            renpy.hide_screen("scolar_method_input")
            renpy.show_screen("task2_go_to_next")
            b1_done = True
        renpy.restart_interaction()

    def get_max_val_in_column(column_id, min_max):
        value = -1 if min_max == 1 else float('inf')
        comp = max if min_max == 1 else min
        for i in range(len(pareto_table)):
            if pareto_table_line_status[i] == 1:
                continue
            value = comp(pareto_table[i][column_id], value)
        return value

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
    
    def add_data_K_index(inp):
        global alphas_task2
        global K_index_data
        global pareto_table
        global K_index
        global table_input
        global show_error
        K_corr = 0
        if not inp:
            return
        data = float(inp)
        table_input = ''
        for i in range(len(pareto_table[K_index-1])):
            K_corr += alphas_task2[i] * ((pareto_table[K_index-1][i]/get_max_val_in_column(i, min_maxing_criteries[i])) ** (-1 if min_maxing_criteries[i] == 0 else 1))
        if round(data, 2) != round(K_corr, 2):
            show_error = True
            return
        K_index_data[K_index-1] = data
        K_index += 1
        while K_index - 1 < len(pareto_table_line_status) and pareto_table_line_status[K_index-1]:
            K_index+=1
        show_error = False
        renpy.restart_interaction()
        

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
        init_K_index()
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
                text str(pareto_table[i][j]) color "#000000" xalign 0.5 yalign 0.5 #pareto_table[i][j]
                xpos int(xy_ev_al_table[0]  + (j+1)*(xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                ypos int(xy_ev_al_table[1] + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(method1_task1_alternatives) + 1))
    for i in range(len(method1_task1_alternatives)):
        if pareto_table_line_status[i] == 1:
            image "kadr b14v" xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))*len(criteries) ypos int(xy_ev_al_table[1] + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)) + ysize_ev_al_table/len(method1_task1_alternatives)/4) xpos int(xy_ev_al_table[0] + (xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))
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
            

screen scolar_method(text):
    text "Формирование обобщающего критерия" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 100 xsize 1800 ysize 100


    #text "[ev_al_task1_info]" color "#000000" xpos 50 ypos 200 xsize 700 ysize 300
    #text "[ev_al_task1_alternatives_info]" color "#000000" xpos 50 ypos 500 xsize 700 ysize 300
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
    frame:
        text "Ki" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0]  + (len(criteries) + 1)*(xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))
        ypos int(xy_ev_al_table[1])
        xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))
        ysize int(ysize_ev_al_table/(len(method1_task1_alternatives) + 1))
    for i in range(len(method1_task1_alternatives)):
        for j in range(len(criteries)):
            frame:
                text str(pareto_table[i][j]) color "#000000" xalign 0.5 yalign 0.5 #pareto_table[i][j]
                xpos int(xy_ev_al_table[0]  + (j+1)*(xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                ypos int(xy_ev_al_table[1] + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(method1_task1_alternatives) + 1))
    for i in range(len(K_index_data)):
        if K_index_data[i] != -1:
            frame:
                text str(round(K_index_data[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
                xpos int(xy_ev_al_table[0] + (xsize_ev_al_table/(len(method1_task1_alternatives) + 1)) * (len(criteries)+1))
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    if K_index > len(method1_task1_alternatives):
        frame:
            text "Ri" color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0]  + (len(criteries) + 2)*(xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))
            ypos int(xy_ev_al_table[1])
            xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(method1_task1_alternatives) + 1))
        for i in range(len(rangs_method1)):
            if rangs_method1[i] != 0:
                frame:
                    text str(round(rangs_method1[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
                    xpos int(xy_ev_al_table[0] + (xsize_ev_al_table/(len(method1_task1_alternatives) + 1)) * (len(criteries)+2))
                    ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)))
                    xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                    ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    for i in range(len(method1_task1_alternatives)):
        if pareto_table_line_status[i] == 1:
            image "kadr b14v" xsize int(xsize_ev_al_table/(len(method1_task1_alternatives) + 1))*len(criteries) ypos int(xy_ev_al_table[1] + (i+1)*(ysize_ev_al_table/(len(method1_task1_alternatives) + 1)) + ysize_ev_al_table/len(method1_task1_alternatives)/4) xpos int(xy_ev_al_table[0] + (xsize_ev_al_table/(len(method1_task1_alternatives) + 1)))

screen scolar_method_input:
    zorder 100
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 30
            if K_index <= len(method1_task1_alternatives):
                label _("K{size=-10}[K_index]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            else:
                label _("R{size=-10}[R_index]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            input:
                default "None"
                color "#000000"
                value answer_input
                xalign 0.5
                length 8
                if K_index <= len(method1_task1_alternatives):
                    allow "0123456789."
                else:
                    allow "0123456789"
                size 24
                        
            hbox:

                xalign 0.5
                spacing 100
                if K_index != len(method1_task1_alternatives) + 1:
                    textbutton _("ввод") action Function(add_data_K_index, table_input)
                else:
                    textbutton _("ввод") action Function(ranging, table_input)
    if show_error:
        text "Ошибка" xpos 1560 ypos 1030  color '#000000'
