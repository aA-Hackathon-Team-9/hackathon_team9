from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = DefaultRouter()
router.register(r'roles', views.RoleViewSet, basename='roles')
router.register(r'formulas', views.FormulaViewSet, basename='formulas')
router.register(r'variables', views.VariablesViewSet, basename='variables')
router.register(r'clock-ins', views.ClockInViewSet, basename='clock-ins')
router.register(r'employees', views.EmployeeViewSet, basename='employees')
router.register(r'checkouts', views.CheckOutViewSet, basename='checkouts')
employee_router = routers.NestedDefaultRouter(
    router, r'employees', lookup='employee')
employee_router.register(
    r'clock-ins', views.EmployeeClockInViewSet, basename='employee-clock-ins')

role_router = routers.NestedDefaultRouter(router, r'roles', lookup='role')
role_router.register(r'clock-ins', views.RoleClockInViewSet,
                     basename='role-clock-ins')

formula_router = routers.NestedDefaultRouter(router, r'formulas', lookup='formula')
formula_router.register(r'variables', views.VariablesViewSet, basename='formula-variables')



urlpatterns = [
    path("auth/login/", views.login, name='login'),
    path("auth/signup/", views.signup, name='signup'),
    path("spreadsheets/", views.generate_sheet_database, name='spreadsheets'),
    path("tables/", views.get_tables_columns,name='tables'),
<<<<<<< HEAD
    path('formulas/<int:pk>/variables/', views.FormulaViewSet.as_view({'post': 'create_formula_variables'}), name='create_formula_variables'),
    path('checkouts/', views.CheckOutViewSet.as_view({'post': 'post_checkout_and_generate_breakdown'})),
=======
>>>>>>> 337f82b9ffe6f6df019dc61ee16227620d77ba1a
    path(r'', include(router.urls)),
    path(r'', include(employee_router.urls)),
    path(r'', include(role_router.urls)),
    path(r'', include(formula_router.urls))
]
