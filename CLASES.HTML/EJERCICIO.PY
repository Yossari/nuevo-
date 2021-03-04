from tkinter import*
root=TK()
frame=Frame(root, width = 500, height=400)
frame.pack()

hora_inicio=9
hora_final=10
hora_ingreso=9.5
estudiante=1
en_clase= FALSE

while hora_ingreso >= hora_inicio and hora_ingreso < hora_final and en_clase==FALSE:
    en_Clase= TRUE
    asistente=Label(frame,text="asistente" + str (estudiante))
    asistente.place(x=100, y=200)


root.mainloop()