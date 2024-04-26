from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from charity.models import Institution, Category
from .forms import CustomUserCreationForm, CustomUserChangeForm, InstitutionForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class InstitutionAdmin(admin.ModelAdmin):
    model = Institution
    form = InstitutionForm
    list_display = ('name', 'type',)
    list_filter = ('name', 'type',)
    ordering = ('name',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Category)

