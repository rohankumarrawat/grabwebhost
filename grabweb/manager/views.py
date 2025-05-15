from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import os
from manager.models import Register,News,Announcement,Ticket,Blog,Invoice,Userdomain,UserService,Service,predevservice
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import uuid
from django.core.mail import send_mail
import razorpay
from datetime import date

import requests
#400 not available
def whois(domain):
    url=f"https://api.connectreseller.com/ConnectReseller/ESHOP/checkDomain?APIKey=38GHnzGmucXJPjT&websiteName={domain}"
    r=requests.get(url)
    data=dict(r.json())
    return data['responseMsg']['statusCode']
   
    
def payinvoice(request):
    d={}
    try:
       
        invoice_id1=request.GET['invoice_id']
        
        x=Invoice.objects.get(checksign=invoice_id1)
     
        d['data']=x
        
        amounttotal=int(float(x.invoice_total))
      
        from django.conf import settings
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount":amounttotal, "currency": "INR"}
        )
        d['payment']=razorpay_order
        
        if x.status ==1:
            return redirect("/dashboard/invoice/")
        
        
        if request.method=="POST":
            
        
            try:
                id12=request.POST['id12']
                orderid=request.POST['orderid']
                signature=request.POST['signature']
                x.orderid=orderid
                x.paymentid=id12
                x.signature=signature
                x.status=1
                x.save()
                if str(x.service_type)=="webdevelopment":
                    
                    lololo=predevservice.objects.create(email=x.email,service_name='Pre WebDevelopment',domain_name=x.domain,first_payment=x.invoice_total,first_payment_date=date.today(),payment_format=2,status=0)
                    lololo.save()
                    send_mail(
    'We have got a PreBuild Web Development Request',
    'PreBuild WebDevelopment.',
    'info@grabwebhost.in',
    ['rohanfreakymg@gmail.com'],
)
                
                    return redirect(f"/currentinvoice?&paymentid={checksign}")
                ds=list(str(x.invoice_data).split(','))
                ds1=list(str(x.invoice_price).split(','))
                
                service=ds[0]
                domain=x.domain
                
              
                try:
                    
                    serviceeee=Service.objects.get(service_name=service).service_no
                except:
                    serviceeee="1"
                    
                
                from datetime import date
                userkadata=Register.objects.get(username=request.user)
                usernam=domain.split('.')[0]
                pa=User.objects.make_random_password()
                
                import pycpanel
                server = pycpanel.conn(hostname='server.grabwebhost.in',username='grabweb', password='19072002ROHANkumar',ssl=True, verify=False, )
                
                params = {
    'username'      : usernam,
    'domain' : domain,
    'contactemail':userkadata.email,
    'password':pa,
    'plan':service
    
}
                try:
                    
                    datata=server.api('createacct', params=params)
                    createdata=UserService.objects.create(status= 1,email=userkadata.email,service_name=service,domain_name=domain,first_payment=amounttotal,first_payment_date=date.today(),payment_format=x.duration,service_no=serviceeee,username=usernam,password=pa,coupan=x.coupan)
                    createdata.save()
                    mail_subject = 'Service Details!'
                    message = render_to_string('serviceemail.html', {
                                   'username': usernam,
                                   'password': pa
                                    })
                    text_content = strip_tags(message)
                    email = EmailMultiAlternatives(
                                    mail_subject,
                                    text_content,
                                    'info@grabwebhost.in',
                                    [userkadata.email]
                                        )
                    email.attach_alternative(message, 'text/html')
                    email.send()
                except:
                      createdata=UserService.objects.create(status= 0,email=userkadata.email,service_name=service,domain_name=domain,first_payment=amounttotal,first_payment_date=date.today(),payment_format=x.duration,service_no=serviceeee,username=usernam,password=pa,coupan=x.coupan)
                      createdata.save()
              
               
                   
                if ds[1]!='0':
                    domaindatacreate=Userdomain.objects.create(status=0,email=userkadata.email,domain_name=domain,first_payment=amounttotal,first_payment_date=date.today(),payment_format=0,provider="connectreseller",NameServer1="ns1.grabwebhost.in",NameServer2="ns2.grabwebhost.in",NameServer3="ns3.grabwebhost.in",NameServer4="ns4.grabwebhost.in",privacy_protection=1,email_service=0,dns_service=1,coupan="0")
                    domaindatacreate.save()  
                return redirect(f"/currentinvoice?&paymentid={x.checksign}")
            except :
                name12=request.POST['name']
                return redirect("/")
        
            
    except:
        
        return redirect("/dashboard/invoice/")
    return render(request,"paymentprocessing.html",d)
