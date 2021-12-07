
#Spēle akmens, šķēres, papīrīts
import tkinter as tk

#Definējam logu
window = tk.Tk()

#Jāpievieno elementi
#Informācija
lbl_info = tk.Label(text = "Sveicināts/a!\nŠī ir spēle akmens, šķēres, papīrīts!")
#Kas jādara
lbl_darit = tk.Label(text = "")
#Rezultāts
#ko katrs ir izvēlējies

window.mainloop()
lbl_lietizv = tk.Label()
lbl_datoraizv = tk.Label()
#Rezultāts
lbl_rezultats = tk.Label()

#Izvēles pogas
btn_akmens = tk.Button(text = "Akmens")
btn_skeres = tk.Button(text = "Šķēres")
btn_papirs = tk.Button(text = "Papīrs")

#.pack(), .place()
lbl_info.pack(fill = tk.X)
lbl_darit.pack()
btn_akmens.pack()
btn_papirs.pack()
btn_skeres.pack()
lbl_lietizv.pack()
lbl_datoraizv.pack()
lbl_rezultats.pack()

#.pack(), .place()
lbl_info.pack(fill = tk.X)
lbl_darit.pack()
btn_akmens.pack()
btn_papirs.pack()
btn_skeres.pack()
lbl_lietizv.pack()
lbl_datoraizv.pack()
lbl_rezultats.pack()


window.mainloop()
#Izvēles pogas
btn_akmens = tk.Button(text = "Akmens")
btn_skeres = tk.Button(text = "Šķēres")
btn_papirs = tk.Button(text = "Papīrs")

#Pogu interaktivitāte - .bind()
btn_akmens.bind("<Button-1>", akmens)
btn_papirs.bind("<Button-1>", papirs)
btn_skeres.bind("<Button-1>", skeres)

#.pack(), .place()
lbl_info.pack(fill = tk.X)
lbl_darit.pack()
btn_akmens.pack()
btn_papirs.pack()
btn_skeres.pack()
lbl_lietizv.pack()
lbl_datoraizv.pack()
lbl_rezultats.pack()

window.mainloop()