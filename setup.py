from cx_Freeze import setup, Executable

executables = [Executable('main.py', target_name='smstg.exe', base="Win32GUI")]

excludes = ['venv']


options = {'build_exe': {
      'include_msvcr': True,
      'excludes': excludes,
      }
}

setup(name='SMS-TG Sender',
      version='1.0.0',
      description='Отправка сообщения в канал Телеграм',
      executables=executables,
      options=options
      )
