# coding:utf-8
from django import forms
# from django.contrib import admin
import xadmin as admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from User.models import user

# xadmin配置
from xadmin import views

class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


admin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings:
    """
    后台修改
    """
    site_title = '易图表后台管理系统'
    site_footer = '若对本平台有改进意见，欢迎反馈'
    menu_style = 'accordion'  # 开启分组折叠


admin.site.register(views.CommAdminView, GlobalSettings)

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ('id', 'email', 'uName')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        print(user.password)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = user
        fields = ('email', 'uName',
                  'uImg', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(object):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'uName', 'uSex',
                    'uImg', 'regist_time', 'email_active',  'is_superuser')
    list_filter = ('email', 'uName')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('id', 'email', 'uName', 'uSex', 'uImg')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )

    def regist_time(self, instance):
        from CommonUtils import stringUtils
        return stringUtils.stringUtil().strTimeStamp(instance.uTime, '-')

    regist_time.short_description = '注册时间'
    regist_time.is_column = True
    regist_time.allow_tags = True
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'uName')
    ordering = ('uTime',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.unregister(user)
admin.site.register(user, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
