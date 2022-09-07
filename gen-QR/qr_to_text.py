import io
import qrcode

def main():
    qr = qrcode.QRCode()
    qr.add_data("Some data or links")
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())


if __name__ == "__main__":
    main()
