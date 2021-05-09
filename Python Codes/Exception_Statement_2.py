try:
    fh = open("testfile","w")
    fh.write("This is my test file for exception handling")
    print("Done")
except IOError:
    print("IOError: can't find file or read data")
else:
    print("Written content in the file succesfull")
finally:
    fh.close()
