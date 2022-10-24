from tkinter import *
from tkinter.messagebox import showinfo

def click():
  items = list(map(int,txt1.get().split()))
  x, y = map(int,txt2.get().split())
  items[0],items[-1]= items[-1], items[0] #Замена первого эл на последнего
  lbl3['text'] = ("Тізімнің суммасы: {} ".format(sum(items)/len(items)))
  list_items = []
  l = 0
  for i in items: # замена эл и заполнение списка
    el = y if i == x else i
    list_items.insert(l,el)
    l +=1
  list_items_str = (" ".join(map(str,list_items)))
  lbl4['text'] = ("Нәтижесі: {} ".format(list_items_str))
  
  lbl5['text'] = ("Сұрыпталған нәтиже: {}".format(sorted(items)))
  
def clear():
  txt1.delete(0, END) 
  txt2.delete(0, END) 
  lbl3['text'] = ("Тізімнің суммасы:")
  lbl4['text'] = ("Нәтижесі:")
  lbl5['text'] = ("Сұрыпталған нәтиже:")
  showinfo(title="Ақпарат", message="Өрістер тазаланды")
  
window = Tk()
window.title("")
window.geometry("280x250")
window.resizable(width=False, height=False)
window.configure(background='#f3f7f8')

frame= Frame(window, relief= 'sunken')
frame.pack(fill= BOTH, expand= True, padx= 15, pady=15)

lbl1 = Label(frame,anchor='w', text="Тізім: ")
lbl1.grid(column=0, row=0)  
txt1 = Entry(frame,width=30)  
txt1.grid(column=1, row=0, columnspan=2, pady=5)  

lbl2 = Label(frame, text="X және У санын енгізіңіз: ", pady=5)
lbl2.grid(column=0, row=1, columnspan=2)  
txt2 = Entry(frame,width=10)  
txt2.grid(column=2, row=1, pady=5)  

lbl3 = Label(frame, text="Тізімнің суммасы: ", anchor='w', pady=5)
lbl3.grid(column=0, row=2, columnspan=3, sticky="W")  
 
lbl4 = Label(frame, text="Нәтижесі: ", anchor='w', pady=5)
lbl4.grid(column=0, row=3, columnspan=3, sticky="W") 

lbl5 = Label(frame, text="Сұрыпталған нәтиже: ", anchor='w', pady=5)
lbl5.grid(column=0, row=4, columnspan=3, sticky="W") 

btn = Button(frame, 
             text="Есептеу",  
             padx=10, 
             command=click, 
             borderwidth = 1, 
             relief = "flat",
             highlightthickness = 0, 
             bg="#03787c", 
             fg="#fff"
             )
btn.grid(column=2, row=5, pady=(20, 0)) 

btn = Button(frame, 
             text="Тазалау",  
             padx=10, 
             command=clear, 
             borderwidth = 1, 
             relief = "flat",
             highlightthickness = 0, 
             bg="#0078d4", 
             fg="#fff"
            )
btn.grid(column=1, row=5, pady=(20, 0)) 

exit_btn = Button(frame, 
                  text="Шығу", 
                  padx=10, 
                  borderwidth = 1, 
                  relief = "flat",
                  highlightthickness = 0, 
                  bg="#ec2553", 
                  fg="#fff",
                  command=window.destroy)
exit_btn.grid(column=0, row=5, pady=(20, 0))

window.mainloop()