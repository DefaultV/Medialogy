import sys, os, getopt, turtle

def main():
    if not len(sys.argv) == 2:
        print("Too many arguments or in need an inputfile as first argument! Use <Program> <file>\nExiting...")
        sys.exit(1)
    inputfile = str(sys.argv[1])
    print("Generating UML Class-diagram for java file: '{}'".format(inputfile))
    getDiagram(inputfile) 

def bleachString(arg_str, arg_with):
    arg_str = arg_str.strip()
    for r in (("{", arg_with),("}", arg_with),("(", arg_with),(")", arg_with),
            (",", arg_with),(";", arg_with),("+", arg_with),("-", arg_with),("#", arg_with)):
        arg_str = arg_str.replace(*r)
    return arg_str.strip()

def findInList(arg_str, consList):
    for i in range(0,len(consList)):
        arg_str = bleachString(arg_str, "")
        n_cons = bleachString(consList[i], "")
        if arg_str == n_cons:
            return True
    return False

def argConst(argList):
    _str = ""
    for i in range(0,len(argList)):
        if not i == len(argList)-1:
            _str += argList[i] +", "
        else:
            _str += argList[i]
    return _str

def saveCanvas(canvas, filename):
    _dir = 'UML/'
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    canvas.postscript(file=_dir+filename, colormode='color')
    turtle.bye()
    print("Output image-file: '{}'\nExiting...".format(_dir+filename))


def turtleSquare(w,h):
    turtle.penup()
    turtle.goto(-w/2,-h/2)
    turtle.pendown()
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)

def makeDiagram(n_class, n_data, n_cons, n_argscons, n_meth):
    arr_len_comb = len(n_class) + len(n_data) + len(n_cons) + len(n_argscons) + len(n_meth)
    arr_len_comb = (arr_len_comb*0.5)*80
    w = 400
    h = arr_len_comb
    currentH = 0
    className = n_class[0]
    turtle.screensize(w,h)
    turtle.title(className + "to UML")
    turtle.setup(width= w+6, height = h+6)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(3)
    turtleSquare(w,h)
    turtle.penup();turtle.goto(-w/2,h*0.5-50);
    turtle.pendown();turtle.goto(w/2,h*0.5-50);turtle.penup()
    turtle.goto(0,h*0.5-40)

    turtle.write(n_class[0], align="center", font=("Arial", 24, "normal"))
    turtle.goto(-w/2+10,h*0.5-100)
    currentH = 100
    for string in n_data:
        turtle.write(string, font=("Arial", 16, "normal"))
        currentH += 20
        turtle.goto(-w/2+10, h*0.5-currentH)
    
    turtle.goto(-w/2, h*0.5-currentH+10);turtle.pendown();turtle.goto(w/2, h*0.5-currentH+10);turtle.penup()

    currentH += 40
    turtle.goto(-w/2+10, h*0.5-currentH)

    for string in n_cons:
        turtle.write(string, font=("Arial", 16, "normal"))
        currentH += 20
        turtle.goto(-w/2+10, h*0.5-currentH)

    for string in n_meth:
        if "S_" in string:
            string = string.replace("S_", "")
            turtle.write(string, font=("Arial", 16, "normal"))
            turtle.goto(-w/2+10, h*0.5-currentH+2)
            turtle.pensize(1);turtle.pendown();turtle.goto(-w/2+len(string)*9, h*0.5-currentH+2);turtle.penup();turtle.pensize(3)
        else:
            turtle.write(string, font=("Arial", 16, "normal"))
            currentH += 20
            turtle.goto(-w/2+10, h*0.5-currentH)
    
    cv = turtle.getcanvas()
    file_str = "UML"+sys.argv[1].replace(".java","")
    saveCanvas(cv, file_str)

