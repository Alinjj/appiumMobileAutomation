FROM reactnativecommunity/react-native-android

# Установка Appium
RUN npm install -g appium
# Установка драйвера uiautomator2 через Appium
RUN appium driver install uiautomator2

# Установка зависимостей Python для тестов
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Копирование тестов и APK файла в образ
COPY . /app

# Установите переменные среды для Appium
ENV APPIUM_ADDRESS=0.0.0.0
ENV APPIUM_PORT=4723

EXPOSE 4723

CMD ["appium", "--address", "0.0.0.0", "--port", "4723"]
