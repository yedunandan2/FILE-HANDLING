import os
import sys
print("start")
def fun():
    print("choose your option \n1.creat file \n 2.read file \n3.edit file\n 4.list all file\n 5.delete file\n 6.end porogram\n")
    d= (input(""))
    a=d
    match a:
        case"1":
            print("---------------------------")
            print("creating file\n")
            print("enter your file name\n:")
            f=input("")
            h=f+",txt"
            with open(h,'x')as file:
                print("file is created succesfully")
                print("-------------------------")
        case"2":
            print("----------------------")
            print("reading file\n")
            print("enter the file name that you want to read")
            f=input("")
            with open(f+",txt","r")as file:
                print(file.read())
                print("the file read succesfully\n")
                print("---------------------")
        case"3":
            print("---------------------")
            print("editing the file\n")
            print("enter the file name that you want to edit\n")
            f=input("")
            with open(f+".txt",'a') as file:
                print(file.write())
                print("the file is edited succesfully\n")
                print("---------------------")
        case"4":
            print("---------------------")
            print("listing all file\n") 
            path='d:\pawan'
            file=os.listdir(path)
            for file in file:
                prit(file)
                print("these are the list of files\n")
                print("---------------------")
        case"5":
            print("---------------------")
            print("delete file\n")
            f=input("")
            file=os.remove(f+'.txt')
            print("deleted the file succesfully\n\n")
            print("---------------------")
        case"6":
            print("---------------------")
            print("stop the program\n")
            sys.exit(0)
            print("---------------------")
            while 1:
                fun()
