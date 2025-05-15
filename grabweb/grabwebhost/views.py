from django.shortcuts import render,redirect
from manager.models import Register,Service,UserService,Domain,Coupan,cart,Invoice,Userdomain,News,Announcement,CustomWebDev,predev,predevservice
from django.contrib.auth.models import User
from datetime import date
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import uuid
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import os
from django.http import HttpResponse
from django.contrib import messages

import razorpay
import uuid
import requests
import requests
#400 not available
def whois(domain):
    url=f"https://api.connectreseller.com/ConnectReseller/ESHOP/checkDomain?APIKey=38GHnzGmucXJPjT&websiteName={domain}"
    r=requests.get(url)
    data=dict(r.json())
    return data['responseMsg']['statusCode']
from manager.views import send_email_token
username=""
promotion=""
def predevelopedcheckout(request):
    global username
    global promotion
    user1=""
    global godata
    email1=""
    global dataa
    global x1x1
    x1x1=""
  
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    try:
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'photo':dataa.user_photo}
    except:
        dataa="None"
        d={'news':news,'announcement':news0}
    data=request.GET['data']
    try:
        x1x1=predev.objects.get(name=data)
        d['x1x1']=x1x1
    except:
        return redirect("/prebuild")
    if request.method=="POST":
        try:
            email=request.POST['email'].lower()
            password=request.POST['password']
            url=request.POST['url']
            try:
                username=User.objects.get(email=email.lower()).username
            except :
                pass
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                checkverify=Register.objects.get(email=email)
                
                if checkverify.email_verify ==0:
                    
                    send_email_token(email,checkverify.email_token)
                    messages.success(request,"Verification Email Send Please verify Email first")
                    return redirect(f"{url}")
                    
                    
                else:
                        
                        login(request , user)
                        dataa=Register.objects.get(username=request.user)
                        mail_subject = 'Account Accessed!'
                        message = render_to_string('accountlogin.html', {
                           'details': "GrabWebHost"
                        })
                        text_content = strip_tags(message)
                        email = EmailMultiAlternatives(
                        mail_subject,
                        text_content,
                        'info@grabwebhost.in',
                        [email]
                                )
                        email.attach_alternative(message, 'text/html')
                        #email.send()
                        return redirect(f"{url}")
                
               
                  
                    
            else:
                messages.success(request,"Invalid Credentials")
                return redirect(f"{url}")
        except:
                    
                   pass
        try:
                    firstname=request.POST.get('firstname')
                    lastname=request.POST.get("lastname","")
                    username=request.POST.get('username')
                    email=request.POST.get('email12').lower()
                    url=request.POST['url']
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
                            return redirect(f"{url}")
                    elif email1:
                            messages.error(request,"Email already exist")
                            return redirect(f"{url}")
        
                    else:
                            user = User.objects.create_user(username, email, password)
                            user.first_name=firstname
                            user.last_name=lastname
                            user.save()
                            b=Register.objects.create(email=email,username=username,first_name=firstname,last_name=lastname,country=country,email_verify=0,usertype=2,phone=phone,address=address,authtype=0,affiliate=0,notificationews=1,notification=1,notificationannouncement=1,notify=0,user_photo="media/default.png",pincode=pincode,city=city,email_token=str(uuid.uuid4()))
                            send_email_token(email,b.email_token)
                            b.save()
       
                            messages.success(request,"Account Created Succesfully Now Please Verify Your EMail That has sent to your Email id ")
        
                            return redirect(f"{url}")
        except:
            
            
            pass
        
        
            
        try:
            
            domainname=request.POST['domain']
            
           
            
            service='basic'
          
            
            if  str(domainname)[-1:-4:-1]=='ni.':
                
           
                dom=whois(domainname)
             
                if dom==400:
                    messages.success(request,"Domain Already Taken")
                    return redirect(f"/predevelopedcheckout/?data={x1x1.name}")
                else:
                    ccc=str(uuid.uuid4())
                    tot=int(x1x1.price)*100
                    a=Invoice.objects.create(domain=domainname,duration='3',coupan="no",invoicetype=0,due_date=date.today(),generates_date=date.today(),status=0,invoice_total=tot,invoice_price=tot,invoice_data=f"{service},{domainname},{x1x1.name}",service_no=x1x1.service_no,service_type="webdevelopment",email=dataa.email,firstname=dataa.first_name,lastname=dataa.last_name,checksign=ccc)
                    a.save()
                    mail_subject = 'Invoice Created!'
                    message = render_to_string('invoiceemail.html', {
                                  'details': f"https://grabwebhost.in/currentinvoice?&paymentid={ccc}"
                                    })
                    text_content = strip_tags(message)
                    email = EmailMultiAlternatives(
                                    mail_subject,
                                    text_content,
                                    'info@grabwebhost.in',
                                    [dataa.email]
                                        )
                    email.attach_alternative(message, 'text/html')
                    #email.send()
                    return redirect("/dashboard/invoice/")
            else:
                messages.success(request,"only .in Domain is freely Availble")
                return redirect(f"/predevelopedcheckout/?data={x1x1.name}")
        except:
            pass
                
    
    return render(request,"predevinformation.html",d)
    
    
