from django.shortcuts import render,redirect  
from django.contrib import messages 
from .forms import *
from .models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
otp=000
import hashlib
# Create your views here.
def create_hash_key(data):
    if isinstance(data, str):
        data = data.encode('utf-8')

    hash_object = hashlib.sha256()

    hash_object.update(data)
    hash_key = hash_object.hexdigest()
    
    return hash_key

def donor_register(request):  
    if request.method=='POST':
        frm = DonorForm(request.POST)  
        if frm.is_valid():
            frm.save()
            d=Donor.objects.latest('id')
            print(d.bgroup)
            hash_key = create_hash_key(d.organ)
            print("Hash key:", hash_key)
            frm=Donor.objects.filter(id=d.id).update(hash=hash_key)
            messages.success(request,'Donor Register Successfully')
            return redirect('/donor_register')
    # context={'form':form}
    return render(request,'donor_register.html')
def doctor_register(request):  
    if request.method=='POST':
        frm = DoctorForm(request.POST)  
        if frm.is_valid():
            frm.save()
            #messages.success(request,'Donor Register Successfully')
            return render(request,'doctor_login.html')
    # context={'form':form}
    return render(request,'doctor_register.html')
def doctor_login(request):  
    if request.method=='POST':
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        m=Doctor.objects.filter(uname=uname,pass1=pass1)
        request.session['uname']=uname
        request.session['pass']=pass1
        
        
        if m:
            print(m[0].dname)
            request.session['dname']=m[0].dname
            request.session['email']=m[0].email
            request.session['hname']=m[0].hname
            request.session['demail']=m[0].email
        # if uname=='admin' and pass1=='admin':
            return redirect('/patient_request')
        else:
            messages.success(request,'Invalid Username/Password')

    return render(request,'doctor_login.html')
def donor_list(request):

    frm=Donor.objects.all()
   
    context={'form':frm}
    print(context)
    return render(request,'admin/donor_list.html',context)  
def admin_login(request):  
    if request.method=='POST':
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        if uname=='admin' and pass1=='admin':
            return redirect('/donor_list')
        else:
            messages.success(request,'Login Failed')
    return render(request,'admin_login.html')
def donor_login(request):  
    if request.method=='POST':
        email=request.POST['email']

        cno=request.POST['cno']
        request.session['email']=email
        request.session['cno']=cno
        
        m=Donor.objects.filter(email=email,cno=cno)
        if m:
            return redirect('/donor_death')
        else:
            messages.success(request,'Login Failed')
    return render(request,'donor_login.html')
def doctor_delete(request,id):
   form=Doctor.objects.get(id=id)
   form.delete()
   messages.success(request,'Doctor Delete Successfully')
   return redirect('/donor_list')
def doctor_list(request):

    frm=Doctor.objects.all()
   
    context={'form':frm}
    print(context)
    return render(request,'admin/doctor_list.html',context) 
def patient_request(request):  
    dname=request.session['dname']
    email=request.session['email']
    hname=request.session['hname']
    context={'dname':dname,'hname':hname,'email':email}
    if request.method=='POST':
        frm = PatientForm(request.POST)  
        if frm.is_valid():
            frm.save()
            d=Patient.objects.latest('id')
            print(d.bgroup)
            hash_key = create_hash_key(d.organ)
            print("Hash key:", hash_key)
            frm=Patient.objects.filter(id=d.id).update(hash=hash_key)
            #messages.success(request,'Donor Register Successfully')
            return render(request,'doctor/patient.html')
    # context={'form':form}
    
    return render(request,'doctor/patient.html',context)
def admin_patient_request_list(request):

    frm=Patient.objects.filter(st='Not Donated').values()
   
    context={'form':frm}
    print(context)
    return render(request,'admin/admin_patient_request.html',context) 
def donate_donor_list(request,id):

    frm=Patient.objects.filter(id=id).values()
    # print(frm)
    request.session['pid']=id
    for f in frm:
        
        
        request.session['bgroup']=f['bgroup']
        request.session['organ']=f['organ']
            
    print(request.session['bgroup'])
    print(request.session['organ'])
    
    frm=Donor.objects.filter(st='Available',bgroup=request.session['bgroup'],organ=request.session['organ']).values()
    print(frm)
    if frm:
        context={'form':frm}
        print(context)
        return render(request,'admin/donor_donate.html',context) 
    messages.success(request,'Donor Not Found')
    return redirect('/admin_patient_request_list')

def donate(request,id):

    frm=Donor.objects.filter(id=id).update(st='Donated')
    pat=Patient.objects.filter(id=request.session['pid']).update(st='Donated')
    
    messages.success(request,'Organ Donated Successfully')
    return redirect('/admin_patient_request_list')
