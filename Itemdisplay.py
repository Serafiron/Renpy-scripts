screen feather:
    imagebutton:
        idle "images/feather-idle.png"
        hover "images/feather-glow.png"
        xalign 0.5
        yalign 0.5
        action (Show("feather_notif"), Hide ("feather"))

screen feather_notif:
    $ whitefeather = True
    text "You got a feather!":
        at transform:
            align (0.5, 0.5) alpha 0.0
            linear 0.5 alpha 1.0
            pause 2
            linear 0.5 alpha 0.0