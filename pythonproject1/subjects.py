from tkinter import*
def compute():
    result=int(e1.get())+int(e2.get())+int(e3.get())
    totText.set(result)
    average=result/3
    avgText.set(average)

    if (average >= 80):
        grade= "distinction"

        gradeText.set(grade)

    elif (average>=65):
        grade="Credit"

        gradeText.set(grade)

    elif (average>=50):
        grade="Pass"

        gradeText.set(grade)
    else:
        grade="Fail"
        gradeText.set(grade)


root=Tk()
root.title("Students Grading System")
root.geometry("300x400")
root.configure(bg="powder blue")

global e1
global e2
global totText
global avgText
global gradeText



totText=StringVar()
avgText=StringVar()
gradeText=StringVar()



Label(root,text="English").place(x=10,y=10)
Label(root,text="Kiswahili").place(x=10,y=40)
Label(root,text="Maths").place(x=10,y=80)
Label(root,text="Total").place(x=10,y=110)
Label(root,text="Average").place(x=10,y=140)
Label(root,text="Grade").place(x=10,y=180)


e1=Entry(root)
e1.place(x=100,y=10)
e2=Entry(root)
e2.place(x=100,y=40)
e3=Entry(root)
e3.place(x=100,y=80)

result=Label(root,text="",textvariable=totText).place(x=100,y=110)
avg=Label(root,text="",textvariable=avgText).place(x=100,y=140)
grade=Label(root,text="",textvariable=gradeText).place(x=100,y=180)
Button(root,text="Calculate",command=compute,height=2,width=8).place(x=10,y=220)

root.mainloop()