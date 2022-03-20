from time import sleep
import re


def fprint(text, theme='', end='\n'):
    """
    Fancy print your text using colors, styles, and timing.

    Note: some styles work in terminal and not the pycharm console, and vice versa
    For more info: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
    """
    styles = {'normal': 0, 'bold': 1, 'faint': 2, 'italic': 3, 'under': 4, 'blink': 5}
    themes = {
        'd'
        'matrix': {'fg': (0, 255, 0), 'bg': (0, 0, 0), 'style': styles['under'], 'speed': 0.05, 'pause': 1},
        'warning': {'fg': (230, 0, 0), 'bg': (255, 255, 50), 'style': 1, 'pause': 1.5},
        'vapor': {'fg': (77, 255, 255), 'bg': (200, 0, 200), 'style': 3, 'speed': 0.1},
        }
    theme = theme if type(theme) is dict else themes[theme] if theme in themes else {}
    fg = f"38;2;{';'.join(map(str, theme['fg']))}" if 'fg' in theme else ''
    bg = f"48;2;{';'.join(map(str, theme['bg']))}" if 'bg' in theme else ''
    style = str(theme['style']) if 'style' in theme else ''
    print(f"\033[{';'.join([code for code in [fg, bg, style] if code])}m", end='')
    speed = theme['speed'] if 'speed' in theme else 0.02
    pauses = [len(line) * speed for line in re.split('[.…!?]', text)]
    pause_index = 0
    if speed:
        for char in text:
            print(char, end='', flush=True)
            if char in '.!?\n':
                sleep(pauses[pause_index])
                pause_index += 1
            else:
                sleep(speed)
    else:
        print(text, end='')
    # if 'pause' in theme:
        sleep(theme['pause'])
    print('\033[m', end=end)


# fprint('  The Matrix  ', 'matrix', end='')
# fprint('  Watch out!  ', 'warning')
# fprint('     (っ◔◡◔)っ ♥ hello ♥     ', 'vapor')
fprint("""This is the default setting. Pause after punctuation is proportional to sentence length.
Does. It. Seem. Ok?... I dunno.""")
