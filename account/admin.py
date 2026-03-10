from django.contrib import admin

from account.models import Account, Role


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user__username", "user__email", "user__is_staff")
    search_fields = (
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )
    list_filter = ("user__is_active", "user__is_staff")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
