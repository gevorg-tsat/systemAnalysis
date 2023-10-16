transform mmove(x0, x1):
    xpos x0[0] ypos x0[1]
    #xpos 1500 ypos 175 zoom 0.03
    linear 1 xpos x1[0] ypos x1[1]
    
init python:
    # from jwcrypto import jwt
    from jose import jwt

    import requests
    import json
    import datetime
    # from jwt.algorithms import RSAAlgorithm
    filepath = "radiant-mercury-303720-8f5d514d724f.json"
    fp = renpy.file(filepath)
    jwt_data = json.load(fp)
    now = datetime.datetime.now().timestamp()
    right_answers = 0
    insert_row_number = None
    all_answers = 0
    jwt_fields = {
        "iss":"system-analysis-game@radiant-mercury-303720.iam.gserviceaccount.com",
        "scope":"https://www.googleapis.com/auth/spreadsheets",
        "aud":"https://oauth2.googleapis.com/token",
        "exp": now + 3598,
        "iat": now - 1
    }
    # jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))
    encoded = jwt.encode(jwt_fields, jwt_data['private_key'], algorithm="RS256")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    get_token_req = requests.post("https://oauth2.googleapis.com/token", headers=headers, data="grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion="+encoded)
    # with open("/Users/gevorgtsaturyan/Downloads/system_analysis/game/log.txt","w") as fw:
    #     fw.write("curl -d '" + f"grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion={encoded}' https://oauth2.googleapis.com/token" )
    #     fw.write(get_token_req.text)
    ACCESS_TOKEN = json.loads(get_token_req.text)['access_token']
    headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    debet0 = ""
    kredit0 = ""
    summa0 = ""    
    debet = None
    kredit = None
    summa = None
    b1quebt = ["Остаточная стоимость амортизируемых активов - это:", "Амортизация основных средств начисляется в течение:", "Первоначальная стоимость объектов основных средств, внесенных в счет вклада в уставный капитал, определяется по:", "Что НЕ относится к факторам, влияющим на определение срока полезного использования основных средств:"]
    b1ansbt = [["их рыночная стоимость", "сумма, на которую активы должны быть застрахованы", "их «недоамортизированная» стоимость", "разница между их первоначальной стоимостью и расходами на амортизацию за последний отчетный период"], ["всего срока их нахождения в организации", "всего срока их полезной службы", "установленного руководством организации срока полезной службы, но не более 20 лет", "от 2 до 12 лет полезной службы в зависимости от принадлежности объекта к амортизационной группе"] ,["чистой рыночной стоимости", "согласованной стоимости", "справедливой стоимости", "остаточной стоимости"], ["ожидаемый физический износ, зависящий от режима эксплуатации, климатических условий", "нормативно-правовые ограничения", "ожидаемый срок производительного использования", "величина первоначальной стоимости – чем дороже, тем дольше эксплуатируется"]]
    b1bt = False
    screens = []
    mXY0 = (1300,290)
    #lim = [Image(f"m{i+1}.png", pos=mXY0) for i in range(2)]
    b1immy = 0
    b1imyet = 0
    req = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA?includeGridData=true", headers=headers)
    row_number = 0
    # google_sheet_data = json.loads(req.text)["sheets"][0]["data"][row_number]["rowData"][0]["values"]
    # symptoms_task1_label = "Определите правильно симптомы/причины этого проишествия"
    # symptoms_task1_options = list(map(str.strip, google_sheet_data[0]["userEnteredValue"]["stringValue"].split(";")))
    # symptoms_task1_correct_answers = list(map(str.strip, google_sheet_data[1]["userEnteredValue"]["stringValue"].split(";")))
    def write_score():
        global right_answers
        global all_answers
        global your_name
        global ACCESS_TOKEN
        global insert_row_number
        global headers
        if insert_row_number is None:
            url = "https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA/values/'Students':append?valueInputOption=RAW"
        else:
            url = f"https://sheets.googleapis.com/v4/spreadsheets/1lc29xReSQYCmZ9cf8PdmAr-mu02LHvx-Uq-dRSVb0QA/values/{insert_row_number}?valueInputOption=RAW"
        # body = '{"values":[[your_name, ]]}'
        body = {"values": [[your_name, f"{right_answers} из {all_answers}"]]}
        if insert_row_number is None:
            text_req = requests.post(url, headers=headers, json=body)
        else:
            text_req = requests.put(url, headers=headers, json=body)
        if text_req.status_code == 200:
            with open("/Users/gevorgtsaturyan/Downloads/system_analysis/game/log.txt","w") as fw:
                fw.write(text_req.text)
            resp = json.loads(text_req.text)
            resp = resp.get("updates", resp)
            insert_row_number = resp["updatedRange"]
            
        elif text_req.status_code == 403:
            tmp_headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            get_token_req = requests.post("https://oauth2.googleapis.com/token", headers=tmp_headers, data="grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion="+encoded)
            ACCESS_TOKEN = json.loads(get_token_req.text)["access_token"]
            write_score()
        else:
            with open("/Users/gevorgtsaturyan/Downloads/system_analysis/game/log.txt","w") as fw:
                fw.write(text_req.text)
            raise Exception


        

    def kadrb1():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b1kadr{nkadr}"):
            renpy.call("startgame")
            return
        renpy.call(f"b1kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()
        #nkadr += 1
        #kadrb1()
    def monetmove():
        global b1immy
        global b1imyet
        for i in range(b1kadr8rez):
            renpy.show(f"m{i+1}", at_list=[mmove(mXY0, [900-48*i, 740])])
            renpy.pause(1)
            b1immy += 1
        for i in range(b1kadr8rez, 18):
            renpy.show(f"m{i+1}", at_list=[mmove(mXY0, [1780-48*(i-b1kadr8rez), 740])])
            renpy.pause(1)
            b1imyet += 1
    
    def clearlup():
        renpy.hide("b1kadrnclup")
    
    def find_index(array, drag):
        for i in range(len(array)):
            if array[i].drag_name == drag.drag_name:
                return i
        return -1

    def drag_placed(drags, drop):
        if not drop:
            if find_index(user_answers1, drags[0]) != -1:
                ind = symptoms_task1_options.index(drags[0].drag_name)
                user_answers1.pop(find_index(user_answers1, drags[0]))
                drags[0].snap(xy_options_symp_task1[0], xy_options_symp_task1[1] + ind*70)
                for i in range(len(user_answers1)):
                    user_answers1[i].snap(xy_answer_symp_task1[0], xy_answer_symp_task1[1] + i*65)
                renpy.restart_interaction()
            return
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        if droppable == "ответы":
            if find_index(user_answers1, drags[0]) == -1:
                user_answers1.append(drags[0])
        drags[0].snap(xy_answer_symp_task1[0], xy_answer_symp_task1[1] + find_index(user_answers1, drags[0]) * 65)
        renpy.restart_interaction()
        return
    def check_answer():
        global xy_answer_symp_task1
        global xy_options_symp_task1
        global tries
        global initial_tries
        global symptoms_task1_correct_answers
        global symptoms_task1_options
        global user_answers1
        global allow_forward
        global is_correct
        answers = [drag.drag_name for drag in user_answers1]
        if tries == 0:
            renpy.hide("mytext")
            t = Text(loser_no_tries_text,  xpos=xy_answer_symp_task1[0], ypos=(xy_answer_symp_task1[1] + 65 * len(symptoms_task1_options) + 85), xsize=550, ysize=20, color="#000000")
            renpy.show("mytext", what=t)
            renpy.hide_screen("butforwardback")
            renpy.show_screen('butforwardback', _zorder=1)
            return
        tries -= 1
        if set(map(str.lower, answers)) == set(map(str.lower, symptoms_task1_correct_answers)):
            is_correct = True
        else:
            is_correct = False
        if is_correct:
            t = Text(winner_text, xpos=xy_answer_symp_task1[0], ypos=(xy_answer_symp_task1[1] + 65 * len(symptoms_task1_options) + 85), xsize=550, ysize=20, color="#000000")
            allow_forward = True
        else:
            if tries != 0:
                t = Text(loser_text, xpos=xy_answer_symp_task1[0], ypos=(xy_answer_symp_task1[1] + 65 * len(symptoms_task1_options) + 85), xsize=550, ysize=20, color="#000000")
            else:
                t = Text(loser_no_tries_text,  xpos=xy_answer_symp_task1[0], ypos=(xy_answer_symp_task1[1] + 65 * len(symptoms_task1_options) + 85), xsize=550, ysize=20, color="#000000")
                allow_forward = True
        renpy.show("mytext", what=t)
        renpy.hide_screen("butforwardback")
        renpy.show_screen('butforwardback', _zorder=1)
        renpy.restart_interaction()

        

image b1kadrnclup = Movie(play="b1kadrnc.ogv", pos=(50,1000),side_mask=False) #, anchor=(50,1000) 
image b1kadr9 = Movie(play="b1kadr9.ogv", pos=(730,740), side_mask=False)
image b1endes = Movie(play="b1endes.ogv", pos=(1600,650),side_mask=False)
image b1endp = Image("b1endp.png", pos=(1300,700))#, zoom=0.133)
image b1ende = Image("b1ende.png", pos=(1700,800))#, zoom=0.114)
image b1endl = Image("b1endl.png", pos=(200, 500))
image m1 = Image("m1.png", pos=mXY0)
image m2 = Image("m1.png", pos=mXY0)
image m3 = Image("m1.png", pos=mXY0)
image m4 = Image("m1.png", pos=mXY0)
image m5 = Image("m1.png", pos=mXY0)
image m6 = Image("m1.png", pos=mXY0)
image m7 = Image("m1.png", pos=mXY0)
image m8 = Image("m1.png", pos=mXY0)
image m9 = Image("m1.png", pos=mXY0)
image m10 = Image("m1.png", pos=mXY0)
image m11 = Image("m1.png", pos=mXY0)
image m12 = Image("m1.png", pos=mXY0)
image m13 = Image("m1.png", pos=mXY0)
image m14 = Image("m1.png", pos=mXY0)
image m15 = Image("m1.png", pos=mXY0)
image m16 = Image("m1.png", pos=mXY0)
image m17 = Image("m1.png", pos=mXY0)
image m18 = Image("m1.png", pos=mXY0)
screen b1kadr3:
    $ s = '''
В составе основных средств Центра учитываются игровые жилеты для передвижных и стационарных площадок.

Срок полезного использования жилетов варьируется от 3-х до 5-ти лет в зависимости от модели.

{color=#ff00ff}Без знаний по начислению амортизации не обойтись!{/color} 
    '''
    if vkadr == "b1" and nkadr == 3:
        frame:
            background "gui/frame1.png"
            text "{size=+0}[s]{/size}" xpos 20 ypos 450 xsize 600 ysize 400 color "#000000" line_spacing 4



screen symptom_identification(symptom_text, allow_forward):
    zorder 100
    text "Идентификация симптомов" color "#000000" xpos 40 ypos 40 xsize 1920 ysize 50 size 80
    text "[symptom_text]"  color "#000000" xpos 40 ypos 150 xsize 1800 ysize 900
    draggroup:
        for i in range(len(symptoms_task1_options)):
            drag:
                drag_name symptoms_task1_options[i]
                xpos xy_options_symp_task1[0] ypos xy_options_symp_task1[1] + i*70
                droppable False
                draggable not allow_forward
                drag_raise True
                dragged drag_placed
                # mouse_drop True
                frame:
                    background Frame([ "gui/confirm_frame.png", "gui/framegrey.png"], gui.frame_borders, tile=gui.frame_tile)
                    xsize 550 ysize 65
                    xpadding 5
                    ypadding 5
                    text symptoms_task1_options[i] color "#000000" size 24 xalign 0.5 yalign 0.5 
        drag:
            drag_name "ответы"
            xpos xy_answer_symp_task1[0]
            ypos xy_answer_symp_task1[1]
            draggable False
            droppable True
            frame:
                xsize 550
                ysize 65 * len(symptoms_task1_options)
    text "Ваш(-и) ответ(-ы)" color "#000000" xpos xy_answer_symp_task1[0] ypos xy_answer_symp_task1[1] - 40 xsize 550 ysize 20
    if len(user_answers1) > 0:
        if not is_correct and tries:
            imagebutton:
                idle "b1butch"
                hover "b1butch_"
                xpos xy_answer_symp_task1[0]
                ypos xy_answer_symp_task1[1] + 65 * len(symptoms_task1_options) + 80
                # xsize 100
                # ysize 65
                action Function(check_answer)


label b1kadr1:
    $ allow_forward = False
    $ screens = ["symptom_identification", "butforwardback"]
    scene white
    $ user_answers1 = []
    $ is_correct = False
    $ xy_options_symp_task1 = [80, 600]
    $ xy_answer_symp_task1 = [1000, 600]
    $ tries = 2
    $ initial_tries = 2
    show screen butforwardback
    show screen symptom_identification(symptoms_task1_label, allow_forward)
    
    pause


label b1kadr2:
    


