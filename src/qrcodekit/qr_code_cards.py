import os

from PIL import Image, ImageDraw, ImageFont

from . import qr_code, qr_code_formatters

ASSETS_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/assets/"


def create_wifi_card(
    ssid: str = "Drop it Like it's Hotspot",
    password: str = "Snoop Doggy Dogg",
    output_path: str = "wifi-card.png",
):
    # Parameters
    authentication_type = "WPA"
    height = 1200
    width = 800
    height_spacing = 0.03
    width_spacing = 0.01

    # Computed parameters
    font_size = round(0.03 * height)

    # Generate blank image with icons and text
    image = Image.new("RGB", (width, height), "white")

    # WIFI icon
    wifi_icon = Image.open(f"{ASSETS_PATH}/wifi.png")
    wifi_x = (width - wifi_icon.width) // 2
    wifi_y = round(5 * height_spacing * height)
    image.paste(wifi_icon, (wifi_x, wifi_y))

    # Network name
    font = ImageFont.truetype(f"{ASSETS_PATH}/arial-bold.ttf", font_size)
    draw = ImageDraw.Draw(image)
    ssid_x = (width - font.getbbox(ssid)[2]) // 2
    ssid_y = wifi_y + wifi_icon.height + round(height_spacing * height)
    draw.text((ssid_x, ssid_y), ssid, font=font, fill="black")

    # Key icon and network password
    key_icon = Image.open(f"{ASSETS_PATH}/key.png")
    font = ImageFont.truetype(f"{ASSETS_PATH}/arial.ttf", font_size)
    key_x = (width - key_icon.width - font.getbbox(password)[2]) // 2 - round(
        width_spacing * width
    )
    key_y = ssid_y + font.getbbox(ssid)[3] + round(height_spacing * height)
    password_x = key_x + key_icon.width + round(width_spacing * width)
    password_y = key_y + (key_icon.height - font.getbbox(password)[3]) // 2
    image.paste(key_icon, (key_x, key_y))
    draw.text((password_x, password_y), password, font=font, fill="black")

    # Generate and add QR code image
    qr_image = qr_code_formatters.wifi(ssid=ssid, password=password)
    qr_image_x = (width - qr_image.width) // 2
    qr_image_y = key_y + key_icon.height + round(height_spacing * height)
    image.paste(qr_image, (qr_image_x, qr_image_y))

    qr_code.save_qr_code_image(image, output_path)
    return image


# def create_bitcoin_card(address, amount, background_image_path):
#     qr_code_image = bitcoin(address, amount)
#     background_image = Image.open(background_image_path)
#     image = add_qr_code_to_image(qr_code_image, background_image)
#     image = add_text_to_image(image, f"Send Bitcoin to {address}")
#     if amount:
#         image = add_text_to_image(
#             image, f"Amount: {amount}", font_size=15, font_color=(128, 128, 128)
#         )
#     return image
