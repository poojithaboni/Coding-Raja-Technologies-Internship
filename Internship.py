Task=[]
PTask=[]
DTask=[]
CTask=[]
global n
n=0
def add():    #adding the task
    t=input("Enter the task you want to add:")
    Task.append(t)
    DTask.append(input("Enter the due date for this task:"))
    PTask.append(input("Is the task of high(H) or medium(M) or low(L) priority ?"))
    print("Task added successfully")   
    with open("Tasks.txt","a") as file: 
        file.write(t+"\n")       #storing the tasks in a file
        file.close
def display():  #displaying the task
    if n==0:
        print("List is empty.Nothing to display.")
        return
    j=0
    for i in range(0,n):
        print(str(j+1)+"."+Task[i]+"\t\tPriority:"+PTask[i]+"\t\tDue Date:"+DTask[i]+"\n")
        int(j)
        j+=1
def remove():   #removing the task
    display()
    if n==0:
        print("List is empty.Nothing to display.")
        return
    p=int(input("Select which task to remove:"))
    del Task[p-1]
    del PTask[p-1]
    del DTask[p-1]
    print("Task deleted successfully")
def mark():    #marking the tasks which have been completed
    display()
    if n==0:
        print("List is empty.Nothing to complete.")
        return
    s=int(input("Select the task which has been completed:"))
    d=Task[s-1]
    CTask.append(d)
    print("Completed Tasks:")
    j=0
    for i in CTask:
        print(str(j+1)+"."+i+"\n")
        int(j)
        j+=1
print("TO DO LIST") #main program
print("1.Add a task\n2.Remove a task\n3.Mark task as completed\n4.Exit")
print("Enter your choice:")
ch=input()
ch=int(ch) 
while(ch!=4):
    if ch==1:
        add()
        n+=1
    if ch==2:
        remove()
        n-=1
    if ch==3:
        mark()
    print("1.Add a task\n2.Remove a task\n3.Mark task as completed\n4.Exit")
    print("Enter your choice:") 
    ch=int(input())