label b4kadr1:
    $ screens = ["structure_of_system", "butforwardback"]
    show screen structure_of_system("scheme.png", "посмотри на эту схемку")
    show screen butforwardback
    pause


init python:
    def kadrb4():
        global nkadr
        global vkadr
        global screens
        dnk = 2 if nkadr == 9 and not b1bt and b1amcor == 0 else "" # and b1scores0
        # renpy.show(f"kadr b1{nkadr}{dnk}",at_list=[top])
        for scr in screens:
            renpy.hide_screen(scr) 
        if not renpy.has_label(f"b4kadr{nkadr}"):
            return
        renpy.call(f"b4kadr{nkadr}")
        #renpy.with_statement(fade)
        
        renpy.pause()
