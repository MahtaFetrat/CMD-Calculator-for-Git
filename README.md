# پروژه‌ی ماشین‌حساب خط فرمان برای نمایش قابلیت‌های Git

## راه‌اندازی اولیه‌ی مخزن
در ابتدا یک مخزن خالی خصوصی در Github ایجاد شد. این مخزن با یک LICENSE، یک فایل ReadMe و یک فایل .gitignore راه‌اندازی شد. سپس به کمک دستورات خط فرمان Git، این مخزن بر روی سیستم محلی، ایجاد و بارگیری شد. این دستورات در تصویر زیر قابل مشاهده هستند.

![git-init](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/dcc5b4f5-c85f-4a3a-81ec-309d401604fc)

سپس یک چهارچوب بسیار ساده و اولیه از منوی ماشین‌حساب مورد نظر، پیاده‌سازی و بر روی شاخه‌ی main بارگذاری شد. تصویر زیر این مراحل را در خط فرمان نمایش می‌دهد.

![main-init](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/6d14d1f7-ddb2-4820-ae04-ed34e4eff202)

در ادامه هریک از اعضای گروه، بر روی یک شاخه‌ی جدا، فرایند توسعه را در پیش گرفتند. این شاخه‌ها شامل موارد زیر می‌شوند.
- عملیات‌های اصلی
- عملیات‌های مثلثاتی

دو تصویر زیر، به ترتیب ساخت محلی یکی از این شاخه‌ها، اعمال اولین کامیت و بارگذاری آن بر روی remote را نمایش می‌دهند.

![basic-op-create](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/02216c23-5886-4ca5-aa81-6a19f5303578)

![basic-op-init](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/1a65af05-556f-455f-8260-8b0f18787747)


پس پیاده‌سازی عملیات تقسیم، متوجه شدیم که پیغام کامیت مربوط به ضرب، به اشتباه به تقسیم اشاره دارد. برای حل این مشکل، ابتدا تغییرات جاری را stash کردیم، سپس پیغام کامیت قبلی را تصحیح کردیم. در ادامه تغییرات stash شده را pop کردیم و یک کامیت هم برای تقسیم زدیم. تصاویر زیر به ترتیب نشان‌دهنده‌ی وضعیت کامیت‌ها قبل از تصحیح این حطا، stash کردن تغییرات و تغییر پیغام کامیت و pop کردن تغییرات، اعمال کامیت تقسیم و وضعیت کامیت‌ها پس از آن هستند.

![git-log](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/8c6aae19-664f-4f54-8c7a-ebce5526a854)

![git-amend](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/5ccc6237-8270-4c80-b835-9ff138614b04)

![git-stash](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/c6a18d53-9e3e-48ff-adab-bc16ce2d446c)

