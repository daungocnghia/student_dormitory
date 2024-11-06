from django.contrib import admin
from .models import *

@admin.register(Student_Account)
class StudentAccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'matric', 'wallet', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'matric')
    list_filter = ('is_student', 'created_at')


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'bank', 'confirm', 'created_at')
    search_fields = ('student__first_name', 'student__last_name', 'bank')
    list_filter = ('confirm', 'created_at')


@admin.register(House_Manager)
class HouseManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_no', 'created_at')
    search_fields = ('full_name', 'email', 'phone_no')
    list_filter = ('created_at',)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_name', 'house_manager', 'created_at')
    search_fields = ('block_name', 'house_manager__full_name')
    list_filter = ('created_at',)


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'block', 'is_available', 'charge', 'created_at')
    search_fields = ('room_name', 'block__block_name')
    list_filter = ('is_available', 'created_at')


@admin.register(Accomodation_Request)
class AccomodationRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'approved', 'created_at')
    search_fields = ('student__first_name', 'student__last_name', 'room__room_name')
    list_filter = ('approved', 'created_at')


@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'status', 'created_at')
    search_fields = ('student__first_name', 'student__last_name', 'subject')
    list_filter = ('status', 'created_at')


@admin.register(GuestStayRequest)
class GuestStayRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'full_name', 'status', 'date_from', 'date_to', 'created_at')
    search_fields = ('student__first_name', 'student__last_name', 'full_name')
    list_filter = ('status', 'created_at')


@admin.register(RoomTransfer)
class RoomTransferAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'approved', 'created_at')
    search_fields = ('student__first_name', 'student__last_name', 'room__room_name')
    list_filter = ('approved', 'created_at')


@admin.register(Guideline)
class GuidelineAdmin(admin.ModelAdmin):
    list_display = ('rule', 'created_at')
    search_fields = ('rule',)
    list_filter = ('created_at',)


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('room', 'rent', 'is_paid')
    search_fields = ('room__room_name',)
    list_filter = ('is_paid',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('is_active', 'created_at')
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Kích hoạt thông báo đã chọn"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Hủy kích hoạt thông báo đã chọn"
