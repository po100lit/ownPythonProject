import qrcode
import qrcode.image.svg


def main():
    factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make('Some data or links', image_factory=factory)
    img.save('qr.svg')


if __name__ == "__main__":
    main()