def invoice(request):
    d={}
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=Register.objects.get(username=request.user)
        
        
        
        d={'news':news,'announcement':news0,'photo':dataa.user_photo}
        d['invoice']=Invoice.objects.all().filter(email=dataa.email)
    else:
        return redirect('/dashboard/login/')  
    return render(request,'invoice.html',d)
def myservice(request):
    d={}
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'photo':dataa.user_photo}
        d['invoice']=UserService.objects.all().filter(email=dataa.email)
        d['invoice2']=predevservice.objects.all().filter(email=dataa.email)
    else:
        return redirect('/dashboard/login/')  
    return render(request,'myservice.html',d)
def mydomain(request):
    d={}
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'photo':dataa.user_photo}
        d['invoice']=Userdomain.objects.all().filter(email=dataa.email)
    else:
        return redirect('/dashboard/login/')  
    return render(request,'mydomain.html',d)
def index(request):

    if request.user.is_superuser:
        return redirect("/admin")
    d={}
    
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=Register.objects.get(username=request.user)
        datalen=len(UserService.objects.all().filter(email=dataa.email))
        datalen2=len(predevservice.objects.all().filter(email=dataa.email))
        d={'news':news,'announcement':news0,'photo':dataa.user_photo,'ser':datalen+datalen2}
    else:
        return redirect('/dashboard/login/')

    
    return render(request,'dashboard.html',d)
def secondway(request):
   
    if request.user.is_active:
        return redirect('/dashboard/')
    else:

        user=request.session.get('user')
        
        x=User.objects.get(username=str(user))

      
        x1=Register.objects.get(username=str(user))
      
        
   
        if request.method=="POST":
            try:
                otp=request.POST['otp']
              
                if str(otp)==str(x1.verify_number):
                           
                           
                            del request.session['user']
                            user = x
                            login(request,user)
                            mail_subject = 'Account Accessed!'
                            message = render_to_string('accountlogin.html', {
                           'details': "grabwebhost"
                            })
                            text_content = strip_tags(message)
                            email = EmailMultiAlternatives(
                            mail_subject,
                            text_content,
                            'info@grabwebhost.in',
                            [x1.email]
                            )
                            email.attach_alternative(message, 'text/html')
                            email.send()
                            
                            return redirect('/dashboard/')
                else:
                    messages.success(request,"Invalid OTP")
            except:

              
           
                import random
                number=random.randint(10000,99000)
                x1=Register.objects.get(username=str(user))
                x1.verify_number=number
                x1.save()
                mail_subject = 'One Time Password.'
                message = render_to_string('2way.html', {
                           'otp': number
                        })
                text_content = strip_tags(message)
                email = EmailMultiAlternatives(
                mail_subject,
                text_content,
                'info@grabwebhost.in',
                [x1.email])
                email.attach_alternative(message, 'text/html')
                email.send()
              
                messages.success(request,"OTP Sent")

            
        
    return render(request,"2ways.html")
def login_view(request):
    username=""
    
    if request.user.is_active:
        return redirect('/dashboard/')
        
    else:
        
        if request.method=="POST":
            email=request.POST['email'].lower()
            password=request.POST['password']
            try:
                username =User.objects.get(email=email.lower()).username
            except :
                pass
            user = authenticate(username=username, password=password)

          
            
            if user is not None:
               
                checkverify=Register.objects.get(email=email)
      

                if checkverify.email_verify ==0:
                    
                    send_email_token(email,checkverify.email_token)
                    messages.success(request,"Verification Email Send Please verify Email first")
                    return redirect("/dashboard/login/")
                    
                    
                else:
                    if checkverify.authtype ==2:
                        request.session['user']=username
                        import random
                        number=random.randint(10000,99000)
                        x1=Register.objects.get(username=username)
                        x1.verify_number=number
                        x1.save()
                        mail_subject = 'One Time Password.'
                        message = render_to_string('2way.html', {
                           'otp': number
                        })
                        text_content = strip_tags(message)
                        email = EmailMultiAlternatives(
                        mail_subject,
                        text_content,
                        'info@grabwebhost.in',
                        [email]
                                )
                        email.attach_alternative(message, 'text/html')
                        email.send()
                       
                        return redirect("/dashboard/secondway/")
                    else:
                    
                        login(request , user)
                        mail_subject = 'Account Accessed!'
                        message = render_to_string('accountlogin.html', {
                           'details': "GrabwebHost"
                        })
                        text_content = strip_tags(message)
                        email = EmailMultiAlternatives(
                        mail_subject,
                        text_content,
                        'info@grabwebhost.in',
                        [email]
                                )
                        email.attach_alternative(message, 'text/html')
                        email.send()
                     
                        return redirect("/dashboard/")
                
               
                  
                    
            else:
                messages.success(request,"Invalid Credentials")

        

    return render(request,'login.html')
    
