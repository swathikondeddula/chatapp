from django.contrib import admin
from .models import Room,Message,ChatModel,Profile
from .models import UserProfileModel
admin.site.register(UserProfileModel)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(ChatModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture_display')  # Add 'profile_picture_display' to the list display

    def profile_picture_display(self, obj):
        return obj.profile_picture.url if obj.profile_picture else None

    profile_picture_display.short_description = 'Profile Picture'  # Customize column header

admin.site.register(Profile, ProfileAdmin)