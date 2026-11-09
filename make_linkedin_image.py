from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 620
MARGIN = 40
RADIUS = 24

img = Image.new("RGB", (W, H), "#FFFFFF")
draw = ImageDraw.Draw(img)

FONT_DIR = "C:/Windows/Fonts/"
def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)

f_header_num = font("arial.ttf", 46)
f_header_sub = font("arial.ttf", 22)
f_label = font("arialbd.ttf", 22)
f_big = font("arial.ttf", 34)
f_small = font("arial.ttf", 18)
f_small_bold = font("arialbd.ttf", 18)
f_body = font("arial.ttf", 21)

def rrect(xy, fill, radius=RADIUS, outline=None, width=0):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def center_text(x_center, y, text, fnt, fill, anchor="mm"):
    draw.text((x_center, y), text, font=fnt, fill=fill, anchor=anchor)

# ---------- Header: icon + number side by side ----------
header_x0, header_y0 = MARGIN, MARGIN
header_x1, header_y1 = W - MARGIN, MARGIN + 140
rrect((header_x0, header_y0, header_x1, header_y1), fill="#CECBF6")

# Triangle alert icon
icon_cx, icon_cy = header_x0 + 80, (header_y0 + header_y1) // 2
tri = [(icon_cx, icon_cy - 35), (icon_cx - 35, icon_cy + 30), (icon_cx + 35, icon_cy + 30)]
draw.polygon(tri, fill="#534AB7")
draw.ellipse((icon_cx - 4, icon_cy - 12, icon_cx + 4, icon_cy + 8), fill="#CECBF6")
draw.ellipse((icon_cx - 4, icon_cy + 14, icon_cx + 4, icon_cy + 22), fill="#CECBF6")

text_x = header_x0 + 150
draw.text((text_x, header_y0 + 35), "63.9% of churn", font=f_header_num, fill="#26215C")
draw.text((text_x, header_y0 + 95), "comes from just one customer group", font=f_header_sub, fill="#3C3489")

# ---------- 3 risk boxes ----------
box_y0 = header_y1 + 20
box_y1 = box_y0 + 240
box_w = (W - 2 * MARGIN - 2 * 20) // 3
gap = 20

risk_data = [
    {
        "x": MARGIN,
        "bg": "#C0DD97",
        "icon_color": "#27500A",
        "title": "Low risk",
        "title_color": "#173404",
        "pct": "65%",
        "pct_color": "#173404",
        "sub": "of customers",
        "sub_color": "#3B6D11",
        "churn": "7.3% churn",
        "churn_color": "#27500A",
        "mood": "smile",
        "outline": None,
    },
    {
        "x": MARGIN + box_w + gap,
        "bg": "#FAC775",
        "icon_color": "#633806",
        "title": "Medium risk",
        "title_color": "#412402",
        "pct": "~20%",
        "pct_color": "#412402",
        "sub": "of customers",
        "sub_color": "#854F0B",
        "churn": "24.4% churn",
        "churn_color": "#633806",
        "mood": "neutral",
        "outline": None,
    },
    {
        "x": MARGIN + 2 * (box_w + gap),
        "bg": "#F7C1C1",
        "icon_color": "#791F1F",
        "title": "High risk",
        "title_color": "#501313",
        "pct": "~15%",
        "pct_color": "#501313",
        "sub": "of customers",
        "sub_color": "#A32D2D",
        "churn": "63.9% churn",
        "churn_color": "#791F1F",
        "mood": "sad",
        "outline": "#E24B4A",
    },
]

for box in risk_data:
    x0, x1 = box["x"], box["x"] + box_w
    if box["outline"]:
        rrect((x0, box_y0, x1, box_y1), fill=box["bg"], outline=box["outline"], width=4)
    else:
        rrect((x0, box_y0, x1, box_y1), fill=box["bg"])

    cx = (x0 + x1) // 2

    # Face icon
    face_cy = box_y0 + 55
    r = 22
    draw.ellipse((cx - r, face_cy - r, cx + r, face_cy + r), outline=box["icon_color"], width=4)
    eye_y = face_cy - 6
    draw.ellipse((cx - 11, eye_y - 3, cx - 5, eye_y + 3), fill=box["icon_color"])
    draw.ellipse((cx + 5, eye_y - 3, cx + 11, eye_y + 3), fill=box["icon_color"])
    if box["mood"] == "smile":
        draw.arc((cx - 12, face_cy - 4, cx + 12, face_cy + 16), start=20, end=160, fill=box["icon_color"], width=3)
    elif box["mood"] == "neutral":
        draw.line((cx - 11, face_cy + 10, cx + 11, face_cy + 10), fill=box["icon_color"], width=3)
    else:
        draw.arc((cx - 12, face_cy + 4, cx + 12, face_cy + 24), start=200, end=340, fill=box["icon_color"], width=3)

    center_text(cx, box_y0 + 100, box["title"], f_label, box["title_color"])
    center_text(cx, box_y0 + 145, box["pct"], f_big, box["pct_color"])
    center_text(cx, box_y0 + 185, box["sub"], f_small, box["sub_color"])
    center_text(cx, box_y0 + 215, box["churn"], f_small_bold, box["churn_color"])

# ---------- Bottom insight box ----------
bottom_y0 = box_y1 + 20
bottom_y1 = bottom_y0 + 110
rrect((MARGIN, bottom_y0, W - MARGIN, bottom_y1), fill="#9FE1CB", radius=14)

# Target icon
tx, ty = MARGIN + 60, (bottom_y0 + bottom_y1) // 2
for rad, w_ in [(26, 5), (16, 5), (5, 0)]:
    if w_:
        draw.ellipse((tx - rad, ty - rad, tx + rad, ty + rad), outline="#085041", width=w_)
    else:
        draw.ellipse((tx - rad, ty - rad, tx + rad, ty + rad), fill="#085041")

f_body_small = font("arial.ttf", 18)
text = ("A churn-prediction model lets a bank focus retention efforts on the smallest,\n"
        "highest-risk group of customers -- instead of guessing, or reaching out to everyone.")
text_x = MARGIN + 130
draw.multiline_text((text_x, (bottom_y0 + bottom_y1) // 2), text, font=f_body_small,
                     fill="#04342C", spacing=10, anchor="lm")

img.save("churn_linkedin_image.png")
print("saved")