def register(request):
    
    user1=""
    email1=""
    if request.user.is_superuser:
        return redirect("/admin")
    if request.user.is_active:
        return redirect('/dashboard/')
    else:
        if request.method=="POST":
            firstname=request.POST.get('firstname')
        
            username=request.POST.get('username')
            email=request.POST.get('email').lower()
            country=request.POST.get('country')
            phone=request.POST.get('number')
            address=request.POST.get('address')
            pincode=request.POST.get('pincode')
            city=request.POST.get('city')
            password=request.POST.get('password')
        
            try:
                user1= User.objects.get(username=username)
                
            
            except:
                pass
            try:
                email1= User.objects.get(email=email)
            except:
                pass

            if user1:
                    messages.error(request,"UserName already exist")
            elif email1:
                    messages.error(request,"Email already exist")

            else:
                   
                    user = User.objects.create_user(username, email, password)
                    user.first_name=firstname
                    user.last_name=""
                    user.save()
                    b=Register.objects.create(email=email,username=username,first_name=firstname,last_name="",country=country,email_verify=0,usertype=2,phone=phone,address=address,authtype=0,affiliate=0,notificationews=1,notification=1,notificationannouncement=1,notify=0,user_photo="media/default.png",pincode=pincode,city=city,email_token=str(uuid.uuid4()))
                    send_email_token(email,b.email_token)
                    b.save()            
                    messages.success(request,"Account Created Succesfully Now Please Verify Your EMail That has sent to your Email id ")
                    return redirect('/dashboard/login/')
            

    return render(request,'register.html')
def send_email_token(email,token):
    mail_subject = 'Activate your account.'
    link=f'https://grabwebhost.in/verify?token={token}'
    message = render_to_string('verification.html', {
                           'link': link
                        })
    text_content = strip_tags(message)
    email = EmailMultiAlternatives(
        mail_subject,
        text_content,
        'info@grabwebhost.in',
        [email]
    )
    email.attach_alternative(message, 'text/html')
    email.send()
  
def send_email_token2(email,token):
    mail_subject = 'Change Your Password.'
    link=f'https://grabwebhost.in/forget?token={token}'
    message = render_to_string('forgetverification.html', {
                           'link': link
                        })
    text_content = strip_tags(message)
    email = EmailMultiAlternatives(
        mail_subject,
        text_content,
        'info@grabwebhost.in',
        [email]
    )
    email.attach_alternative(message, 'text/html')
    email.send()
   

def forgot(request):
    if request.user.is_active:
        return redirect('/dashboard/')
    else:
        d={'email':"Your Email Id",}
        global otpnumber
        global email
        global ucome
        if request.method=="POST":
           
                email=request.POST['email'].lower()
                try:
                    x=Register.objects.get(email=email)
                    if x:
                        email_token=str(uuid.uuid4())
                        x.email_token=email_token
                        x.save()
                        send_email_token2(email,email_token)
                    
    
                        messages.success(request,"Email has been Sent to your email Id")
                        return redirect("/dashboard/login/")
                except:
                    messages.success(request,"Email id not found")
                    return redirect('/dashboard/forgot/')
                    

    return render(request,'forget.html',d)
def profile(request):
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=User.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'username':request.user,'email':dataa.email}
        data=Register.objects.get(username=request.user)
        d['data']=data
        d['photo']=data.user_photo
        if request.method=="POST":
            first=request.POST['firstname']
            last=request.POST['lastname']
            email=request.POST['email'].lower()
            if data.email== email:
                messages.success(request,"Email ALready Exist")
            else:
                data.email=email
                data.first_name=first
                data.last_name=last
                data.save()
                messages.success(request,"please Verify Your Email")
                logout(request)
                return redirect("/dashboard/emailverify/")

    else:
        return redirect('/')
    return render(request,'profile.html',d)
def blog(request):
    if request.user.is_active:
       
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=Register.objects.get(username=request.user)
        post=Blog.objects.filter().all()
        d={'news':news,'announcement':news0,'photo':dataa.user_photo,'post':post,'len1':len(post)}
    else:
        return redirect('/dashboard/login/')

    return render(request,'blog.html',d)
