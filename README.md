# أداة جلب معلومات مستخدم GitHub باللغة العربية

أداة بسيطة مكتوبة بلغة Python، تقوم بجلب بيانات أي مستخدم على GitHub باستخدام الـ API الرسمي، وتعرضها بطريقة مرتبة باللغة العربية.

## المميزات:

- جلب الاسم وعدد الريبو والمتابعين والمتابَعين
- عرض النبذة التعريفية والموقع الجغرافي
- عرض رابط الحساب
- متوافقة تمامًا مع Termux

---

## المتطلبات

- Python 3
- مكتبة requests

### تثبيت المتطلبات على Termux:

```bash
pkg update && pkg install python -y
pip install requests
pkg install git
https://github.com/DevElsHazlY/GitHub-Users-Information.git
ls
cd GitHub-Users-Information
python GHUI.py
```
