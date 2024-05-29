from .models import *
from Login_Logout.models import Profile,User

def getBaseData(request):
    
    # nabbar Text
    
    navbarText = Navbar_text.objects.all().last()
    
    # footer header text
    Footer_other_header_name = Footer_other_detail_header.objects.all()
    
    # footer li text
    
    CattegoryHeader = Footer_other_detail_header.objects.all()
    CattegoryHeaderData = {}
    
    for header in CattegoryHeader:
        CattegoryHeaderData[header] = Header_li.objects.filter(HeaderChoice = header )
        
        
    # payment merchent image
    
    
    
    

    # fOOTER LAST PART
    
    footer_last = [Footer_Last_section.objects.last()]  # Wrap the object in a list
    
    
    return {'navbarText': navbarText, 
            'Footer_other_header_name':Footer_other_header_name, 
            'CattegoryHeaderData':CattegoryHeaderData,
            'footer_last':footer_last,
            
            }
    
   
def Account_id(request):
    account_number = None  # Default value if user is not authenticated or no profile exists

    if request.user.is_authenticated:
        try:
            account = User.objects.get(pk=request.user.id)
            profile = Profile.objects.filter(user=account).first()
            
            if profile:
                account_number = profile.account_number
        except User.DoesNotExist:
            pass  # Handle the case where the user does not exist, if necessary

    return {'account_number': account_number}