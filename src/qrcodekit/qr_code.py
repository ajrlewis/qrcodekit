from PIL import Image
import qrcode


def create_qr_code(box_size: int = 10, border: int = 0) -> qrcode.QRCode:
    """
    Creates a QR code object with the specified box size and border.

    Args:
        box_size (int): The size of each box in the QR code. Defaults to 10.
        border (int): The size of the border around the QR code. Defaults to 0.

    Returns:
        qrcode.QRCode: The created QR code object.
    """
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    return qr_code


def add_data_to_qr_code(qr_code: qrcode.QRCode, data: str) -> None:
    """
    Adds data to a QR code object and generates the QR code matrix.

    Args:
        qr_code (qrcode.QRCode): The QR code object to add data to.
        data (str): The data to be encoded in the QR code.
    """
    qr_code.add_data(data)
    qr_code.make(fit=True)


def qr_code_to_image(
    qr_code: qrcode.QRCode, fill_color: str = "black", back_color: str = "white"
) -> Image.Image:
    """
    Converts a QR code object to an image.

    Args:
        qr_code (qrcode.QRCode): The QR code object to convert.
        fill_color (str): The color to use for the QR code's fill. Defaults to "black".
        back_color (str): The color to use for the QR code's background. Defaults to "white".

    Returns:
        Image.Image: The QR code image.
    """
    qr_image = qr_code.make_image(fill_color=fill_color, back_color=back_color)
    qr_image = qr_image.convert("RGBA")
    return qr_image


def generate_qr_code_image(
    data: str,
    box_size: int = 10,
    border: int = 0,
    fill_color: str = "black",
    back_color: str = "white",
) -> Image.Image:
    """
    Generates a QR code image with the specified data.

    Args:
        data (str): The data to be encoded in the QR code.
        box_size (int): The size of each box in the QR code. Defaults to 10.
        border (int): The size of the border around the QR code. Defaults to 0.
        fill_color (str): The color to use for the QR code's fill. Defaults to "black".
        back_color (str): The color to use for the QR code's background. Defaults to "white".

    Returns:
        Image.Image: The generated QR code image.
    """
    qr_code = create_qr_code(box_size=box_size, border=border)
    add_data_to_qr_code(qr_code, data)
    qr_image = qr_code_to_image(qr_code, fill_color=fill_color, back_color=back_color)
    return qr_image


def get_image_with_data_and_logo(
    data: str, logo_image: Image.Image, **kwargs
) -> Image.Image:
    qr_image = get_image_with_data(data, **kwargs)
    add_logo(qr_image, logo_image)
    return qr_image


def add_logo_to_qr_code_image(
    qr_image: Image.Image,
    logo_image: Image.Image,
    box_size: int = 10,
    box_multiple: int = 7,
) -> Image.Image:
    """
    Adds a logo to the center of a QR code image.

    Args:
        qr_image (Image.Image): The QR code image to add the logo to.
        logo_image (Image.Image): The logo image to add to the QR code.
        box_size (int): The size of each box in the QR code. Defaults to BOX_SIZE.
        box_multiple (int): The multiple of the box size to use for the logo size. Defaults to 7.

    Returns:
        Image.Image: The QR code image with the added logo.
    """
    logo_size = (box_multiple * box_size, box_multiple * box_size)
    logo_image = logo_image.resize(logo_size)
    logo_position = (
        (qr_image.size[0] - logo_image.size[0]) // 2,
        (qr_image.size[1] - logo_image.size[1]) // 2,
    )
    qr_image.paste(logo_image, logo_position, logo_image)
    return qr_image


def save_qr_code_image(qr_image: Image.Image, output_path: str) -> None:
    """
    Saves a QR code image to a file.

    Args:
        qr_image (Image.Image): The QR code image to save.
        output_path (str): The path to save the image to.

    Returns:
        None
    """
    qr_image.save(output_path, "PNG")
