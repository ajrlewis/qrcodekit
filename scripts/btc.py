import sys
import argparse
from PIL import Image

sys.path.append("./")
from qrcodekit import qrcodekit


def main(args: argparse.Namespace):
    address = args.address
    output_path = args.output_path
    # Load the bitcoin logo image
    logo_path = "images/bitcoin.png"
    logo_image = Image.open(logo_path).convert("RGBA")
    qr_image = qrcodekit.get_image_with_data_and_logo(address, logo_image)
    qrcodekit.save_image(qr_image, output_path)
    return qr_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bitcoin QRCode")
    parser.add_argument(
        "--address",
        type=str,
        default="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        help="Bitcoin address to put on the QR code",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="btc.png",
        help="Output path for QR code PNG file.",
    )
    args = parser.parse_args()
    main(args)
