from django.shortcuts import render, redirect
from .models import Submission,Register,Student_details
from django.http import JsonResponse

def scan_item(request):
    if request.method == 'POST':
        qr_code_data = request.POST.get('qr_code_data')
        # Save qr_code_data to the database (e.g., ScannedItem model)
        # ...
        return JsonResponse({'message': 'Data saved successfully!'})
    return JsonResponse({'message': 'Invalid request method.'}, status=400)




def home(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/dash.html', context)


def commerce(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/commerce.html', context)

def applied(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/applied.html', context)

def medicine(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/medicine.html', context)

def sports(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/sports.html', context)

def built(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/built.html', context)

def science(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/science.html', context)

def applied4(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/applied4.html', context)

def applied2(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/applied2.html', context)

def SCS1101(request):
    reg = Register.objects.all()
    context = {
        'reg': reg
    }
    return render(request, 'students/SCS1101.html', context)



def SCS1102(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS1102.html', context)

def SCS1104(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS1104.html', context)

def SCS1203(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS1203.html', context)

def SCS2101(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS2101.html', context)

def SCS2102(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS2102.html', context)

def SCS2104(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS2104.html', context)

def SCS2203(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS2203.html', context)

def SCS4101(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS4101.html', context)

def SCS4102(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS4102.html', context)

def SCS4104(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS4104.html', context)

def SCS4203(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/SCS4203.html', context)

def QR(request):
    sub = Submission.objects.all()
    context = {
        'sub': sub
    }
    return render(request, 'students/QR.html', context)

# views.py



def scan_qr_code(request):
    if request.method == 'POST':
        scanned_content = request.POST.get('scanned_content')  # Assuming you send the scanned content via POST
        try:
            student = Student_details.objects.get(student_id=scanned_content)
            # Student found, update checkbox status or perform other actions
            # Example: student.checked = True
            # Save the updated student record
            student.save()
        except Student_details.DoesNotExist:
            # Student not found, handle accordingly (e.g., show an error message)
            pass
    return render(request, 'your_template.html')

