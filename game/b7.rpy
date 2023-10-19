default table_input = ""
init python:
    show_error = False
    row_number = 0
    ev_al_task1_label = "Представьте себя в роли эксперта, рассматривающие альтернативы. Вам надо сравнить их между собой и дать оценку. Для этого необходимо заполнить таблицу, рекомендуется это делать следующим образом:"
    ev_al_task1_info = "Ставь:\n1, если A{size=-10}i{/size} и A{size=-10}j{/size} примерно равноценны\n3 - A{size=-10}i{/size} немного предпочтительнее A{size=-10}j{/size}\n5 - A{size=-10}i{/size} предпочтительнее A{size=-10}j{/size}\n7 - A{size=-10}i{/size} значительно предпочтительнее A{size=-10}j{/size}\n9 - A{size=-10}i{/size} явно предпочтительнее A{size=-10}j{/size}"
    ev_al_task1_info += "\nМожно ставить промежуточные баллы. И обратные(0.2, 0.33 и тд)"
    ev_al_task1_alternatives = method1_task1_alternatives[:]
    ev_al_task1_alternatives_info = "Альтерантивы:"
    ev_al_task2_label = "Теперь необходимо провести обработку этих данных. Для каждой строки матрицы попарных сравнений определяется цена альтернативы Ci - среднее геометрическое строки матрицы. Определяется сумма цен альтернатив: C = ΣCi. Определяется вес каждой альтернативы: Vi = Ci/C, i=1,...,N"
    ev_al_task3_label = "Проверка позволяет выявить ошибки, которые мог допустить эксперт при заполнении матрицы парных сравнений. Рассчитывается вспомогательная величина I путем суммирования произведений сумм столбцов матрицы на веса альтернатив. Находится величина, называемая индексом согласованности ИС = (I-N)/(N-1). Отношение согласованности: ОС = ИС / СлС. Если оно превышает 0,2, то допушена экспертная ошибка."
    fir = 1
    sec = 2
    C_index = 1
    V_index = 1
    I_value = None
    IS_value = None
    OS_value = None
    b2_task_number = 1
    rangs_method2 = [0] * len(method1_task1_alternatives)
    R_index_method2 = 1
    for i in range(len(ev_al_task1_alternatives)):
        ev_al_task1_alternatives_info += f"\nA{i+1} - {ev_al_task1_alternatives[i]}"
    # init table
    ev_al_task1_table_data = [[0 for _ in range(len(ev_al_task1_alternatives))] for _ in range(len(ev_al_task1_alternatives))]
    ev_al_task2_C_index_data = list()
    ev_al_task2_V_index_data = list()
    sls_info_table = [0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
    #ev_al_task1_correct_answers = list(map(str.strip, google_sheet_data[1]["userEnteredValue"]["stringValue"].split(";")))
    
    def ranging_b2(inp):
        global rangs_method2
        global R_index_method2
        global allow_forward
        global table_input
        global show_error
        global statistics
        global b2_task_number
        statistics.append([your_name, f"b2_{b2_task_number}", f"{datetime.datetime.now()}"])
        V_sorted = ev_al_task2_V_index_data[:]
        V_sorted.sort(reverse=True)
        if not inp:
            return
        value = int(inp)
        table_input = ''
        if value != V_sorted.index(ev_al_task2_V_index_data[R_index_method2-1]) + 1:
            show_error = True
            return
        b2_task_number += 1
        show_error = False
        rangs_method2[R_index_method2-1] = value
        R_index_method2 += 1
        if R_index_method2 > len(ev_al_task1_alternatives):
            allow_forward = True
            renpy.hide_screen("ev_al_task2_input")
            renpy.show_screen("task2_go_to_next")
        renpy.restart_interaction()
    
    def geom_mean(myList):
        result = 1
        for x in myList:
            result = result * x
        return result**(1/len(myList))
    def get_I_value(table, V_table):
        result = 0
        for i in range(len(table)):
            sum_var = 0
            for j in range(len(table)):
                sum_var += table[j][i]
            result += (sum_var * V_table[i])
        return result
    def kadrb7():
        global nkadr
        global vkadr
        global screens
        write_score()
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b7kadr{nkadr}"):
            renpy.call("startgame")
            return
        renpy.call(f"b7kadr{nkadr}")
        #renpy.with_statement(fade)
        renpy.pause()
    def rewrite_table(inp):
        global fir
        global sec
        global allow_forward
        global table_input
        global statistics
        global b2_task_number
        statistics.append([your_name, f"b2_{b2_task_number}", f"{datetime.datetime.now()}"])
        if not inp:
            return
        b2_task_number += 1
        value = float(inp)
        table_input = ''
        global ev_al_task1_table_data
        ev_al_task1_table_data[fir-1][sec-1] = value
        ev_al_task1_table_data[sec-1][fir-1] = 1/value
        if sec == (len(ev_al_task1_alternatives)):
            fir += 1
            sec = fir
        else:
            sec += 1
        if sec == fir:
            ev_al_task1_table_data[fir-1][sec-1] = 1
            sec+=1
        if sec == len(ev_al_task1_alternatives) + 1:
            allow_forward = True
            renpy.hide_screen("ev_al_task1_input")
            renpy.show_screen("task1_go_to_next")
        renpy.restart_interaction()
    def rewrite_table_task2(inp):
        global statistics
        global b2_task_number
        statistics.append([your_name, f"b2_{b2_task_number}", f"{datetime.datetime.now()}"])
        global show_error
        global table_input
        global C_index
        global allow_forward
        if not inp:
            return
        value = float(inp)
        table_input = ''
        global ev_al_task2_C_index_data
        global ev_al_task1_table_data
        if round(geom_mean(ev_al_task1_table_data[C_index-1]), 2) != round(value,2):
            show_error = True
            return
        b2_task_number += 1
        show_error = False
        ev_al_task2_C_index_data.append(value)
        C_index+=1
        
            # renpy.show_screen("task1_go_to_next")
        renpy.restart_interaction()
    
    def rewrite_table_task2_V(inp):
        global statistics
        global b2_task_number
        statistics.append([your_name, f"b2_{b2_task_number}", f"{datetime.datetime.now()}"])
        global show_error
        global V_index
        global allow_forward
        global table_input
        if not inp:
            return
        value = float(inp)
        table_input = ''
        global ev_al_task2_C_index_data
        global ev_al_task2_V_index_data
        global ev_al_task1_table_data
        if round(ev_al_task2_C_index_data[V_index-1]/sum(ev_al_task2_C_index_data), 2) != round(value,2):
            show_error = True
            return
        b2_task_number += 1
        ev_al_task2_V_index_data.append(value)
        V_index+=1
        show_error = False
        renpy.restart_interaction()
    
    def rewrite_data_task3(inp):
        global show_error
        global table_input
        global I_value
        global IS_value
        global OS_value
        global ev_al_task2_V_index_data
        global ev_al_task1_table_data
        global statistics
        global b2_task_number
        statistics.append([your_name, f"b2_{b2_task_number}", f"{datetime.datetime.now()}"])
        if not inp:
            return
        value = float(inp)
        table_input = ''
        if I_value is None:
            I_correct = get_I_value(ev_al_task1_table_data, ev_al_task2_V_index_data)
            if round(value, 2) != round(I_correct, 2):
                show_error = True
                return
            I_value = value
            b2_task_number += 1
            show_error = False
            renpy.restart_interaction()
            return
        if IS_value is None:
            IS_correct = ((I_value - len(ev_al_task1_alternatives))/ (len(ev_al_task1_alternatives) - 1))
            if round(value, 2) != round(IS_correct, 2):
                show_error = True
                return
            b2_task_number +=1
            IS_value = value
            show_error = False
            renpy.restart_interaction()
            return
        if OS_value is None:
            OS_correct = (IS_value)/(sls_info_table[len(ev_al_task1_alternatives) - 3])
            if round(value, 2) != round(OS_correct, 2):
                show_error = True
                return
            b2_task_number += 1
            OS_value = value
            show_error = False
            renpy.show_screen("eval_trueness_of_expert")
            renpy.hide_screen("ev_al_task3_input")
            renpy.restart_interaction()
    def check_sogl(sogl):
        global OS_value
        global b2_done
        global allow_forward
        global show_error
        global statistics
        global b2_task_number
        statistics.append([your_name, f"b2_{b2_task_number}", f"{datetime.datetime.now()}"])
        if (sogl and OS_value <=0.2) or (sogl == False and OS_value > 0.2):
            text = "Верно! Поздравляю! переходи вперед, в меню"
            b2_done = True
            allow_forward = True
            b2_task_number += 1
            renpy.hide_screen("eval_trueness_of_expert")
            renpy.show_screen("final_go_to_next", text)
        else:
            show_error = True
        renpy.restart_interaction()

    

label b7kadr1:
    $ screens = ["eval_alternative", "butforwardback", "ev_al_task1_input", "task1_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [800, 200]
    $ xsize_ev_al_table = 800
    $ ysize_ev_al_table = 600
    $ ev_al_task1_table_data[0][0] = 1
    show screen eval_alternative(ev_al_task1_label)
    if fir == len(ev_al_task1_alternatives) and sec == len(ev_al_task1_alternatives) + 1:
        hide screen ev_al_task1_input
        $ allow_forward = True
    else:
        show screen ev_al_task1_input
    show screen butforwardback
    pause

label b7kadr2:
    $ screens = ["check_exp_eval", "butforwardback", "ev_al_task2_input", "task2_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [30, 225]
    $ xsize_ev_al_table = 800
    $ ysize_ev_al_table = 600
    show screen check_exp_eval(ev_al_task2_label)
    if V_index != len(ev_al_task1_alternatives) + 1:
        show screen ev_al_task2_input
    else:
        $ allow_forward = True
        show screen task2_go_to_next
    show screen butforwardback
    pause

label b7kadr3:
    $ screens = ["check_sls_eval", "butforwardback", "ev_al_task3_input","final_go_to_next" , "eval_trueness_of_expert"]
    $ allow_forward = False
    $ xy_ev_al_table = [30, 225]
    $ xsize_ev_al_table = 750
    $ ysize_ev_al_table = 600
    $ xy_sls_info = [1200, 225]
    $ xsize_sls_info = 700
    $ ysize_sls_info = 200
    show screen check_sls_eval(ev_al_task3_label)
    if OS_value is None:
        show screen ev_al_task3_input
    else:
        $ allow_forward = True
    show screen butforwardback
    pause



    
        

screen eval_alternative(text):
    text "Оценка альтернатив" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 100 xsize 1800 ysize 100
    text "[ev_al_task1_info]" color "#000000" xpos 50 ypos 200 xsize 700 ysize 300
    text "[ev_al_task1_alternatives_info]" color "#000000" xpos 50 ypos 500 xsize 700 ysize 300
    frame:
        xpos xy_ev_al_table[0]
        ypos xy_ev_al_table[1]
        xsize xsize_ev_al_table
        ysize ysize_ev_al_table
    for i in range(len(ev_al_task1_alternatives)):
        frame:
            text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + (i+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
        frame:
            text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos xy_ev_al_table[0] 
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    for i in range(len(ev_al_task1_alternatives)):
        for j in range(len(ev_al_task1_alternatives)):
            frame:
                xpos int(xy_ev_al_table[0] + (j+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                if sec - 1 == j and fir - 1 == i:
                    background "#FFA12B"
                if ev_al_task1_table_data[i][j] != 0:
                    text str(round(ev_al_task1_table_data[i][j], 2)) color "#000000" xalign 0.5 yalign 0.5
                elif i == j:
                    text "1" color "#000000" xalign 0.5 yalign 0.5
screen ev_al_task1_input:
    zorder 100
    frame:
        xpos 50 ypos 800
        xsize 500 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 30
            
            label _("A{size=-10}[fir][sec]{/size}"):
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

                textbutton _("ввод") action Function(rewrite_table, table_input)
    if show_error:
        text "Ошибка" xpos 1560 ypos 1030  color '#000000'    
                
                # input default "":
                #     color "#000000"
                #     value VariableInputValue(f"ev_al_task1_table_data[{i}{j}]")
                #     length 8
                #     allow "0123456789"
                #     size 20
screen task1_go_to_next:
    frame:
        xpos 50 ypos 800
        xsize 500 ysize 200
        text "Ты заполнил(-а) таблицу, можешь двигаться дальше ->"color "#000000" 


screen check_exp_eval(text):
    text "Обработка оценки эксперта" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 100 xsize 1800 ysize 100


    #text "[ev_al_task1_info]" color "#000000" xpos 50 ypos 200 xsize 700 ysize 300
    #text "[ev_al_task1_alternatives_info]" color "#000000" xpos 50 ypos 500 xsize 700 ysize 300
    frame:
        xpos xy_ev_al_table[0]
        ypos xy_ev_al_table[1]
        xsize xsize_ev_al_table
        ysize ysize_ev_al_table
    for i in range(len(ev_al_task1_alternatives)):
        frame:
            text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + (i+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
        frame:
            text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos xy_ev_al_table[0] 
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    frame:
        text "Ci" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 1))
        ypos xy_ev_al_table[1]
        xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
        ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    if C_index == len(ev_al_task1_alternatives) + 1:
        frame:
            text "Vi" color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 2))
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    if V_index == len(ev_al_task1_alternatives) + 1:
        frame:
            text "Ri" color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 3))
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    for i in range(len(ev_al_task1_alternatives)):
        for j in range(len(ev_al_task1_alternatives)):
            frame:
                xpos int(xy_ev_al_table[0] + (j+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                if ev_al_task1_table_data[i][j] != 0:
                    text str(round(ev_al_task1_table_data[i][j], 2)) color "#000000" xalign 0.5 yalign 0.5
                elif i == j:
                    text "1" color "#000000" xalign 0.5 yalign 0.5
    for i in range(len(ev_al_task2_C_index_data)):
        frame:
            text str(round(ev_al_task2_C_index_data[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 1))
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))

    for i in range(len(ev_al_task2_V_index_data)):
        frame:
            text str(round(ev_al_task2_V_index_data[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 2))
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    for i in range(R_index_method2-1):
        frame:
            text str(round(rangs_method2[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 3))
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))


screen ev_al_task2_input:
    zorder 100
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 30
            if C_index != len(ev_al_task1_alternatives) + 1:
                label _("C{size=-10}[C_index]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            elif V_index != len(ev_al_task1_alternatives) + 1:
                label _("V{size=-10}[V_index]{/size}"):
                    style "confirm_prompt"
                    xalign 0.5
            else:
                label _("R{size=-10}[V_index]{/size}"):
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
                if C_index != len(ev_al_task1_alternatives) + 1:
                    textbutton _("ввод") action Function(rewrite_table_task2, table_input)
                elif V_index != len(ev_al_task1_alternatives) + 1:
                    textbutton _("ввод") action Function(rewrite_table_task2_V, table_input)
                else:
                    textbutton _("ввод") action Function(ranging_b2, table_input)
    if show_error:
        text "Ошибка" xpos 1560 ypos 1030  color '#000000'

screen task2_go_to_next:
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        text "Ты заполнил(-а) таблицу, можешь двигаться дальше ->"color "#000000" 

screen check_sls_eval(text):
    text "Проверка экспертных оценок на противоречивость" color "#000000" xpos 40 ypos 20 xsize 1920 ysize 50 size 50
    text "[text]"  color "#000000" xpos 50 ypos 80 xsize 1800 ysize 100


    #text "[ev_al_task1_info]" color "#000000" xpos 50 ypos 200 xsize 700 ysize 300
    #text "[ev_al_task1_alternatives_info]" color "#000000" xpos 50 ypos 500 xsize 700 ysize 300
    frame:
        xpos xy_ev_al_table[0]
        ypos xy_ev_al_table[1]
        xsize xsize_ev_al_table
        ysize ysize_ev_al_table
    for i in range(len(ev_al_task1_alternatives)):
        frame:
            text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + (i+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            ypos xy_ev_al_table[1]
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
        frame:
            text "A" + str(i+1) color "#000000" xalign 0.5 yalign 0.5 
            xpos xy_ev_al_table[0] 
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    frame:
        text "Ci" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 1))
        ypos xy_ev_al_table[1]
        xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
        ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    frame:
        text "Vi" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 2))
        ypos xy_ev_al_table[1]
        xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
        ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    frame:
        text "Ri" color "#000000" xalign 0.5 yalign 0.5 
        xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 3))
        ypos xy_ev_al_table[1]
        xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
        ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    for i in range(len(ev_al_task1_alternatives)):
        for j in range(len(ev_al_task1_alternatives)):
            frame:
                xpos int(xy_ev_al_table[0] + (j+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                if ev_al_task1_table_data[i][j] != 0:
                    text str(round(ev_al_task1_table_data[i][j], 2)) color "#000000" xalign 0.5 yalign 0.5
                elif i == j:
                    text "1" color "#000000" xalign 0.5 yalign 0.5
    for i in range(len(ev_al_task2_C_index_data)):
        frame:
            text str(round(ev_al_task2_C_index_data[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 1))
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))

    for i in range(len(ev_al_task2_V_index_data)):
        frame:
            text str(round(ev_al_task2_V_index_data[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 2))
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    for i in range(len(ev_al_task2_V_index_data)):
        frame:
            text str(round(rangs_method2[i], 2)) color "#000000" xalign 0.5 yalign 0.5 
            xpos int(xy_ev_al_table[0] + int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)) * (len(ev_al_task1_alternatives) + 3))
            ypos int(xy_ev_al_table[1]  + (i+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
            xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
            ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
    frame:
        xpos xy_sls_info[0]
        ypos xy_sls_info[1]
        xsize int(xsize_sls_info/(len(sls_info_table) + 1))
        ysize int(ysize_sls_info/2)
        text "N" color "#000000" xalign 0.5 yalign 0.5
    frame:
        xpos xy_sls_info[0]
        ypos int(xy_sls_info[1] + ysize_sls_info/2)
        xsize int(xsize_sls_info/(len(sls_info_table) + 1))
        ysize int(ysize_sls_info/2)
        text "SLS" color "#000000" xalign 0.5 yalign 0.5
    for i in range(len(sls_info_table)):
        frame:
            text str(i+3) color "#000000" xalign 0.5 yalign 0.5
            xpos int(xy_sls_info[0] + (i+1)*(xsize_sls_info/(len(sls_info_table) + 1)))
            ypos xy_sls_info[1]
            xsize int(xsize_sls_info/(len(sls_info_table) + 1))
            ysize int(ysize_sls_info/2)
        frame:
            text str(sls_info_table[i]) color "#000000" xalign 0.5 yalign 0.5
            xpos int(xy_sls_info[0] + (i+1)*(xsize_sls_info/(len(sls_info_table) + 1)))
            ypos int(xy_sls_info[1] + ysize_sls_info/2)
            xsize int(xsize_sls_info/(len(sls_info_table) + 1))
            ysize int(ysize_sls_info/2)
    if I_value is not None:
        frame:
            xpos xy_sls_info[0]
            ypos int(xy_sls_info[1] + ysize_sls_info)
            xsize int(2*xsize_sls_info/(len(sls_info_table) + 1))
            ysize int(ysize_sls_info/2)
            text "I = " + str(round(I_value, 2)) color "#000000" xalign 0.5 yalign 0.5
    if IS_value is not None:
        frame:
            xpos xy_sls_info[0]
            ypos int(xy_sls_info[1] + 1.5*ysize_sls_info)
            xsize int(2*xsize_sls_info/(len(sls_info_table) + 1))
            ysize int(ysize_sls_info/2)
            text "ИС = " + str(round(IS_value, 2)) color "#000000" xalign 0.5 yalign 0.5
    if OS_value is not None:
        frame:
            xpos xy_sls_info[0]
            ypos int(xy_sls_info[1] + 2*ysize_sls_info)
            xsize int(2*xsize_sls_info/(len(sls_info_table) + 1))
            ysize int(ysize_sls_info/2)
            text "ОС = " + str(round(OS_value, 2)) color "#000000" xalign 0.5 yalign 0.5
    

    


screen ev_al_task3_input:
    zorder 100
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 30
            if I_value is None:
                label _("Величина I"):
                    style "confirm_prompt"
                    xalign 0.5
            elif IS_value is None:
                label _("Величина ИС"):
                    style "confirm_prompt"
                    xalign 0.5
            elif OS_value is None:
                label _("Величина ОС"):
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
                textbutton _("ввод") action Function(rewrite_data_task3, table_input)
    if show_error:
        text "Ошибка" xpos 1560 ypos 1030  color '#000000'
screen eval_trueness_of_expert:
    zorder 100
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _("Отношение"):
                    style "confirm_prompt"
                    xalign 0.5
            
            textbutton _("согласовано") xalign 0.5 action Function(check_sogl, True) 
            textbutton _("не согласовано") xalign 0.5 action Function(check_sogl, False)
    if show_error:
        text "Ошибка" xpos 1560 ypos 1030  color '#000000'

screen final_go_to_next(text):
    frame:
        xpos 1450 ypos 800
        xsize 400 ysize 200
        text "[text]" color "#000000" 