def webdev(request):
    return render(request, "webdevelopment.html")

def prebuild(request):
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    try:
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'photo':dataa.user_photo}
    except:
        dataa="None"
        d={'news':news,'announcement':news0}
    post=predev.objects.filter().all()
    d['post']=post
    d['len1']=len(post)
   
        
    return render(request,"prebuild.html",d) 
def webdevcustom(request):
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    try:
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'photo':dataa.user_photo}
    except:
        dataa="None"
        d={'news':news,'announcement':news0}
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        number=request.POST['number']
        type1=request.POST['type']
        Discription=request.POST['Discription']
        datasave=CustomWebDev.objects.create(email=email,name=name,number=number,webtype=type1,discription=Discription)
        datasave.save()
        messages.success(request,"We have Received Your request, we will get back to you as soon as possible")
        send_mail(
    'We have got a custom Web Development Request',
    'Custom WebDevelopment.',
    'info@grabwebhost.in',
    ['rohanfreakymg@gmail.com'],
)
        
        return redirect('/webdevcustom/')
    return render(request, "customwebcheckout.html",d) 
def refund(request):
    return render(request, "refund.html")
def test(request):
    send_mail(
    'This is going to be test mail',
    'lololol.',
    'info@grabwebhost.in',
    ['rohanfreakymg@Gmail.com'],
)
    return render(request, "commingsoon.html")
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email'].lower()
        phone=request.POST['phone']
        message=request.POST['message']
        messagee=message+name
        send_mail('Contact US', messagee, email, ['info@grabwebhost.in'])
        messages.success(request,"We have Received Your request and working on it ")
        
    return render(request,"contactus.html")
def blog(request):
   
    return render(request, "commingsoon.html")
def aboutus(request):
   
    return render(request, "aboutus.html")
def sharedhosting(request):
    return render(request, "shared.html")
def domain(request):
    if request.method=="POST":
        domain_name=request.POST['domain']
        if "." not in domain_name:
            domain_name+=".com"
        return redirect(f'/domainresult?currentdomain={domain_name}')
    return render(request, "domain.html")
def domaincart(request):
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    dataa=Register.objects.get(username=request.user)
    d={'news':news,'announcement':news0,'photo':dataa.user_photo}
    domain=request.GET['domain']
    priice=request.GET['price']
    pricecurre=request.session.get('pricedomain')
    d['domain']=domain
    d['price']=pricecurre
    if priice==pricecurre:
        if request.method=="POST":
            ns1=request.POST['n1']
            ns2=request.POST['n2']
            ns3=request.POST.get('n3','NS3.grabwebhost.in')
            ns4=request.POST.get('n4','NS4.grabwebhost.in')
            request.session['ns1']=ns1
            request.session['ns2']=ns2
            request.session['ns3']=ns3
            request.session['ns4']=ns4
            request.session['pricedomain']=priice
            return redirect(f'/domainreview?domain={domain}&price={priice}')
    else:
        return redirect("/domain/")
        
    return render(request,'domaincart.html',d)