def admin_patient_donated_list(request):

    frm=Patient.objects.filter(st='Donated').values()
   
    context={'form':frm}
    print(context)
    return render(request,'admin/patient_donated_list.html',context) 
def admin_donor_donated_list(request):

    frm=Donor.objects.filter(st='Donated').values()
   
    context={'form':frm}
    print(context)
    return render(request,'admin/donor_donated_list.html',context)
def admin_donor_available_list(request):

    frm=Donor.objects.filter(st='Available').values()
   
    context={'form':frm}
    print(context)
    return render(request,'admin/donor_available_list.html',context)
def donor_death(request):
    
    if request.method=='POST':
        ddate=request.POST['ddate']
        email=request.session['email']
        cno=request.session['cno']
        place=request.POST['place']
        frm1=Doctor.objects.filter(place=place).values()
        frm2=Donor.objects.filter(email=email,cno=cno).values()
        msg=""
        for k in frm2:
            dname=k["dname"]
            rname=k["rname"]
            dob=k["dob"]
            gender=k["gender"]
            bgroup=k["bgroup"]
            organ=k["organ"]
            msg=msg+"<h3 style=color:red>Organ Available</h3>"
            msg=msg+"<table cellpadding=0 width=300>"
            msg=msg+"<tr>"
            msg=msg+"<td>Donor Name</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ dname +"</td>"
            msg=msg+"</tr>"
            msg=msg+"<tr>"
            msg=msg+"<td>Relative Name</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ rname +"</td>"
            msg=msg+"</tr>"
            msg=msg+"<tr>"
            msg=msg+"<td>Date-Of-Birth</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ dob +"</td>"
            msg=msg+"</tr>"
            msg=msg+"<tr>"
            msg=msg+"<td>Gender</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ gender +"</td>"
            msg=msg+"</tr>"
            msg=msg+"<tr>"
            msg=msg+"<td>Blood Group</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ bgroup +"</td>"
            msg=msg+"</tr>"
            msg=msg+"<tr>"
            msg=msg+"<td>Organ</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ organ +"</td>"
            msg=msg+"</tr>"
            msg=msg+"<tr>"
            msg=msg+"<td>Date of Death</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ ddate +"</td>"
            msg=msg+"</tr>"        
            msg=msg+"<tr>"
            msg=msg+"<td>Place of Death</td>"
            msg=msg+"<td style=color:green;font-weight:bold>"+ place +"</td>"
            msg=msg+"</tr>"        
            msg=msg+"</table>"        
            
        if request.session['otp1']==request.POST['otp']:
            for k in frm1:
                x=k["place"]
                if x==place:
                    mail=k['email']
                    
                    sendmail(mail,msg)
                print("----------------->",x)
    
            frm=Donor.objects.filter(email=email,cno=cno).update(ddate=ddate,st='Available')
            messages.success(request,'Your Organs Save to Another Life')
        else:
            messages.success(request,'Please Check OTP')
        return render(request,'donor_death.html')
    otp=otp_process()
    msg="<h3>OTP : "+str(otp)+"</h3>"
    sendmail(request.session['email'],msg)
    request.session['otp1']=str(otp)
    return render(request,'donor_death.html')
def doctor_patient_request_list(request):

    frm=Patient.objects.filter(st='Not Donated',demail=request.session['demail']).values()
   
    context={'form':frm}
    print(context)
    return render(request,'doctor/patient_request_list.html',context) 
def doctor_donated_patient_list(request):

    frm=Patient.objects.filter(st='Donated',demail=request.session['demail']).values()
   
    context={'form':frm}
    print(context)
    return render(request,'doctor/patient_donated_list.html',context) 
def patient_delete_request(request,id):
   form=Patient.objects.get(id=id)
   form.delete()
   messages.success(request,'Patient Request Delete Successfully')
   return redirect('/doctor_patient_request_list')
def otp_process():
    import random
    otp=random.randint(1111,9999)
    return otp
def sendmail(to,btext):
    msg = MIMEMultipart('alternative')
    msg['From'] = 'demo2020itech@gmail.com'
    msg['To'] = to
    msg['Subject'] = 'Organs Available'
    body = btext
    msg.attach(MIMEText(body, 'html'))

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('linocoasta@gmail.com', 'bceefffzadjrtfag')
    # server.login('demo2020itech@gmail.com', 'hzgeofewvmrqraam')
    text = msg.as_string()
    server.sendmail('demo2020itech@gmail.com', to, text)
    server.quit()

def index1(request):

    return render(request,'index.html')  
