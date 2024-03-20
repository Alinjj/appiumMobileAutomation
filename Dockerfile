# Используйте базовый образ с предустановленным Android SDK и Node.js
FROM reactnativecommunity/react-native-android

# Установка Java
RUN apt-get update && apt-get install -y openjdk-11-jdk

# Установите Appium
RUN npm install -g appium

# Установка драйверов для Appium
RUN npm install -g appium-uiautomator2-driver

# Установка плагинов Appium, если они нужны
# Пример: RUN appium plugin install --source=npm <имя_плагина>

# Установите Python и зависимости для тестов
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Копируйте тесты и вспомогательные файлы в образ
COPY . /app

# Установите переменные среды для Appium
ENV APPIUM_ADDRESS=0.0.0.0
ENV APPIUM_PORT=4723

# Откройте порт для Appium
EXPOSE 4723

# Запустите Appium сервер
CMD ["appium", "--address", "0.0.0.0", "--port", "4723"]
