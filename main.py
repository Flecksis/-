import json
import os
import re
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import SlideTransition
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.image import Image
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
# from g4f.client import Client
from kivy.animation import Animation
from kivy.utils import platform
from kivy.clock import Clock
from kivy.uix.video import Video
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.screenmanager import ScreenManager, Screen
import random

try:
    from kivy_garden.mapview import MapView, MapMarker
except ImportError:
    MapView = MapMarker = None
    print("Не удалось импортировать kivy_garden.mapview. Установите его с помощью: pip install kivy-garden.mapview")

if platform == 'android':
    from jnius import autoclass

    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')

#Window.size = (400, 700)

KV = '''
MDScreenManager:
    LoginScreen:
    RegisterScreen:
    InterestSelectionScreen:
    NavigationScreen:
    MapScreen:
    MovieScreen:

<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(30)
        spacing: dp(20)
        md_bg_color: app.theme_cls.bg_normal  # Используем цвет темы

        # Добавляем логотип и название приложения
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(150)  # Увеличиваем высоту для логотипа
            padding: dp(10)
            spacing: dp(10)

            Image:
                source: "source/logo.png"
                size_hint: None, None
                size: dp(140), dp(140)  # Размер логотипа
                pos_hint: {'center_x': 0.5}
                allow_stretch: True
                keep_ratio: True

        MDLabel:
            text: "Вход"
            halign: 'center'
            theme_text_color: 'Custom'
            text_color:  [1, 1, 1, 1]
            font_style: 'H4'
            bold: True
            size_hint_y: None
            height: dp(60)  # Уменьшаем высоту, так как логотип выше

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(300)
            pos_hint: {'center_y': 0.5}

            MDCard:
                orientation: 'vertical'
                padding: dp(20)
                size_hint: .9, None
                height: dp(250)
                elevation: 5
                radius: [15,]
                pos_hint: {'center_x': 0.5}
                md_bg_color: app.theme_cls.bg_light

                MDTextField:
                    id: login_username
                    hint_text: "Логин"
                    helper_text: "Введите ваш логин"
                    helper_text_mode: "on_focus"
                    mode: "rectangle"
                    fill_color: 0, 0, 0, .05
                    line_color_focus: app.theme_cls.accent_color  # Оранжевый

                MDTextField:
                    id: login_password
                    hint_text: "Пароль"
                    helper_text: "Введите ваш пароль"
                    helper_text_mode: "on_focus"
                    password: True
                    mode: "rectangle"
                    fill_color: 0, 0, 0, .05
                    line_color_focus: app.theme_cls.accent_color

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)
                    MDRaisedButton:
                        text: "Войти"
                        pos_hint: {'center_x': .5}
                        md_bg_color: app.theme_cls.accent_color
                        text_color:  [1, 1, 1, 1]
                        on_release: app.login(login_username.text, login_password.text)

                    MDRaisedButton:
                        text: "Нет аккаунта?"
                        pos_hint: {'center_x': .5}
                        md_bg_color: app.theme_cls.primary_color
                        text_color:  [1, 1, 1, 1]
                        on_release: 
                            app.root.current = 'register'
                            app.root.transition.direction = 'left'

            Widget:
                size_hint_y: None  
                height: dp(160)

<RegisterScreen>:
    name: 'register'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        md_bg_color: app.theme_cls.bg_normal

        MDLabel:
            text: "Регистрация"
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            font_style: 'H3'
            bold: True
            size_hint_y: None
            height: dp(80)  # Уменьшаем высоту

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(380)
            pos_hint: {'center_y': 0.5}

            MDCard:
                orientation: 'vertical'
                padding: dp(20)
                size_hint: .9, None
                height: dp(380)
                elevation: 5
                radius: [15,]
                pos_hint: {'center_x': 0.5}
                md_bg_color: app.theme_cls.bg_light

                MDTextField:
                    id: reg_username
                    hint_text: "Логин"
                    helper_text: "Придумайте логин"
                    helper_text_mode: "on_focus"
                    mode: "rectangle"
                    fill_color: 0, 0, 0, .05
                    line_color_focus: app.theme_cls.accent_color

                MDTextField:
                    id: reg_email
                    hint_text: "Email"
                    helper_text: "Введите ваш email"
                    helper_text_mode: "on_focus"
                    mode: "rectangle"
                    fill_color: 0, 0, 0, .05
                    line_color_focus: app.theme_cls.accent_color

                MDTextField:
                    id: reg_password
                    hint_text: "Пароль"
                    helper_text: "Придумайте пароль"
                    helper_text_mode: "on_focus"
                    password: True
                    mode: "rectangle"
                    fill_color: 0, 0, 0, .05
                    line_color_focus: app.theme_cls.accent_color

                MDTextField:
                    id: reg_confirm_password
                    hint_text: "Подтверждение пароля"
                    helper_text: "Введите пароль еще раз"
                    helper_text_mode: "on_focus"
                    password: True
                    mode: "rectangle"
                    fill_color: 0, 0, 0, .05
                    line_color_focus: app.theme_cls.accent_color

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)

                    MDRaisedButton:
                        text: "Зарегистрироваться"
                        pos_hint: {'center_x': .5}
                        md_bg_color: app.theme_cls.accent_color
                        text_color:  [1, 1, 1, 1]
                        on_release: app.register(reg_username.text, reg_password.text, reg_confirm_password.text, reg_email.text)

                    MDRaisedButton:
                        text: "Есть аккаунт?"
                        pos_hint: {'center_x': .5}
                        md_bg_color: app.theme_cls.primary_color
                        text_color:  [1, 1, 1, 1]
                        on_release: 
                            app.root.current = 'login'
                            app.root.transition.direction = 'right'

        Widget:
            size_hint_y: None
            height: dp(120)

<InterestSelectionScreen>:
    name: 'interest_selection'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal

        MDLabel:
            text: "Выберите интересы"
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            font_style: 'H5'
            size_hint_y: None
            height: dp(60)

        MDScrollView:
            MDBoxLayout:
                id: interest_list
                orientation: 'vertical'
                padding: dp(20)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

        MDRaisedButton:
            text: "Сохранить"
            pos_hint: {'center_x': .5}
            md_bg_color: app.theme_cls.accent_color
            text_color: app.theme_cls.text_color
            on_release: app.save_interests()

<MapScreen>:
    name: 'map'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal

        MDLabel:
            text: "Карта"
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            font_style: 'H5'
            size_hint_y: None
            height: dp(60)

        MDBoxLayout:
            id: map_container
            size_hint_y: None
            height: self.parent.height - dp(120)

        MDRaisedButton:
            text: "Назад"
            pos_hint: {'center_x': .5}
            md_bg_color: app.theme_cls.primary_color
            text_color: app.theme_cls.text_color
            on_release: 
                app.root.current = 'navigation'
                app.root.transition.direction = 'right'

<NavigationScreen>:
    name: 'navigation'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal

        MDBottomNavigation:
            panel_color: app.theme_cls.bg_light
            id: bottom_navigation  # Убедитесь, что id задан

            MDBottomNavigationItem:
                name: 'recommendations'
                icon: "home"
                on_tab_press: app.update_recommendations()

                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal

                    MDLabel:
                        text: "Рекомендации"
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        font_style: 'H5'
                        size_hint_y: None
                        height: dp(60)

                    MDSwiper:
                        id: recommended_places
                        size_hint_y: None
                        height: self.parent.height - dp(60) - dp(48)
                        swipe_distance: dp(50)
                        swipe_transition: 'out_quad'

            MDBottomNavigationItem:
                name: 'routes'
                icon: "map"
                on_tab_press: app.update_routes()

                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal

                    MDLabel:
                        text: "Маршруты"
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        font_style: 'H5'
                        size_hint_y: None
                        height: dp(60)

                    MDScrollView:
                        scroll_y: 1  # Устанавливаем начальную позицию прокрутки вверху
                        MDBoxLayout:
                            id: recommended_routes
                            orientation: 'vertical'
                            padding: dp(10)
                            spacing: dp(10)
                            size_hint_y: None
                            height: 0  # Начальная высота

            MDBottomNavigationItem:
                name: 'favorites'
                icon: "heart"
                on_tab_press: app.update_favorites()

                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal

                    MDLabel:
                        text: "Избранное"
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        font_style: 'H5'
                        size_hint_y: None
                        height: dp(60)

                    MDScrollView:
                        MDBoxLayout:
                            id: favorite_items
                            orientation: 'vertical'
                            padding: dp(10)
                            spacing: dp(10)
                            size_hint_y: None
                            height: self.minimum_height

            MDBottomNavigationItem:
                name: 'chatbot'
                icon: "chat"
                on_tab_press: app.start_chat()

                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal

                    MDLabel:
                        text: "Выбор интересов"
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        font_style: 'H5'
                        size_hint_y: None
                        height: dp(60)

                    MDBoxLayout:
                        id: chat_container
                        orientation: 'vertical'
                        padding: dp(20)
                        spacing: dp(20)
                        size_hint: (1, 1)  # Full size within the tab

                    MDBoxLayout:
                        orientation: 'horizontal'
                        padding: dp(10)
                        spacing: dp(10)
                        size_hint_y: None
                        height: dp(60)

                        MDTextField:
                            id: chat_input
                            hint_text: "Дополните интересы уникально"
                            mode: "rectangle"
                            line_color_focus: app.theme_cls.accent_color

                        MDRaisedButton:
                            text: "Отправить"
                            md_bg_color: app.theme_cls.accent_color
                            text_color:  [1, 1, 1, 1]
                            on_release: app.send_chat_message(chat_input.text)

            MDBottomNavigationItem:
                name: 'movies'
                icon: "movie"
                on_tab_press: app.update_movies()

                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal

                    MDLabel:
                        text: "Исторические фильмы"
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        font_style: 'H5'
                        size_hint_y: None
                        height: dp(60)

                    MDScrollView:
                        MDBoxLayout:
                            id: movie_list
                            orientation: 'vertical'
                            padding: dp(10)
                            spacing: dp(10)
                            size_hint_y: None
                            height: self.minimum_height
            MDBottomNavigationItem:
                name: 'tests'
                icon: "school"
                on_tab_press: app.update_tests()

                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal

                    MDLabel:
                        text: "Тесты"
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color
                        font_style: 'H5'
                        size_hint_y: None
                        height: dp(60)

                    MDScrollView:
                        MDBoxLayout:
                            id: test_list
                            orientation: 'vertical'
                            padding: dp(10)
                            spacing: dp(10)
                            size_hint_y: None
                            height: self.minimum_height

            MDBottomNavigationItem:
                name: 'profile'
                icon: "account"
                on_tab_press: app.update_profile()
            
                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal
                    padding: dp(10)
            
                    MDCard:
                        size_hint: (1, 1)
                        padding: dp(15)
                        radius: [20,]
                        elevation: 5
                        md_bg_color: app.theme_cls.bg_light
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
                        # Информация о пользователе (логин и email)
                        MDBoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(10)
                            size_hint_y: None
                            height: dp(80)
        
            
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: dp(5)
            
                                MDLabel:
                                    id: username_label
                                    text: ""
                                    halign: 'left'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.primary_color
                                    font_style: 'H6'
                                    bold: True
                                    size_hint_y: None
                                    height: dp(30)
            
                                MDLabel:
                                    id: email_label
                                    text: ""
                                    halign: 'left'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.primary_color
                                    font_style: 'Body2'
                                    size_hint_y: None
                                    height: dp(20)
                                    
                                # Доска с достижениями (перемещена вниз)
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint: (0.9, None)
                            height: dp(100)  # Можно оставить фиксированную высоту или сделать динамической
                            pos_hint: {'center_x': 0.5}
                            padding: [dp(10), dp(5), dp(10), dp(5)]
            
                            MDLabel:
                                text: "Достижения"
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.primary_color
                                font_style: 'H5'
                                size_hint_y: None
                                height: dp(30)
            
                            MDBoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(15)
                                size_hint_y: None
                                height: dp(55)
                                pos_hint: {'center_x': 0.5}
            
                                MDIconButton:
                                    id: ach1_image
                                    size_hint: (None, None)
                                    size: (dp(50), dp(50))
                                    on_release: app.show_achievement_info(1)
                                MDIconButton:
                                    id: ach2_image
                                    size_hint: (None, None)
                                    size: (dp(50), dp(50))
                                    on_release: app.show_achievement_info(2)
                                MDIconButton:
                                    id: ach3_image
                                    size_hint: (None, None)
                                    size: (dp(50), dp(50))
                                    on_release: app.show_achievement_info(3)
            
                            MDBoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(15)
                                size_hint_y: None
                                height: dp(55)
                                pos_hint: {'center_x': 0.5}
            
                                MDIconButton:
                                    id: ach4_image
                                    size_hint: (None, None)
                                    size: (dp(50), dp(50))
                                    on_release: app.show_achievement_info(4)
                                MDIconButton:
                                    id: ach5_image
                                    size_hint: (None, None)
                                    size: (dp(50), dp(50))
                                    on_release: app.show_achievement_info(5)
                                MDIconButton:
                                    id: ach6_image
                                    size_hint: (None, None)
                                    size: (dp(50), dp(50))
                                    on_release: app.show_achievement_info(6)
            
                        # Статистика (прогресс, маршруты, избранное)
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            padding: [dp(0), dp(10), dp(0), dp(10)]
            
                            MDLabel:
                                id: progress_label
                                text: ""
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.accent_color
                                font_style: 'Body1'
                                size_hint_y: None
                                height: dp(20)
            
                            MDLabel:
                                id: routes_completed_label
                                text: ""
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.primary_color
                                font_style: 'Caption'
                                size_hint_y: None
                                height: dp(40)
            
                            MDLabel:
                                id: favorites_count_label
                                text: ""
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.primary_color
                                font_style: 'Caption'
                                size_hint_y: None
                                height: dp(20)
            
                        # Кнопки "Интересы", "Пароль", "Отзывы"
                        MDBoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(10)
                            padding: [dp(10), dp(0), dp(10), dp(10)]
                            size_hint_y: None
                            height: dp(50)
            
                            MDRaisedButton:
                                text: "Интересы"
                                pos_hint: {'center_x': .5}
                                md_bg_color: app.theme_cls.accent_color
                                text_color: [1, 1, 1, 1]
                                size_hint_x: 0.33
                                font_size: '12sp'
                                on_release: 
                                    app.root.current = 'interest_selection'
                                    app.root.transition.direction = 'left'
            
                            MDRaisedButton:
                                text: "Пароль"
                                pos_hint: {'center_x': .5}
                                md_bg_color: app.theme_cls.accent_color
                                text_color: [1, 1, 1, 1]
                                size_hint_x: 0.33
                                font_size: '12sp'
                                on_release: app.show_change_password_dialog()
            
                            MDRaisedButton:
                                text: "Отзывы"
                                pos_hint: {'center_x': .5}
                                md_bg_color: app.theme_cls.accent_color
                                text_color: [1, 1, 1, 1]
                                size_hint_x: 0.33
                                font_size: '12sp'
                                on_release: app.show_user_reviews()
            
                        # Кнопки "Маршруты" и "Тесты"
                        MDBoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(10)
                            padding: [dp(10), dp(0), dp(10), dp(10)]
                            size_hint_y: None
                            height: dp(50)
            
                            MDRaisedButton:
                                text: "Маршруты"
                                pos_hint: {'center_x': .5}
                                md_bg_color: app.theme_cls.accent_color
                                text_color: [1, 1, 1, 1]
                                size_hint_x: 0.5
                                font_size: '12sp'
                                on_release: app.show_completed_routes()
            
                            MDRaisedButton:
                                text: "Тесты"
                                pos_hint: {'center_x': .5}
                                md_bg_color: app.theme_cls.accent_color
                                text_color: [1, 1, 1, 1]
                                size_hint_x: 0.5
                                font_size: '12sp'
                                on_release: app.show_completed_tests()
            
                        # Кнопка "Выйти"
                        MDRaisedButton:
                            text: "Выйти"
                            pos_hint: {'center_x': .5}
                            md_bg_color: app.theme_cls.primary_color
                            text_color: [1, 1, 1, 1]
                            size_hint: (0.8, None)
                            height: dp(40)
                            font_size: '14sp'
                            on_release: 
                                app.logout()
                                app.root.current = 'login'
                                app.root.transition.direction = 'right'
            
                        

<MovieScreen>:
    name: 'movie_player'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: app.theme_cls.bg_normal

        MDLabel:
            text: "Переход к видео..."
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            font_style: 'H5'
            size_hint_y: None
            height: dp(60)

        MDRaisedButton:
            text: "Назад"
            pos_hint: {'center_x': .5}
            md_bg_color: app.theme_cls.primary_color
            text_color: app.theme_cls.text_color
            on_release: 
                app.root.current = 'navigation'
                app.root.transition.direction = 'right'
'''


