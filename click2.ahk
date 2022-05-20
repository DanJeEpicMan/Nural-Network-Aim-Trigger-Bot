loop
{
    if (GetKeyState("NumPad9"))
        mouseclick, left
    if (GetKeyState("8"))
    {
        loop, 5
        {
            mouseclick, left
            sleep, 25
        }
    ExitApp
    }

}