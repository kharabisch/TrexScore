
from tkinter import *

haupt=Tk()

haupt.title('TrexScore')
haupt.configure(bg='#F7F2E0')
haupt.geometry('500x770')

labA=Label(haupt,text='A',bg='#F8E6E0')
labA.grid(row=1,column=1)

labB=Label(haupt,text='b',bg='#58D3F7')
labB.grid(row=1,column=2)
labC=Label(haupt,text='c',bg='#D0F5A9')
labC.grid(row=1,column=3)
labD=Label(haupt,text='d',bg='#F8E6E0')
labD.grid(row=1,column=4)

trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=2,column=1)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=3,column=1)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=4,column=1)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=5,column=1)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=6,column=1)

result=Label(haupt,text='RES1')
result.grid(row=7,column=1,sticky='w')
#---------------------------------------------AAAAAAAAAAA
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=2,column=2)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=3,column=2)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=4,column=2)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=5,column=2)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=6,column=2)

result=Label(haupt,text='RES1')
result.grid(row=7,column=2,sticky='w')
#-------------------------------------------------BBBBBBBBBBB
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=2,column=3)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=3,column=3)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=4,column=3)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=5,column=3)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=6,column=3)

result=Label(haupt,text='RES1')
result.grid(row=7,column=3,sticky='w')
#------------------------------------------------------CCCCCCCCCCCC
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=2,column=4)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=3,column=4)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=4,column=4)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=5,column=4)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=6,column=4)

result=Label(haupt,text='RES1')
result.grid(row=7,column=4,sticky='w')
#-------------------------------------------------DDDDDDDDDDDDDD










haupt.mainloop()