from uuid import uuid4
from nicegui import ui

messages = []

@ui.refreshable
def chat_messages(own_id):
    with ui.column().classes():
        for user_id, avatar, text in messages:
            with ui.card().classes('my-2 shadow-md rounded-lg p-3'):
                ui.chat_message(avatar=avatar, text=text, sent=user_id==own_id)

@ui.page('/')
def index():
    def send():
        messages.append((user, avatar, text.value))
        chat_messages.refresh()
        text.value = ''

    user = str(uuid4())
    avatar = f'https://robohash.org/{user}?bgset=bg2'
    with ui.column().classes('w-full items-stretch'):
        chat_messages(user)

    with ui.footer().classes('bg-teal'):
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar)
            text = ui.input(placeholder='message') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send)

ui.run()
