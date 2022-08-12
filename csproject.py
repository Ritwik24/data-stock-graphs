from tkinter import *
import os
 
def register():
    
  global register_screen
  register_screen = Toplevel(main_screen)
  register_screen.title("Register")
  register_screen.geometry("300x250")
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
  Label(register_screen, text="Please enter details below", bg="yellow").pack()
  Label(register_screen, text="").pack()
  username_lable = Label(register_screen, text="Username * ")
  username_lable.pack()
  username_entry = Entry(register_screen, textvariable=username)
  username_entry.pack()
  password_lable = Label(register_screen, text="Password * ")
  password_lable.pack()
  password_entry = Entry(register_screen, textvariable=password, show='*')
  password_entry.pack()
  Label(register_screen, text="").pack()
  Button(register_screen, text="Register", width=10, height=1, bg="yellow", command = register_user).pack() 
 
def login():
    
  global login_screen
  login_screen = Toplevel(main_screen)
  login_screen.title("Login")
  login_screen.geometry("300x250")
  Label(login_screen, text="Please enter details below to login").pack()
  Label(login_screen, text="").pack()
  global username_verify
  global password_verify
  username_verify = StringVar()
  password_verify = StringVar()
  global username_login_entry
  global password_login_entry
  Label(login_screen, text="Username * ").pack()
  username_login_entry = Entry(login_screen, textvariable=username_verify)
  username_login_entry.pack()
  Label(login_screen, text="").pack()
  Label(login_screen, text="Password * ").pack()
  password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
  password_login_entry.pack()
  Label(login_screen, text="").pack()
  Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
def register_user():
 
  username_info = username.get()
  password_info = password.get()
  file = open(username_info, "w")
  file.write(username_info + "\n")
  file.write(password_info)
  file.close()
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  Label(register_screen, text="Registration Success, Go to the front page and login with the same username and password", fg="black", font=("calibri", 11)).pack()
 
def login_verify():
    
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_login_entry.delete(0, END)
  password_login_entry.delete(0, END)
 
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
      login_success()
 
    else:
      password_not_recognised()
 
  else:
    user_not_found()

