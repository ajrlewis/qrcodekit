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


def create_nostr_card(npub: str):
    front, back = card(color=NOSTR_PURPLE)
    width, height = front.size

    # Logo on front

    logo = read(f"{ASSETS_PATH}/nostr-logo-with-text.png")
    logo_width, logo_height = logo.size
    scale_factor = height * 0.8 / logo_height
    logo = shrink(logo, scale_factor)
    logo_width, logo_height = logo.size
    origin = (width - logo_width) // 2, (height - logo_height) // 2
    front.paste(logo, origin, mask=logo)  # Use alpha channel of logo for mask
    qr = qrcode(f"nostr:{npub}", fill_color=WHITE, back_color=NOSTR_PURPLE)
    scale_factor = height * 0.6 / qr.height
    qr = shrink(qr, scale_factor)
    qr_width, qr_height = qr.size
    origin = (width - qr_width) // 2, int(round((height - qr_height) / 2.5))
    logger.debug(f"{origin = }")
    back.paste(qr, origin, mask=qr)  # Use alpha channel of logo for mask

    # QRCode and npub on back

    font_name = f"{ASSETS_PATH}/Ubuntu-Regular.ttf"
    font_size = 26
    font = ImageFont.truetype(font_name, size=font_size)

    bbox = font.getbbox(npub)  # (left, top, right, bottom)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[1] - bbox[3]
    text_origin = (width - text_width) // 2, origin[1] + int(round(1.1 * qr_height))
    draw = ImageDraw.Draw(back)
    draw.text(text_origin, npub, font=font, fill=WHITE)

    return front, back
