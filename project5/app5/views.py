from django.shortcuts import render

# Create your views here.
def showIndex(request):
    student_info = { "data": [

                            {"idno":101,"name":"Ravi","marks":[36,45,87,99,70,56]},
                            {"idno":102,"name":"Kumar","marks":[86,15,80,79,60,55]},
                            {"idno":103,"name":"Rani","marks":[86,40,77,91,50,96]},
                            {"idno":104,"name":"Mohan","marks":[66,47,27,89,40,56]},
                            {"idno":105,"name":"Seema","marks":[57,25,87,99,70,16]}

                            ]
                    }

    return render(request,"index.html",student_info)
















