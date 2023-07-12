from nicegui import ui

ui.icon('thumb_up')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('CSS').style('color: #888; font-weight: bold')
    ui.label('Tailwind').classes('font-serif bg-red-600 text-white')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()