def domainreview(request):
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    dataa=Register.objects.get(username=request.user)
    d={'news':news,'announcement':news0,'photo':dataa.user_photo}
    domain=request.GET['domain']
    priice=request.GET['price']
    pricecurre=request.session.get('pricedomain')
    d['domain']=domain
    d['price']=pricecurre
    
    if priice==pricecurre:
      if request.method=="POST":
        try:
            email=request.POST['email'].lower()
            password=request.POST['password']
            url=request.POST['url']
            try:
                username=User.objects.get(email=email.lower()).username
            except :
                pass
            user = authenticate(username=username, password=password)
            if user is not None:
               
                checkverify=Register.objects.get(email=email)
                if checkverify.email_verify ==0:
                    
                    send_email_token(email,checkverify.email_token)
                    messages.success(request,"Verification Email Send Please verify Email first")
                    return redirect(f"{url}")
                    
                    
                else:
                       

                        login(request , user)
                        mail_subject = 'Account Accessed!'
                        message = render_to_string('accountlogin.html', {
                           'details': ip
                        })
                        text_content = strip_tags(message)
                        email = EmailMultiAlternatives(
                        mail_subject,
                        text_content,
                        'info@grabwebhost.in',
                        [email]
                                )
                        email.attach_alternative(message, 'text/html')
                        #email.send()
                        return redirect(f"{url}")
                
               
                  
                    
            else:
                messages.success(request,"Invalid Credentials")
                return redirect(f"{url}")
        except:
                    
                   pass
        try:
                    firstname=request.POST.get('firstname')
                    lastname=request.POST.get("lastname","")
                    username=request.POST.get('username')
                    email=request.POST.get('email').lower()
                    url=request.POST['url']
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
                            os.system(f"mkdir {username}")
                            user = User.objects.create_user(username, email, password)
                            user.first_name=firstname
                            user.last_name=lastname
                            user.save()
                            b=Register.objects.create(email=email,username=username,first_name=firstname,last_name=lastname,country=country,email_verify=0,usertype=2,phone=phone,address=address,authtype=0,affiliate=0,notificationews=1,notification=1,notificationannouncement=1,notify=0,user_photo="media/default.png",pincode=pincode,city=city,email_token=str(uuid.uuid4()))
                            send_email_token(email,b.email_token)
                            b.save()
                            
                           
                         
                            
                            
                           
                          
                            messages.success(request,"Account Created Succesfully Now Please Verify Your EMail That has sent to your Email id ")
        
                            return redirect(f"{url}")
        except:
            
            
            pass
        try:
            promotion=request.POST['promotion']
            url=request.POST['url']
            try:
                
                x=Coupan.objects.get(coupan=promotion)
                
                if str(x.service_name).lower() == str(request.GET['hosting']).lower():
                    from datetime import datetime
                    max_date=(x.coupan_final).strftime('%Y-%m-%d')
                    today=datetime.today().strftime('%Y-%m-%d')
                    if x.applytonew==1:
                        
                            data=UserService.objects.all().filter(username=request.user)
                           
                            if len(data)>0:
                                messages.error(request,"Coupan Not Valid")
                                return redirect(f"{url}")
                    
                    if today<=max_date:
                        
                        percent=x.discountpercent
                        request.session['coupan']=promotion
                        messages.error(request,"Coupan Applied")
                        return redirect(f"{url}&discount={percent}")
                        
                    else:
                        
                        messages.error(request,"Coupan Expired")
                        return redirect(f"{url}")
                else:
                    messages.error(request,"Coupan Doen't Exist")
                        
                    
            except:
                messages.error(request,"Coupan Doen't Exist")
                return redirect(f"{url}")
        except:
            pass
        try:
            
            add=request.POST['add']
       
            a=cart.objects.create(email=Register.objects.get(username=request.user).email,service_name=d['domain'],service_type='domain',service_no=1)
            a.save()
            return redirect('/services/')
            
        except:
       
            price=request.POST['price']
            url=request.POST['url']
            domain=request.POST['domain']
            price=float(price)
            price=price*100
            request.session['tokencheck']=str(uuid.uuid4())
            request.session['amounttotal']=price
            url=url+f"&tokencheck={request.session.get('tokencheck')}&amounttotal={request.session.get('amounttotal')}"
            url=url.replace("domainreview","paymentprocessingdomain")
            from datetime import date
            dp=Register.objects.get(username=request.user)
            
          
            a=Invoice.objects.create(domain=domain,duration=12,coupan="None",invoicetype=0,due_date=date.today(),generates_date=date.today(),status=0,invoice_total=price,invoice_price=f"0,{price},0",invoice_data=f"0,{domain}",service_no=1,service_type="Domain",email=dp.email,firstname=dp.first_name,lastname=dp.last_name,checksign=request.session.get('tokencheck'))
            a.save
            mail_subject = 'Invoice Created!'
            message = render_to_string('invoiceemail.html', {
                           'details': f"https://grabwebhost.in/currentinvoice?&paymentid={request.session.get('tokencheck')}"
                            })
            text_content = strip_tags(message)
            email = EmailMultiAlternatives(
                            mail_subject,
                            text_content,
                            'info@grabwebhost.in',
                            [email]
                            )
            email.attach_alternative(message, 'text/html')
            #email.send()
                
            return redirect(f"{url}")
    else:
        return redirect(f"/domain")
    return render(request,'domainreview.html',d)

    