def login_success():
    
  global login_success_screen
  login_success_screen = Toplevel(login_screen)
  login_success_screen.title("Success")
  login_success_screen.geometry("150x100")
  Label(login_success_screen, text="Login Success").pack()
  Button(login_success_screen, text="OK", command=delete_login_success).pack()
  a=2
  while a>1:
    import numpy as np
    import matplotlib.pyplot as plt
    from pandas_datareader.data import DataReader
    import datetime as dt
    import csv
    print('after getting the output, if u want to continue, close the login interface and output tab(save the output if you want)')
    choice=input('do you want to: 1.read and plot data from a text files, 2. plot a graph of any type according to user inputs, 3.plot a graph of a given equation, 4.see stock prices (enter 1, 2, 3 or 4):')

    if choice=='1':
      import csv
      f=input('enter file name(ex. test.txt)')
      ch=input('do you want to update the output lively?(yes/no)')
      if ch=='yes':
        import matplotlib.animation as animation
        from matplotlib import style
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        def animate(i):
          graph_data = open(f,'r').read()
          lines = graph_data.split('\n')
          x6 = []
          y6 = []
          for line in lines:
            if len(line) > 1:
              x, y = line.split(',')
              x6.append(float(x))
              y6.append(float(y))
          ax1.clear()
          ax1.plot(x6, y6)
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
      
      elif ch=='no':
        x2=[]
        y2=[]
        with open(f,'r') as f1:
          data=f1.read()
          lines=data.split('\n')
          for line in lines:
            if len(line) > 1:
              x, y = line.split(',')
              x2.append(float(x))
              y2.append(float(y))
        x_axis1=input('enter x axis label')
        y_axis1=input('enter y axis label')
        titl=input('enter title')
        labl=input('enter label for the line')
        plt.plot(x2,y2, label=labl)
        plt.xlabel(x_axis1)
        plt.ylabel(y_axis1)
        plt.title(titl)
        plt.legend()
        plt.show()
      else:
        print('invalid input')
  
    elif choice=='2':
      typ=input('enter the type of graph(line/bar/2 bars/horizontal bar/histogram/pie/scatter plot/contour plot/3D surface plot)')
      if typ=='line':
        n=int(input('enter no.of lines to be plotted'))
        for i in range(0,n):
          ls=input("enter the line's style(solid/dashed/dotted/dashdot)")
          lw=float(input("enter the line's width"))
          c=input("enter the line's colour(blue/green/red/magenta/yellow/black/cyan/white/brown)")
          m=input("enter the marker's colour")
          s=int(input("enter the marker's size"))
          lt=input("enter the marker's type(point'.'/pixel','/circle'o'/plus'P'/x marker'x,X'/diamond'D'/square's'/Pentagon'p'/star'*'/hexagon'h,H'/triangle'^,>,<,v')")
          x=eval(input('enter x coordinates as list'))
          y=eval(input('enter same no.of y coordinates as list'))
          plt.plot(x,y,color=c,linestyle=ls,linewidth=lw,marker=lt,markerfacecolor=m,markersize=s,label='line'+' '+str(i+1))
        x_axis=input('enter x axis label')
        y_axis=input('enter y axis label')
        titl=input('enter title')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(titl)
        plt.legend()
        plt.show()
      elif typ=='bar':
        def bar(x,h):
          tl=eval(input('enter x axis parameters as list'))
          w=float(input('enter width'))
          c=eval(input('enter color(s) as list'))
          x_axis=input('enter x axis label')
          y_axis=input('enter y axis label')
          titl=input('enter title')
          plt.bar(x,h,tick_label=tl,width=w,color=c)
          plt.title(titl)
          plt.xlabel(x_axis)
          plt.ylabel(y_axis)
          plt.show()
        x=eval(input('enter x coordinates as list'))
        h=eval(input('enter height of bars as list'))
        print(bar(x,h))
      elif typ=='2 bars':
        def mult_bar(A,B):
          X=np.arange(len(A))
          c1=input('enter colour of first bar')
          c2=input('enter colour of 2nd bar')
          l1=input('enter label for first bar')
          l2=input('enter label for 2nd bar')
          w=float(input('enter width'))
          titl=input('enter title')
          plt.bar(X,A,color=c1,width=w,label=l1)
          plt.bar(X+w,B,color=c2,width=w,label=l2)
          plt.legend()
          plt.title(titl)
          plt.show()
        A=eval(input('enter heights of bar 1 as list'))
        B=eval(input('enter heights of bar 2 as list'))
        print(mult_bar(A,B))
      elif typ=='horizontal bar':
        def hori_bar(A,B):
          x_axis=input('enter x axis label')
          y_axis=input('enter y axis label')
          titl=input('enter title') 
          plt.barh(A,B)
          plt.xlabel(x_axis)
          plt.ylabel(y_axis)
          plt.title(titl)
          plt.show()
        A=eval(input('enter parameters as list'))
        B=eval(input('enter width of bars as list'))
        print(hori_bar(A,B))
      elif typ=='histogram':
        def hist(A):
          c=input('enter color')
          w=float(input('enter width'))
          plt.hist(A,color=c,histtype='bar',rwidth=w)
          x_axis=input('enter x axis label')
          y_axis=input('enter y axis label')
          titl=input('enter title')
          plt.xlabel(x_axis)
          plt.ylabel(y_axis)
          plt.title(titl)
          plt.show()
        A=eval(input('enter list of frequencies'))
        print(hist(A))
      elif typ=='pie':
        def pie(parts,slices):
          c=eval(input('enter colours of the parts as a list'))
          r=float(input('enter radius of the pie chart'))
          plt.pie(slices, labels = parts, colors=c, startangle=90, shadow = True, radius = r, autopct = '%1.1f%%')
          plt.legend()
          plt.show()
        A=eval(input('enter the different parts of the pie chart as a list'))
        B=eval(input('enter corresponding proportions as list'))
        print(pie(A,B))
      elif typ=='scatter plot':
        def scatter(X,Y):
          m=input("enter the marker's colour")
          ms=int(input("enter the marker's size"))
          lt=input("enter the marker's type")
          x_axis=input('enter x axis label')
          y_axis=input('enter y axis label')
          titl=input('enter title')
          labl=input('enter label for the marker')
          plt.scatter(X,Y,label=labl,color=m,marker=lt,s=ms)
          plt.xlabel(x_axis)
          plt.ylabel(y_axis)
          plt.title(titl)
          plt.legend()
          plt.show()
        x=eval(input('enter x axis values as a list'))
        y=eval(input('enter corresponding y axis values as list'))
        print(scatter(x,y))
      elif typ=='contour plot':
        x1=float(input('enter starting point of the axes'))
        x2=float(input('enter ending points of the axes'))
        X=np.linspace(x1,x2,100)
        Y=np.linspace(x1,x2,100)
        [x,y]=np.meshgrid(X,Y)
        fig, ax = plt.subplots(1, 1)
        print('enter RHS of the equation in terms of x and y(Instructions: use ** for raising exponents, * for multiplication,/ for division, np.sin(x), np.cos(x), etc. for trigonometric functions, np.exp(x) for e^x and np.pi() for π')
        Z=eval(input('z='))
        f=input('enter 1 for filled contours, 2 for contour lines')
        titl=input('enter title')
        if f=='1':
          ax.contourf(x,y,Z)
          ax.set_title(titl) 
          ax.set_xlabel('x') 
          ax.set_ylabel('y')
          plt.show()
        elif f=='2':
          ax.contour(x,y,Z)
          ax.set_title(titl) 
          ax.set_xlabel('x') 
          ax.set_ylabel('y')
          plt.show()
      elif typ=='3D surface plot':
        from mpl_toolkits import mplot3d
        fig = plt.figure()
        def z(x, y):
          import numpy as np
          print('enter RHS of the equation in terms of x and y(Instructions: use ** for raising exponents, * for multiplication,/ for division, np.sin(x), np.cos(x), etc. for trigonometric functions, np.exp(x) for e^x and np.pi() for π')
          z=eval(input('z='))
          return z
        y1=float(input('enter starting point of the axes'))
        y2=float(input('enter ending points of the axes'))
        A=np.linspace(y1,y2,50)
        B=np.linspace(y1,y2,50)
        C, D= np.meshgrid(A, B)
        E = z(C, D)
        ax = plt.axes(projection='3d')
        c_set=input('choose a colour set(Accent,Accent_r,Blues,Blues_r, BrBG,BrBG_r,BuGn,BuGn_r,BuPu,BuPu_r,CMRmap,CMRmap_r,Dark2,Dark2_r,GnBu,GnBu_r,Greens,Greens_r,Greys,Greys_r,OrRd,OrRd_r,Oranges,Oranges_r,PRGn,PRGn_r,Paired,Paired_r,Pastel1,Pastel1_r,Pastel2, Pastel2_r, PiYG,PiYG_r,PuBu,PuBuGn,PuBuGn_r,PuBu_r, PuOr, PuOr_r, PuRd,PuRd_r,Purples,Purples_r,RdBu,RdBu_r,RdGy,RdGy_r,RdPu,RdPu_r,RdYlBu,RdYlBu_r,RdYlGn,RdYlGn_r,Reds,Reds_r,Set1,Set1_r,Set2,Set2_r,Set3,Set3_r,Spectral,Spectral_r,Wistia,Wistia_r,YlGn,YlGnBu,YlGnBu_r,YlGn_r,YlOrBr,YlOrBr_r,YlOrRd,YlOrRd_r,afmhot,afmhot_r,autumn,autumn_r,binary,binary_r,bone,bone_r,brg,brg_r,bwr,bwr_r,cividis,cividis_r,cool,cool_r,coolwarm,coolwarm_r,copper,copper_r,cubehelix,cubehelix_r,flag,flag_r,gist_earth,gist_earth_r,gist_gray,gist_gray_r,gist_heat,gist_heat_r,gist_ncar,gist_ncar_r,gist_rainbow,gist_rainbow_r,gist_stern,gist_stern_r,gist_yarg,gist_yarg_r,gnuplot,gnuplot2,gnuplot2_r,gnuplot_r,gray,gray_r,hot,hot_r,hsv,hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r,nipy_spectral,nipy_spectral_r,ocean,ocean_r,pink,pink_r,plasma,plasma_r,prism,prism_r,rainbow,rainbow_r,seismic, seismic_r,spring,spring_r, summer, summer_r,tab10,tab10_r,tab20,tab20_r,tab20b,tab20b_r,tab20c,tab20c_r,terrain,terrain_r,turbo,turbo_r,twilight,twilight_r,twilight_shifted,twilight_shifted_r,viridis,viridis_r,winter,winter_r)')
        titl=input('enter title')
        ax.plot_surface(C, D, E, rstride=1, cstride=1,cmap=c_set, edgecolor='none')
        ax.set_title(titl)
        plt.show()
      else:
        print('invalid input')
  
    elif choice=='3':
      n=int(input('enter no.of equations to be plotted'))
      a=float(input('enter starting point of x axis'))
      b=float(input('enter ending point of x axis'))
      x=np.linspace(a,b,100)
      for i in range(0,n):
        print('enter RHS of the equation in terms of x(Instructions: use ** for raising exponents, * for multiplication/ for division, np.sin(x), np.cos(x), etc. for trigonometric functions, np.exp(x) for e^x and np.pi() for π')
        y=eval(input('y='))
        ls=input("enter the line's style(solid/dashed/dotted/dashdot)")
        lw=float(input("enter the line's width"))
        c=input("enter the line's colour(blue/green/red/magenta/yellow/black/cyan/white/brown)")
        m=input("enter the marker's colour")
        s=int(input("enter the marker's size"))
        lt=input("enter the marker's type(point'.'/pixel','/circle'o'/plus'P'/x marker'x,X'/diamond'D'/square's'/Pentagon'p'/star'*'/hexagon'h,H'/triangle'^,>,<,v')")
        labl=input('enter label for the equation')
        plt.plot(x, y, label=labl, color=c, linestyle=ls, linewidth = lw, marker =lt,  markersize = s, markerfacecolor =m, markeredgecolor =m)
      x_axis=input('enter x axis label')
      y_axis=input('enter y axis label')
      titl=input('enter title')
      plt.grid(True)
      plt.xlabel(x_axis)
      plt.ylabel(y_axis)
      plt.title(titl)
      plt.legend()
      plt.show()
  
    elif choice=='4':
      t_name=input('enter ticker name of the company(ex., AAPL for apple, MSFT for microsoft)search on the web for ticker names if you do not know')
      yyyy1=int(input('enter start year'))
      mm1=int(input('enter start month'))
      dd1=int(input('enter start day'))
      yyyy2=int(input('enter end year'))
      mm2=int(input('enter end month'))
      dd2=int(input('enter end day'))
      dt_start = dt.datetime(yyyy1, mm1, dd1)                                                      
      dt_end = dt.datetime(yyyy2,mm2,dd2)
      data = DataReader(t_name, 'yahoo', dt_start, dt_end)['Adj Close']
      plt.plot(data)
      str1=t_name+' '+'closing prices'
      plt.title(str1)
      plt.show()
 
    else:
      print('invalid input')
    continue

def password_not_recognised():
    
  global password_not_recog_screen
  password_not_recog_screen = Toplevel(login_screen)
  password_not_recog_screen.title("Success")
  password_not_recog_screen.geometry("150x100")
  Label(password_not_recog_screen, text="Invalid Password ").pack()
  Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def user_not_found():
    
  global user_not_found_screen
  user_not_found_screen = Toplevel(login_screen)
  user_not_found_screen.title("Success")
  user_not_found_screen.geometry("150x100")
  Label(user_not_found_screen, text="User Not Found").pack()
  Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 

def delete_login_success():
  login_success_screen.destroy()
 
 
def delete_password_not_recognised():
  password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
  user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
  global main_screen
  main_screen = Tk()
  main_screen.geometry("300x250")
  main_screen.title("Account Login")
  Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
  Label(text="").pack()
  Button(text="Login", height="2", width="30", command = login).pack()
  Label(text="").pack()
  Button(text="Register", height="2", width="30", command=register).pack()
 
  main_screen.mainloop()
 
 
main_account_screen()
