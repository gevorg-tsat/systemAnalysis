label b3kadr1:
    $ screens = ["goal_defenition", "butforwardback"]
    show screen goal_defenition("Sample text")
    show screen butforwardback
    pause


init python:
    def kadrb3():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b3kadr{nkadr}"):
            return
        renpy.call(f"b3kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()
