# Importing modules  
import tkinter as tk  
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql 
  
# Function to add tasks  
def add_task():
    
    task_string = task_field.get()    
    if len(task_string) == 0:   
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        list_update()   
        task_field.delete(0, 'end')  

  
# Function to update list  
def list_update():
      
    clear_list()    
    for task in tasks:    
        task_listbox.insert('end', task)  
  
# Function to delete task  
def delete_task():
      
    try:    
        the_value = task_listbox.get(task_listbox.curselection())   
        if the_value in tasks:    
            tasks.remove(the_value)    
            list_update()    
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# Function to clear tasks  
def delete_all_tasks():
         
    while(len(tasks) != 0):  
        tasks.pop()  
        the_cursor.execute('delete from tasks')    
        list_update()  
  
# Function to clear list  
def clear_list():
      
    task_listbox.delete(0, 'end')  
  
# Function to close  
def close():  
      
    print(tasks)   
    guiWindow.destroy()  
  
# Function to retrieve data from the database  
def retrieve_database():
      
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
  
# Main function  
if __name__ == "__main__":  
    # Creating an object  
    guiWindow = tk.Tk()
    
    # Setting title  
    guiWindow.title("To-Do List")  

    # Setting geometry 
    guiWindow.geometry("500x450+750+250")  

    # Disabling resizable option  
    guiWindow.resizable(0, 0)  

    # Setting background color  
    guiWindow.configure(bg = "#9db6ba")  
  
    # Connect to the database  
    the_connection = sql.connect('listOfTasks.db')  

    # Creating cursor object  
    the_cursor = the_connection.cursor()  

    # Execute a SQL statement  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    # Defining an empty list  
    tasks = []  
      
    # Defining frames  
    header_frame = tk.Frame(guiWindow, bg = "#9db6ba", width = 500)  
    functions_frame = tk.Frame(guiWindow, bg = "#9db6ba", height=110, width = 500)  
    listbox_frame = tk.Frame(guiWindow, bg = "#9db6ba", height=280, width = 500)  
  
    # Place the frames  
    header_frame.pack(side = "top", fill = "x")
    functions_frame.pack(side = "top", expand = True, fill = "x")  
    listbox_frame.pack(side = "top", expand = True, fill = "x")
    header_frame.place(y = 0 , x = 170)
    functions_frame.place(y = 60)
    listbox_frame.place(y = 170)
      
    # Defining a label  
    header_label = ttk.Label(  
        header_frame,  
        text = "To-Do List",  
        font = ("Impact", "30"),  
        background = "#9db6ba",  
        foreground = "#000000"  
    )  
    # Place the label  
    header_label.pack(padx = 0, pady = 0)  
  
    # Defining label  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#9db6ba",  
        foreground = "#000000"  
    )  
    # Place the label  
    task_label.place(x = 30, y = 0)  
      
    # Defining an entry field  
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 40,
        background = "#ecf0f1",  
        foreground = "#92aaa9"  
    )  
    # Place the entry field  
    task_field.place(x = 30, y = 40)  
  
    # Adding buttons  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",
        width = 12,
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 12,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Clear Tasks",  
        width = 12,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Close",  
        width = 12,  
        command = close  
    )  
    # Placing buttons  
    add_button.place(x = 405, y = 41)  
    del_button.place(x = 30, y = 80)  
    del_all_button.place(x = 130, y = 80)  
    exit_button.place(x = 230, y = 80)  
  
    # Defining a list box  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 53,  
        height = 12,
        font = ("Consolas", "12"),
        selectmode = 'SINGLE',  
        background = "#ecf0f1",  
        foreground = "#92aaa9",  
        selectbackground = "#decfcc",  
        selectforeground = "#92aaa9"  
    )  
    # Placing the list box 
    task_listbox.place(x = 10, y = 20)  
  
    # calling functions  
    retrieve_database()  
    list_update()  

    # Run the application  
    guiWindow.mainloop()  

    # Connection with database  
    the_connection.commit()  
    the_cursor.close()  
