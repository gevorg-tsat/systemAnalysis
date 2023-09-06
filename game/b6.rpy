label b6kadr1:
    $ screens = ["finding_alternative", "butforwardback"]
    show screen finding_alternative("посмотри на эту схемку")
    show screen butforwardback
    pause

init python:
    def kadrb6():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b6kadr{nkadr}"):
            renpy.call("startgame")
            return
        renpy.call(f"b6kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()