def paymentprocessingdomain(request):
    domain=request.GET['domain']
    tokencheck=request.GET['tokencheck']
    amounttotal=request.GET['amounttotal']
    d={'domain':domain,'amounttotal':amounttotal,'tokencheck':tokencheck}
    checktpken=Invoice.objects.get(checksign=tokencheck)
    if tokencheck == str(request.session.get('tokencheck')) and amounttotal == str(request.session.get('amounttotal')):
        amounttotal=int(float(amounttotal))
    else:
        return redirect("/domain")
    from django.conf import settings
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    razorpay_order = client.order.create(
            {"amount":amounttotal, "currency": "INR", "payment_capture": "1"}
        )
    d['payment']=razorpay_order
    if request.method=="POST":
        
        try:
            id12=request.POST['id12']
            orderid=request.POST['orderid']
            signature=request.POST['signature']
            checktpkn=Invoice.objects.get(checksign=tokencheck)
            checktpkn.orderid=orderid
            checktpkn.paymentid=id12
            checktpkn.signature=signature
            checktpkn.status=1
            checktpkn.save()
            mail_subject = 'Invoice updated!'
            message = render_to_string('invoiceemail.html', {
                           'details': f"https://grabwebhost.in/currentinvoice?&paymentid={tokencheck}"
                            })
            text_content = strip_tags(message)
            email = EmailMultiAlternatives(
                            mail_subject,
                            text_content,
                            'info@grabwebhost.in',
                            [email]
                            )
            email.attach_alternative(message, 'text/html')
            #email.send()
            userdetail=Register.objects.get(username=request.user)
            from datetime import date
            userd=Register.objects.get(username=request.user)
            domaindatacreate=Userdomain.objects.create(status=0,email=userdetail.email,domain_name=domain,first_payment=amounttotal,first_payment_date=date.today(),payment_format=0,provider="connectreseller",NameServer1=request.session.get("ns1"),NameServer2=request.session.get("ns2"),NameServer3=request.session.get("ns3"),NameServer4=request.session.get("ns4"),privacy_protection=1,email_service=0,dns_service=1,coupan="0")
            domaindatacreate.save()  
            return redirect(f"/currentinvoice?&paymentid={tokencheck}")
        except:
            name12=request.POST['name']
            return redirect("/")
            
            
            
    return render(request,"paymentprocessingdomain.html",d)
    
def domainresult(request):
    d={}
    
    try:
        domainname=request.GET['currentdomain']
    except:
         return redirect("/domain/")

 
    if request.method=="POST":
            try:
                domain_name=request.POST['name']
                if "." not in domain_name:
                    domain_name+=".com"
                
                return redirect(f'/domainresult?currentdomain={domain_name}')
            except:
                domain=request.POST['domain']
                price=request.POST['price']
                request.session['pricedomain']=price
                return redirect(f'/domaincart?domain={domain}&price={price}')
        
    response=requests.get(f'https://api.connectreseller.com/ConnectReseller/ESHOP/checkdomainavailable?APIKey=38GHnzGmucXJPjT&websiteName={domainname}').json()
    d['domain']=domainname
    d['domainstatus']=response['responseMsg']['statusCode']
    if d['domainstatus']==200:
                d['price']=int(response['responseData']['registrationFee'])+50
    # domainpurelen=domainname.find('.')
    # d['domainpure']=domainname[:domainpurelen]
    # domainpure=domainname[:domainpurelen]
    # try:
    #             newdomainone=domainpure+".in"
    #             whois.whois(newdomainone)
    #             d['domainstatusin']=0
    # except:
    #             d['domainstatusin']=200
    #             d['pricein']=Domain.objects.get(domain_extention=".in").price
    # try:
    #             newdomainone=domainpure+".net"
    #             whois.whois(newdomainone)
    #             d['domainstatusnet']=0
                
    # except:
    #             d['domainstatusnet']=200
    #             d['pricenet']=Domain.objects.get(domain_extention=".net").price
    # try:
    #             newdomainone=domainpure+".org"
    #             whois.whois(newdomainone)
    #             d['domainstatusorg']=0
                
    # except:
    #             d['domainstatusorg']=200
    #             d['priceorg']=Domain.objects.get(domain_extention=".org").price
    # try:
    #             newdomainone=domainpure+".info"
    #             whois.whois(newdomainone)
    #             d['domainstatusinfo']=0
    # except:
    #             d['domainstatusinfo']=200
    #             d['priceinfo']=Domain.objects.get(domain_extention=".info").price
    # try:
    #             newdomainone=domainpure+".xyz"
    #             whois.whois(newdomainone)
    #             d['domainstatusxyz']=0
    # except:
    #             d['domainstatusxyz']=200
    #             d['pricexyz']=Domain.objects.get(domain_extention=".xyz")
    # try:
    #             newdomainone=domainpure+".buzz"
    #             whois.whois(newdomainone)
    #             d['domainstatusbuzz']=0
    # except:
    #             d['domainstatusbuzz']=200
    #             d['pricebuzz']=Domain.objects.get(domain_extention=".buzz")
    # try:
    #             newdomainone=domainpure+".cam"
    #             whois.whois(newdomainone)
    #             d['domainstatuscam']=0
    # except:
    #             d['domainstatuscam']=200
    #             d['pricecam']=Domain.objects.get(domain_extention=".cam")
    return render(request, "domainresult.html",d)
        
def services(request):
    return render(request, "service.html")
 
def resellerhosting (request):
    return render(request, "reseller.html")
def feature(request):
    return render(request, "features.html")

def tac(request):
    return render(request, "tac.html")
def pap(request):
    return render(request, "pap.html")
def faq(request):
    return render(request, "faq.html")
    
