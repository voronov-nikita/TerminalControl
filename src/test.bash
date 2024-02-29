running_gui_apps() {

    # loop through all open windows (ids)
    for win_id in $( wmctrl -l | cut -d' ' -f1 ); do 

        # test if window is a normal window
        if  $( xprop -id $win_id _NET_WM_WINDOW_TYPE | grep -q _NET_WM_WINDOW_TYPE_NORMAL ) ; then 

            echo "$( xprop -id $win_id WM_CLASS | cut -d" " -f4- )"", window id: $win_id"

        fi

    done
}