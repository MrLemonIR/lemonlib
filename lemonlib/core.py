# core.py
import requests

def fast_print(text, repeat=1):
    """
    چاپ سریع یک متن
    :param text: متنی که باید چاپ بشه
    :param repeat: چند بار تکرار بشه
    """
    for _ in range(repeat):
        print(text)

def fast_connect(url):
    """
    اتصال سریع به یک URL و دریافت اطلاعات پایه
    :param url: لینک سایت
    :return: دیکشنری شامل وضعیت
    """
    try:
        r = requests.get(url)
        return {"status": r.status_code, "length": len(r.text)}
    except Exception as e:
        return {"error": str(e)}
