from typing import Optional

from PIL import Image

from . import qr_code


def website(domain: str) -> Image.Image:
    data = f"{https://{domain}}"
    qr_code_image = qr_code.generate_qr_code_image(data)
    return qr_code_image


def email(address: str, subject: Optional[str] = None) -> Image.Image:
    data = f"mailto:{address}"
    if subject:
        data = f"{data}?subject={subject}"
    qr_code_image = qr_code.generate_qr_code_image(data)
    return qr_code_image


def wifi(ssid: str, password: str) -> Image.Image:
    data = f"WIFI:T:WPA;S:{ssid};P:{password};H:true;"
    qr_code_image = qr_code.generate_qr_code_image(data)
    return qr_code_image


def bitcoin(address: str, amount: Optional[int] = None) -> Image.Image:
    data = f"btc:{address}"
    if amount:
        data = f"{data}?amount={amount}"
    qr_code_image = qr_code.generate_qr_code_image(data)
    return qr_code_image


def nostr(npub: str) -> Image.Image:
    data = f"nostr:{npub}"
    qr_code_image = qr_code.generate_qr_code_image(data)
    return qr_code_image
