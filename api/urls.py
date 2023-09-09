from .views import CommentsListView
from .views import CommentsDetailView

urlpatterns = [
    path("comments", CommentsListView.as_view(), name="comment_list_view"),
    path ("comments/<int:id>", CommentsDetailView.as_view(),name="comment_detail_view"),
]