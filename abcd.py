{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "root=Tk()\n",
    "# myLabel=Label(root,text=\"My Label\")\n",
    "# myLabel.pack()\n",
    "myButton = Button(root, text = \"Click here\")\n",
    "myButton.pack()\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "root=Tk()\n",
    "myLabel=Label(root,text=\"My Label\")\n",
    "myLabel.pack()\n",
    "myButton = Button(root, text = \"Click here\")\n",
    "myButton.pack()\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "root=Tk()\n",
    "def myClick():\n",
    "     myLabel=Label(root,text=\"You clicked it....\")\n",
    "     myLabel.pack()\n",
    "myButton = Button(root, text = \"Click here\" ,command=myClick ,fg = \"blue\",bg =\"red\")\n",
    "myButton.pack()\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "root=Tk()\n",
    "myLabel1=Label(root,text=\"Enter the name:\")\n",
    "myLabel1.pack()\n",
    "myEntry = Entry(root, width= 40,borderwidth=5)\n",
    "myEntry.insert(0,\"Enter your name here\")\n",
    "myEntry.pack()\n",
    "\n",
    "def myClick():\n",
    "     myLabel2=Label(root,text=\"You clicked it \" + myEntry.get()+ \"......\")\n",
    "     myLabel2.pack()\n",
    "myButton = Button(root, text = \"Click here\" ,command=myClick ,width=15,fg = \"blue\",bg =\"red\")\n",
    "myButton.pack()\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\\lib\\tkinter\\__init__.py\", line 1921, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"C:\\Users\\Student\\AppData\\Local\\Temp\\ipykernel_10276\\2699925776.py\", line 19, in click\n",
      "    myLabel4=Label(root,add)\n",
      "  File \"C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\\lib\\tkinter\\__init__.py\", line 3187, in __init__\n",
      "    Widget.__init__(self, master, 'label', cnf, kw)\n",
      "  File \"C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\\lib\\tkinter\\__init__.py\", line 2598, in __init__\n",
      "    classes = [(k, v) for k, v in cnf.items() if isinstance(k, type)]\n",
      "AttributeError: 'str' object has no attribute 'items'\n"
     ]
    }
   ],
   "source": [
    "from tkinter import *\n",
    "root=Tk()\n",
    "myLabel1=Label(root,text=\"Enter the first number:\")\n",
    "myLabel1.pack()\n",
    "myEntry1 = Entry(root, width= 40,borderwidth=5)\n",
    "myEntry1.pack()\n",
    "# myButton = Button(root, text = \"Submit\" ,command=myClick ,width=15)\n",
    "# myButton.pack()\n",
    "myLabel1=Label(root,text=\"Enter the second number:\")\n",
    "myLabel1.pack()\n",
    "myEntry2 = Entry(root, width= 40,borderwidth=5)\n",
    "myEntry2.pack()\n",
    "# myButton = Button(root, text = \"Submit\" ,command=myClick ,width=15)\n",
    "# myButton.pack()\n",
    "add= myEntry1.get()+ myEntry2.get()\n",
    "def click():\n",
    "    myLabel2=Label(root,text=\"Sum=\")\n",
    "    myLabel2.pack()\n",
    "    myLabel4=Label(root,add)\n",
    "    myLabel4.pack()\n",
    "myButton = Button(root, text = \"Sum\", command=click,width=15)\n",
    "myButton.pack()\n",
    "root.mainloop()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