def index(request):
        username=""
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
                    
                    #send_email_token(email,checkverify.email_token)
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
                        #email.send()
                     
                        return redirect("/dashboard/secondway/")
                    else:
                        
                       

                        login(request , user)
                        mail_subject = 'Account Accessed!'
                        message = render_to_string('accountlogin.html', {
                           'details': 'grabwebhost'
                        })
                        text_content = strip_tags(message)
                        email = EmailMultiAlternatives(
                        mail_subject,
                        text_content,
                        'info@grabwebhost.in',
                        [email]
                                )
                        email.attach_alternative(message, 'text/html')
                        #email.send()
                        
                        return redirect("/")
                
               
                  
                    
            else:
                messages.success(request,"Invalid Credentials")
                return redirect("/")

        return render(request, "index.html")
def verify(request):
    token=request.GET['token']
    try:
        obj=Register.objects.get(email_token=token)
        obj.email_verify=1
        obj.save()
        return render(request,'verified.html')
    except:
        return render(request,"invalid.html")
def forget(request):
    token=request.GET['token']
    try:
        obj=Register.objects.get(email_token=token)
        if request.method=="POST":
             password=request.POST['password']
             password1=request.POST['password1']
             if password==password1:
                u = User.objects.get(username=obj.username)
                u.set_password(password)
                u.save()
                messages.error(request,"Password Changed")
                mail_subject = 'PassWord Changed!'
                message = render_to_string('passwordchange.html')
                text_content = strip_tags(message)
                email = EmailMultiAlternatives(
                mail_subject,
                text_content,
                'info@grabwebhost.in',
                [obj.email]
                )
                
                return redirect ('/dashboard/login/')
             else:
                  messages.error(request,"Password Doesn't match")
        return render(request,'forgetpass.html')
    except:
        return render(request,"invalid.html")
def shared(request):
    
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    try:
        dataa=Register.objects.get(username=request.user)
        d={'news':news,'announcement':news0,'photo':dataa.user_photo}
    except:
        dataa="None"
        d={'news':news,'announcement':news0}
    hosting=request.GET['hosting']
    try:
        x=Service.objects.get(service_name=hosting)
        if request.method=="POST":
            try:
                newdomain=request.POST['newdomain'].lower()
                if '.' in  newdomain:
                    request.session['domainget']='newdomain'
                    return redirect(f"/paymentinformation/?hosting={hosting}&domainget=newdomain&domain={newdomain}")
                else:
                    messages.error(request,"Please Enter Valid Domain Name")
                    return redirect(f"/shared/?hosting={hosting}")
                    
                    
            except:
                alreadydomain=request.POST['alreadydomain'].lower()
                if '.' in  alreadydomain:
                    request.session['domainget']='alreadydomain'
                    try:
                        all=UserService.objects.get(domain_name=alreadydomain)
                    except:
                
                        all=1
                    if all==1:
                     return redirect(f"/paymentinformation/?hosting={hosting}&domainget=alreadydomain&domain={alreadydomain}")
                    else:
                         messages.error(request,"Domain already Exist")
                         return redirect(f"/shared/?hosting={hosting}")
                
                    
                else:
                    messages.error(request,"Please Enter Valid Domain Name")
                    return redirect(f"/shared/?hosting={hosting}")
                
                
    except:
        return redirect('/sharedhosting/')
    
    return render(request,"secondhostingcheckout.html",d)

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
    #email.send()
    
