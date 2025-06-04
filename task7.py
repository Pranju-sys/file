try:
    f=open("sample.txt","r")
except:
    print(f"the file \"sample.txt\" is not found ")
finally:
    f=open("sample.txt","a")
    f.write("line1:-finally opened the sample file.")
    f.write("\nline2:-you can write anything in it now.")
    f.close()
    f=open("sample.txt","r")
    print(f.readline())
    print(f.readline())
    f.close()