## کلون کردن مخزن و ادامه تغییرات
ابتدا مخزن ایجاد شده در ریموت را کلون می‌کنیم.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/3fde060c-97f8-4640-8eb8-d76562fe836a)
سپس با اضافه کردن منوی اعمال مثلثاتی در فایل menu.py این فایل را ابتدا add می‌کنیم و سپس چیزهایی که روی استیج قرار دارد را کامیت می‌کنیم. و سپس پوش می‌کنیم. هم اکنون همچنان روی شاخه اصلی قرار داریم و چون پروژه را از ابتدا کلون کرده بودیم ریموت آن مشخص بود و هنگام پوش مستقیما به آن ریموت پوش شد.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/88472951-68cd-4e7c-9af9-31ecd05a6f53)
یک شاخه جدید برای کار روی عملیات‌های مثلثاتی ایجاد کرده و روی آن چک‌اوت می‌کنیم.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/fdff2633-1ca1-42e0-ae80-f0eebe9ffabf)
ّمنوی اولیه عملیات مثلثاتی را ایجاد می کنیم. این تغییر مستلزم تغییراتی در فایل‌های trigonometric.py وmenu.py می‌باشد. این فایل‌ها را به استیج اضافه کرده و کامیت می‌کنیم. با توجه به اینکه در حال حاضر هد روی شاخه جدیدی است که در ریموت وجود ندارد باید در پوش مشخص کنیم که این شاخه در ریپازیتوری ریموت نیز ساخته شود.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/73d0c4a0-fdc2-4535-b2f1-dac5235a0ab2)
عملیات سینوس را اضافه می‌کنیم و به استیج اضافه، و کامیت و پوش می‌کنیم.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/7060428b-b9a0-4398-a57e-889a5c98e81c)
عملیات کسینوس را اضاقه می‌کنیم و به استیج اضافه و کامیت و پوش می‌کنیم.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/7712aba8-bca6-416c-bc12-34cdeeb136d0)
عملیات‌های دیگر را هم به ترتیب اضافه می‌کنیم و برای هر پیشرفت جزئی مفهومی یک کامیت انجام می‌دهیم.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/03c79ed8-30b6-44dd-8513-5f8489813623)
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/c0fd8e95-66bc-4a89-993d-9b5ebdbff10e)
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/b6385cb6-87be-4bf5-a49a-7c7ef3b4213e)
تغییرات شاخه جدید را روی شاخه اصلی لوکال ادغام می‌کنیم:
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/90647a1a-26a8-4633-ae2a-25f4b38d0e8f)
تغییرات جدید ریموت را دریافت می‌کنیم:
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/fad644d1-e3c3-4a99-8350-2feaeca94e61)
هنگام پوش کردن تغییرات متوجه می‌شویم به علت محافظت شده بودن شاخه مین باید پول ریکوئست ایجاد کنیم:
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/5184582c-6ebd-4e39-b48c-4c0cd29e9569)
پول ریکوئست را ایجاد کرده و کاربر دارای دسترسی آن را اکسپت و ادغام می‌کند. و در صورت وجود تداخل آن را حل می‌کند.
یک شاخه جدید جهت اضافه کردن یک قابلیت به عملیات سینوس ماشین حساب ایجاد می‌کنیم:
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/5e4be687-cb2c-455c-b7f6-66589566cfbb)
عملیات مربوطه را اضافه کرده و روی همان شاخه پوش می‌کنیم (مشابه توضیحات قبل)
چون اینجا نیاز است فایل منو نیز تغییری بکند احتمال دارد به تداخل بخوریم.
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/4cd2e382-680f-4288-9a63-20820bf4cae3)
و مشابه شاخه قبل پول ریکوئست می‌زنیم:
![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/24840082/4af9aa0b-63dc-410f-bb74-dd085a7b2646)
در یکی از کامیت‌ها یک فایل از پروژه به نام the_file_to_ignore.txt را که نمیخواهیم در گیت ردگیری شود به .gitignore اضافه می‌کنیم.










## محافظت شاخه‌ی main
با اعمال یک rule بر روی شاخه‌ی main می‌توانیم شاخه‌ی main را از ادغام بدون `pull request` محافظت کنیم. تصویر زیر این تنظیمات را نشان می‌دهد.

![image](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/38d89f35-973b-4f06-8ed6-e82edb925968)

## رفع conflict ها

اولین کانفلیکتی که به آن برخوردیم در مرج کردن برنچ basic_operations با main بود. تصویر کامیت مربوط به این کانفلیکت در زیر آمده است.
![conflict1](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/d187d875-b6b0-4734-93e4-86fa406f5cde)

سپس برای شبیه‌سازی کانفلیکت دوم، یک پیغام را در دو شاخه به نحو مختلفی نوشتیم که به کانفلیکت دیگری منجر شد. مراحل رخ‌داد و رفع این کانفلیکت در تصاویر زیر آمده‌است.

![conflict](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/1162f713-fe2b-4b85-ac96-e231d38b254a)

