from django.shortcuts import render

# Create your views here.

from crud.models import StudentModel

from django.views.generic import View

class createstudentview(View):

    def get(self,request):

        return render(request,"add_student.html")
    
    def post(self,request):

        print(request.POST)

        StudentModel.objects.create(name = request.POST.get("username"),
                                    roll_no = request.POST.get("userrollno"),
                                    department = request.POST.get("userdepart"),
                                    email = request.POST.get("useremail"),
                                    marks = request.POST.get("usermark")
                                     )
        
        return render(request,"add_student.html")
    
class StudentUpdate(View):

    def get(self,request,**kwargs):

        update_id = kwargs.get("pk")

        stud_data = StudentModel.objects.get(id=update_id)

        return render(request,"stud_update.html",{"stud_data":stud_data})
    
    def post(self,request,**kwargs):

        update_id = kwargs.get("pk")

        stud_data = StudentModel.objects.get(id=update_id)

        print(request.POST)

        stud_data.name = request.POST.get("username") 

        stud_data.roll_no = request.POST.get("userrollno")

        stud_data.department = request.POST.get("userdepart")

        stud_data.email = request.POST.get("useremail")

        stud_data.marks = request.POST.get("usermark")

        stud_data.save()

        return render(request,"stud_update.html")
    
class StudentRead(View):

    def get(self,request):

        data =StudentModel.objects.all()

        return render(request,"studentread.html",{"data":data})
    
class Studentdelete(View):

     def get(self,request,**kwargs):

        delete_id = kwargs.get("pk")

        stud_data = StudentModel.objects.get(id=delete_id)

        stud_data.delete()

        return render(request,"add_student.html")
     
class StudentretriveView(View):

    def get(self,request,**kwargs):

        retrive_id = kwargs.get("pk")

        stud_data =  StudentModel.objects.get(id= retrive_id)
        
        return render(request,"stud_details.html",{"stud_data":stud_data})
    


