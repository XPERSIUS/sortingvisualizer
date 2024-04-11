from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
root=Tk()
root.title('Sorting Algorithm Visualizer') 
root.geometry('900x600+200+80')
root.config(bg='#082A46')
data=[]
def drawData(data,colorArray):
  
    Canvas.delete("all")
    canvas_height=450
    canvas_width=870
    x_width=canvas_width/(len(data)+1)
    offset=10
    spacing_bet_rect=10
    normalised_data=[i/max(data) for i in data]

    for i,height in enumerate(normalised_data):
        x0=i*x_width+offset+spacing_bet_rect
        y0=canvas_height - height  * 400 

        x1=(i+1)*x_width
        y1=canvas_height

        Canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        Canvas.create_text (x0+2,y0,anchor=SW,text=str(data[i]),font=("new roman",15,"italic bold"),fill="orange")
    root.update_idletasks()

def StartAlgorithm():
    global data
    if not data :
        return 
    if(algo_menu.get()=='quick sort'):
        quick_sort(data,0,len(data)-1,drawData,speedscale.get())
      
    elif algo_menu.get()=="Bubble sort":
        bubble_sort(data,drawData,speedscale.get())
    elif algo_menu.get()=="Merge sort":
        merge_sort(data,drawData,speedscale.get())
    drawData(data,['green' for x in range(len(data))])


def Generate():
    global data
    print('Selected Algorithm:'+selected_algorithm.get())
    
    minivalue=int(minvalue.get())
    maxivalue=int(maxvalue.get())
    sizeevalue=int(sizevalue.get())
       
    data=[]

    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue,maxivalue+1))
         
    drawData(data,["#A90042"for x in range(len(data))])

selected_algorithm=StringVar()
mainlabel=Label(root,text="Algorithm:",font=("new roman",16,"italic bold"),bg="#05897A",width=10,fg="black",relief=GROOVE,bd=5)
mainlabel.place(x=0,y=0)
algo_menu=ttk.Combobox(root,width=15,font=("new roman",19,"italic bold"),textvariable=selected_algorithm,values=['Bubble sort','Merge sort','quick sort'])
algo_menu.place(x=145,y=0)
algo_menu.current(0)
random_generate=Button(root,text="Generate",bg="#2DAE94",font=("arial",12,"italic bold"),relief=SUNKEN,activebackground="#059458",activeforeground="white",bd=5,width=10,command=Generate)
random_generate.place(x=750,y=60)

sizevalulabel=Label(root,text="Size:",font=("new roman",12,"italic bold"),bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
sizevalulabel.place(x=0,y=60)
sizevalue=Scale(root,from_=0,to=30,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
sizevalue.place(x=120,y=60)


minvalulabel=Label(root,text="Min Value:",font=("new roman",12,"italic bold"),bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
minvalulabel.place(x=250,y=60)
minvalue=Scale(root,from_=0,to=10,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
minvalue.place(x=370,y=60)


maxvalulabel=Label(root,text="Max value:",font=("new roman",12,"italic bold"),bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
maxvalulabel.place(x=500,y=60)
maxvalue=Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
maxvalue.place(x=620,y=60)

start=Button(root,text="Start",bg="#C45B09",font=("arial",12,"italic bold"),relief=SUNKEN,activebackground="#059458",activeforeground="white",bd=5,width=10,command=StartAlgorithm)
start.place(x=750,y=0)
random_generate.place(x=750,y=60)

speedlabel=Label(root,text="Speed:",font=("new roman",12,"italic bold"),bg="#0E6DA5",width=10,fg="black",height=2,relief=GROOVE,bd=5)
speedlabel.place(x=400,y=0)

speedscale=Scale(root,from_=0.1,to=5.0,resolution=0.2,length=200,digits=2,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)

speedscale.place(x=520,y=0)
Canvas=Canvas(root,width=870,height=450,bg="black")
Canvas.place(x=10,y=130)



root.mainloop()