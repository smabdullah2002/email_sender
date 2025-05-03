from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def mail_sender(request):
    notification={}
    
    if request.method=="POST":
        recipient= request.POST.get("recipient")
        subj=request.POST.get("subj")
        msg=request.POST.get("msg")
        
        if recipient and subj and msg:
            try:
                #keyword arguments
                send_mail(recipient_list=[recipient],
                            subject=subj,
                            message=msg,
                            from_email=settings.EMAIL_HOST_USER,
                          )
                
                # positional arguments
                # send_mail(subj, msg, settings.EMAIL_HOST_USER, [recipient])
                
                notification["status"]="Email sent successfully"
                
            except Exception as e:
                notification["status"]=f"Error: {str(e)}"
                
        
        else:
            notification["status"]="Please fill all fields"
    return render(request, "mail/index.html", notification)