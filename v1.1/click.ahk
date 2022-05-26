duration := 0
Loop, {
9_key := GetKeyState("8")
mouseclick, left
        
start := A_TickCount
if (GetKeyState("8"))
{
loop, 5
{
mouseclick, left
sleep, 25
}
ExitApp
}
; Sleep, 1
; duration := A_TickCount - start
; if duration > 500
; ExitApp
}

; 9
