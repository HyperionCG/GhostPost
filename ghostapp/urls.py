from django.urls import path

from ghostapp import views

urlpatterns = [
    path('',views.index, name ='homepage'),
    path('upvote/<int:id>/', views.upvote_view),
    path('downvote/<int:id>/', views.downvote_view),
    path('postview/', views.post_view),
    path('boastview/', views.boast_view),
    path('roastview/', views.roast_view),
    path('highview/', views.highvote_view),
    path('lowview/', views.lowvote_view),
    #path('history/',views.historyview)
    #path('admin/', admin.site.urls),
]