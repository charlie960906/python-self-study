"""
百錢百雞問題

說明：百錢百雞是我國古代數學家張丘建在《算經》一書中提出的數學問題
雞翁一值錢五，雞母一值錢三，雞雛三值錢一。問雞翁、雞母、雞現代雛各幾何？
翻譯成白話文是：公雞5元一隻，母雞3元一隻，小雞1元三隻，用100塊錢買一百隻雞，問公雞、母雞、小雞各有多少隻
"""

for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        if 5*x+3*y+z/3==100:
            print(f'公雞:{x}隻，母雞{y}隻，小雞{z}隻')