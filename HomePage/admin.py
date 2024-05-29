from django.contrib import admin
from .models import Navbar_text, Footer_other_detail_header,Header_li , Footer_Last_section

# category Page model
from. models import CourseInfo

# All Course page html model import 



# seminer page html model import

from .models import Seminer_Time,Seminer_Image_Text

admin.site.register(Navbar_text)
admin.site.register(Footer_other_detail_header)
admin.site.register(Header_li)
admin.site.register(Footer_Last_section)





# seminer html page


admin.site.register(Seminer_Time)
admin.site.register(Seminer_Image_Text)



# category page model admin
admin.site.register(CourseInfo)
