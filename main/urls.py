from django.urls import path
from main.views import show_main, add_jersey, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_jersey, delete_jersey, add_jersey_ajax, create_jersey_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-jersey/', add_jersey, name='add_jersey'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('edit-jersey/<uuid:id>/', edit_jersey, name='edit_jersey'),
    path('delete-jersey/<uuid:id>/', delete_jersey, name='delete_jersey'),
    path('add-jersey-ajax', add_jersey_ajax, name='add_jersey_ajax'),
    path('create-flutter/', create_jersey_flutter, name='create_jersey_flutter'),
 ]
