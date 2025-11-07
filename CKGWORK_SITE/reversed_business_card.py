from reportlab.lib.pagesizes import landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# 出力ファイル
output_path = "reversed_business_card.pdf"

# 名刺サイズ
card_width, card_height = 91 * mm, 55 * mm

# カラー設定
bg_color = colors.Color(0.12, 0.12, 0.12)  # 濃いグレー
accent_color = colors.Color(0.75, 0.65, 0.35)  # ゴールド
text_color = colors.whitesmoke

# スタイル
styles = getSampleStyleSheet()
style = ParagraphStyle(
    "CardText",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=14,
    textColor=text_color,
    alignment=1,
)

# 内容（白紙名義）
content = [
    Paragraph("<b>R I S T O R A N T E</b>", style),
    Spacer(1, 4),
    Paragraph("<font color='#C8AA3E'>Design Sample</font>", style),
    Spacer(1, 12),
    Paragraph("info@example.com", style),
    Paragraph("〒100-0000 東京都港区南青山1-2-3", style),
    Paragraph("Tel: 〇〇〇-〇〇〇-〇〇〇〇", style),
]

# 背景描画
def draw_background(canv, doc):
    canv.setFillColor(bg_color)
    canv.rect(0, 0, card_width, card_height, stroke=0, fill=1)
    canv.setStrokeColor(accent_color)
    canv.setLineWidth(3)
    canv.line(10 * mm, card_height - 6 * mm, card_width - 10 * mm, card_height - 6 * mm)

# PDF生成
pdf = SimpleDocTemplate(output_path, pagesize=(card_width, card_height))
pdf.build(content, onFirstPage=draw_background)

print(f"✅ 出力完了: {output_path}")
