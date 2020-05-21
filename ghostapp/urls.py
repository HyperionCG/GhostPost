from django.urls import path

from ghostapp import views

urlpatterns = [
    path('',views.index, name ='homepage'),
    path('upvote/<int:post_id>/', views.upvote_view),
    path('downvote/<int:post_id>/', views.downvote_view),
    path('postview/', views.post_view),
    path('boastview/', views.boast_view),
    path('roastview/', views.roast_view),
    path('sortview/', views.sort_view),
    #path('history/',views.historyview)
    #path('admin/', admin.site.urls),
]