![solve-conflict](https://github.com/MahtaFetrat/CMD-Calculator-for-Git/assets/62302965/a6587c68-c8e9-4bc4-9438-051fc5134e8a)



## پرسش‌ها
1. **پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟**

پوشه‌ی .git پوشه‌ای است که تمام اطلاعات لازم برای سیستم کنترل ورژن یک پروژه را شامل می‌شود. از جمله‌ی این اطلاعات، سابقه‌ی کامیت‌ها، تغییرات، برنچ‌های موجود، فایل‌های کامیت‌شده، تغییرات فایل‌ها، کد‌های اجرایی گیت قبل و بعد از دستورات آن و ... می‌باشد. این پوشه با دستور `git init` ای که ما هم برای initialize کردن پروژه‌ی خود از آن استفاده کردیم ساخته می‌شود. البته یک روش دیگر برای ساخت/دریافت اولیه‌ی یک مخزن وجود دارد و آن `git clone` است. اجرای این دستور نیز پوشه‌ی .git را می‌سازد.

پوشه‌ی .git اطلاعات مورد نیاز را در قالب تعدادی پوشه و فایل در خود ذخیره می‌کند. این فایل‌ها و پوشه‌ها شامل Hooks, Info, Config, Objects, Description و HEAD می‌شوند. پوشه‌ی Objects که شاید بتوان گفت مهم‌ترین آن‌ها است، شامل تمام فایل‌های ایجاد‌شده، کامیت‌ها و ... می‌باشد. هر کدام از این فایل‌ها/آبجکت‌ها یک hash دارند که آن‌ها را به صورت یکتا مشخص (احتمال تصادم بسیار پایین) و قابل trace کردن می‌کنند. پوشه‌ی Hooks شامل تمام script های اجرایی توسط git است. به عنوان مثال، اسکریپت‌هایی که پیش و پس از دستور commit باید اجرا شوند. به این ترتیب در موارد کاربرد حاص، می‌توان این اسکریپت‌ها را تغییر و customize کرد. پوشه‌ی Info شامل فایل exclude است که معادل یک .gitignore پرایوت می‌باشد. پوشه‌ی کانفیگ مشخصا شامل تنظیمات و اطلاعات کلیدی مخزن مانند email و username و ... می‌باشد. فایل HEAD نیز به برنچ کنونی توسعه‌دهنده اشاره می‌کند. 

2. **منظور از atomic بودن در atomic commit و atomic pull-request چیست؟**

منظور از `atomic commit`، کامیتی است که در آن یک و تنها یک تغییر ایجاد شده‌است. یعنی کستقل از حجم کدی که اضافه/کم شده، کاری که در آن کامیت انجام شده در یک جمله‌ی ساده قابل بیان باشد و کوچکترین واحد کار انجام شده را شامل شود. در مقابل، هر `pull request` از تعدادی کامیت تشکیل شده‌است. اتمیک بودن `pull request` به آن معناست که هر `pull request` یک و تنها یک functionality را در قالب کامیت‌های خود اضافه کند یا تغییر بدهد. به طور خاص نباید هیچ تغییر کامیتی که مربوط به آن functionality نیست در آن `pull request` باشد. مثلا نباید در حین تغییر استایل یک فرم، کد را ریفکتور کرد یا یک تایپو یا باگ را حل کرد.

3. **تفاوت دستورهای fetch و pull و merge و rebase را بیان کنید.**

دو دستور `git merge` و `git rebase` هر دو دستوراتی برای ادغام کردن تغییرات شاخه‌ها هستند اما تفاوت‌هایی با هم دارند. در دستور merge، سابقه‌ی کامیت‌های برنچ مرج‌‌شونده حفظ می‌شود و این کامیت‌ها تغییر نمی‌کنند. تغییرات دو برنچ با هم ادغام می‌شود و نسخه‌ی ادغام‌شده، در قالب کامیت جدیدی به برنچ جاری اضافه می‌شود. اما در مقابل، rebase باعث می‌شود تمام کامیت‌های یک برنچ، تغییر یافته و به گونه‌ای به برنچ مورد نظر اضافه شوند که گویی برنچ جداگانه‌ای وجود نداشته‌است و تمام تغییرات مستقیما روی برنچ مورد نظر اعمال و کامیت شده‌بودند. یعنی سابقه از دست می‌رود. به عنوان مثال، زمان و ترتیب و رابطه‌ی والد-فرزندی کامیت‌ها تغییر می‌یابند و به صورت خطی در ادامه‌ی کامیت‌های برنچ مورد نظر قرار می‌گیرند. به این ترتیب می‌توان نتیجه گرفت که rebase برای ادغام برنچ‌های خصوصی مناسب‌تر است و merge برای ادغام برنچ‌هایی بهتر است که میان توسعه‌دهندگان به اشتراک گذاشته‌شده و افراد دیگری هم بر روی آن مشغول به کار هستند.

دستور `git fetch` آخرین نسخه‌ی remote یک شاخه را دریافت می‌کند. سپس این نسخه‌ی بارگیری‌شده، می‌تواند به یکی از روش‌های ادغام (merge یا rebase) با شاخه‌ی دیگری روی لوکال ادغام شود. در مقابل، pull آخرین نسخه‌ی یک شاخه‌ی remote را دریافت و آن را با شاخه‌ی لوکالی که pull روی آن اجرا شده ادغام می‌کند. در واقع pull دقیقا معادل با یک عملیات fetch است که به دنبال آن، یک عملیات ادغام نیز انجام شده‌است. یعنی fetch به خودی خود، تفاوت‌های میان شاخه‌ها را در شاخه‌ی لوکال تاثیر نمی‌دهد و آن را دچار تغییر نمی‌کند. بلکه تنها تغییرات جدید شاخه‌ی remote را دریفات می‌کند و می‌تواند برای به‌روز‌رسانی شاخه‌ی مورد نظر استفاده شود.

4. **تفاوت سه دستور reset و revert و restore را بیان کنید.**

دستور reset در حقیقت واقعا می‌تواند یک کامیت را به حالت قبل برگرداند به طوری که انگار نبوده است. یعنی در تاریخچه گیت هم دست می‌برد و کامیت یا کامیت‌های مورد نظر را حذف کرده و طبیعتا با تغییر شکل و وضعیت شاخه وضعیت به حالت ابتدایی برمی‌گردد.
دستور restore میتواند فایل‌های مشخصی را از یک کامیت در گدشته یا یک شاخه دیگر بیاورد و به شاخه فعلی اضافه کند یعنی وضعیت یک فایل را از یک کامیت دیگر بیاورد.
دستور revert یک کامیت جدید ایجاد میکند که تغییر اعمال شده در این کامیت بازگشتن به شرایط یک کامیت در گذشته است.

5. **منظور از stage چیست؟ دستور stash چه کاری را انجام می‌دهد؟**

مفهوم stage در گیت مشابه نامش به منزله یک سکوی آمادگی پیش از ارسال به گیت است. فرض کنید تعدادی فایل ویرایش شده داریم که می‌خواهیم در گیت کامیت کنیم. میتوانیم همه آن‌ها را همزمان به سکوی پرتاب ببریم و همزمان کامیت کنیم که در این صورت یک کامیت خواهیم داشت ولی ممکن است از نظر منطقی همه تغییرات فایل ها نباید یکجا کامیت می‌شدند. اما میتوان فایل ها را یکی یکی یا در دسته‌هایی که تغییراتشان پیوستگی مفهومی داشته است به سکوی پرتاب برد و کامیت کرد در حقیقت stage به ما این امکان را می‌دهد که فایل‌ها را گزینش شده به سکوی پرتاب ببریم. عبارت بهتر از این سکوی پرتاب این است که تا وقتی فایلی روی سکوی پرتاب نباشد انگار گیت از تغییرات اعمال شده در آن باخبر نیست و پیمایشش نمیکند ولی به محض اینکه روی stage قرار گرفت تغییرات آن پیمایش و ثبت می‌شود هرچند تا وقتی کامیت صورت نگرفته این تغییرات به صورت دائمی وارد گیت و تاریخچه آن نخواهد شد. 
دستور stash به ما این امکان را می‌دهد که تغییرات روی یک  فایل را تا یک مرحله‌ای به نوعی نامرئی کنیم. یعنی گیت از وجود این تغییرات باخبر است اما ما با حذف موقت یک سری تغییرات، به یک نسخه موقت برمیگردیم و می‌توانیم تغییرات جدید مورد نظر خود را اعمال کنیم در حالی که هنوز سری تغییرات قبلی stash شده و بدون اینکه در گیت کامیت شده باشد از بین نرفته است. به عبارتی می‌توان گفت stash کردن یعنی اعمال تغییرات موقت خارج از stage. یعنی دور از چشم گیت تغییراتی اعمال کنیم. با دستورات stash pop یا stash apply میتوانیم به حالت قبل از stash برگردیم و تغییرات مجددا توسط گیت ردگیری می‌شوند.

6. **مفهوم snapshot به چه معناست؟**

به یک نمای کلی از وضعیت تغییرات و فایل‌های پروژه اسنپ‌شات می‌گویند. ممکن است هر فایل مستقلا یک تاریخچه تغییرات و فعالیت‌های مربوط به خودش را داشته باشد ولی به مجموعه این وضعیت‌ها در لحظه اسنپ‌شات می‌گویند. نکته اصلی در اسنپ‌شات این است که وضعیت پروژه در گیت را در لحظه مشخص می‌کند و اسنپ‌شات سیستم بعد از هر تغییرعوض می‌شود.
