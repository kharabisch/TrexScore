
from tkinter import *




haupt=Tk()

haupt.title('TrexScore')
haupt.configure(bg='#F7F2E0')
haupt.geometry('500x770')

labA=Label(haupt,text='A',bg='#F8E6E0')
labA.grid(row=0,column=0)

labB=Label(haupt,text='b',bg='#58D3F7')
labB.grid(row=0,column=1)
labC=Label(haupt,text='c',bg='#D0F5A9')
labC.grid(row=0,column=2)
labD=Label(haupt,text='d',bg='#F8E6E0')
labD.grid(row=0,column=3)

trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=2,column=1)

king1=Label(haupt,text='King')
king1=Entry(haupt)
king1.grid(row=3,column=1)

dame1=Label(haupt,text='Dame')
dame1=Entry(haupt)
dame1.grid(row=4,column=1)

karo1=Label(haupt,text='Karo')
karo1=Entry(haupt)
karo1.grid(row=5,column=1)

plus1=Label(haupt,text='Trex')
plus1=Entry(haupt)
plus1.grid(row=6,column=1)


def res1():
    erg = int(karo1.get())+int(plus1.get())+int(king1.get())+int(dame1.get())+int(trex1.get)
    return
result1=Label(haupt,text='RES1')
result1=Button(haupt,text ='RES1',command=res1)
result1.grid(row=7,column=1,sticky='w')
#result1.config(text = str(res1))
#---------------------------------------------AAAAAAAAAAA111111111
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

result=Label(haupt,text='RES100')
result.grid(row=7,column=2,sticky='w')
#-------------------------------------------------BBBBBBBBBBB111111111111
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

result=Label(haupt,text='RES1000')
result.grid(row=7,column=3,sticky='w')
#------------------------------------------------------CCCCCCCCCCCC111111111111

#-------------------------------------------------DDDDDDDDDDDDDD1111111111111111111

trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=2,column=0)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=3,column=0)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=4,column=0)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=5,column=0)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=6,column=0)

result=Label(haupt,text='RES10000')
result.grid(row=7,column=0,sticky='w')
#---------------------------------------------AAAAAAAAAAA22222222222
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=8,column=0)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=9,column=0)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=10,column=0)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=11,column=0)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=12,column=0)

result=Label(haupt,text='RES2')
result.grid(row=13,column=0,sticky='w')
#-------------------------------------------------BBBBBBBBBBB22222222222
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=8,column=1)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=9,column=1)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=10,column=1)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=11,column=1)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=12,column=1)

result=Label(haupt,text='RES2')
result.grid(row=13,column=1,sticky='w')
#------------------------------------------------------CCCCCCCCCCCC222222222
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=8,column=2)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=9,column=2)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=10,column=2)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=11,column=2)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=12,column=2)

result=Label(haupt,text='RES2')
result.grid(row=13,column=2,sticky='w')
#-------------------------------------------------DDDDDDDDDDDDDD222222222222222222222
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=8,column=3)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=9,column=3)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=10,column=3)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=11,column=3)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=12,column=3)

result=Label(haupt,text='RES2')
result.grid(row=13,column=3,sticky='w')
#---------------------------------------------AAAAAAAAAAA333333333333
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=14,column=0)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=15,column=0)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=16,column=0)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=17,column=0)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=18,column=0)

result=Label(haupt,text='RES3')
result.grid(row=19,column=0,sticky='w')
#-------------------------------------------------BBBBBBBBBBB333333333333
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=14,column=1)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=15,column=1)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=16,column=1)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=17,column=1)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=18,column=1)

result=Label(haupt,text='RES3')
result.grid(row=19,column=1,sticky='w')
#------------------------------------------------------CCCCCCCCCCCC33333333333
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=14,column=2)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=15,column=2)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=16,column=2)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=17,column=2)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=18,column=2)

result=Label(haupt,text='RES3')
result.grid(row=19,column=2,sticky='w')
#-------------------------------------------------DDDDDDDDDDDDDD33333333333333333333333
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=14,column=3)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=15,column=3)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=16,column=3)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=17,column=3)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=18,column=3)

result=Label(haupt,text='RES3')
result.grid(row=19,column=3,sticky='w')
#---------------------------------------------AAAAAAAAAAA44444444444444444
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=20,column=0)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=21,column=0)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=22,column=0)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=23,column=0)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=24,column=0)

result=Label(haupt,text='RES4')
result.grid(row=25,column=0,sticky='w')
#-------------------------------------------------BBBBBBBBBBB44444444444444444
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=20,column=1)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=21,column=1)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=22,column=1)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=23,column=1)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=24,column=1)

result=Label(haupt,text='RES4')
result.grid(row=25,column=1,sticky='w')
#------------------------------------------------------CCCCCCCCCCCC4444444444444444
trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=20,column=2)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=21,column=2)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=22,column=2)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=23,column=2)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=24,column=2)

result=Label(haupt,text='RES4')
result.grid(row=25,column=2,sticky='w')


trex1=Label(haupt,text='Trex')
trex1=Entry(haupt)
trex1.grid(row=20,column=3)

king=Label(haupt,text='King')
king=Entry(haupt)
king.grid(row=21,column=3)

dame=Label(haupt,text='Dame')
dame=Entry(haupt)
dame.grid(row=22,column=3)

karo=Label(haupt,text='Karo')
karo=Entry(haupt)
karo.grid(row=23,column=3)

plus=Label(haupt,text='Trex')
plus=Entry(haupt)
plus.grid(row=24,column=3)

result=Label(haupt,text='RES4')
result.grid(row=25,column=3,sticky='w')
#-------------------------------------------------DDDDDDDDDDDDDD4444444444444444












haupt.mainloop()