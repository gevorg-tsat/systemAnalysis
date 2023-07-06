screen rez:
    zorder 90
    add "kadr rez.png"
    if b1kadr4rez != -1:
        text "[b1kadr8rez]" xpos 425 ypos 600 size 60 color "#000000" bold True
        text "[b1kadr8rez]" xpos 1775 ypos 600 size 60 color "#000000" bold True
        if b1kadr8rez == 18:
            text "«ХРАНИТЕЛЬ БОГАТСТВ»" xpos 365 ypos 810 xsize 200 size 24 color "#000000" bold True
            text "«ХРАНИТЕЛЬ БОГАТСТВ»" xpos 1730 ypos 810 xsize 200 size 24 color "#000000" bold True
    else:
        $ scores = persistent.scores
        if scores is not None:
            text "[scores]" xpos 425 ypos 600 size 60 color "#000000" bold True
            text "[scores]" xpos 1775 ypos 600 size 60 color "#000000" bold True
            if scores == 18:
                text "«ХРАНИТЕЛЬ БОГАТСТВ»" xpos 365 ypos 810 xsize 200 size 24 color "#000000" bold True
                text "«ХРАНИТЕЛЬ БОГАТСТВ»" xpos 1730 ypos 810 xsize 200 size 24 color "#000000" bold True
label rez:
    #hide screen main_menu
    $ vkadr = "rez"
    #scene white
    #show kadr rez at top with fade layer overlay
    #$ renpy.show_screen("rez")#layer='overlay'
    show screen rez with dissolve
    show screen butforwardback
    pause
    return