def profile2(request):
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'username':request.user,'data':dataa,'photo':dataa.user_photo}

        
        if dataa.notificationews==1:
            d['checkednews']='checked'
        if dataa.notificationannouncement==1:
            d['checkannouncement']='checked'
        if dataa.authtype==2:
            d['auth']='checked'
        if request.method=="POST" :
            try:
                user_photo = request.FILES['photo']
            except:
                 user_photo=dataa.user_photo
            phone=request.POST['phone']
            address=request.POST['address']
            about=request.POST['about']
            insta=request.POST['insta']
            twitter=request.POST['twitter']
            linkedIn=request.POST['linkedIn']
            notificationews=request.POST.get('checkednews','0')
            notificationannouncement=request.POST.get('checkannouncement','0')
            autht=request.POST.get('auth','0')
            dataa.user_photo=user_photo
            dataa.phone=phone
            dataa.authtype=autht
            dataa.address=address
            dataa.about=about
            dataa.insta=insta
            dataa.twitter=twitter
            dataa.linkedIn=linkedIn
            print(notificationews)
            if notificationews=='1':
                dataa.notificationews=1
            else:
                dataa.notificationews=0
            if notificationannouncement=='1':
                dataa.notificationannouncement=1
            else:
                dataa.notificationews=0
            dataa.save()
            messages.success(request,"Data Updated")
            return redirect("/dashboard/privacy_profile/")

    else:
        return redirect('/dashboard/login/')
    return render(request,'profile2.html',d)
def openticket(request):
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=User.objects.get(username=request.user)
        dataa1=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'username':request.user,'email':dataa.email,'photo':dataa1.user_photo}
      
        
       
       
        if request.method == 'POST':
            subject=request.POST['subject']
            data=request.POST['data']
            priority=request.POST['priority']
            dump=Ticket.objects.create(email=dataa.email,username=request.user,subject=subject,data=data,priority=priority,status=2)
            dump.save()
            mail_subject = 'New Ticket Created'
            message = render_to_string('newticket.html', {
                           'username': request.user
                        })
            text_content = strip_tags(message)
            email = EmailMultiAlternatives(
            mail_subject,
            text_content,
            'info@grabwebhost.in',
            [dataa.email,'info@grabwebhost.in']
            )
            email.attach_alternative(message, 'text/html')
            email.send()
           
            messages.success(request,"Ticket Submitted")
            return redirect('/dashboard/ticket/')
            
    else:
        return redirect('/dashboard/login/')

    
   
    return render(request,'openticket.html',d)
def ticket(request):
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        totlticket=Ticket.objects.filter(username=request.user)
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'lentik':len(totlticket),'data':totlticket,'photo':dataa.user_photo}

    else:
        return redirect('/dashboard/login/')

    
   
    return render(request,'ticket.html',d)
def news(request):
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=Register.objects.get(username=request.user)
        post=News.objects.filter().all()
        d={'news':news,'announcement':news0,'photo':dataa.user_photo,'post':post,'len1':len(post)}
    else:
        return redirect('/dashbaord/login/')
    return render(request,'news.html',d)
def changepassword(request):
    if request.user.is_active:
        news=News.objects.all().order_by('news_id')[:2]
        news0=Announcement.objects.all().order_by('accouncement_id')[:2]
        dataa=User.objects.get(username=request.user)
        dataa1=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'username':request.user,'email':dataa.email,'photo':dataa1.user_photo}
        if request.method=="POST":
            oldpassword=request.POST['password']
            newpass=request.POST['p1']
            newpass2=request.POST['p2']
            user=authenticate(username=request.user,password=oldpassword)
            if user is not None:
                if newpass==newpass2:
                    x=User.objects.get(username=request.user)
                    x.set_password(newpass2)
                    x.save()
                    
                    return redirect('/dashboard/')
                else:
                    messages.success(request,"New Password Doesn't Match")

            else:
                messages.success(request,"You have Entered Invalid Password")
    else:
        return redirect('/dashboard/')
    
    return render(request,'changepassword.html',d)
def logout1(request):
    if request.user.is_active:
        logout(request)
        return redirect('/')

    else:
        return redirect('/dashboard/login/')
def securitypin(request):
    x=Register.objects.get(username=request.user).pin
    messages.success(request,f"Security pin is{x}")
    return redirect('/dashboard/')

