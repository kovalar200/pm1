from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from .singleton import SuspiciousQueryLogger
from .models import QueryTypeFactory


def index(request):
    logger = SuspiciousQueryLogger()


    results = []
    for qtype, qtext, dur in [
        ("slow", "SELECT * FROM orders", 12.5),
        ("noindex", "SELECT * FROM users WHERE email = 'x@y.z'", 0.0),
        ("injection", "SELECT * FROM users WHERE id = 1 OR 1=1", 0.0),
    ]:
        obj = QueryTypeFactory.create(qtype, qtext, dur)
        info = obj.get_info()
        logger.log(qtype, qtext)
        results.append(info)

    # Демонстрация Singleton: два «разных» менеджера — один объект
    logger2 = SuspiciousQueryLogger()
    singleton_ok = id(logger) == id(logger2)

    html = "<h1>Журнал подозрительных запросов</h1>"
    html += f"<p><b>Singleton (id совпадают):</b> {singleton_ok}</p>"
    html += "<h2>Созданные запросы (Factory):</h2><ul>"
    html += "".join(f"<li>{r}</li>" for r in results)
    html += "</ul>"
    html += f"<h2>Журнал ({len(logger.get_all_logs())} записей):</h2><ul>"
    html += "".join(f"<li>{l}</li>" for l in logger.get_all_logs())
    html += "</ul>"
    html += '<p><a href="/servers/logs/">Посмотреть журнал (JSON)</a></p>'
    return HttpResponse(html)


def logs_view(request):
    logger = SuspiciousQueryLogger()
    return JsonResponse({"count": len(logger.get_all_logs()),
                         "logs": logger.get_all_logs()})


def create_query_view(request):

    qtype = request.GET.get("type", "slow")
    qtext = request.GET.get("query", "SELECT 1")
    try:
        duration = float(request.GET.get("duration", 0))
        obj = QueryTypeFactory.create(qtype, qtext, duration)
        logger = SuspiciousQueryLogger()
        logger.log(qtype, qtext)
        return JsonResponse({"ok": True, "info": obj.get_info()})
    except ValueError as e:
        return JsonResponse({"ok": False, "error": str(e)}, status=400)