def paymentinformation(request):
    global username
    global promotion
    user1=""
    email1=""
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    
    hosting=request.GET['hosting']
    domainget=request.GET['domainget']
    domain=request.GET['domain'].lower()
    d={'hosting':hosting,'domain':domain,'domainget':domainget,'news':news,'announcement':news0}
    try:
        dataa=Register.objects.get(username=request.user)
        d['photo']=dataa.user_photo
    except:
        dataa="None"
    
    try:
        discount=request.GET['discount']
        promotion=request.session.get('coupan')
        x1=Coupan.objects.get(coupan=promotion)
        d['discount']=discount
        d['placeholder']=promotion
       
    except:
        d['discount']=0
        d['placeholder']="Apply Promo Code"
    d['domainprice']=0
    if domainget == "newdomain":
        
         
        doma=whois(domain)
        if doma==400:
            messages.error(request,"Domain Not Available")
            return redirect(f"/shared/?hosting={hosting}")
        else:
            price=Domain.objects.get(domain_extention=domain[domain.find('.'):]).price
            d['domainprice']=price

            
    try:
    
        x=Service.objects.get(service_name=hosting)
        d['serviceprice']=x.price
        d['serviceprice12']=x.price12
        d['serviceprice3']=x.price3
        d['serviceprice6']=x.price6
        if str(request.session.get('domainget'))==str(domainget):
            pass
        else:
            return redirect("/sharedhosting/")
        
    except:
         return redirect('/sharedhosting/')
    if request.method=="POST":
        try:
            email=request.POST['email'].lower()
            password=request.POST['password']
            url=request.POST['url']
            try:
                username=User.objects.get(email=email.lower()).username
            except :
                pass
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                checkverify=Register.objects.get(email=email)
                
                if checkverify.email_verify ==0:
                    
                   # send_email_token(email,checkverify.email_token)
                    messages.success(request,"Verification Email Send Please verify Email first")
                    return redirect(f"{url}")
                    
                    
                else:
                        
                        login(request , user)
                        mail_subject = 'Account Accessed!'
                        message = render_to_string('accountlogin.html', {
                           'details': "GrabWebHost"
                        })
                        text_content = strip_tags(message)
                        email = EmailMultiAlternatives(
                        mail_subject,
                        text_content,
                        'info@grabwebhost.in',
                        [email]
                                )
                        email.attach_alternative(message, 'text/html')
                        #email.send()
                        return redirect(f"{url}")
                
               
                  
                    
            else:
                messages.success(request,"Invalid Credentials")
                return redirect(f"{url}")
        except:
                    
                   pass
        try:
                    firstname=request.POST.get('firstname')
                    lastname=request.POST.get("lastname","")
                    username=request.POST.get('username')
                    email=request.POST.get('email12').lower()
                    url=request.POST['url']
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
                            return redirect(f"{url}")
                    elif email1:
                            messages.error(request,"Email already exist")
                            return redirect(f"{url}")
        
                    else:
                            user = User.objects.create_user(username, email, password)
                            user.first_name=firstname
                            user.last_name=lastname
                            user.save()
                            b=Register.objects.create(email=email,username=username,first_name=firstname,last_name=lastname,country=country,email_verify=0,usertype=2,phone=phone,address=address,authtype=0,affiliate=0,notificationews=1,notification=1,notificationannouncement=1,notify=0,user_photo="media/default.png",pincode=pincode,city=city,email_token=str(uuid.uuid4()))
                           # send_email_token(email,b.email_token)
                            b.save()
       
                            messages.success(request,"Account Created Succesfully Now Please Verify Your EMail That has sent to your Email id ")
        
                            return redirect(f"{url}")
        except:
            
            
            pass
        try:
            promotion=request.POST['promotion']
            url=request.POST['url']
            try:
                
                x=Coupan.objects.get(coupan=promotion)
                
                if str(x.service_name).lower() == str(request.GET['hosting']).lower():
                    from datetime import datetime
                    max_date=(x.coupan_final).strftime('%Y-%m-%d')
                    today=datetime.today().strftime('%Y-%m-%d')
                    
                    if x.applytonew==1:
                        
                            data=UserService.objects.all().filter(username=request.user)
                           
                            if len(data)>0:
                                messages.error(request,"Coupan Not Valid")
                                return redirect(f"{url}")
                    
                    if today<=max_date:
                        
                        percent=x.discountpercent
                        request.session['coupan']=promotion
                        messages.error(request,"Coupan Applied")
                        return redirect(f"{url}&discount={percent}")
                        
                    else:
                        
                        messages.error(request,"Coupan Expired")
                        return redirect(f"{url}")
                else:
                    messages.error(request,"Coupan Doen't Exist")
                    return redirect(f"{url}")
                        
                    
            except:
                messages.error(request,"Coupan Doen't Exist")
                return redirect(f"{url}")
        except:
            pass
        try:
            
            add=request.POST['add']
       
            a=cart(email=Register.objects.get(username=request.user).email,service_name=hosting,service_type=Service.objects.get(service_name=hosting).service_type,service_no=Service.objects.get(service_name=hosting).service_no)
            a.save()
            
            if domainget=='newdomain':
                
                a1=cart(email=Register.objects.get(username=request.user).email,service_name=domain,service_type="domain",service_no="1")
                a1.save()
                return redirect('/services/')
            
            else:
                return redirect('/services/')
        except:
            month=request.POST['month']
            request.session['month']=month
            amountyo=request.POST['amo']
            url=request.POST['url']
            service=request.POST['service']
            domain69=request.POST['domain']
            discount=request.POST['discount']
            amountyo=float(amountyo)
            amountyo=amountyo*100
            request.session['tokencheck']=str(uuid.uuid4())
            request.session['amounttotal']=amountyo
            url=url+f"&tokencheck={request.session.get('tokencheck')}&amounttotal={request.session.get('amounttotal')}"
            url=url.replace("paymentinformation","paymentprocessing")
            from datetime import date
            xyo=Service.objects.get(service_name=hosting)
            dp=Register.objects.get(username=request.user)
            
            if int(domain69)==0:
               
                a=Invoice.objects.create(domain=request.GET['domain'],duration=month,coupan=promotion,invoicetype=0,due_date=date.today(),generates_date=date.today(),status=0,invoice_total=amountyo,invoice_price=f"{service},0,{discount}",invoice_data=hosting,service_no=xyo.service_no,service_type=xyo.service_type,email=dp.email,firstname=dp.first_name,lastname=dp.last_name,checksign=request.session.get('tokencheck'))
                a.save()
                mail_subject = 'Invoice Created!'
                message = render_to_string('invoiceemail.html', {
                           'details': f"https://grabwebhost.in/currentinvoice?&paymentid={request.session.get('tokencheck')}"
                            })
                text_content = strip_tags(message)
                email = EmailMultiAlternatives(
                            mail_subject,
                            text_content,
                            'info@grabwebhost.in',
                            [dp.email]
                                )
                email.attach_alternative(message, 'text/html')
                #email.send()
            else:
                a=Invoice.objects.create(domain=request.GET['domain'],duration=month,coupan=promotion,invoicetype=0,due_date=date.today(),generates_date=date.today(),status=0,invoice_total=amountyo,invoice_price=f"{service},{domain69},{discount}",invoice_data=f"{hosting},{request.GET['domain']}",service_no=xyo.service_no,service_type=xyo.service_type,email=dp.email,firstname=dp.first_name,lastname=dp.last_name,checksign=request.session.get('tokencheck'))
                a.save()
                mail_subject = 'Invoice Created!'
                message = render_to_string('invoiceemail.html', {
                           'details': f"https://grabwebhost.in/currentinvoice?&paymentid={request.session.get('tokencheck')}"
                            })
                text_content = strip_tags(message)
                email = EmailMultiAlternatives(
                            mail_subject,
                            text_content,
                            'info@grabwebhost.in',
                            [dp.email]
                                )
                email.attach_alternative(message, 'text/html')
                #email.send()
            return redirect(f"{url}")
        
    return render(request,"paymentinformation.html",d)
            

