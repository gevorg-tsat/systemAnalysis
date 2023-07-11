default table_input = ""
init python:
    req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true&key={TOKEN}")
    # TODO дергает ручку с гугл таблицы
    row_number = 0
    google_sheet_data = json.loads(req.text)["sheets"][1]["data"][row_number]["rowData"][0]["values"]
    ev_al_task1_label = "Представьте себя в роли эксперта, рассматривающие альтернативы. Вам надо сравнить их между собой и дать оценку. Для этого необходимо заполнить таблицу, рекомендуется это делать следующим образом:"
    ev_al_task1_info = "Ставь:\n1, если A{size=-10}i{/size} и A{size=-10}j{/size} примерно равноценны\n3 - A{size=-10}i{/size} немного предпочтительнее A{size=-10}j{/size}\n5 - A{size=-10}i{/size} предпочтительнее A{size=-10}j{/size}\n7 - A{size=-10}i{/size} значительно предпочтительнее A{size=-10}j{/size}\n9 - A{size=-10}i{/size} явно предпочтительнее A{size=-10}j{/size}"
    ev_al_task1_info += "\nМожно ставить промежуточные баллы. И обратные(0.2, 0.33 и тд)"
    ev_al_task1_alternatives = list(map(str.strip, google_sheet_data[0]["userEnteredValue"]["stringValue"].split(";")))
    ev_al_task1_alternatives_info = "Альтерантивы:"
    for i in range(len(ev_al_task1_alternatives)):
        ev_al_task1_alternatives_info += f"\nA{i+1} - {ev_al_task1_alternatives[i]}"
    # init table
    ev_al_task1_table_data = [[0 for _ in range(len(ev_al_task1_alternatives))] for _ in range(len(ev_al_task1_alternatives))]
    #ev_al_task1_correct_answers = list(map(str.strip, google_sheet_data[1]["userEnteredValue"]["stringValue"].split(";")))
    def kadrb7():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b7kadr{nkadr}"):
            return
        renpy.call(f"b7kadr{nkadr}")
        #renpy.with_statement(fade)
        renpy.pause()
    def rewrite_table(inp):
        global fir
        global sec
        global allow_forward
        if not inp:
            return
        value = float(inp)
        global ev_al_task1_table_data
        ev_al_task1_table_data[fir-1][sec-1] = value
        ev_al_task1_table_data[sec-1][fir-1] = 1/value
        if sec == (len(ev_al_task1_alternatives)):
            fir += 1
            sec = fir
        else:
            sec += 1
        if sec == fir:
            sec+=1
        if sec == len(ev_al_task1_alternatives) + 1:
            allow_forward = True
            renpy.hide_screen("ev_al_task1_input")
            renpy.show_screen("task1_go_to_next")
        renpy.restart_interaction()
    

label b7kadr1:
    $ screens = ["eval_alternative", "butforwardback", "ev_al_task1_input", "task1_go_to_next"]
    $ allow_forward = False
    $ xy_ev_al_table = [800, 200]
    $ xsize_ev_al_table = 1000
    $ ysize_ev_al_table = 700
    $ fir = 1
    $ sec = 2
    show screen eval_alternative(ev_al_task1_label)
    if fir == len(ev_al_task1_alternatives) and sec == len(ev_al_task1_alternatives) + 1:
        hide screen ev_al_task1_input
        $ allow_forward = True
    else:
        show screen ev_al_task1_input
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
                xpos int(xy_ev_al_table[0] + (i+1)*(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                ypos int(xy_ev_al_table[1]  + (j+1)*(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1)))
                xsize int(xsize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                ysize int(ysize_ev_al_table/(len(ev_al_task1_alternatives) + 1))
                if sec - 1 == i and fir - 1 == j:
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
    