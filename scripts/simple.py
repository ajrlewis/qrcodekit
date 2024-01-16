import sys
import argparse
from PIL import Image

sys.path.append("./")
from qrcodekit import qrcodekit


def main(args: argparse.Namespace):
    data = args.data
    output_path = args.output_path
    qr_image = qrcodekit.get_image_with_data(data)
    qrcodekit.save_image(qr_image, output_path)
    return qr_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data QRCode")
    parser.add_argument(
        "--data",
        type=str,
        default="Hello World!",
        help="Data to put on the QR code",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="simple.png",
        help="Output path for QR code PNG file",
    )
    args = parser.parse_args()
    main(args)
