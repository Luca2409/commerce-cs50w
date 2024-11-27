from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listings/<int:id>", views.listings, name="listings"),
    path("watchlist", views.WatchlistView, name="watchlist"),
    path("addwatchlist/<int:id>", views.AddWatchlist, name="addwatchlist"),
    path("deletewatchlist/<int:id>", views.DeleteWatchlist, name="deletewatchlist"),
    path("categories", views.Categories, name="categories"), 
    path("categorypage/<str:category>", views.CategoryPage, name="categorypage"),
    path("comment/<int:id>", views.CommentView, name="comment"),
    path("delete/<int:id>", views.Delete, name="delete"),
    path("winhistory", views.WinHistory, name="winhistory")
]
