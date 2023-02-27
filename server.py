from flask import Flask, request,render_template
# import requests
 

app= Flask(__name__ ,template_folder='my_templates')

def getContent(file, start, end):
    try:
       encodings = ['utf-8', 'utf-16']
       for encode in encodings:
            try:
                with open(f"files/{file}.txt", 'r',encoding=encode) as f:
                    content = f.readlines()
                    l=len(content)
                    if end>l:
                        end= -1
                    if start < 0:
                        start=0
                    msg=""
                    print(content)
                    break
            except Exception as p:
                continue
    except FileNotFoundError:
        msg= "File not present"
        content=""

    except Exception as e:
            msg= "Something went wrong",e
            content=""
    

    return content[start:end],msg

# Displaying Not Found page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")



@app.route("/display")
def file_diaplay():

    # extratcing values from request url
    file_name = request.args.get('file')
    start_line = request.args.get('start')
    end_line =request.args.get('end')

    print(start_line,end_line,file_name)


    # checkingif filename is empty
    if file_name is None:
        # setting default file name
        file_name = 'file1'
    
    if start_line is None:
        start_line = 0
    if end_line is None:
         end_line= -1

    F_list=["file1","file2","file3","file4"]
    if file_name in F_list:
        result = getContent(file_name, int(start_line), int(end_line))
        content,msg=result
    else:
        content= ""
        msg="Invalid File Name, Please enter valid file name"
        

    # return file content to user
    return render_template('index.html' , content={'content':content,"msg":msg})


if __name__ == '__main__' :
    app.run(debug = True)