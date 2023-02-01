from decimal import Decimal, ROUND_HALF_UP


def round_decimal(number: Decimal, ndigits: int) -> Decimal:
    return number.quantize(Decimal('0.1') ** ndigits, ROUND_HALF_UP)


def normalize(number) -> Decimal:
    number = Decimal(number)
    if number.is_zero():
        return Decimal("0.0")
    s = str(number)
    return Decimal(s.rstrip('0').rstrip('.')) if '.' in s else s


def to_decimal(number) -> Decimal:
    return Decimal(str(number))


def is_number(number_str: str) -> bool:
    try:
        float(number_str)
        return True
    except (ValueError, TypeError):
        return False


def to_italic(text: str) -> str:
    return f"\x1B[3m{text}\x1B[0m"
