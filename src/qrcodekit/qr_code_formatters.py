from typing import Optional

from PIL import Image

from . import qr_code


def website(domain: str, output_path: Optional[str] = None) -> Image.Image:
    data = f"{https://{domain}}"
    qr_code_image = qr_code.generate_qr_code_image(data)
    if output_path:
        qr_code.save_qr_code_image(qr_code_image, output_path)
    return qr_code_image


def email(
    address: str, subject: Optional[str] = None, output_path: Optional[str] = None
) -> Image.Image:
    data = f"mailto:{address}"
    if subject:
        data = f"{data}?subject={subject}"
    qr_code_image = qr_code.generate_qr_code_image(data)
    if output_path:
        qr_code.save_qr_code_image(qr_code_image, output_path)
    return qr_code_image


def wifi(ssid: str, password: str, output_path: Optional[str] = None) -> Image.Image:
    data = f"WIFI:T:WPA;S:{ssid};P:{password};H:true;"
    qr_code_image = qr_code.generate_qr_code_image(data)
    if output_path:
        qr_code.save_qr_code_image(qr_code_image, output_path)
    return qr_code_image


def bitcoin(
    address: str,
    amount: Optional[int] = None,
    fill_color: str = "#000000",
    back_color: str = "#F2A900",
    output_path: Optional[str] = None,
) -> Image.Image:
    data = f"bitcoin:{address}"
    if amount:
        data = f"{data}?amount={amount}"
    qr_code_image = qr_code.generate_qr_code_image(
        data, fill_color=fill_color, back_color=back_color
    )
    if output_path:
        qr_code.save_qr_code_image(qr_code_image, output_path)
    return qr_code_image


def nostr(
    npub: str,
    fill_color: str = "#FFFFFF",
    back_color: str = "#A915FF",
    output_path: Optional[str] = None,
) -> Image.Image:
    data = f"nostr:{npub}"
    qr_code_image = qr_code.generate_qr_code_image(
        data, fill_color=fill_color, back_color=back_color
    )
    if output_path:
        qr_code.save_qr_code_image(qr_code_image, output_path)
    return qr_code_image