def paymentauth(request):
        global datata
        global userd
    
        tokencheck=request.GET['tokencheck']
        checktpkn=Invoice.objects.get(checksign=tokencheck)
        checktpkn.orderid='offline'
        checktpkn.paymentid='offline'
        checktpkn.signature='offline'
        checktpkn.status=1
        checktpkn.save()
        mail_subject = 'Invoice Updated!'
        message = render_to_string('invoiceemail.html', {
                               'details': f"https://grabwebhost.in/currentinvoice?&paymentid={tokencheck}"
                                })
        text_content = strip_tags(message)
        email = EmailMultiAlternatives(
                                mail_subject,
                                text_content,
                                'info@grabwebhost.in',
                                [checktpkn.email]
                                    )
        email.attach_alternative(message, 'text/html')
        #email.send()
        from datetime import date
        userd=Register.objects.get(email=checktpkn.email)
        domain=checktpkn.domain
        usernam=domain.split('.')[0]
        pa=User.objects.make_random_password()
        createdata=UserService.objects.create(status=0,email=checktpkn.email,service_name=checktpkn.invoice_data,domain_name=domain,first_payment_date=date.today(),username=usernam,password=pa,payment_format=0)
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
                                    [userd.email]
                                        )
        email.attach_alternative(message, 'text/html')
        #email.send()
        return HttpResponse("Hogya cpanel banaojaldi and check domain and update status")
   
                   
           
            
            
            
        return HttpResponse("Progress")
    
    
    
    
    
    
