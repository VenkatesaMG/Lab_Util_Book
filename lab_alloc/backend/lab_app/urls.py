from django.urls import path
from . import views
urlpatterns = [
    path('schedule/<str:lab_name>/<str:date>/',views.schedule_list_detail_view),
    path('schedule/create',views.schedule_create_view),
    path('laboratory',views.laboratory_list_create_view, name="laboratory"),
    path('user',views.user_list_create_view, name="user_list_create"),
    path('schedule',views.schedule_list_view, name="schedule_list_view"),
    path('daily',views.daily_list_view, name="daily_list_view"),
    path('daily/<int:date>/',views.daily_list_detail_view, name="daily_list_detail_view"),
    path('week/<int:week>/',views.week_list_detail_view, name="week_list_detail_view"),
    path('week',views.week_list_view, name="week_list_view"),
    path('schedule_req', views.schedule_request_list_view, name="schedule_req"),
    path('schedule_req/create',views.schedule_request_create_view, name="schedule_req_create"),
    path('checkin/<str:user_name>',views.handleQR, name="scan_qr"),
    path('schedule_req/<int:id>/',views.schedule_request_update_view, name="schedule_req_update_view"),
    path('admin',views.admin_list_view, name="admin_list_view"),
    path('user/<str:username>',views.user_detail_api_view, name="user_detail_api_view"),
    path('cur_schedules',views.schedule_req_mod_view, name="schedule_req_mod_view"),
    path('maintenance', views.main_list_view, name="main_list_view"),
    path('maintenance/create',views.main_list_create, name="main_list_create"),
    path('maintenance/<str:custom_date>/<str:custom_lab>',views.instance_api_view, name="instance_api_view"),
    path('schedule_req/<int:page_state>', views.schedule_request_list_view, name="schedule_request_list_view"),
    path('cal_events/<str:req_date>/', views.get_calendar_schedules, name="get_calendar_schedules"),
    path('alexa/book-lab/', views.book_lab_session, name='book_lab_session')
]