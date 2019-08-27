from django.urls import path
from .views import home, NewPost, PostDetail, PostDelete, PostUpdate, UserPosts



urlpatterns = [
	path('', home, name='home'),
	path('post/new/', NewPost.as_view(), name='new-post'),
	path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
	path('post/<int:pk>/delete/', PostDelete.as_view(), name='del-post' ),
	path('post/<int:pk>/update/', PostUpdate.as_view(), name='update-post'),
	path('user/<str:username>', UserPosts.as_view(), name='user-posts'),

]
