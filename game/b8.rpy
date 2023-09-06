label b8kadr1:
    $ screens = ["choose_alternative", "butforwardback"]
    show screen choose_alternative("посмотри на эту схемку")
    show screen butforwardback
    pause

init python:
    def kadrb8():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b8kadr{nkadr}"):
            renpy.call("startgame")
            return
        renpy.call(f"b8kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()