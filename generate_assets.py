"""Generate Fintapp-branded PNG assets for JavaFX (requires Pillow)."""
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    raise SystemExit("Install Pillow: pip install pillow")

ROOT = Path(__file__).resolve().parent / "src/main/resources/images"
FEATURE = ROOT / "feature_buttons"
FEATURE.mkdir(parents=True, exist_ok=True)

ACCENT = (16, 122, 90)  # deep teal
ACCENT2 = (34, 197, 160)  # mint
BG = (15, 23, 42)  # slate


def rounded_rect(draw, xy, fill, radius=12):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill)


def draw_logo(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    margin = size // 12
    rounded_rect(d, (margin, margin, size - margin, size - margin), BG, radius=size // 8)
    # stylized F bar
    bar_w = size // 3
    x0 = size // 4
    y0 = size // 5
    d.rounded_rectangle([x0, y0, x0 + bar_w, y0 + size // 10], fill=ACCENT2)
    d.rounded_rectangle([x0, y0 + size // 5, x0 + bar_w * 1.2, y0 + size // 5 + size // 12], fill=ACCENT)
    d.rounded_rectangle([x0, y0 + size * 2 // 5, x0 + bar_w * 0.9, y0 + size * 2 // 5 + size // 12], fill=ACCENT)
    # word mark
    try:
        font = ImageFont.truetype("arial.ttf", max(size // 8, 14))
    except OSError:
        font = ImageFont.load_default()
    text = "Fintapp"
    tw, th = d.textbbox((0, 0), text, font=font)[2:]
    tx = (size - tw) // 2
    ty = size * 11 // 16
    d.text((tx, ty), text, fill=(248, 250, 252), font=font)
    return img


def feature_tile(idx: int, label: str, size: int = 128) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    rounded_rect(d, (4, 4, size - 4, size - 4), BG, radius=18)
    hue_shift = (idx * 22) % 80
    c = (ACCENT[0], min(255, ACCENT[1] + hue_shift), ACCENT[2])
    d.ellipse([size // 4, size // 5, size * 3 // 4, size * 3 // 5], outline=c, width=6)
    try:
        font = ImageFont.truetype("arial.ttf", size // 10)
    except OSError:
        font = ImageFont.load_default()
    tw, th = d.textbbox((0, 0), label, font=font)[2:]
    d.text(((size - tw) // 2, size * 13 // 16), label, fill=(226, 232, 240), font=font)
    return img


def main():
    logo = draw_logo(512)
    logo.save(ROOT / "logo.png", "PNG")
    logo.resize((64, 64), Image.Resampling.LANCZOS).save(ROOT / "icon1.png", "PNG")

    user = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    ud = ImageDraw.Draw(user)
    rounded_rect(ud, (8, 8, 120, 120), BG, radius=24)
    ud.ellipse([44, 28, 84, 68], fill=ACCENT2)
    ud.arc([32, 70, 96, 120], start=180, end=0, fill=ACCENT2, width=8)
    user.save(ROOT / "user.png", "PNG")

    labels = [
        "Add money",
        "Pay",
        "Send",
        "Top up",
        "To bank",
        "Withdraw",
        "Bills",
        "Tickets",
        "Calc",
    ]
    for i, lab in enumerate(labels, start=1):
        feature_tile(i, lab).save(FEATURE / f"{i}.png", "PNG")

    print("Wrote images to", ROOT)


if __name__ == "__main__":
    main()
