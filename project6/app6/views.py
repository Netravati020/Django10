from django.shortcuts import render

# Create your views here.
def showIndex(request):
    student_info = {"data":

                       [
                           {"idno":101,"name":"Ravi","marks":[23,45,55,97,25,80]},
                           {"idno":102,"name":"Kumar","marks":[83,"A",95,57,20,34]},
                           {"idno":103,"name":"Rani","marks":[63,49,95,77,35,90]},
                           {"idno":104,"name":"Mohan","marks":[73,45,"A",87,95,10]},
                           {"idno":105,"name":"Seema","marks":[53,85,50,27,45,40]}
                         ]

                     }
    return render(request,"index.html",student_info)