class LoginScreen(MDScreen):
    pass


class RegisterScreen(MDScreen):
    pass


class InterestSelectionScreen(MDScreen):
    def on_enter(self):
        self.ids.interest_list.clear_widgets()
        app = MDApp.get_running_app()
        for interest in app.available_interests:
            box = MDBoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=dp(40),
                spacing=dp(10)
            )
            checkbox = MDCheckbox(
                size_hint=(None, None),
                size=(dp(48), dp(48)),
                active=interest in app.user_interests
            )
            checkbox.bind(active=lambda instance, value, i=interest: app.toggle_interest(i, value))
            box.add_widget(checkbox)
            box.add_widget(MDLabel(
                text=interest,
                theme_text_color='Custom',
                text_color=app.theme_cls.primary_color
            ))
            self.ids.interest_list.add_widget(box)


class MapScreen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        map_container = self.ids.map_container
        map_container.clear_widgets()
        if MapView:
            map_view = MapView(
                lat=56.3269,
                lon=44.0059,
                zoom=12,
                size_hint=(1, 1)
            )
            map_container.add_widget(map_view)
            app.current_map_view = map_view
            app.display_map_markers()


class NavigationScreen(MDScreen):
    pass


class MovieScreen(MDScreen):
    def on_leave(self):
        self.ids.video_container.clear_widgets()


class RostelecomApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"  # Смягченный фиолетовый
        self.theme_cls.accent_palette = 'DeepOrange'  # Смягченный оранжевый
        self.current_user = ""
        self.current_email = ""
        self.user_interests = []
        self.current_test_route = None
        self.current_test_questions = []
        self.current_test_answers = []
        self.current_test_index = 0
        self.user_progress = 0
        self.dialog = None
        self.available_interests = ["История", "Архитектура", "Природа", "Культура", "Гастрономия"]
        self.current_active_route = None
        self.current_attraction_index = 0
        self.visited_attractions = []
        self.places = self.load_places()
        self.routes = self.load_routes()
        self.chat_history = []
        self.gpt_client = 1  # Client()
        self.chat_state = "initial"
        self.chat_cache = {}
        self.current_map_view = None
        self.current_map_type = None
        self.current_route = None
        self.image_cache = {}
        self.updating_recommendations = False
        sm = Builder.load_string(KV)
        sm.transition = SlideTransition()
        self.sm = sm
        return sm

    movies = [
        {"title": "История Кремля", "icon_path": "source/kremlin_sqr.png",
         "url": "https://www.youtube.com/watch?v=7jR3QgUGPcQ"},
        {"title": "Чкаловская лестница", "icon_path": "source/chkal_stair_sqr.png",
         "url": "https://www.youtube.com/watch?v=7jR3QgUGPcQ"},
        {"title": "Усадьба Рукавишниковых", "icon_path": "source/rekavishnikov_sqr.png",
         "url": "https://www.youtube.com/watch?v=7jR3QgUGPcQ"}
    ]

    achievements = [
        {
            "id": 1,
            "name": "Начинающий",
            "condition": "Пройти 1 маршрут",
            "description": "Пройди свой первый исторический маршрут",
            "open_image": "source/ach1_open.png",
            "close_image": "source/ach1_close.png"
        },
        {
            "id": 2,
            "name": "Умелец",
            "condition": "Пройти 3 маршрута",
            "description": "Окончание целых 3 маршрута и познай город",
            "open_image": "source/ach2_open.png",
            "close_image": "source/ach2_close.png"
        },
        {
            "id": 3,
            "name": "Гений",
            "condition": "Ответить в любом тесте на 100%",
            "description": "Написал?",
            "open_image": "source/ach3_open.png",
            "close_image": "source/ach3_close.png"
        },
        {
            "id": 4,
            "name": "Сказочный умник",
            "condition": "Решил тест на 0%",
            "description": "Как ты смог это сделать",
            "open_image": "source/ach4_open.png",
            "close_image": "source.ach4_close.png"
        },
        {
            "id": 5,
            "name": "Настоящий Dungeon Master",
            "condition": "Завершил курс на 100%",
            "description": "",
            "open_image": "source/ach5_open.png",
            "close_image": "source/ach5_close.png"
        },
        {
            "id": 6,
            "name": "Добро пожаловать",
            "condition": "Дано изначально",
            "description": "Да поддержим тебе ветер",
            "open_image": "source/ach6_open.png",
            "close_image": "source/ach6_close.png"
        }
    ]

    # Добавим в класс RostelecomApp:
    def show_achievement_info(self, ach_id):
        ach = next(a for a in self.achievements if a["id"] == ach_id)
        achievements_data = self.load_achievements()
        is_unlocked = ach_id in achievements_data[self.current_user]["unlocked"]

        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(200)
        )
        content.add_widget(Image(
            source=self.get_image_path(ach["open_image"] if is_unlocked else ach["close_image"]),
            size_hint=(None, None),
            size=(dp(100), dp(100)),
            pos_hint={'center_x': 0.5}
        ))
        content.add_widget(MDLabel(
            text=ach["name"],
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H6',
            size_hint_y=None,
            height=dp(30)
        ))
        content.add_widget(MDLabel(
            text=ach["description"],
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body1',
            size_hint_y=None,
            height=dp(40)
        ))

        dialog = MDDialog(
            title="Достижение",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def load_achievements(self):
        """Загружает данные о достижениях пользователя из achievements.json"""
        if os.path.exists("achievements.json"):
            try:
                with open("achievements.json", "r", encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Ошибка чтения achievements.json. Создаётся пустой список.")
                return {}
        return {}

    def save_achievements(self, achievements_data):
        """Сохраняет данные о достижениях в achievements.json"""
        with open("achievements.json", "w", encoding='utf-8') as f:
            json.dump(achievements_data, f, ensure_ascii=False, indent=4)

    def initialize_user_achievements(self):
        """Инициализирует достижения для нового пользователя"""
        achievements_data = self.load_achievements()
        if self.current_user not in achievements_data:
            achievements_data[self.current_user] = {
                "unlocked": [6],  # "Добро пожаловать" даётся изначально
                "locked": [1, 2, 3, 4, 5]
            }
            self.save_achievements(achievements_data)

    def check_achievements(self):
        """Проверяет условия для разблокировки достижений"""
        users = self.load_users()
        achievements_data = self.load_achievements()
        user_achievements = achievements_data.get(self.current_user, {"unlocked": [6], "locked": [1, 2, 3, 4, 5]})

        completed_routes = len(users[self.current_user].get("completed_routes", []))
        completed_tests = users[self.current_user].get("completed_tests", [])

        # Проверка условий для каждого достижения
        for ach in self.achievements:
            ach_id = ach["id"]
            if ach_id in user_achievements["locked"]:
                if ach_id == 1 and completed_routes >= 1:  # Начинающий: Пройти 1 маршрут
                    self.unlock_achievement(ach_id)
                elif ach_id == 2 and completed_routes >= 3:  # Умелец: Пройти 3 маршрута
                    self.unlock_achievement(ach_id)
                elif ach_id == 5 and self.user_progress >= 100:  # Dungeon Master: Завершил курс на 100%
                    self.unlock_achievement(ach_id)

    def check_test_achievements(self, percentage):
        """Проверяет достижения, связанные с тестами"""
        achievements_data = self.load_achievements()
        user_achievements = achievements_data.get(self.current_user, {"unlocked": [6], "locked": [1, 2, 3, 4, 5]})

        # Гений: 100% в любом тесте
        if percentage == 100 and 3 in user_achievements["locked"]:
            self.unlock_achievement(3)
        # Сказочный умник: 0% в тесте
        elif percentage == 0 and 4 in user_achievements["locked"]:
            self.unlock_achievement(4)

    def unlock_achievement(self, ach_id):
        """Разблокирует достижение и показывает уведомление"""
        achievements_data = self.load_achievements()
        user_achievements = achievements_data[self.current_user]
        if ach_id in user_achievements["locked"]:
            user_achievements["locked"].remove(ach_id)
            user_achievements["unlocked"].append(ach_id)
            self.save_achievements(achievements_data)
            ach = next(a for a in self.achievements if a["id"] == ach_id)
            self.show_notification(f"Достижение разблокировано: {ach['name']}!")

    def check_test_achievements(self, percentage):
        """Проверяет достижения, связанные с тестами"""
        achievements_data = self.load_achievements()
        user_achievements = achievements_data[self.current_user]

        if percentage == 100 and 3 in user_achievements["locked"]:
            self.unlock_achievement(3)  # Гений
        elif percentage == 0 and 4 in user_achievements["locked"]:
            self.unlock_achievement(4)  # Сказочный умник

    def load_places(self):
        """Загружает данные о местах из places.json"""
        try:
            with open("places.json", "r", encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Файл places.json не найден. Создаётся пустой список.")
            return []
        except json.JSONDecodeError:
            print("Ошибка чтения places.json. Создаётся пустой список.")
            return []

    def load_routes(self):
        """Загружает данные о маршрутах из routes.json"""
        try:
            with open("routes.json", "r", encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Файл routes.json не найден. Создаётся пустой список.")
            return []
        except json.JSONDecodeError:
            print("Ошибка чтения routes.json. Создаётся пустой список.")
            return []

    def save_places(self):
        """Сохраняет данные о местах в places.json"""
        with open("places.json", "w", encoding='utf-8') as f:
            json.dump(self.places, f, ensure_ascii=False, indent=4)

    def save_routes(self):
        """Сохраняет данные о маршрутах в routes.json"""
        with open("routes.json", "w", encoding='utf-8') as f:
            json.dump(self.routes, f, ensure_ascii=False, indent=4)

    def load_users(self):
        if os.path.exists("users.json"):
            try:
                with open("users.json", "r", encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Ошибка чтения JSON. Пересоздаю файл.")
                return {}
        return {}

    def save_users(self, users):
        with open("users.json", "w", encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

    def load_reviews(self):
        if os.path.exists("reviews.json"):
            try:
                with open("reviews.json", "r", encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Ошибка чтения reviews.json. Пересоздаю файл.")
                return {"places": {}, "routes": {}}
        return {"places": {}, "routes": {}}

    def save_reviews(self, reviews):
        with open("reviews.json", "w", encoding='utf-8') as f:
            json.dump(reviews, f, ensure_ascii=False, indent=4)

    def show_notification(self, message):
        snackbar = Snackbar(
            duration=2,
            snackbar_x=dp(10),
            snackbar_y=dp(10),
            size_hint_x=0.95,
            bg_color=self.theme_cls.accent_color
        )
        snackbar.add_widget(MDLabel(
            text=message,
            halign="center",
            theme_text_color="Custom",
            text_color=self.theme_cls.text_color
        ))
        snackbar.open()

    def validate_password(self, password):
        if not re.fullmatch(r'[A-Za-z0-9_ ]{8,}', password):
            return "Пароль должен содержать только латинские буквы, цифры, _ и пробелы и быть не короче 8 символов."
        return None

    def validate_email(self, email, users):
        # Регулярное выражение для проверки формата email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return "Некорректный формат email. Пример: user@domain.com"
        for user in users.values():
            if user["email"] == email:
                return "Пользователь с таким email уже существует!"
        return None

    def register(self, username, password, confirm_password, email):
        if not username or not password or not confirm_password or not email:
            self.show_notification("Все поля должны быть заполнены!")
            return
        if password != confirm_password:
            self.show_notification("Пароли не совпадают!")
            return
        users = self.load_users()
        if username in users:
            self.show_notification("Пользователь уже существует!")
            return
        password_error = self.validate_password(password)
        if password_error:
            self.show_notification(password_error)
            return
        email_error = self.validate_email(email, users)
        if email_error:
            self.show_notification(email_error)
            return
        users[username] = {
            "password": password,
            "email": email,
            "interests": [],
            "progress": 0,
            "favorites": {"places": [], "routes": []},
            "completed_routes": [],
            "completed_tests": []
        }
        self.save_users(users)
        self.current_user = username
        self.current_email = email
        self.user_interests = []
        self.user_progress = 0
        self.initialize_user_achievements()  # Добавляем инициализацию достижений
        self.root.current = 'interest_selection'
        self.root.transition.direction = 'left'
        self.show_notification(f"Регистрация успешна: {username}")

    def login(self, username, password):
        users = self.load_users()
        if username in users and users[username]["password"] == password:
            self.current_user = username
            self.current_email = users[username]["email"]
            self.user_interests = users[username].get("interests", [])
            self.user_progress = users[username].get("progress", 0)
            self.root.current = 'navigation'
            self.root.transition.direction = 'left'
            self.update_recommendations()
            self.show_notification(f"Вход выполнен: {username}")
        else:
            self.show_notification("Неверный логин или пароль!")

    def logout(self):
        self.current_user = ""
        self.current_email = ""
        self.user_interests = []
        self.user_progress = 0

    def toggle_interest(self, interest, value):
        if value and interest not in self.user_interests:
            self.user_interests.append(interest)
        elif not value and interest in self.user_interests:
            self.user_interests.remove(interest)

    def save_interests(self):
        users = self.load_users()
        users[self.current_user]["interests"] = self.user_interests
        self.save_users(users)
        self.root.current = 'navigation'
        self.root.transition.direction = 'left'
        self.update_recommendations()
        self.show_notification("Интересы сохранены!")

    def calculate_compatibility(self, tags):
        if not self.user_interests:
            return 0
        common_tags = len(set(tags).intersection(set(self.user_interests)))
        return (common_tags / len(self.user_interests)) * 100

    def get_image_path(self, image_path):
        if image_path in self.image_cache:
            return self.image_cache[image_path]
        if os.path.exists(image_path):
            self.image_cache[image_path] = image_path
            return image_path
        self.image_cache[image_path] = "source/zag.png"
        return "source/zag.png"

    def toggle_favorite(self, item_type, item_name, button=None):
        users = self.load_users()
        favorites = users[self.current_user]["favorites"]
        if item_type not in favorites:
            favorites[item_type] = []
        if item_name in favorites[item_type]:
            favorites[item_type].remove(item_name)
            self.show_notification(f"{item_name} удален из избранного")
            if button:
                button.icon = "heart-outline"  # Меняем иконку на пустое сердце
        else:
            favorites[item_type].append(item_name)
            self.show_notification(f"{item_name} добавлен в избранное")
            if button:
                button.icon = "heart"  # Меняем иконку на заполненное сердце
        self.save_users(users)
        self.update_favorites()  # Обновляем вкладку "Избранное"

        # Обновляем рекомендации, если они открыты
        if self.root.current == 'navigation':
            nav_screen = self.root.get_screen('navigation')
            if hasattr(nav_screen.ids,
                       'bottom_navigation') and nav_screen.ids.bottom_navigation.current == 'recommendations':
                self.update_recommendations()

    def is_favorite(self, item_type, item_name):
        users = self.load_users()
        favorites = users[self.current_user]["favorites"]
        return item_name in favorites.get(item_type, [])

    def show_place_info(self, place):
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(600)  # Увеличиваем высоту, чтобы вместить новую кнопку
        )
        content.add_widget(MDLabel(
            text=place['name'],
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H6'
        ))
        content.add_widget(Image(
            source=self.get_image_path(place['image_path']),
            size_hint=(1, None),
            height=dp(150),
            allow_stretch=True,
            keep_ratio=True
        ))
        content.add_widget(MDLabel(
            text=place['description'],
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body1'
        ))
        content.add_widget(MDLabel(
            text=f"Адрес: {place['address']}",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body2'
        ))
        content.add_widget(MDLabel(
            text=f"Рейтинг: {place['rating']:.1f}/5",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body2'
        ))
        rating_box = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(40),
            spacing=dp(5),
            pos_hint={'center_x': 0.5}
        )
        self.rating_stars = []
        for i in range(5):
            star = MDIconButton(
                icon="star-outline",
                theme_text_color="Custom",
                text_color=self.theme_cls.accent_color,
                on_release=lambda x, idx=i + 1: self.set_temp_rating(idx)
            )
            self.rating_stars.append(star)
            rating_box.add_widget(star)
        content.add_widget(rating_box)
        review_field = MDTextField(
            hint_text="Ваш отзыв",
            multiline=True,
            size_hint_y=None,
            height=dp(60)
        )
        content.add_widget(review_field)
        content.add_widget(MDRaisedButton(
            text="Отправить отзыв",
            pos_hint={'center_x': 0.5},
            size_hint_x=0.5,
            md_bg_color=self.theme_cls.accent_color,
            text_color=self.theme_cls.text_color,
            on_release=lambda x: self.submit_review('places', place['name'], review_field.text, place)
        ))
        content.add_widget(MDRaisedButton(
            text="Историческая сводка",
            pos_hint={'center_x': 0.5},
            size_hint_x=0.5,
            md_bg_color=self.theme_cls.primary_color,
            text_color=self.theme_cls.text_color,
            on_release=lambda x: self.show_historical_info(place)
        ))
        content.add_widget(MDRaisedButton(
            text="Просмотреть отзывы",
            pos_hint={'center_x': 0.5},
            size_hint_x=0.5,
            md_bg_color=self.theme_cls.primary_color,
            text_color=self.theme_cls.text_color,
            on_release=lambda x: self.show_all_reviews('places', place['name'])
        ))
        dialog = MDDialog(
            title="Информация о достопримечательности",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def set_temp_rating(self, rating):
        for i, star in enumerate(self.rating_stars):
            star.icon = "star" if i < rating else "star-outline"
        self.temp_rating = rating  # Сохраняем временный рейтинг

    def submit_review(self, item_type, item_name, review_text, item):
        if not hasattr(self, 'temp_rating') or self.temp_rating is None:
            self.show_notification("Пожалуйста, выберите рейтинг!")
            return
        if not review_text.strip():
            self.show_notification("Отзыв не может быть пустым!")
            return
        reviews = self.load_reviews()
        if item_type not in reviews:
            reviews[item_type] = {}
        if item_name not in reviews[item_type]:
            reviews[item_type][item_name] = []
        review = {"user": self.current_user, "rating": self.temp_rating, "comment": review_text}
        reviews[item_type][item_name].append(review)
        self.save_reviews(reviews)

        # Обновляем рейтинг в соответствующем списке
        if item_type == 'places':
            items = self.places
        else:
            items = self.routes
        for i, current_item in enumerate(items):
            if current_item['name'] == item_name:
                ratings = [r['rating'] for r in reviews[item_type][item_name]]
                items[i]['rating'] = sum(ratings) / len(ratings)
                break

        # Сохраняем обновленные данные
        if item_type == 'places':
            self.save_places()
        else:
            self.save_routes()

        self.show_notification("Отзыв отправлен!")
        self.temp_rating = None

        # Обновляем рекомендации только если находимся на вкладке "recommendations"
        nav_screen = self.root.get_screen('navigation')
        if hasattr(nav_screen.ids,
                   'bottom_navigation') and nav_screen.ids.bottom_navigation.current == 'recommendations':
            self.update_recommendations()

    def show_user_reviews(self):
        reviews = self.load_reviews()
        user_reviews = []
        for place, place_reviews in reviews.get('places', {}).items():
            for review in place_reviews:
                if review['user'] == self.current_user:
                    user_reviews.append((place, review))

        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        scroll = MDScrollView()
        review_list = MDBoxLayout(
            orientation='vertical',
            spacing=dp(10),
            padding=[dp(5), dp(5), dp(5), dp(5)],
            size_hint_y=None,
            height=len(user_reviews) * dp(110) if user_reviews else dp(60)  # Увеличиваем высоту
        )
        if not user_reviews:
            review_list.add_widget(MDLabel(
                text="Вы пока не оставили отзывов",
                halign='center',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(60)
            ))
        else:
            for place, review in user_reviews:
                # Карточка для отзыва
                review_card = MDCard(
                    size_hint=(0.95, None),
                    height=dp(100),
                    padding=dp(10),
                    radius=[10, ],
                    elevation=2,
                    md_bg_color=self.theme_cls.bg_light,
                    pos_hint={'center_x': 0.5}
                )
                card_layout = MDBoxLayout(
                    orientation='vertical',
                    spacing=dp(5)
                )
                # Название места
                card_layout.add_widget(MDLabel(
                    text=place,
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Body2',
                    bold=True,
                    size_hint_y=None,
                    height=dp(25)
                ))
                # Рейтинг и звёзды
                rating_box = MDBoxLayout(
                    orientation='horizontal',
                    spacing=dp(2),
                    size_hint_y=None,
                    height=dp(25)
                )
                for i in range(5):
                    star = MDIconButton(
                        icon="star" if i < review['rating'] else "star-outline",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.accent_color,
                        disabled_color=(1.0, 0.31, 0.07, 1),
                        icon_size="16sp",
                        disabled=True
                    )
                    rating_box.add_widget(star)
                card_layout.add_widget(rating_box)
                # Комментарий
                card_layout.add_widget(MDLabel(
                    text=review['comment'],
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Body1',
                    size_hint_y=None,
                    height=dp(40),
                    shorten=True,
                    shorten_from='right'
                ))
                review_card.add_widget(card_layout)
                review_list.add_widget(review_card)
        scroll.add_widget(review_list)
        content.add_widget(scroll)
        dialog = MDDialog(
            title="Мои отзывы",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def set_rating(self, item_type, item_name, rating):
        if item_type == 'places':
            items = self.places
        else:
            items = self.routes
        for i, item in enumerate(items):
            if item['name'] == item_name:
                items[i]['rating'] = (item['rating'] + rating) / 2 if item['rating'] else rating
                break
        # Сохраняем изменения
        if item_type == 'places':
            self.save_places()
        else:
            self.save_routes()
        for i, star in enumerate(self.rating_stars):
            star.icon = "star" if i < rating else "star-outline"
        self.show_notification(f"Оценка {rating} сохранена!")

    def animate_card(self, widget, index):
        anim = Animation(opacity=1, duration=0.7 + index * 0.2)  # Увеличиваем длительность
        widget.opacity = 0
        anim.start(widget)

    def show_all_reviews(self, item_type, item_name):
        reviews = self.load_reviews().get(item_type, {}).get(item_name, [])
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        scroll = MDScrollView()
        review_list = MDBoxLayout(
            orientation='vertical',
            spacing=dp(10),
            padding=[dp(5), dp(5), dp(5), dp(5)],
            size_hint_y=None,
            height=max(len(reviews) * dp(100), dp(60))
        )
        if not reviews:
            review_list.add_widget(MDLabel(
                text="Отзывов пока нет",
                halign='center',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(60)
            ))
        else:
            for review in reviews:
                print(f"Отзыв от {review['user']}: рейтинг = {review['rating']}")
                review_card = MDCard(
                    size_hint=(0.95, None),
                    height=dp(90),
                    padding=dp(10),
                    radius=[10, ],
                    elevation=2,
                    md_bg_color=self.theme_cls.bg_light,
                    pos_hint={'center_x': 0.5}
                )
                card_layout = MDBoxLayout(
                    orientation='vertical',
                    spacing=dp(5)
                )
                user_rating_box = MDBoxLayout(
                    orientation='horizontal',
                    spacing=dp(5),
                    size_hint_y=None,
                    height=dp(30),
                    size_hint_x=None,  # Фиксируем ширину
                    width=dp(200)  # Увеличиваем ширину для вмещения имени и звёзд
                )
                user_rating_box.add_widget(MDLabel(
                    text=review['user'],
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Body2',
                    bold=True,
                    size_hint_x=0.5
                ))
                stars_box = MDBoxLayout(
                    orientation='horizontal',
                    spacing=dp(-10),  # Уменьшаем расстояние между звёздами
                    size_hint_x=None,
                    width=dp(120),  # Увеличиваем ширину для 5 звёзд
                    pos_hint={'center_y': 0.5}
                )
                rating = min(max(int(review['rating']), 0), 5)
                for i in range(5):
                    star = MDIconButton(
                        icon="star" if i < rating else "star-outline",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.accent_color,
                        disabled_color=(1.0, 0.31, 0.07, 1),
                        icon_size="16sp",  # Уменьшаем размер иконок
                        disabled=True
                    )
                    stars_box.add_widget(star)
                user_rating_box.add_widget(stars_box)
                card_layout.add_widget(user_rating_box)
                card_layout.add_widget(MDLabel(
                    text=review['comment'],
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Body1',
                    size_hint_y=None,
                    height=dp(40),
                    shorten=True,
                    shorten_from='right'
                ))
                review_card.add_widget(card_layout)
                review_list.add_widget(review_card)
        scroll.add_widget(review_list)
        content.add_widget(scroll)
        dialog = MDDialog(
            title=f"Отзывы о {item_name}",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_historical_info(self, place):
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        scroll = MDScrollView()
        history_label = MDLabel(
            text=place.get('history', 'Историческая информация отсутствует'),
            halign='left',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body1',
            size_hint_y=None,
            height=dp(350)
        )
        scroll.add_widget(history_label)
        content.add_widget(scroll)

        dialog = MDDialog(
            title=f"История: {place['name']}",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def update_recommendations(self):
        # Проверяем, не выполняется ли уже обновление
        if hasattr(self, 'updating_recommendations') and self.updating_recommendations:
            print("Update already in progress, skipping...")
            return

        self.updating_recommendations = True
        print("Starting recommendations update...")

        nav_screen = self.root.get_screen('navigation')
        swiper = nav_screen.ids.recommended_places

        # Полностью очищаем swiper перед добавлением новых виджетов
        print(f"Before clear, swiper children: {len(swiper.children)}")
        swiper.clear_widgets()
        print(f"After clear, swiper children: {len(swiper.children)}")

        # Сортируем места по совместимости
        sorted_places = sorted(self.places, key=lambda x: self.calculate_compatibility(x['tags']), reverse=True)

        # Добавляем только первые 5 уникальных мест
        added_places = set()
        for idx, place in enumerate(sorted_places):
            if place['name'] in added_places or len(added_places) >= 5:
                continue

            swiper_item = MDSwiperItem()
            card = MDCard(
                id=f"rec_card_{place['name']}",
                size_hint=(0.95, None),
                height=dp(500),
                radius=[20, 20, 20, 20],
                elevation=3,
                md_bg_color=self.theme_cls.bg_light,
                pos_hint={'center_x': 0.5},
                ripple_behavior=True,
                on_release=lambda x, p=place: self.show_place_info(p)
            )
            layout = MDBoxLayout(
                orientation='vertical',
                spacing=dp(5),
                padding=dp(10)
            )
            image_container = MDCard(
                size_hint=(1, None),
                height=dp(250),
                radius=[20, 20, 0, 0],
                elevation=0,
                md_bg_color=self.theme_cls.bg_normal
            )
            image_container.add_widget(Image(
                source=self.get_image_path(place['image_path']),
                size_hint=(1, None),
                height=dp(290),
                allow_stretch=True,
                keep_ratio=True
            ))
            layout.add_widget(image_container)
            text_layout = MDBoxLayout(
                orientation='vertical',
                padding=[dp(15), dp(10), dp(15), dp(10)],
                spacing=dp(8)
            )
            text_layout.add_widget(MDLabel(
                text=place['name'],
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='H5',
                size_hint_y=None,
                height=dp(40),
                bold=True
            ))
            text_layout.add_widget(MDLabel(
                text=place['description'],
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(100),
            ))
            text_layout.add_widget(MDLabel(
                text=f"Совместимость: {int(self.calculate_compatibility(place['tags']))}%",
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.accent_color,
                font_style='Caption',
                size_hint_y=None,
                height=dp(20)
            ))
            text_layout.add_widget(MDLabel(
                text=f"Рейтинг: {place['rating']}/5",
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.accent_color,
                font_style='Caption',
                size_hint_y=None,
                height=dp(20)
            ))
            action_box = MDBoxLayout(
                orientation='horizontal',
                spacing=dp(10),
                size_hint_y=None,
                height=dp(50),
                pos_hint={'center_x': 0.5}
            )
            favorite_button = MDIconButton(
                icon="heart" if self.is_favorite('places', place['name']) else "heart-outline",
                theme_text_color="Custom",
                text_color=self.theme_cls.accent_color,
                icon_size="30sp"
            )
            favorite_button.bind(
                on_release=lambda x, p=place, btn=favorite_button: self.toggle_favorite('places', p['name'], btn))
            action_box.add_widget(favorite_button)
            action_box.add_widget(MDIconButton(
                icon="map-marker",
                theme_text_color="Custom",
                text_color=self.theme_cls.accent_color,
                icon_size="30sp",
                on_release=lambda x, p=place: self.open_google_maps(p['address'])
            ))
            layout.add_widget(text_layout)
            layout.add_widget(action_box)
            card.add_widget(layout)
            swiper_item.add_widget(card)
            swiper.add_widget(swiper_item)
            added_places.add(place['name'])
            # Анимация запускается только после добавления всех виджетов
            Clock.schedule_once(lambda dt, w=card, i=idx: self.animate_card(w, i), 0.1)

        print(f"Added {len(added_places)} recommendations")
        self.updating_recommendations = False

    def toggle_favorite(self, item_type, item_name, button=None):
        users = self.load_users()
        favorites = users[self.current_user]["favorites"]
        if item_type not in favorites:
            favorites[item_type] = []
        if item_name in favorites[item_type]:
            favorites[item_type].remove(item_name)
            self.show_notification(f"{item_name} удален из избранного")
            if button:
                button.icon = "heart-outline"
        else:
            favorites[item_type].append(item_name)
            self.show_notification(f"{item_name} добавлен в избранное")
            if button:
                button.icon = "heart"
        self.save_users(users)
        self.update_favorites()

        # Обновляем рекомендации только если текущая вкладка — "recommendations"
        nav_screen = self.root.get_screen('navigation')
        if hasattr(nav_screen.ids,
                   'bottom_navigation') and nav_screen.ids.bottom_navigation.current == 'recommendations':
            self.update_recommendations()

    def open_google_maps(self, address):
        if platform == 'android':
            uri = f"geo:0,0?q={address}"
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(uri))
            PythonActivity.mActivity.startActivity(intent)
        else:
            self.show_notification("Открытие Google Maps доступно только на Android!")

    def share_item(self, item_type, item):
        text = f"Рекомендую {item_type}: {item['name']} в Нижнем Новгороде! {item['description']}"
        if platform == 'android':
            intent = Intent(Intent.ACTION_SEND)
            intent.setType("text/plain")
            intent.putExtra(Intent.EXTRA_TEXT, text)
            PythonActivity.mActivity.startActivity(Intent.createChooser(intent, "Поделиться"))
        else:
            self.show_notification("Поделиться доступно только на Android!")

    def show_completed_routes(self):
        users = self.load_users()
        completed_routes = users[self.current_user].get("completed_routes", [])

        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        scroll = MDScrollView()
        route_list = MDBoxLayout(
            orientation='vertical',
            spacing=dp(10),
            padding=[dp(5), dp(5), dp(5), dp(5)],
            size_hint_y=None,
            height=len(completed_routes) * dp(60) if completed_routes else dp(60)
        )
        if not completed_routes:
            route_list.add_widget(MDLabel(
                text="Вы пока не завершили ни одного маршрута",
                halign='center',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(60)
            ))
        else:
            for route_name in completed_routes:
                route_card = MDCard(
                    size_hint=(0.95, None),
                    height=dp(50),
                    padding=dp(10),
                    radius=[10, ],
                    elevation=2,
                    md_bg_color=self.theme_cls.bg_light,
                    pos_hint={'center_x': 0.5}
                )
                route_card.add_widget(MDLabel(
                    text=route_name,
                    halign='left',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Body1',
                    size_hint_y=None,
                    height=dp(30)
                ))
                route_list.add_widget(route_card)
        scroll.add_widget(route_list)
        content.add_widget(scroll)

        dialog = MDDialog(
            title="Завершённые маршруты",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def reset_routes_tab(self):
        print("Resetting routes tab")
        nav_screen = self.root.get_screen('navigation')

        # Проверяем, существует ли bottom_navigation
        if not hasattr(nav_screen.ids, 'bottom_navigation'):
            print("Error: bottom_navigation not found in NavigationScreen")
            return

        # Получаем ScreenManager из MDBottomNavigation
        bottom_navigation = nav_screen.ids.bottom_navigation
        screen_manager = None
        for child in bottom_navigation.children:
            if isinstance(child, ScreenManager):
                screen_manager = child
                break

        if not screen_manager:
            print("Error: ScreenManager not found in bottom_navigation")
            return

        # Ищем вкладку "Маршруты"
        routes_tab = None
        for screen in screen_manager.screens:
            if screen.name == 'routes':
                routes_tab = screen
                break

        if not routes_tab:
            print("Error: routes tab not found")
            return

        # Очищаем вкладку
        routes_tab.clear_widgets()
        print("Cleared routes tab widgets")

        # Создаём базовый layout
        layout = MDBoxLayout(
            orientation='vertical',
            md_bg_color=self.theme_cls.bg_normal
        )
        layout.add_widget(MDLabel(
            text="Маршруты",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H5',
            size_hint_y=None,
            height=dp(60)
        ))
        scroll_view = MDScrollView()
        recommended_routes = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=0  # Начальная высота, будет обновлена
        )
        # Привязываем recommended_routes к ids вручную
        nav_screen.ids['recommended_routes'] = recommended_routes
        scroll_view.add_widget(recommended_routes)
        layout.add_widget(scroll_view)
        routes_tab.add_widget(layout)
        print("Routes tab reset successfully")

    def update_routes(self):
        print("Updating routes tab: Starting")
        try:
            nav_screen = self.root.get_screen('navigation')
            print("Navigation screen retrieved")

            # Проверяем, существует ли recommended_routes
            if 'recommended_routes' not in nav_screen.ids:
                print("Error: recommended_routes not found in NavigationScreen")
                return

            recommended_routes = nav_screen.ids.recommended_routes
            print("Recommended routes widget retrieved")
            recommended_routes.clear_widgets()
            recommended_routes.height = 0  # Сбрасываем высоту
            print("Cleared recommended routes widgets")

            sorted_routes = sorted(self.routes, key=lambda x: self.calculate_compatibility(x['tags']), reverse=True)
            print(f"Sorted {len(sorted_routes)} routes")
            for idx, route in enumerate(sorted_routes):
                print(f"Processing route {route['name']} (index {idx})")
                card = MDCard(
                    size_hint=(0.9, None),
                    height=dp(120),
                    padding=dp(10),
                    radius=[10, ],
                    elevation=3,
                    pos_hint={'center_x': 0.5},
                    orientation='horizontal',
                    ripple_behavior=True,
                    on_release=lambda x, r=route: self.show_route_info(r)
                )
                card.add_widget(Image(
                    source=self.get_image_path(route['image_path']),
                    size_hint=(None, None),
                    size=(dp(80), dp(80)),
                    pos_hint={'center_y': 0.5}
                ))
                text_box = MDBoxLayout(
                    orientation='vertical',
                    padding=(dp(10), 0),
                    spacing=dp(5)
                )
                text_box.add_widget(MDLabel(
                    text=route['name'],
                    halign='left',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Body1',
                    size_hint_y=None,
                    height=dp(40)
                ))
                text_box.add_widget(MDLabel(
                    text=f"Продолжительность: {route['duration']}",
                    halign='left',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Caption',
                    size_hint_y=None,
                    height=dp(20)
                ))
                text_box.add_widget(MDLabel(
                    text=f"Рейтинг: {route['rating']}/5",
                    halign='left',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.accent_color,
                    font_style='Caption',
                    size_hint_y=None,
                    height=dp(20)
                ))
                card.add_widget(text_box)
                action_box = MDBoxLayout(
                    orientation='vertical',
                    spacing=dp(5),
                    size_hint_x=None,
                    width=dp(60)
                )
                action_box.add_widget(MDIconButton(
                    icon="heart" if self.is_favorite('routes', route['name']) else "heart-outline",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.accent_color,
                    icon_size="30sp",
                    pos_hint={'center_y': 0.5},
                    on_release=lambda x, r=route: self.toggle_favorite('routes', r['name'])
                ))
                action_box.add_widget(MDIconButton(
                    icon="map",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.accent_color,
                    icon_size="30sp",
                    pos_hint={'center_y': 0.5},
                    on_release=lambda x, r=route: self.show_route_on_map(r)
                ))
                card.add_widget(action_box)
                recommended_routes.add_widget(card)
                print(f"Added card for route {route['name']}")
                # Обновляем высоту recommended_routes
                recommended_routes.height += card.height + recommended_routes.spacing
                Clock.schedule_once(lambda dt, w=card, i=idx: self.animate_card(w, i), 0.1)

            # Устанавливаем прокрутку вверху
            scroll_view = recommended_routes.parent
            if isinstance(scroll_view, MDScrollView):
                scroll_view.scroll_y = 1  # Устанавливаем прокрутку вверху
                print("Set scroll_y to 1 (top of the list)")

            print("Updating routes tab: Finished")
        except Exception as e:
            print(f"Exception in update_routes: {str(e)}")
            raise

    def restrict_scroll_up(self, scroll_view, scroll_y):
        # Если пытаемся прокрутить вверх (scroll_y увеличивается) и уже находимся вверху
        if scroll_y > 1:
            scroll_view.scroll_y = 1  # Фиксируем прокрутку вверху
        return True

    def start_route(self, route):
        print(f"Starting route: {route['name']}")
        # Сохраняем текущий маршрут
        self.current_active_route = route
        self.current_attraction_index = 0
        self.visited_attractions = []

        # Обновляем вкладку "Маршруты"
        self.show_current_route()
        self.show_notification(f"Маршрут '{route['name']}' начат!")

        # Обновляем вкладку "Маршруты"
        self.show_current_route()
        self.show_notification(f"Маршрут '{route['name']}' начат!")

    def show_current_route(self):
        print("Entering show_current_route")
        nav_screen = self.root.get_screen('navigation')

        # Проверяем, существует ли bottom_navigation
        if not hasattr(nav_screen.ids, 'bottom_navigation'):
            print("Error: bottom_navigation not found in NavigationScreen")
            return

        # Получаем ScreenManager из MDBottomNavigation
        bottom_navigation = nav_screen.ids.bottom_navigation
        screen_manager = None
        for child in bottom_navigation.children:
            if isinstance(child, ScreenManager):
                screen_manager = child
                break

        if not screen_manager:
            print("Error: ScreenManager not found in bottom_navigation")
            return

        # Ищем вкладку "Маршруты" среди экранов ScreenManager
        routes_tab = None
        for screen in screen_manager.screens:
            print(f"Screen: {screen}, Name: {screen.name}")
            if screen.name == 'routes':
                routes_tab = screen
                break

        if not routes_tab:
            print("Error: routes tab not found")
            return

        print("Found routes_tab, clearing widgets")
        # Очищаем содержимое вкладки "Маршруты"
        routes_tab.clear_widgets()

        # Создаём новый layout для текущего маршрута
        main_layout = MDBoxLayout(
            orientation='vertical',
            md_bg_color=self.theme_cls.bg_normal,
            padding=dp(10),
            spacing=dp(10)
        )

        # 1/10: Название маршрута и прогресс-бар
        progress_card = MDCard(
            size_hint_y=None,
            height=dp(80),
            radius=[15, 15, 15, 15],
            elevation=3,
            md_bg_color=self.theme_cls.primary_color
        )
        progress_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(5)
        )
        progress_layout.add_widget(MDLabel(
            text=self.current_active_route['name'],
            halign='center',
            theme_text_color='Custom',
            text_color=[1, 1, 1, 1],
            font_style='H5',
            size_hint_y=None,
            height=dp(40)
        ))
        progress = len(self.visited_attractions) / len(self.current_active_route['attractions']) * 100
        progress_bar = MDProgressBar(
            value=progress,
            size_hint_y=None,
            height=dp(20),
            color=self.theme_cls.accent_color,
            back_color=[0.2, 0.2, 0.2, 1],
            radius=[10, 10, 10, 10]
        )
        progress_layout.add_widget(progress_bar)
        progress_card.add_widget(progress_layout)
        main_layout.add_widget(progress_card)

        # 4/10: Карусель достопримечательностей
        route_map_layout = MDBoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=dp(140),
            padding=[dp(10), dp(5), dp(10), dp(5)]
        )
        route_map_layout.add_widget(MDLabel(
            text="Пункты маршрута",
            halign='left',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H6',
            size_hint_y=None,
            height=dp(30)
        ))
        scroll = MDScrollView(
            do_scroll_y=False,
            do_scroll_x=True,
            scroll_type=['bars', 'content'],
            bar_width=dp(4),
            bar_color=self.theme_cls.accent_color
        )
        carousel_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            padding=[dp(5), 0, dp(5), 0],
            size_hint_x=None,
            width=len(self.current_active_route['attractions']) * dp(100)
        )
        for idx, attraction in enumerate(self.current_active_route['attractions']):
            attraction_card = MDCard(
                size_hint=(None, None),
                size=(dp(90), dp(90)),
                radius=[15, 15, 15, 15],
                elevation=2 if idx != self.current_attraction_index else 5,
                md_bg_color=self.theme_cls.accent_color if idx in self.visited_attractions else [0.9, 0.9, 0.9, 1],
                padding=dp(5),
                pos_hint={'center_y': 0.5}
            )
            if idx == self.current_attraction_index:
                attraction_card.border = [2, 2, 2, 2]
                attraction_card.border_color = self.theme_cls.primary_color
            attraction_card.add_widget(MDLabel(
                text=attraction,
                halign='center',
                theme_text_color='Custom',
                text_color=[1, 1, 1, 1] if idx in self.visited_attractions else self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(60)
            ))
            carousel_layout.add_widget(attraction_card)
        scroll.add_widget(carousel_layout)
        route_map_layout.add_widget(scroll)
        main_layout.add_widget(route_map_layout)

        # Информация о текущей достопримечательности
        current_attraction = self.current_active_route['attractions'][self.current_attraction_index]
        place = next((p for p in self.places if p['name'] == current_attraction), None)
        if place:
            print("Adding info about current attraction")
            info_layout = MDBoxLayout(
                orientation='vertical',
                padding=dp(10),
                spacing=dp(5)
            )
            info_card = MDCard(
                size_hint=(0.95, None),
                height=dp(250),
                radius=[20, 20, 20, 20],
                elevation=3,
                md_bg_color=self.theme_cls.bg_light,
                pos_hint={'center_x': 0.5}
            )
            card_layout = MDBoxLayout(
                orientation='vertical',
                spacing=dp(5),
                padding=dp(10)
            )
            image_container = MDCard(
                size_hint=(1, None),
                height=dp(120),
                radius=[20, 20, 0, 0],
                elevation=0,
                md_bg_color=self.theme_cls.bg_normal
            )
            image_container.add_widget(Image(
                source=self.get_image_path(place['image_path']),
                size_hint=(1, None),
                height=dp(120),
                allow_stretch=True,
                keep_ratio=True
            ))
            card_layout.add_widget(image_container)
            text_layout = MDBoxLayout(
                orientation='vertical',
                padding=[dp(15), dp(10), dp(15), dp(10)],
                spacing=dp(8)
            )
            text_layout.add_widget(MDLabel(
                text=place['name'],
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='H5',
                size_hint_y=None,
                height=dp(40),
                bold=True
            ))
            text_layout.add_widget(MDLabel(
                text=place['description'],
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(60),
            ))
            text_layout.add_widget(MDLabel(
                text=f"Рейтинг: {place['rating']}/5",
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.accent_color,
                font_style='Caption',
                size_hint_y=None,
                height=dp(20)
            ))
            card_layout.add_widget(text_layout)
            info_card.add_widget(card_layout)
            info_layout.add_widget(info_card)
            main_layout.add_widget(info_layout)

        # Кнопки "Посещено", "На карте" и "Историческая сводка"
        button_layout = MDBoxLayout(
            orientation='horizontal',
            padding=[dp(20), 0, dp(20), 0],
            spacing=dp(10),
            size_hint_y=None,
            height=dp(60)
        )
        button_layout.add_widget(MDRaisedButton(
            text="Посещено",
            pos_hint={'center_x': 0.5},
            md_bg_color=self.theme_cls.accent_color,
            text_color=[1, 1, 1, 1],
            size_hint_x=0.33,  # Уменьшаем размер, чтобы вместить три кнопки
            on_release=self.mark_attraction_visited
        ))
        if place:
            button_layout.add_widget(MDRaisedButton(
                text="На карте",
                pos_hint={'center_x': 0.5},
                md_bg_color=self.theme_cls.primary_color,
                text_color=[1, 1, 1, 1],
                size_hint_x=0.33,
                on_release=lambda x: self.open_google_maps(place['address'])
            ))
            button_layout.add_widget(MDRaisedButton(
                text="История",
                pos_hint={'center_x': 0.5},
                md_bg_color=self.theme_cls.accent_color,
                text_color=[1, 1, 1, 1],
                size_hint_x=0.33,
                on_release=lambda x: self.show_historical_info(place)
            ))
        main_layout.add_widget(button_layout)

        print("Adding main_layout to routes_tab")
        routes_tab.add_widget(main_layout)
        print("Finished show_current_route")

    def mark_attraction_visited(self, instance):
        # Отмечаем текущую достопримечательность как посещённую
        if self.current_attraction_index not in self.visited_attractions:
            self.visited_attractions.append(self.current_attraction_index)

        # Переходим к следующей достопримечательности
        self.current_attraction_index += 1

        # Проверяем, завершили ли маршрут
        if self.current_attraction_index >= len(self.current_active_route['attractions']):
            self.complete_route()
        else:
            # Обновляем вкладку "Текущий маршрут" с анимацией прогресс-бара
            self.show_current_route()
            # Находим прогресс-бар и анимируем его
            progress = len(self.visited_attractions) / len(self.current_active_route['attractions']) * 100
            for child in self.root.get_screen('navigation').walk():
                if isinstance(child, MDProgressBar):
                    anim = Animation(value=progress, duration=0.5)
                    anim.start(child)
                    break
            self.show_notification("Достопримечательность отмечена как посещённая!")

    def complete_route(self):
        print("Completing route: Starting")

        # Убеждаемся, что мы на экране navigation
        if self.root.current != 'navigation':
            print(f"Switching to navigation from {self.root.current}")
            self.root.current = 'navigation'
            self.root.transition.direction = 'right'

        # Добавляем маршрут в список завершённых
        users = self.load_users()
        self.check_achievements()  # Проверяем достижения после завершения маршрута
        if "completed_routes" not in users[self.current_user]:
            users[self.current_user]["completed_routes"] = []
        if self.current_active_route['name'] not in users[self.current_user]["completed_routes"]:
            users[self.current_user]["completed_routes"].append(self.current_active_route['name'])
            print(f"Route {self.current_active_route['name']} added to completed routes")

        # Обновляем прогресс пользователя
        total_routes = len(self.routes)
        completed_routes = len(users[self.current_user]["completed_routes"])
        self.user_progress = (completed_routes / total_routes) * 100
        users[self.current_user]["progress"] = self.user_progress
        self.save_users(users)
        print(f"User progress updated: {self.user_progress}%")

        # Сбрасываем текущий маршрут
        self.current_active_route = None
        self.current_attraction_index = 0
        self.visited_attractions = []
        print("Current route reset")

        # Получаем nav_screen и проверяем наличие bottom_navigation
        nav_screen = self.root.get_screen('navigation')
        if not hasattr(nav_screen.ids, 'bottom_navigation'):
            print("Error: bottom_navigation not found in NavigationScreen")
            self.show_notification("Ошибка интерфейса. Попробуйте позже.")
            return

        # Переключаем на вкладку "routes" с задержкой
        def switch_and_update(dt):
            try:
                nav_screen.ids.bottom_navigation.switch_tab('routes')
                print("Switched to routes tab")
                self.reset_routes_tab()
                self.update_routes()
                self.show_notification("Маршрут завершён!")
            except Exception as e:
                print(f"Error during switch and update: {str(e)}")
                self.show_notification("Не удалось обновить вкладку маршрутов.")

        # Планируем переключение и обновление с небольшой задержкой
        Clock.schedule_once(switch_and_update, 0.1)

        print("Completing route: Finished")

    def _update_routes_wrapper(self):
        print("Inside _update_routes_wrapper")
        try:
            self.update_routes()
            print("update_routes completed successfully")
        except Exception as e:
            print(f"Error in update_routes: {str(e)}")

    def show_route_info(self, route):
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        content.add_widget(Image(
            source=self.get_image_path(route['image_path']),
            size_hint=(1, None),
            height=dp(150),
            allow_stretch=True,
            keep_ratio=True
        ))
        content.add_widget(MDLabel(
            text=route['name'],
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H5',
            size_hint_y=None,
            height=dp(40)
        ))
        content.add_widget(MDLabel(
            text=f"Продолжительность: {route['duration']}",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body1',
            size_hint_y=None,
            height=dp(30)
        ))
        content.add_widget(MDLabel(
            text=f"Рейтинг: {route['rating']}/5",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.accent_color,
            font_style='Body1',
            size_hint_y=None,
            height=dp(30)
        ))
        attractions_list = MDBoxLayout(
            orientation='vertical',
            spacing=dp(5),
            size_hint_y=None,
            height=len(route['attractions']) * dp(30)
        )
        for attraction in route['attractions']:
            attractions_list.add_widget(MDLabel(
                text=f"- {attraction}",
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(30)
            ))
        scroll = MDScrollView()
        scroll.add_widget(attractions_list)
        content.add_widget(scroll)

        self.dialog = MDDialog(
            title="Информация о маршруте",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="Начать маршрут",
                    md_bg_color=self.theme_cls.accent_color,
                    text_color=[1, 1, 1, 1],
                    on_release=lambda x: [
                        self.dialog.dismiss(),
                        self.start_route(route),
                        self.root.get_screen('navigation').ids.bottom_navigation.switch_tab('routes')
                        # Переключение на вкладку "Маршруты"
                    ]
                )
            ]
        )
        self.dialog.open()

    def animate_card_for_route(self, widget, index):
        # Начальная позиция карточки относительно её текущей позиции
        widget.opacity = 0
        start_y = widget.y  # Сохраняем текущую позицию y
        widget.y = start_y + dp(20)  # Смещаем немного вниз для анимации
        anim = Animation(y=start_y, opacity=1, duration=0.5 + index * 0.1)
        anim.start(widget)

    def show_route_on_map(self, route):
        self.current_map_type = 'route'
        self.current_route = route
        self.root.current = 'map'
        self.root.transition.direction = 'left'

    def display_map_markers(self):
        if not self.current_map_view:
            return
        self.current_map_view.clear_widgets()
        if self.current_map_type == 'route':
            for attraction in self.current_route['attractions']:
                for place in self.places:
                    if place['name'] == attraction:
                        marker = MapMarker(
                            lat=place['lat'],
                            lon=place['lon'],
                            source="source/marker.png" if os.path.exists("source/marker.png") else None
                        )
                        self.current_map_view.add_widget(marker)
                        break
        else:
            for place in self.places:
                marker = MapMarker(
                    lat=place['lat'],
                    lon=place['lon'],
                    source="source/marker.png" if os.path.exists("source/marker.png") else None
                )
                self.current_map_view.add_widget(marker)

    def update_favorites(self):
        nav_screen = self.root.get_screen('navigation')
        favorite_items = nav_screen.ids.favorite_items
        favorite_items.clear_widgets()

        users = self.load_users()
        favorites = users[self.current_user]["favorites"]

        # Секция "Достопримечательности в избранном"
        favorite_items.add_widget(MDLabel(
            text="Достопримечательности в избранном",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H5',
            size_hint_y=None,
            height=dp(50)
        ))

        places = favorites.get('places', [])
        if not places:
            favorite_items.add_widget(MDLabel(
                text="Нет избранных достопримечательностей",
                halign='center',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(30)
            ))
        else:
            for place_name in places:
                place = next((p for p in self.places if p['name'] == place_name), None)
                if place:
                    card = MDCard(
                        size_hint=(0.9, None),
                        height=dp(100),
                        padding=dp(10),
                        radius=[10, ],
                        elevation=3,
                        pos_hint={'center_x': 0.5},
                        orientation='horizontal',
                        ripple_behavior=True,  # Добавляем эффект нажатия
                        on_release=lambda x, p=place: self.show_place_info(p)  # Открытие окна информации
                    )
                    card.add_widget(Image(
                        source=self.get_image_path(place['image_path']),
                        size_hint=(None, None),
                        size=(dp(80), dp(80)),
                        pos_hint={'center_y': 0.5}
                    ))
                    text_box = MDBoxLayout(
                        orientation='vertical',
                        padding=(dp(10), 0),
                        spacing=dp(5)
                    )
                    text_box.add_widget(MDLabel(
                        text=place['name'],
                        halign='left',
                        theme_text_color='Custom',
                        text_color=self.theme_cls.primary_color,
                        font_style='Body1',
                        size_hint_y=None,
                        height=dp(40)
                    ))
                    text_box.add_widget(MDLabel(
                        text=f"Рейтинг: {place['rating']}/5",
                        halign='left',
                        theme_text_color='Custom',
                        text_color=self.theme_cls.accent_color,
                        font_style='Caption',
                        size_hint_y=None,
                        height=dp(20)
                    ))
                    card.add_widget(text_box)
                    # Кнопка "Избранное" с обновлением
                    favorite_button = MDIconButton(
                        icon="heart",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.accent_color,
                        icon_size="30sp",
                        pos_hint={'center_y': 0.5}
                    )
                    favorite_button.bind(
                        on_release=lambda x, p=place, btn=favorite_button: self.toggle_favorite('places', p['name'],
                                                                                                btn)
                    )
                    card.add_widget(favorite_button)
                    favorite_items.add_widget(card)

        # Разделительная черта
        favorite_items.add_widget(MDCard(
            size_hint=(0.9, None),
            height=dp(2),
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={'center_x': 0.5}
        ))

        # Секция "Маршруты в избранном"
        favorite_items.add_widget(MDLabel(
            text="Маршруты в избранном",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H5',
            size_hint_y=None,
            height=dp(50)
        ))

        routes = favorites.get('routes', [])
        if not routes:
            favorite_items.add_widget(MDLabel(
                text="Нет избранных маршрутов",
                halign='center',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(30)
            ))
        else:
            for route_name in routes:
                route = next((r for r in self.routes if r['name'] == route_name), None)
                if route:
                    card = MDCard(
                        size_hint=(0.9, None),
                        height=dp(100),
                        padding=dp(10),
                        radius=[10, ],
                        elevation=3,
                        pos_hint={'center_x': 0.5},
                        orientation='horizontal',
                        ripple_behavior=True,  # Добавляем эффект нажатия
                        on_release=lambda x, r=route: self.show_route_info(r)  # Открытие окна маршрута
                    )
                    card.add_widget(Image(
                        source=self.get_image_path(route['image_path']),
                        size_hint=(None, None),
                        size=(dp(80), dp(80)),
                        pos_hint={'center_y': 0.5}
                    ))
                    text_box = MDBoxLayout(
                        orientation='vertical',
                        padding=(dp(10), 0),
                        spacing=dp(5)
                    )
                    text_box.add_widget(MDLabel(
                        text=route['name'],
                        halign='left',
                        theme_text_color='Custom',
                        text_color=self.theme_cls.primary_color,
                        font_style='Body1',
                        size_hint_y=None,
                        height=dp(40)
                    ))
                    text_box.add_widget(MDLabel(
                        text=f"Рейтинг: {route['rating']}/5",
                        halign='left',
                        theme_text_color='Custom',
                        text_color=self.theme_cls.accent_color,
                        font_style='Caption',
                        size_hint_y=None,
                        height=dp(20)
                    ))
                    card.add_widget(text_box)
                    # Кнопка "Избранное" с обновлением
                    favorite_button = MDIconButton(
                        icon="heart",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.accent_color,
                        icon_size="30sp",
                        pos_hint={'center_y': 0.5}
                    )
                    favorite_button.bind(
                        on_release=lambda x, r=route, btn=favorite_button: self.toggle_favorite('routes', r['name'],
                                                                                                btn)
                    )
                    card.add_widget(favorite_button)
                    favorite_items.add_widget(card)

        # Обновляем высоту контейнера
        favorite_items.height = favorite_items.minimum_height

    def update_profile(self):
        nav_screen = self.root.get_screen('navigation')
        users = self.load_users()
        achievements_data = self.load_achievements()
        user_achievements = achievements_data.get(self.current_user, {"unlocked": [6], "locked": [1, 2, 3, 4, 5]})
        favorites = users[self.current_user]["favorites"]
        completed_routes = users[self.current_user].get("completed_routes", [])
        completed_tests = users[self.current_user].get("completed_tests", [])

        nav_screen.ids.username_label.text = f"Логин: {self.current_user}"
        nav_screen.ids.email_label.text = f"Email: {self.current_email}"
        for ach in self.achievements:
            ach_id = ach["id"]
            image_id = f"ach{ach_id}_image"
            image_path = ach["open_image"] if ach_id in user_achievements["unlocked"] else ach["close_image"]
            nav_screen.ids[image_id].source = self.get_image_path(image_path)

        nav_screen.ids.progress_label.text = f"Прогресс курса: {self.user_progress:.1f}%"
        nav_screen.ids.routes_completed_label.text = f"Пройдено маршрутов: {len(completed_routes)}/{len(self.routes)}\nПройдено тестов: {len(completed_tests)}/{len(self.routes)}"
        nav_screen.ids.favorites_count_label.text = f"Избранное: мест - {len(favorites.get('places', []))}, маршрутов - {len(favorites.get('routes', []))}"

    def start_chat(self):
        nav_screen = self.root.get_screen('navigation')
        chat_container = nav_screen.ids.chat_container
        chat_container.clear_widgets()
        self.current_interest_index = 0
        self.user_interests = []
        self.ask_next_interest_question()

    def ask_next_interest_question(self):
        nav_screen = self.root.get_screen('navigation')
        chat_container = nav_screen.ids.chat_container
        chat_container.clear_widgets()

        if self.current_interest_index >= len(self.available_interests):
            self.show_notification(f"Ваши интересы: {', '.join(self.user_interests)}")
            self.save_interests()
            self.update_recommendations()
            chat_container.clear_widgets()
            chat_container.add_widget(MDLabel(
                text="Интересы сохранены!",
                halign='center',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='H5',
                size_hint=(1, 1)
            ))
            return

        interest = self.available_interests[self.current_interest_index]

        # Создаём layout для вопроса
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(20),
            size_hint=(1, 1)
        )

        # Вопрос
        content.add_widget(MDLabel(
            text=f"Вам нравится {interest.lower()}?",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H5',
            size_hint_y=None,
            height=dp(60)
        ))

        # Кнопки "Интересы" и "Пароль"
        button_layout = MDBoxLayout(
            orientation='horizontal',
            padding=dp(20),
            spacing=dp(20),
            size_hint=(1, None),
            height=dp(60),
            pos_hint={'center_x': 0.5}
        )
        button_layout.add_widget(MDRaisedButton(
            text="Да",
            md_bg_color=self.theme_cls.accent_color,
            text_color=[1, 1, 1, 1],
            size_hint_x=0.4,
            on_release=lambda x: self.answer_interest(True, interest)
        ))
        button_layout.add_widget(MDRaisedButton(
            text="Нет",
            md_bg_color=self.theme_cls.primary_color,
            text_color=[1, 1, 1, 1],
            size_hint_x=0.4,
            on_release=lambda x: self.answer_interest(False, interest)
        ))
        content.add_widget(button_layout)

        # Кнопка "Выйти"

        chat_container.add_widget(content)

    def answer_interest(self, answer, interest):
        if answer:
            self.user_interests.append(interest)
        self.current_interest_index += 1
        self.ask_next_interest_question()

    def add_chat_message(self, message):
        nav_screen = self.root.get_screen('navigation')
        chat_messages = nav_screen.ids.chat_messages
        chat_messages.add_widget(MDLabel(
            text=message,
            halign='left',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            size_hint_y=None,
            height=dp(40)
        ))

    def send_chat_message(self, message):
        if not message:
            return
        nav_screen = self.root.get_screen('navigation')
        chat_messages = nav_screen.ids.chat_messages
        chat_input = nav_screen.ids.chat_input
        chat_messages.add_widget(MDLabel(
            text=message,
            halign='right',
            theme_text_color='Custom',
            text_color=self.theme_cls.accent_color,
            size_hint_y=None,
            height=dp(40)
        ))
        chat_input.text = ""
        self.chat_history.append({"role": "user", "content": message})

        if self.chat_state == "gathering":
            self.gather_interests(message)
        elif self.chat_state == "recommending":
            self.provide_recommendations(message)
        elif self.chat_state == "free":
            self.handle_free_chat(message)

    def gather_interests(self, message):
        if message in self.chat_cache:
            self.add_chat_message(self.chat_cache[message])
            return

        try:
            prompt = f"""
                Пользователь ответил: "{message}". Выясни его интересы (История, Архитектура, Природа, Культура, Гастрономия). 
                Задай следующий естественный вопрос, чтобы уточнить или продолжить выявление интересов. 
                Если уже понятно, какие интересы у пользователя, напиши "Интересы ясны: [список интересов]" и ничего больше.
                Отвечай кратко, на русском, в дружелюбном тоне.
            """
            response = self.gpt_client.chat.completions.create(
                model='gpt4free',
                messages=self.chat_history + [{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
            self.chat_history.append({"role": "assistant", "content": answer})
            self.chat_cache[message] = answer

            if "Интересы ясны:" in answer:
                interests = answer.replace("Интересы ясны: ", "").strip("[]").split(", ")
                self.user_interests = [i for i in interests if i in self.available_interests]
                self.add_chat_message(f"Класс, я понял, что тебе интересно: {', '.join(self.user_interests)}!")
                self.chat_state = "recommending"
                self.add_chat_message("Хочешь рекомендации по местам или маршрутам?")
                self.save_interests()
            else:
                self.add_chat_message(answer)
        except Exception as e:
            self.add_chat_message(f"Ошибка: {str(e)}. Давай попробуем еще раз?")
            self.add_chat_message("Что тебя привлекает в Нижнем Новгороде?")

    def provide_recommendations(self, message):
        if message in self.chat_cache:
            self.add_chat_message(self.chat_cache[message])
            return

        try:
            if "места" in message.lower():
                self.add_chat_message("Вот несколько мест, которые могут тебе понравиться:")
                sorted_places = sorted(self.places, key=lambda x: self.calculate_compatibility(x['tags']), reverse=True)
                for place in sorted_places[:2]:
                    self.add_chat_message(f"- {place['name']} ({place['duration']})")
                self.chat_cache[message] = "Рекомендации по местам предоставлены"
            elif "маршруты" in message.lower():
                self.add_chat_message("Вот несколько маршрутов для тебя:")
                sorted_routes = sorted(self.routes, key=lambda x: self.calculate_compatibility(x['tags']), reverse=True)
                for route in sorted_routes[:2]:
                    self.add_chat_message(f"- {route['name']} ({route['duration']})")
                self.chat_cache[message] = "Рекомендации по маршрутам предоставлены"
            else:
                answer = "Уточни, пожалуйста: места или маршруты?"
                self.chat_cache[message] = answer
                self.add_chat_message(answer)
                return

            self.chat_state = "free"
            self.add_chat_message("Если хочешь узнать что-то еще о Нижнем Новгороде, просто спроси!")
        except Exception as e:
            self.add_chat_message(f"Ошибка: {str(e)}. Попробуй еще раз!")

    def handle_free_chat(self, message):
        if message in self.chat_cache:
            self.add_chat_message(self.chat_cache[message])
            return

        try:
            prompt = f"""
                Пользователь спросил: "{message}". Ответь кратко, на русском, как гид по Нижнему Новгороду. 
                Если вопрос связан с местами или маршрутами, используй список: {self.places} и {self.routes}.
            """
            response = self.gpt_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.chat_history + [{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
            self.chat_history.append({"role": "assistant", "content": answer})
            self.chat_cache[message] = answer
            self.add_chat_message(answer)
        except Exception as e:
            self.add_chat_message(f"Ошибка: {str(e)}. Попробуй еще раз!")

    def show_change_password_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Смена пароля",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        id="old_password",
                        hint_text="Старый пароль",
                        password=True,
                        helper_text="Введите текущий пароль",
                        helper_text_mode="on_focus",
                        line_color_focus=self.theme_cls.accent_color
                    ),
                    MDTextField(
                        id="new_password",
                        hint_text="Новый пароль",
                        password=True,
                        helper_text="Введите новый пароль",
                        helper_text_mode="on_focus",
                        line_color_focus=self.theme_cls.accent_color
                    ),
                    orientation="vertical",
                    spacing=dp(10),
                    padding=dp(10),
                    size_hint_y=None,
                    height=dp(150)
                ),
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="Сохранить",
                        text_color=self.theme_cls.accent_color,
                        on_release=lambda x: self.change_password(
                            self.dialog.content_cls.ids.old_password.text,
                            self.dialog.content_cls.ids.new_password.text
                        )
                    ),
                ]
            )
        self.dialog.open()

    def change_password(self, old_password, new_password):
        users = self.load_users()
        if users[self.current_user]["password"] == old_password:
            password_error = self.validate_password(new_password)
            if password_error:
                self.show_notification(password_error)
                return
            users[self.current_user]["password"] = new_password
            self.save_users(users)
            self.show_notification("Пароль успешно изменен!")
            self.dialog.dismiss()
        else:
            self.show_notification("Неверный старый пароль!")

    def update_movies(self):
        nav_screen = self.root.get_screen('navigation')
        movie_list = nav_screen.ids.movie_list
        movie_list.clear_widgets()

        for movie in self.movies:
            card = MDCard(
                size_hint=(0.9, None),
                height=dp(100),
                padding=dp(10),
                radius=[10, ],
                elevation=3,
                pos_hint={'center_x': 0.5},
                orientation='horizontal',
                ripple_behavior=True,
                on_release=lambda x, m=movie: self.play_movie(m)
            )
            card.add_widget(Image(
                source=self.get_image_path(movie['icon_path']),
                size_hint=(None, None),
                size=(dp(80), dp(80)),
                pos_hint={'center_y': 0.5}
            ))
            text_box = MDBoxLayout(
                orientation='vertical',
                padding=(dp(10), 0),
                spacing=dp(5)
            )
            text_box.add_widget(MDLabel(
                text=movie['title'],
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(40)
            ))
            card.add_widget(text_box)
            movie_list.add_widget(card)

    def update_tests(self):
        nav_screen = self.root.get_screen('navigation')
        test_list = nav_screen.ids.test_list
        test_list.clear_widgets()

        for route in self.routes:
            card = MDCard(
                size_hint=(0.9, None),
                height=dp(120),
                padding=dp(10),
                radius=[10, ],
                elevation=3,
                pos_hint={'center_x': 0.5},
                orientation='horizontal',
                ripple_behavior=True,
                on_release=lambda x, r=route: self.confirm_start_test(r)
            )
            card.add_widget(Image(
                source=self.get_image_path(route['image_path']),
                size_hint=(None, None),
                size=(dp(80), dp(80)),
                pos_hint={'center_y': 0.5}
            ))
            text_box = MDBoxLayout(
                orientation='vertical',
                padding=(dp(10), 0),
                spacing=dp(5)
            )
            text_box.add_widget(MDLabel(
                text=route['name'],
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(40)
            ))
            text_box.add_widget(MDLabel(
                text=f"Вопросов: 10 из 15",
                halign='left',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Caption',
                size_hint_y=None,
                height=dp(20)
            ))
            card.add_widget(text_box)
            test_list.add_widget(card)
            test_list.height = test_list.minimum_height

    def confirm_start_test(self, route):
        dialog = MDDialog(
            title="Начать тест?",
            text=f"Желаете ли вы приступить к тесту по маршруту '{route['name']}'?",
            buttons=[
                MDFlatButton(
                    text="Нет",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: dialog.dismiss()
                ),
                MDRaisedButton(
                    text="Да",
                    md_bg_color=self.theme_cls.accent_color,
                    text_color=[1, 1, 1, 1],
                    on_release=lambda x: [dialog.dismiss(), self.start_test(route)]
                )
            ]
        )
        dialog.open()

    def start_test(self, route):
        self.current_test_route = route
        self.current_test_questions = random.sample(route['questions'], 10)  # Выбираем 10 случайных вопросов
        self.current_test_answers = []
        self.current_test_index = 0
        self.show_test_question()

    def show_test_question(self):
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        content.add_widget(MDLabel(
            text=f"Вопрос {self.current_test_index + 1}/10",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='H6',
            size_hint_y=None,
            height=dp(40)
        ))
        content.add_widget(MDLabel(
            text=self.current_test_questions[self.current_test_index]['question'],
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body1',
            size_hint_y=None,
            height=dp(60)
        ))
        options_box = MDBoxLayout(
            orientation='vertical',
            spacing=dp(5),
            size_hint_y=None,
            height=dp(200)
        )
        self.test_checkboxes = []
        for option in self.current_test_questions[self.current_test_index]['options']:
            option_box = MDBoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=dp(40)
            )
            checkbox = MDCheckbox(
                size_hint=(None, None),
                size=(dp(48), dp(48)),
                group=f"question_{self.current_test_index}"  # Группа для взаимоисключения
            )
            checkbox.bind(active=lambda instance, value, opt=option: self.select_test_answer(opt, value))
            option_box.add_widget(checkbox)
            option_box.add_widget(MDLabel(
                text=option,
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color
            ))
            self.test_checkboxes.append(checkbox)
            options_box.add_widget(option_box)
        content.add_widget(options_box)

        button_text = "Следующий вопрос" if self.current_test_index < 9 else "Завершить тест"
        button_action = self.next_test_question if self.current_test_index < 9 else self.finish_test
        content.add_widget(MDRaisedButton(
            text=button_text,
            pos_hint={'center_x': 0.5},
            md_bg_color=self.theme_cls.accent_color,
            text_color=[1, 1, 1, 1],
            on_release=button_action
        ))

        self.test_dialog = MDDialog(
            title=f"Тест: {self.current_test_route['name']}",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Отмена",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.cancel_test()
                )
            ]
        )
        self.test_dialog.open()

    def select_test_answer(self, option, value):
        if value:
            if self.current_test_index < len(self.current_test_answers):
                self.current_test_answers[self.current_test_index] = option
            else:
                self.current_test_answers.append(option)

    def next_test_question(self, instance):
        if self.current_test_index >= len(self.current_test_answers):
            self.show_notification("Выберите ответ!")
            return
        self.test_dialog.dismiss()
        self.current_test_index += 1
        self.show_test_question()

    def finish_test(self, instance):
        if self.current_test_index >= len(self.current_test_answers):
            self.show_notification("Выберите ответ!")
            return
        self.test_dialog.dismiss()
        correct_answers = sum(1 for i, answer in enumerate(self.current_test_answers) if
                              answer == self.current_test_questions[i]['correct'])
        percentage = (correct_answers / 10) * 100

        # Сохраняем результат в профиле
        users = self.load_users()
        self.check_test_achievements(percentage)  # Проверяем достижения тестов
        if "completed_tests" not in users[self.current_user]:
            users[self.current_user]["completed_tests"] = []
        if self.current_test_route['name'] not in users[self.current_user]["completed_tests"]:
            if percentage >= 80:
                users[self.current_user]["completed_tests"].append(self.current_test_route['name'])
        self.update_progress(users)
        self.save_users(users)

        # Показываем результат
        result_color = [1, 0, 0, 1] if percentage < 80 else [0, 1, 0, 1]  # Красный или зелёный
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(150)
        )
        content.add_widget(MDLabel(
            text=f"Результат: {int(percentage)}%",
            halign='center',
            theme_text_color='Custom',
            text_color=result_color,
            font_style='H5',
            size_hint_y=None,
            height=dp(60)
        ))
        content.add_widget(MDLabel(
            text="Правильных ответов: 8/10 для прохождения" if percentage < 80 else "Тест пройден!",
            halign='center',
            theme_text_color='Custom',
            text_color=self.theme_cls.primary_color,
            font_style='Body1',
            size_hint_y=None,
            height=dp(40)
        ))
        dialog = MDDialog(
            title="Результат теста",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="ОК",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: [dialog.dismiss(),
                                          self.root.get_screen('navigation').ids.bottom_navigation.switch_tab('tests')]
                )
            ]
        )
        dialog.open()
        self.current_test_route = None

    def cancel_test(self):
        self.test_dialog.dismiss()
        self.current_test_route = None
        self.root.get_screen('navigation').ids.bottom_navigation.switch_tab('tests')

    def update_progress(self, users):
        total_items = len(self.routes) + len(self.routes)  # Маршруты + тесты
        completed_routes = len(users[self.current_user].get("completed_routes", []))
        completed_tests = len(users[self.current_user].get("completed_tests", []))
        self.user_progress = ((completed_routes + completed_tests) / total_items) * 100
        users[self.current_user]["progress"] = self.user_progress

    # Обновляем update_profile для отображения пройденных тестов
    def update_profile(self):
        nav_screen = self.root.get_screen('navigation')
        users = self.load_users()
        favorites = users[self.current_user]["favorites"]
        completed_routes = users[self.current_user].get("completed_routes", [])
        completed_tests = users[self.current_user].get("completed_tests", [])
        nav_screen.ids.username_label.text = f"Логин: {self.current_user}"
        nav_screen.ids.email_label.text = f"Email: {self.current_email}"
        nav_screen.ids.progress_label.text = f"Прогресс курса: {self.user_progress:.1f}%"
        nav_screen.ids.routes_completed_label.text = f"Пройдено маршрутов: {len(completed_routes)}/{len(self.routes)}\nПройдено тестов: {len(completed_tests)}/{len(self.routes)}"
        nav_screen.ids.favorites_count_label.text = f"Избранное: мест - {len(favorites.get('places', []))}, маршрутов - {len(favorites.get('routes', []))}"

    # Добавляем метод для отображения пройденных тестов в профиле
    def show_completed_tests(self):
        users = self.load_users()
        completed_tests = users[self.current_user].get("completed_tests", [])

        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(400)
        )
        scroll = MDScrollView()
        test_list = MDBoxLayout(
            orientation='vertical',
            spacing=dp(10),
            padding=[dp(5), dp(5), dp(5), dp(5)],
            size_hint_y=None,
            height=len(completed_tests) * dp(60) if completed_tests else dp(60)
        )
        if not completed_tests:
            test_list.add_widget(MDLabel(
                text="Вы пока не прошли ни одного теста",
                halign='center',
                theme_text_color='Custom',
                text_color=self.theme_cls.primary_color,
                font_style='Body1',
                size_hint_y=None,
                height=dp(60)
            ))
        else:
            for test_name in completed_tests:
                test_card = MDCard(
                    size_hint=(0.95, None),
                    height=dp(50),
                    padding=dp(10),
                    radius=[10, ],
                    elevation=2,
                    md_bg_color=self.theme_cls.bg_light,
                    pos_hint={'center_x': 0.5}
                )
                test_card.add_widget(MDLabel(
                    text=test_name,
                    halign='left',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    font_style='Body1',
                    size_hint_y=None,
                    height=dp(30)
                ))
                test_list.add_widget(test_card)
        scroll.add_widget(test_list)
        content.add_widget(scroll)

        dialog = MDDialog(
            title="Пройденные тесты",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    text_color=self.theme_cls.accent_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def play_movie(self, movie):
        if platform == 'android':
            uri = movie['url']
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(uri))
            PythonActivity.mActivity.startActivity(intent)
            self.root.current = 'movie_player'  # Переходим на экран для показа уведомления
            self.root.transition.direction = 'left'
        else:
            self.show_notification("Открытие ссылок доступно только на Android!")

    def toggle_play_stop(self):
        movie_screen = self.root.get_screen('movie_player')
        play_stop_button = movie_screen.ids.play_stop_button

        if self.current_video:
            if self.current_video.state == 'play':
                self.current_video.state = 'pause'
                play_stop_button.text = "Играть"
            else:
                self.current_video.state = 'play'
                play_stop_button.text = "Пауза"

    def adjust_volume(self, value):
        if self.current_video:
            self.current_video.volume = value

    def stop_video(self):
        if hasattr(self, 'current_video') and self.current_video:
            self.current_video.state = 'stop'
            self.current_video = None


if __name__ == '__main__':
    RostelecomApp().run()