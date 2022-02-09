from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext as _
from django.contrib import admin
from .models import *
from datetime import datetime
# Register your models here.
admin.site.register(StudentRegistrationCollage)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Enroll)
admin.site.register(Result)
admin.site.register(Financial)
admin.site.register(Contact)
admin.site.register(Notice)


admin.site.site_header = 'NCBT ADMIN PORTAL'


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff',
                'is_active')
    fieldsets = (
        (("User Details"), {'fields': ('username','email', 'password')}),
        (_("Account Details"), {'fields': ('date_joined', 'last_login')}),
        (_("Permission"), {'fields': ('is_active', 'is_staff',)}),
    )
    add_fieldsets = (
        ("User Details", {'fields': ('username','email', 'password1', 'password2')}),
        ("Permission", {'fields': ('is_active', 'is_staff',)}),
    )


class StdUAdmin(admin.ModelAdmin):
    list_display=('name','student_id','phone','get_username','academic_status')
    exclude = ['user',]

    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username if obj.user else 'N/A'
    

    def save_model(self, request, obj, form, change):
        if not obj.user:
            user = User(username=obj.student_id)
            user.set_password(obj.dob.strftime('%d%m%y'))
            user.email = obj.email
            user.save()
            obj.user = user

        return super().save_model(request, obj, form, change)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)

admin.site.register(StudentRegistrationUni,StdUAdmin)