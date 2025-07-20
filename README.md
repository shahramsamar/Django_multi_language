# 🌐 Django Multi-language Website | وب‌سایت چندزبانه با جنگو | Mehrsprachige Django-Webseite

---

## 🇮🇷 فارسی | معرفی پروژه

این پروژه یک وب‌سایت چندزبانه با استفاده از Django است که از `gettext` و `locale` برای ترجمه قالب‌ها، مدل‌ها و مسیرها استفاده می‌کند. کاربران می‌توانند زبان را تغییر دهند و محتوای سایت با توجه به زبان انتخابی نمایش داده می‌شود. مسیرهای URL با `i18n_patterns` تعریف شده‌اند و پوشه‌های ترجمه `.po` و `.mo` در ساختار `locale` نگهداری می‌شوند.

### ✨ ویژگی‌ها:
- پشتیبانی از چند زبان با gettext
- ترجمه قالب‌های HTML، مدل‌ها و فرم‌ها
- تغییر زبان پویا توسط کاربر
- ساختار آماده برای افزودن زبان‌های جدید

---

## 🇬🇧 English | Project Overview

This is a multilingual Django website utilizing `gettext` and `locale` files to support translation of templates, models, and URLs. Users can switch languages dynamically, and content adapts accordingly. URL internationalization is handled with `i18n_patterns`, and translations are stored in `.po` and `.mo` files under the `locale` folder.

### ✨ Features:
- Multi-language support using gettext
- Template, model, and form translation
- Dynamic language switching by user
- Easily extendable to new languages

---

## 🇩🇪 Deutsch | Projektübersicht

Dies ist eine mehrsprachige Django-Webseite, die `gettext` und `locale` verwendet, um Templates, Modelle und URLs zu übersetzen. Benutzer können die Sprache dynamisch wechseln, und die Inhalte passen sich entsprechend an. Die Internationalisierung der URL erfolgt mit `i18n_patterns`, und Übersetzungsdateien befinden sich im `locale`-Verzeichnis.

### ✨ Funktionen:
- Mehrsprachigkeit mit gettext
- Übersetzung von Templates, Modellen und Formularen
- Dynamischer Sprachwechsel durch Benutzer
- Erweiterbar um weitere Sprachen

---

## 🚀 Installation & Setup

```bash
# نصب کتابخانه‌های موردنیاز
pip install Django

# ساخت فایل‌های ترجمه
django-admin makemessages -l fa
django-admin compilemessages

# اجرا
python manage.py runserver
 
