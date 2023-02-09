from tkinter import HORIZONTAL


row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
map=["row1","row2","row3"]
print(f"{row1}\n{row2}\n{row3}")
a=input("where do you want put your treasure?")
vertical=int(a[0])
horizontal=int(a[1])
map[vertical-1][horizontal-1]="X"
print(f"{row1}\n{row2}\n{row3}")

