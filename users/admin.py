# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from .models import Profile
from django.contrib.auth.models import User


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Perfil del admin


    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__lastname',
        'phone_number'
    )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            ),
        }),
        ('Extra infor', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            ),
        }),
        ('Metadata', {
            'fields' : (('created', 'modified'),),
        }
        ),
    )

    readonly_fields = ('created', 'modified',)


# Para unir el perfil con el usuario

class ProfileInLine(admin.StackedInline):
    # Admin for users

    model = Profile
    can_delete = False
    verbose_name = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


