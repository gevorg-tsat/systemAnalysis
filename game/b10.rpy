label b10kadr1:
    $ screens = ["recognition_decision", "butforwardback"]
    show screen recognition_decision("посмотри на эту схемку")
    show screen butforwardback
    pause

init python:
    def kadrb10():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b10kadr{nkadr}"):
            return
        renpy.call(f"b10kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()