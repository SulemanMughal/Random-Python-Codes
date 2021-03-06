import mysql.connector as view
import cgi


from tkinter import *
from tkinter.messagebox import *
import Pmw

class QueryWindow(Frame):
    """GUI Database Query Frame"""

    def __init__(self):
        """QueryWindow Constructor"""

        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Enter Query, Click Submit to See  Results.")
        self.master.geometry("525x525")

        #   scrolled text pane for query string
        self.query = Pmw.ScrolledText(self, text_height = 8)
        self.query.pack(fill=X)

        #   button to  submit query
        self.submit = Button(self, text="Submit query", command=self.submitQuery)
        self.submit.pack(fill=X)

        #   frame to display query results
        self.frame=Pmw.ScrolledFrame(self, hscrollmode="static", vscrollmode = "static")
        self.frame.pack(expand=YES, fill=BOTH)

        self.panes = Pmw.PanedWidget(self.frame.interior(), orient="horizontal")
        self.panes.pack(expand=YES, fill=BOTH)


    def submitQuery(self):
        """Execute user-entered query agains database"""

        #   open connection, retrieve cursor and execute query
        try:
            connection = view.connect(host = 'localhost',
                          database='Books',
                          user='root',
                          password='Sul03314307703')
            cursor=connection.cursor()
            cursor.execute(self.query.get())
        except view.OperationalError as message:
            errorMessage = "Error %d:\n%s" %(message[0], message[1])
            showerror("Error", errorMessage)
            return
        else:
            data = cursor.fetchall()
            fields = cursor.description
            cursor.close()
            connection.close()

        self.panes.destroy()
        self.panes = Pmw.PanedWidget(self.frame.interior(), orient="horizontal")
        self.panes.pack(expand=YES, fill=BOTH)

        for item in fields:
            self.panes.add(item[0])
            label = Label(self.panes.pane(item[0]), text = item[0], relief=RAISED)
            label.pack(fill=X)

        for entry in data:
            for i in range(len(entry)):
                label=Label(self.panes.pane(fields[i][0]), text=str(entry[i]), anchor=W, relief = GROOVE, bg="white")
                label.pack(fill=X)
        self.panes.setnaturalsize()

def main():
    QueryWindow().mainloop()

if __name__ == "__main__":
    main()
