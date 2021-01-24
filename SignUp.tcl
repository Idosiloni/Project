#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Jan 22, 2021 06:37:46 PM +0200  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+660+210
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "SignUp"
    vTcl:DefineAlias "$top" "SignUp" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    entry $top.ent45 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent45" "EntUser" vTcl:WidgetProc "SignUp" 1
    label $top.lab46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text SignUp 
    vTcl:DefineAlias "$top.lab46" "lblSign" vTcl:WidgetProc "SignUp" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Username 
    vTcl:DefineAlias "$top.lab47" "LblUsr" vTcl:WidgetProc "SignUp" 1
    entry $top.ent48 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent48" "EntPass" vTcl:WidgetProc "SignUp" 1
    label $top.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Password 
    vTcl:DefineAlias "$top.lab49" "LblPass" vTcl:WidgetProc "SignUp" 1
    checkbutton $top.che50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text Student -variable che50 
    vTcl:DefineAlias "$top.che50" "Checkbutton1" vTcl:WidgetProc "SignUp" 1
    checkbutton $top.che51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text Teacher -variable che51 
    vTcl:DefineAlias "$top.che51" "Checkbutton2" vTcl:WidgetProc "SignUp" 1
    button $top.but61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Confirm 
    vTcl:DefineAlias "$top.but61" "BtnConfirm" vTcl:WidgetProc "SignUp" 1
    bind $top.but61 <Button-1> {
        lambda e: btnConfirm_1click(e)
    }
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent45 \
        -in $top -x 0 -relx 0.45 -y 0 -rely 0.222 -width 84 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 0 -relx 0.417 -y 0 -rely 0.067 -width 0 -relwidth 0.173 \
        -height 0 -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.317 -y 0 -rely 0.222 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 0 -relx 0.45 -y 0 -rely 0.311 -width 84 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.317 -y 0 -rely 0.311 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.che50 \
        -in $top -x 0 -relx 0.45 -y 0 -rely 0.4 -width 0 -relwidth 0.135 \
        -height 0 -relheight 0.1 -anchor nw -bordermode ignore 
    place $top.che51 \
        -in $top -x 0 -relx 0.45 -y 0 -rely 0.489 -width 0 -relwidth 0.135 \
        -height 0 -relheight 0.1 -anchor nw -bordermode ignore 
    place $top.but61 \
        -in $top -x 0 -relx 0.467 -y 0 -rely 0.644 -width 57 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

