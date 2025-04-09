# -
Приложения для путешествий в Нижнем Новгороде при поддержке Ростелеком
---

# RostelecomApp

Добро пожаловать в RostelecomApp — мобильное приложение для всех, кто хочет познакомиться с Нижним Новгородом поближе! Это удобный и современный инструмент для туристов, любителей истории и просто любопытных людей. Приложение создано с использованием KivyMD, что делает его стильным и приятным в использовании. Оно поможет вам открыть для себя город через интересные места, увлекательные маршруты и даже небольшие тесты, которые проверят ваши знания. Если вы хотите узнать больше о Нижнем Новгороде, это приложение — ваш идеальный спутник!

## Что умеет приложение

Приложение предлагает множество функций, чтобы сделать ваше путешествие по городу интересным и запоминающимся. Вы сможете зарегистрироваться или войти в свой аккаунт, выбрать свои интересы, получить рекомендации мест и маршрутов, пройти тесты и даже посмотреть исторические фильмы. Всё это упаковано в удобный интерфейс с красивыми карточками, кнопками и плавными переходами между экранами.

Вы начинаете с экрана входа или регистрации. После этого можно выбрать, что вам интересно — история, архитектура, природа или что-то ещё. На основе этого приложение подскажет, куда сходить и что посмотреть. Есть вкладка с маршрутами, где можно выбрать прогулку и следовать по ней шаг за шагом. А если вы любите проверять свои знания, то тесты по маршрутам точно для вас!

Кроме того, в приложении есть чат-бот, который поможет вам определиться с интересами или ответит на вопросы о городе. Вы сможете добавлять места и маршруты в избранное, чтобы вернуться к ним позже. А для любителей истории есть раздел с видео, которые можно посмотреть прямо из приложения (на Android они открываются в YouTube).

## Как установить

Просто скачай апк в релизе)

## Как это работает

Когда вы запускаете приложение, первым делом появляется экран входа. Если у вас нет аккаунта, можно зарегистрироваться — придумать логин, пароль и указать email. После входа вы попадёте на экран выбора интересов. Там можно отметить, что вам нравится: история, культура, гастрономия и так далее. Это нужно, чтобы приложение знало, что вам рекомендовать.

На главном экране есть несколько вкладок. В "Рекомендациях" вы увидите карточки с местами — с фото, названием и описанием. Можно нажать на карточку и узнать больше, например, адрес или рейтинг. Там же есть кнопка, чтобы добавить место в избранное. Вкладка "Маршруты" показывает список маршрутов, которые можно начать и пройти, отмечая посещённые точки.

Ещё есть вкладка "Избранное", где хранятся все ваши любимые места и маршруты. Вы можете убрать что-то из избранного или открыть подробности. В "Профиле" отображается ваш прогресс — сколько маршрутов и тестов вы прошли. А если захотите узнать больше о городе, загляните в "Чат-бот" или "Фильмы".


## Зачем это нужно

RostelecomApp создано, чтобы помочь вам узнать Нижний Новгород с новой стороны. Вы сможете не просто гулять по городу, а делать это с умом — следовать маршрутам, узнавать историю, проверять свои знания. Это как личный гид в вашем кармане, который всегда готов подсказать что-то интересное.

Приложение подойдёт и туристам, и местным жителям, которые хотят лучше понять свой город. Оно простое в использовании, но при этом даёт много возможностей — от просмотра видео до прохождения тестов. Попробуйте, и Нижний Новгород откроется для вас по-новому!

---
## Инструкция по сборке

1. **Подготовка окружения**:
   - Убедитесь, что у вас установлена Ubuntu версии ниже 20.
   - Распакуйте архив с исходниками в выбранную папку.

2. **Установка необходимых зависимостей**:
   Откройте терминал в папке с распакованным проектом и выполните следующие команды:

   ```bash
   sudo apt update
   sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
   pip3 install --user --upgrade Cython==0.29.33 virtualenv
   sudo apt install openjdk-17-jdk
   pip3 install --user --upgrade buildozer
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   buildozer -v android debug
    
3. **Запуск**:
   Зайдите в папку 'bin' И перекиньте apk файл на смартфон и запустите!


### Дополнительные пояснения:
- **Ubuntu ниже 20 версии**: Убедитесь, что вы используете подходящую версию Ubuntu, так как более новые версии могут иметь несовместимые изменения.
- **VPN**: Если у вас возникают проблемы с загрузкой библиотек.
- **В релизах исходники в архиве и готовое апк**:

