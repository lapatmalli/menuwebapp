from flask import Flask, render_template, request
import random

app = Flask(__name__)

# ข้อมูลเมนูอาหาร
foods = {
    "เผ็ด": {
        "อาหารไทย": [
            {"name": "ผัดกะเพรา", "img": "krapao.jpg"},
            {"name": "ต้มยำกุ้ง", "img": "tomyum.jpg"},
            {"name": "แกงเขียวหวาน", "img": "green_curry.jpg"},
            {"name": "ส้มตำไทย", "img": "somtum.jpg"}
        ],
        "อาหารเกาหลี": [
            {"name": "บิบิมบับ", "img": "bibimbap.jpg"},
            {"name": "ซุปกิมจิ", "img": "kimchi_stew.jpg"},
            {"name": "ไก่ทอดเกาหลี", "img": "korean_fried_chicken.jpg"},
            {"name":"จาจังมยอน","img":"jajangmyeon.jpg"}
        ],
        "อาหารญี่ปุ่น": [
            {"name": "ราเม็งเผ็ด", "img": "spicy_ramen.jpg"},
            {"name": "คาราอาเกะราดซอสเผ็ด", "img": "karaage.jpg"},
            {"name": "ยากิโทริ", "img": "yakitori.jpg"},
            
        ],
        "อาหารฝรั่ง": [
            {"name": "พิซซ่าฮาวายเอี้ยน", "img": "pizza.jpg"},
            {"name": "สปาเก็ตตี้อาราเบียต้า", "img": "spaghetti_arrabiata.jpg"},
            {"name": "บาร์บีคิวริบส์", "img": "bbq_ribs.jpg"},
            {"name": "ชิลลี่ด็อก", "img": "chili_dog.jpg"}
        ]
    },
    "หวาน": {
        "อาหารไทย": [
            {"name": "บัวลอย", "img": "bualoy.jpg"},
            {"name": "ข้าวเหนียวมะม่วง", "img": "mango_sticky_rice.jpg"},
            {"name": "ลอดช่อง", "img": "lodchong.jpg"},
            {"name": "ขนมครก", "img": "khanom_krok.jpg"}
        ],
  	"อาหารเกาหลี": [
             {"name": "ฮันนี่โทสต์", "img": "honey_toast.jpg"},
             {"name": "แพนเค้กเกาหลี", "img": "hotteok.jpg"},
             {"name": "บิงซู", "img": "bingsu.jpg"},
             {"name": "ขนมต๊อก", "img": "tteok.jpg"}
        ],

        "อาหารญี่ปุ่น": [
            {"name": "โมจิ", "img": "mochi.jpg"},
            {"name": "โดรายากิ", "img": "dorayaki.jpg"},
            {"name": "พาร์เฟ่ต์ชาเขียว", "img": "matcha_parfait.jpg"},
            {"name": "ครีมพัฟ", "img": "cream_puff.jpg"}
        ],
        "อาหารฝรั่ง": [
            {"name": "เค้กช็อคโกแลต", "img": "chocolate_cake.jpg"},
            {"name": "ไอศกรีมวานิลลา", "img": "vanilla_icecream.jpg"},
            {"name": "แพนเค้กกับน้ำผึ้ง", "img": "pancakes_honey.jpg"},
            {"name": "บราวนี่", "img": "brownie.jpg"}
        ]
    },
    "เค็ม": {
        "อาหารไทย": [
            {"name": "ข้าวคลุกกะปิ", "img": "khao_kluk_kapi.jpg"},
            {"name": "ผัดซีอิ๊ว", "img": "pad_see_ew.jpg"},
            {"name": "หมูทอดกระเทียมพริกไทย", "img": "fried_pork_garlic_pepper.jpg"},
            {"name": "ไข่เจียว", "img": "omelette.jpg"}
        ],
        "อาหารเกาหลี": [
            {"name": "ต๊อกโบกี", "img": "tteokbokki.jpg"},
            {"name": "คิมบับ", "img": "gimbap.jpg"},
            {"name": "ซุนแด", "img": "sundae.jpg"},
            {"name": "พาจอน", "img": "pajeon.jpg"}
        ],
        "อาหารญี่ปุ่น": [
            {"name": "ซูชิ", "img": "sushi.jpg"},
            {"name": "ข้าวหน้าเนื้อ", "img": "gyudon.jpg"},
            {"name": "เทมปุระ", "img": "tempura.jpg"},
            {"name": "ยากิโซบะ", "img": "yakisoba.jpg"}
        ],
        "อาหารฝรั่ง": [
            {"name": "แฮมเบอร์เกอร์", "img": "burger.jpg"},
            {"name": "มันฝรั่งทอด", "img": "fries.jpg"},
            {"name": "พิซซ่าเปปเปอโรนี", "img": "pepperoni_pizza.jpg"}
            
        ]
    }
}

@app.route("/")
def index():
    tastes = foods.keys()
    categories = set()
    for t in foods.values():
        categories.update(t.keys())
    return render_template("index.html", tastes=tastes, categories=sorted(categories))

@app.route("/result", methods=["POST"])
def result():
    taste = request.form.get("taste")
    category = request.form.get("category")

    dish_list = foods.get(taste, {}).get(category, [])
    if not dish_list:
        return render_template("result.html", taste=taste, category=category, food=None)

    selected_food = random.choice(dish_list)
    return render_template("result.html", taste=taste, category=category, food=selected_food)

if __name__ == "__main__":
    app.run(debug=True)
