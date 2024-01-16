import sys
import argparse
from PIL import Image, ImageDraw, ImageFont

sys.path.append("./")
from qrcodekit import qrcodekit


def main(args: argparse.Namespace):
    # Get script parameters
    ssid = args.ssid
    password = args.password
    authentication_type = args.authentication_type
    height = args.height
    width = args.width
    height_spacing = args.height_spacing
    width_spacing = args.width_spacing
    output_path = args.output_path

    # font_size = 36
    font_size = round(0.03 * height)

    # Generate blank image with icons and text
    image = Image.new("RGB", (width, height), "white")

    # WIFI icon
    wifi_icon = Image.open("images/icon-wifi.png")
    wifi_x = (width - wifi_icon.width) // 2
    wifi_y = round(5 * height_spacing * height)
    image.paste(wifi_icon, (wifi_x, wifi_y))

    # Network name
    font = ImageFont.truetype("fonts/arial-bold.ttf", font_size)
    draw = ImageDraw.Draw(image)
    ssid_x = (width - font.getbbox(ssid)[2]) // 2
    ssid_y = wifi_y + wifi_icon.height + round(height_spacing * height)
    draw.text((ssid_x, ssid_y), ssid, font=font, fill="black")

    # Key icon and network password
    key_icon = Image.open("images/icon-key.png")
    font = ImageFont.truetype("fonts/arial.ttf", font_size)
    key_x = (width - key_icon.width - font.getbbox(password)[2]) // 2 - round(
        width_spacing * width
    )
    key_y = ssid_y + font.getbbox(ssid)[3] + round(height_spacing * height)
    password_x = key_x + key_icon.width + round(width_spacing * width)
    password_y = key_y + (key_icon.height - font.getbbox(password)[3]) // 2
    image.paste(key_icon, (key_x, key_y))
    draw.text((password_x, password_y), password, font=font, fill="black")

    # Generate and add QR code image
    data = f"WIFI:T:{authentication_type};S:{ssid};P:{password};H:true;"
    qr_image = qrcodekit.get_image_with_data(data)
    qr_image_x = (width - qr_image.width) // 2
    qr_image_y = key_y + key_icon.height + round(height_spacing * height)
    image.paste(qr_image, (qr_image_x, qr_image_y))

    qrcodekit.save_image(image, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WIFI QRCode")
    parser.add_argument(
        "--ssid",
        type=str,
        default="Drop it Like it's Hotspot",
        help="The WIFI network name",
    )
    parser.add_argument(
        "--password",
        type=str,
        default="Snoop Doggy Dogg",
        help="The WIFI network password",
    )
    parser.add_argument(
        "--authentication_type",
        type=str,
        default="WPA",
        help="The authentication type of the WIFI network",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=800,
        help="The page width of the WIFI credentials",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=1200,
        help="The page height of the WIFI credentials",
    )
    parser.add_argument(
        "--height_spacing",
        type=float,
        default=0.03,
        help="The height spacing of elements on the page as a percentage of the height",
    )
    parser.add_argument(
        "--width_spacing",
        type=float,
        default=0.01,
        help="The width spacing of elements on the page as a percentage of the width",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="wifi.png",
        help="Output path for QR code PNG file.",
    )
    args = parser.parse_args()
    main(args)