def getDiagram(i_file):
    classNames = []
    dataNames = []
    consNames = []
    methNames = []
    f_args_cons = []
    bracketCount = 0
    with open(i_file, 'r+') as f:
        while True:
            line = f.readline()
            if not line: break

            if "{" in line:
                bracketCount += 1
            if "}" in line:
                bracketCount -= 1
            if bracketCount==1:
                b_line = line.strip()
                if not "}" in b_line:
                    if not "/" in b_line:
                        if not b_line == "":
                            if not "class" in b_line:
                                if not "()" in b_line:
                                    v_str = ""
                                    b_line = b_line.replace(";", " ")
                                    b_line = b_line.split()
                                    if len(b_line) <= 2:
                                        b_line.append("")
                                        b_line = [b_line[-1]] + b_line[:-1]
                                    v_sel = b_line[2]
                                    v_typ = b_line[1]
                                    v_vis = b_line[0]
                                    if v_vis == 'public':
                                        v_str = "+ "+v_sel+" : "+v_typ
                                    elif v_vis == 'private':
                                        v_str = "- "+v_sel+" : "+v_typ
                                    elif v_vis == 'protected':
                                        v_str = "# "+v_sel+" : "+v_typ
                                    elif v_vis == '':
                                        v_str = "  "+v_sel+" : "+v_typ
                                    if len(v_str) > 0:
                                        dataNames.append(v_str)

            if "()" and "{" in line:
                if "class" in line:
                    line = line.replace("{", "")
                    if "public" in line:
                        s_line = line.strip().split()
                        classNames.append(s_line[2])
                        continue
                    else:
                        s_line = line.strip().split()
                        classNames.append(s_line[1])
                        continue

                if not "class" in line:
                    line = bleachString(line, " ")
                    s_line = line.strip().split()
                    # Constructors
                    if len(s_line) <= 2:
                        if 'public' in s_line:
                            s_line.remove('public')
                            s_line[0] = "+ " + s_line[0]
                        consNames.append(s_line[0])
                        continue

                    #methods
                    args = []
                    f_vis = ""
                    f_type = ""
                    f_selector = ""
                    if "public" or "private" or "protected" in s_line:
                        #catch mutators
                        if findInList(s_line[1], consNames):
                            args_cons = []
                            f_vis = s_line[0]
                            f_select = s_line[1]
                            arg_str = "("
                            for i in range(2,len(s_line)):
                                if not (i%2): #type
                                    if not i == len(s_line)-2:
                                        arg_str += s_line[i] + ", "
                                    else:
                                        arg_str += s_line[i] + ")"
                            consNames.append(consNames[0] + arg_str)
                            continue

                        if len(s_line) == 3:
                            f_vis = s_line[0]
                            f_type = s_line[1]
                            f_selector = s_line[2]

                        staticFunc = 0
                        if len(s_line) > 3:
                            f_vis = s_line[0]
                            f_type = s_line[1]
                            if f_type == "static":
                                staticFunc = 1
                                f_type = s_line[2]
                                f_selector = s_line[3]
                                for i in range(4, len(s_line)):
                                    if not (i%2):
                                        args.append(s_line[i])
                            else:
                                f_selector = s_line[2]
                                for i in range(3,len(s_line)):
                                    if (i%2): #type
                                        args.append(s_line[i])
                        #print("vis: {}, type: {}, select: {}, args: {}".format(f_vis, f_type, f_selector, args))
                    if f_vis == 'public':
                        f_selector = "+ "+f_selector
                    elif f_vis == 'private':
                        f_selector = "- "+f_selector
                    elif f_vis == 'protected':
                        f_selector = "# "+f_selector
                    else: #CATCH DEFAULT
                        f_selector = "   "+s_line[1]
                        f_type = s_line[0]
                        args=[]
                        for i in range(2, len(s_line)):
                            if not (i%2): #type
                                args.append(s_line[i])
                    if staticFunc:
                        app_str = "S_"+f_selector+"("+argConst(args)+") : "+f_type
                    else:
                        app_str = f_selector+"("+argConst(args)+") : "+f_type
                    methNames.append(app_str)
        #print("Class: {}\nDatas: {}\nCons: {} with: {}\nMeths: {}".format(classNames, dataNames, consNames, f_args_cons, methNames))
    makeDiagram(classNames, dataNames, consNames, f_args_cons, methNames)

main()
