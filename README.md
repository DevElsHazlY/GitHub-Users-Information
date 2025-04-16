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


---

طريقة الاستخدام:

1. افتح Termux


2. شغل السكربت:



python GHUI.py

3. أدخل اسم المستخدم على GitHub (مثلًا: torvalds)


4. هتظهرلك البيانات كاملة باللغة العربية.




---

مثال:

اكتب اسم المستخدم على GitHub: torvalds

معلومات المستخدم @torvalds:

الاسم: Linus Torvalds
عدد الريبو: 6
عدد المتابعين: 280000
يتابع: 0
الموقع: Portland, OR
النبذة: Linux creator, hacker, scuba diver, and curmudgeon.
رابط البروفايل: https://github.com/torvalds


---

رابط الأداة

يمكنك تعديل أو استخدام الأداة بحرية:
GitHub: https://github.com/اسم_المستخدم/اسم_المستودع


---

المطور

Telegram: T6GIO
