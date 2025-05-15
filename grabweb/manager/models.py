from django.db import models

# Create your models here.
from django.db import models
class Data(models.Model):
    email = models.EmailField()
    Name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
class emp(models.Model):
    email = models.EmailField()
    Name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    time= models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    empid= models.CharField(max_length=30)
class Register(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.AutoField(primary_key=True)
    email_verify=models.IntegerField()#0 for not verify
    usertype=models.IntegerField()  #0 for admin 1 for employ and 2 for client 3 for reseller
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    about=models.TextField()
    insta=models.CharField(max_length=30)
    twitter=models.CharField(max_length=30)
    linkedIn=models.CharField(max_length=30)
    authtype=models.IntegerField()#0 for single 1 for 2 way
    user_photo=models.ImageField(upload_to='media/',default='media/default.png')
    notificationews=models.IntegerField()
    notificationannouncement=models.IntegerField()  #0 for off 1 for on
    notification=models.IntegerField() 
    affiliate=models.IntegerField() #0 for not and #1 for yes
    verify_number=models.CharField(max_length=10) 
    notify=models.IntegerField()
    email_token=models.CharField(max_length=100) 



class predev(models.Model):
    service_no=models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=200)
    tags= models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    webtype = models.IntegerField()#0 for static and 1 for dynamc
    user_photo=models.ImageField(upload_to='media/web/',default='media/default.png')
    requestdate=models.DateField(auto_now_add=True)
    
class predevservice(models.Model):
    email = models.EmailField()
    service_name=models.CharField(max_length=100)
    domain_name=models.CharField(max_length=100)
    first_payment=models.CharField(max_length=20) 
    first_payment_date=models.DateField()
    payment_format=models.IntegerField() #0for monthly 1 for quaterly  2 for semianually 3 for anually
    status=models.IntegerField()
    

class CustomWebDev(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    webtype = models.CharField(max_length=30)
    discription=models.CharField(max_length=300)
    requestdate=models.DateField(auto_now_add=True)
    
    
class Ticket(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    ticket_id = models.IntegerField(primary_key=True)
    subject=models.CharField(max_length=70)
    data=models.TextField()
    ticketdate=models.DateField(auto_now_add=True)
    priority=models.IntegerField() #0for normal 1 for important 2 for most important
    status=models.IntegerField() #0 for solved 1 for underforecess 2 for no reply

class Blog(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    blogtitle=models.CharField(max_length=70) 
    blogtype=models.CharField(max_length=70) #server hosting domain webdevelopment
    blogdata=models.TextField()
    blogimage=models.ImageField(upload_to='media/blog/')

class FAQ(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=30,unique=True)
    faqtitle=models.CharField(max_length=70) 
    faqtype=models.CharField(max_length=70) #server hosting domain webdevelopment
    faqdata=models.TextField()

class Invoice(models.Model):
    checksign=models.CharField(max_length=100,null=True)
    duration=models.CharField(max_length=100,null=True)
    domain=models.CharField(max_length=100,null=True)
    orderid=models.CharField(max_length=100,null=True)
    paymentid=models.CharField(max_length=100,null=True)
    signature=models.CharField(max_length=100,null=True)
    email = models.EmailField()
    firstname = models.CharField(max_length=100,null=True)
    coupan = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    invoice_no=models.AutoField(primary_key=True)
    service_type=models.CharField(max_length=100)
    service_no=models.CharField(max_length=15)
    invoice_data=models.TextField()
    invoice_price=models.TextField(null=True)
    invoice_total=models.TextField(null=True)
    status=models.IntegerField() #0 for unpaid 1 for paid
    generates_date=models.DateField()
    due_date=models.DateField()
    invoicetype=models.IntegerField() #0 for auto and 1 for manual

class Service(models.Model):
    service_name=models.CharField(max_length=100)
    service_type=models.CharField(max_length=100)
    service_no=models.CharField(max_length=15)
    Service_details=models.TextField()
    price=models.CharField(max_length=15)
    price3=models.CharField(max_length=15)
    price6=models.CharField(max_length=15)
    price12=models.CharField(max_length=15)
    coupan=models.CharField(max_length=25)
    affiliate_percentage=models.CharField(max_length=10)


class Domain(models.Model):
    domain_extention=models.CharField(max_length=100)
    price=models.CharField(max_length=15)
    renew=models.CharField(max_length=15)
    transfer=models.CharField(max_length=15)
    provider=models.CharField(max_length=15)


class UserService(models.Model):
    email = models.EmailField()
    service_name=models.CharField(max_length=100)
    domain_name=models.CharField(max_length=100)
    first_payment=models.CharField(max_length=20) 
    first_payment_date=models.DateField()
    payment_format=models.IntegerField() #0for monthly 1 for quaterly  2 for semianually 3 for anually
    service_no=models.CharField(max_length=15)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    coupan=models.CharField(max_length=25)
    status=models.IntegerField()

class Userdomain(models.Model):
    email = models.EmailField(primary_key=True)
    domain_name=models.CharField(max_length=100)
    first_payment=models.CharField(max_length=20) 
    first_payment_date=models.DateField()
    payment_format=models.IntegerField() #0for anually 1 for bianually 
    provider=models.CharField(max_length=15)
    NameServer1=models.CharField(max_length=20)
    NameServer2=models.CharField(max_length=20)
    NameServer3=models.CharField(max_length=20)
    NameServer4=models.CharField(max_length=20)
    privacy_protection=models.IntegerField() #0False 1 for True
    email_service=models.IntegerField() #0False 1 for True
    dns_service=models.IntegerField() #0False 1 for True
    coupan=models.CharField(max_length=25)
    status=models.IntegerField()



class DNSRecord(models.Model):
    domain_name = models.CharField(max_length=255)
    record_type = models.CharField(max_length=10)
    record_data = models.CharField(max_length=255)
    ttl = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TrendingService(models.Model):
    service_name=models.CharField(max_length=100)
    service_type=models.CharField(max_length=100)
    service_no=models.CharField(max_length=15)
    Service_details=models.TextField()
    price=models.CharField(max_length=15)
    
class Announcement(models.Model):
    accouncement_id=models.IntegerField(primary_key=True)
    announcement_title=models.CharField(max_length=70) 
    announcement_data=models.TextField()
    announcement_date=models.DateField()
    
class News(models.Model):
    usertype=models.IntegerField() 
    news_id=models.IntegerField(primary_key=True)
    new_title=models.CharField(max_length=70) 
    newstype=models.CharField(max_length=70) #server hosting domain webdevelopment
    newsdata=models.TextField()
    news_date=models.DateField()

class Coupan(models.Model):
    coupan=models.CharField(max_length=100)
    service_name=models.CharField(max_length=100)
    service_type=models.CharField(max_length=100)
    service_no=models.CharField(max_length=15)
    coupan_date=models.DateField()
    coupan_final=models.DateField()
    discountpercent=models.CharField(max_length=10)
    applytonew=models.IntegerField() #0 for all 1 for new

class cart(models.Model):
    id = models.EmailField(primary_key=True)
    email = models.CharField(max_length=30)
    service_name=models.CharField(max_length=100)
    service_type=models.CharField(max_length=100)
    service_no=models.CharField(max_length=15)

class Affiliate(models.Model):
    email = models.EmailField(primary_key=True)
    link=models.CharField(max_length=100)
    totalclicks=models.CharField(max_length=5)
    number_of_purchases=models.CharField(max_length=5)
    total_amount=models.CharField(max_length=10)
    paid=models.CharField(max_length=10)
    pending=models.CharField(max_length=10)    





    


