# پروژه‌ی ماشین‌حساب خط فرمان برای نمایش قابلیت‌های Git

## راه‌اندازی اولیه‌ی مخزن
در ابتدا یک مخزن خالی خصوصی در Github ایجاد شد. این مخزن با یک LICENSE، یک فایل ReadMe و یک فایل .gitignore راه‌اندازی شد. سپس به کمک دستورات خط فرمان Git، این مخزن بر روی سیستم محلی، ایجاد و بارگیری شد. این دستورات در تصویر زیر قابل مشاهده هستند.

![git-init](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/3d777d74-1b9d-48c5-bcce-a4d105090374)

سپس یک چهارچوب بسیار ساده و اولیه از منوی ماشین‌حساب مورد نظر، پیاده‌سازی و بر روی شاخه‌ی main بارگذاری شد. تصویر زیر این مراحل را در خط فرمان نمایش می‌دهد.

![main-init](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/f870894a-e873-43f6-b484-a897cfd54743)

در ادامه هریک از اعضای گروه، بر روی یک شاخه‌ی جدا، فرایند توسعه را در پیش گرفتند. این شاخه‌ها شامل موارد زیر می‌شوند.
- عملیات‌های اصلی
- عملیات‌های مثلثاتی

دو تصویر زیر، به ترتیب ساخت محلی یکی از این شاخه‌ها، اعمال اولین کامیت و بارگذاری آن بر روی remote را نمایش می‌دهند.


![basic-op-create](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/cff5f122-c95d-4b36-9858-b5b14323115c)

![basic-op-init](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/c5babc67-8a8f-49da-91ad-991ef32e62e5)

پس پیاده‌سازی عملیات تقسیم، متوجه شدیم که پیغام کامیت مربوط به ضرب، به اشتباه به تقسیم اشاره دارد. برای حل این مشکل، ابتدا تغییرات جاری را stash کردیم، سپس پیغام کامیت قبلی را تصحیح کردیم. در ادامه تغییرات stash شده را pop کردیم و یک کامیت هم برای تقسیم زدیم. تصاویر زیر به ترتیب نشان‌دهنده‌ی وضعیت کامیت‌ها قبل از تصحیح این حطا، stash کردن تغییرات و تغییر پیغام کامیت و pop کردن تغییرات، اعمال کامیت تقسیم و وضعیت کامیت‌ها پس از آن هستند.

![git-log](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/f178660a-e79a-4c45-836b-2ac11c6a6c74)

![git-amend](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/623a11f8-87b8-45f1-88dc-9df44255fa5b)

![git-stash](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/a666806f-764e-4de2-abd0-01614d07fdb2)
