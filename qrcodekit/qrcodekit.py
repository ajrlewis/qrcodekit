from PIL import Image
import qrcode


BOX_SIZE = 10
BORDER = 0


def get(box_size: int = BOX_SIZE, border: int = BORDER):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    return qr


def get_image_with_data(data: str, **kwargs) -> Image.Image:
    qr = get(**kwargs)
    add_data(qr, data)
    qr_image = to_image(qr)
    return qr_image


def get_image_with_data_and_logo(
    data: str, logo_image: Image.Image, **kwargs
) -> Image.Image:
    qr_image = get_image_with_data(data, **kwargs)
    add_logo(qr_image, logo_image)
    return qr_image


def add_data(qr: qrcode.QRCode, data: str):
    qr.add_data(data)
    qr.make(fit=True)


def add_logo(
    qr_image: Image.Image,
    logo_image: Image.Image,
    box_size: int = BOX_SIZE,
    box_multiple: int = 7,
):
    # Resize the logo image to fit in the center of the QR code
    logo_size = (box_multiple * box_size, box_multiple * box_size)
    logo_image = logo_image.resize(logo_size)

    # Calculate the position to place the logo in the center of the QR code
    logo_position = (
        (qr_image.size[0] - logo_image.size[0]) // 2,
        (qr_image.size[1] - logo_image.size[1]) // 2,
    )

    # Paste the logo image onto the QR code
    qr_image.paste(logo_image, logo_position, logo_image)


def to_image(
    qr: qrcode.QRCode, fill_color: str = "black", back_color: str = "white"
) -> Image.Image:
    qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
    qr_image = qr_image.convert("RGBA")
    return qr_image


def save_image(qr_image, output_path: str):
    qr_image.save(output_path, "PNG")
