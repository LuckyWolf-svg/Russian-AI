![image](https://github.com/user-attachments/assets/09ee1fa8-319d-49e0-b1fd-ce2a5aae665f)

Не забывайте, как долго он отвечает и выполняет действия зависит от вашего компьютере.

Я старался сделать его частично работающим даже без интернета (Учитывая что он работает в Discord это смешно я знаю)
Используйте ChatGPT и можете все поменять в лучшие варианты

Инструкция. Внутри кода я так же вставил пояснения почти каждого предложения, весь проект сделан в PyCharm (python 3.12)
В коде присутствует 2 теста

На забудьте скачать все библиотеки в packages

AI строится на библиотеке gpt4all (2.7.0), скачиваете модель и всё, в .cache своего компьюетера можете вставить свою, я проверял все модели в формате .gguf, но по документации можно и другие но за роботоспособность никто не отвечает. 'https://docs.gpt4all.io/gpt4all_python/home.html'

Создаём 2ой аккаунт Discord, в настройках изменяете ввод и вывод, вы можете скачать дополнительные устройства на сайте вирутальных кабелей
'https://vb-audio.com/Cable/', используйте код в папке для получения всех кодов ваших index вводов и выводов (не забываем что счёт идет с 0) и меняем в коде индексы

(Я использую 2 аккаунт в браузере, и в приложении на компьюетере уже общаюсь)

Скачиваем модель для распозванавия речи, я использую 'vosk-model-small-ru-0.22' 'https://alphacephei.com/vosk/models'
Скачиваем модель для озвучки текста 'https://models.silero.ai/models/tts/ru'
Закидываем всё в нашу папку с проектом

Если появилась данная ошибка то 2 варианта либо исправляйте ошибку с CUDA либо удаляйте их 
YourProjectFolder\.venv\Lib\site-packages\gpt4all\llmodel_DO_NOT_MODIFY
![image](https://github.com/user-attachments/assets/b694921c-1524-461e-b6f7-c25b6ac435aa)

Я сделал её для развлечения и не вижу причин как либо улучшать, но
если хотите как либо улучшить данную модель 
1) Перенесите код на C++\C# для быстродействия
2) используйте движок по типу Unity, чтобы дать аватар и стримить в OBS, а в самом discord\twitch включить захват OBS
3) Вставить свою модель и промпт в файле gpt.py (Кем является модель, это можно хоть у ChatGpt спросить и он сделает)
Есть всякие модели здесь 'https://huggingface.co/models' & 'https://llm.extractum.io/list/'