def paymentprocessing(request):
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    dataa=Register.objects.get(username=request.user)
    global promotion
    hosting=request.GET['hosting']
    domainget=request.GET['domainget']
    domain=request.GET['domain']
    tokencheck=request.GET['tokencheck']
    amounttotal=request.GET['amounttotal']
    d={'hosting':hosting,'domain':domain,'domainget':domainget,'amounttotal':amounttotal,'tokencheck':tokencheck,'news':news,'announcement':news0,'photo':dataa.user_photo}
    checktpken=Invoice.objects.get(checksign=tokencheck)
    if tokencheck == str(request.session.get('tokencheck')) and amounttotal == str(request.session.get('amounttotal')):
        amounttotal=int(float(amounttotal))
    else:
        return redirect("/")
    
    try:
        discount=request.GET['discount']
        promotion=request.session.get('coupan')
        x1=Coupan.objects.get(coupan=promotion)
    except:
        pass
    d['domainprice']=0
    if domainget == "newdomain":
        
        
        domai=whois(domain)
        if domai==400:
            messages.error(request,"Domain Not Available")
            return redirect(f"/shared/?hosting={hosting}")
        
            
    try:
    
        x=Service.objects.get(service_name=hosting)
        if str(request.session.get('domainget'))==str(domainget):
            pass
        else:
            return redirect("/sharedhosting/")
        
    except:
         return redirect('/sharedhosting/')
    from django.conf import settings
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    razorpay_order = client.order.create(
            {"amount":amounttotal, "currency": "INR", "payment_capture": "1"}
        )
    d['payment']=razorpay_order
    if request.method=="POST":
        
        try:
            id12=request.POST['id12']
            orderid=request.POST['orderid']
            signature=request.POST['signature']
            checktpkn=Invoice.objects.get(checksign=tokencheck)
            checktpkn.orderid=orderid
            checktpkn.paymentid=id12
            checktpkn.signature=signature
            checktpkn.status=1
            checktpkn.save()
            mail_subject = 'Invoice Updated!'
            message = render_to_string('invoiceemail.html', {
                           'details': f"https://grabwebhost.in/currentinvoice?&paymentid={tokencheck}"
                            })
            text_content = strip_tags(message)
            email = EmailMultiAlternatives(
                            mail_subject,
                            text_content,
                            'info@grabwebhost.in',
                            [dataa.email]
                                )
            email.attach_alternative(message, 'text/html')
            #email.send()
            userdetail=Register.objects.get(username=request.user)
            
                
 
            try:
                currentcoupan=request.session['coupan']
                serviceeee=Service.objects.get(service_name=hosting).service_no
            except:
                serviceeee=Service.objects.get(service_name=hosting).service_no
                currentcoupan="No"
            from datetime import date
            userd=Register.objects.get(username=request.user)
            usernam=domain.split('.')[0]
            pa=User.objects.make_random_password()
            import pycpanel
            server = pycpanel.conn(hostname='server.grabwebhost.in',username='grabweb', password='19072002ROHANkumar',ssl=True, verify=False, )
            
            params = {
    'username'      : usernam,
    'domain' : domain,
    'contactemail':userd.email,
    'password':pa,
    'plan':hosting
    
            }
            try:
                    datata=server.api('createacct', params=params)
                    createdata=UserService.objects.create(status=datata['result'][0]['status'],email=userd.email,service_name=hosting,domain_name=domain,first_payment=amounttotal,first_payment_date=date.today(),payment_format=request.session.get('month'),service_no=serviceeee,username=usernam,password=pa,coupan=currentcoupan)
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
                                    [userd.email]
                                        )
                    email.attach_alternative(message, 'text/html')
                    #email.send()
                    return redirect(f"/currentinvoice?&paymentid={tokencheck}")
            except:
                        createdata=UserService.objects.create(status=datata['result'][0]['status'],email=userd.email,service_name=hosting,domain_name=domain,first_payment=amounttotal,first_payment_date=date.today(),payment_format=request.session.get('month'),service_no=serviceeee,username=usernam,password=pa,coupan=currentcoupan)
                        createdata.save()
                        return redirect(f"/currentinvoice?&paymentid={tokencheck}")
           

          
            
            if request.GET['domainget']=='newdomain':
                domaindatacreate=Userdomain.objects.create(status=0,email=userdetail.email,domain_name=domain,first_payment=amounttotal,first_payment_date=date.today(),payment_format=0,provider="connectreseller",NameServer1="ns1.grabwebhost.in",NameServer2="ns2.grabwebhost.in",NameServer3="ns3.grabwebhost.in",NameServer4="ns4.grabwebhost.in",privacy_protection=1,email_service=0,dns_service=1,coupan="0")
                domaindatacreate.save()  
                return redirect(f"/currentinvoice?&paymentid={tokencheck}")
            return redirect(f"/currentinvoice?&paymentid={tokencheck}")
        except:
            name12=request.POST['name']
            return redirect("/")
            
            
            
    return render(request,"paymentprocessing.html",d)
def currentinvoice(request):
    paymentid=request.GET['paymentid']
    d={}
    news=News.objects.all().order_by('news_id')[:2]
    news0=Announcement.objects.all().order_by('accouncement_id')[:2]
    dataa=Register.objects.get(username=request.user)
    d={'news':news,'announcement':news0,'photo':dataa.user_photo}
    
    try:    
            d['hostingdata']='yes'
            billing_data=Invoice.objects.get(checksign=paymentid)
            dis=list(str(billing_data.invoice_price).split(','))
            d['discount']=dis[2]
            ds=list(str(billing_data.invoice_data).split(','))
            if len(ds)>1:
                d['service']=ds[0]
                d['domain23']=ds[1]
            else:
                d['service']=ds[0]
                d['domain23']=0
            d['intermediateprice']=int(float(dis[0])) + int(float(dis[1]))
                
            d['total']=int(float(billing_data.invoice_total))/100
            d['info']=billing_data
            d['paymentid']=paymentid
            d['info']=billing_data
    except:
            pass
    try:
        billing_data=Invoice.objects.get(checksign=paymentid)
        d['total']=int(float(billing_data.invoice_total))/100
        d['paymentid']=paymentid
        d['hostingdata']='no'
        d['ds']=billing_data.invoice_data
        d['info']=billing_data
        
        
    except:
        pass
 
            
    
            
        
    return render(request,"billinginvoice.html",d)


