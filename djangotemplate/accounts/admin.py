# coding:utf-8

from django.contrib import admin
# from accounts.models import LabMember

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.models import LabMember
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

class LabMemberChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

    class Meta(UserChangeForm.Meta):
        model = LabMember

class LabMemberCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

    # このメソッドをオーバーロードしないと、
    # 元々のUserクラスのインスタンスを生成しようとするお茶目なDjangoさん
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            # Not sure why UserCreationForm doesn't do this in the first place,
            # or at least test to see if _meta.model is there and if not use User...
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = LabMember

class LabMemberAdmin(UserAdmin):
    form = LabMemberChangeForm
    add_form = LabMemberCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'email', 'year_in_school')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
        (_('Personal info'), {
            'classes': ('wide',),
            'fields': ('last_name', 'first_name', 'email', 'year_in_school')}
         ),
    )

    list_display = ('username', 'year_in_school', 'last_name', 'first_name', 'email', 'is_staff')
    list_filter = ('year_in_school', 'groups', 'is_staff', 'is_superuser', 'is_active')

admin.site.register(LabMember, LabMemberAdmin)
