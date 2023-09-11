from django.contrib import admin


from.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('email',)