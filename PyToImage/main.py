from pytoimage import PyImage
import os


def pycode_to_img(file_path='main.py'):

    if not os.path.exists(file_path):
        return 'Файл не найден :/'

    code = PyImage(file_path, background=(255, 255, 255))
    palette = {
        'line': (255, 0, 255),
        'normal': (0, 0, 0)
    }

    code.set_color_palette(palette=palette)
    code.generate_image()
    img_name = f'{file_path.split(".")[0]}.jpg'
    code.save_image(img_name)

    return f'{img_name} сохранён!'


def main():
    file_path = input('Введите путь к файлу: ')
    print(pycode_to_img(file_path=file_path))


if __name__ == '__main__':
    main()