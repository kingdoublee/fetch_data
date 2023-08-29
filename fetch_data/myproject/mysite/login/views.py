from django.http import HttpResponse
from login.models import Administrator
from utils.utils import utlis


def index(request):
    # if request.method == "POST":
    mysql=utlis()
    mysql.connect()
    sql = "select * from login_Administrator"
    a=mysql.execute_query(sql)
    