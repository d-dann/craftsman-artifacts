"""Builds every page of the site, English (root) and Chinese (/zh/), from the wording below.
Edit the text in T, then run from the repo root:  python3 tools/build_pages.py .
Do not hand-edit the generated index.html files; changes there are overwritten."""
import sys, os
OUT = sys.argv[1]

PAGES = ["", "services/", "products/", "gallery/", "contact/"]

T = {
"en": {
    "html_lang": "en",
    "nav": ["Home", "Services", "Collection", "Gallery", "Contact"],
    "titles": ["Home", "Services", "Collection", "Gallery", "Contact"],
    "other_lang_label": "中文", "other_lang_name": "Chinese",
    "chat": "Have a chat",
    "wa_general": "Hi, I was referred to Craftsman Artifacts and would like to find out more.",
    "footer_copy": "&copy; 2026 Craftsman Artifacts, Singapore",
    "footer_replies": "Replies",
    "hours": "9am – 6pm",
    "hero_h1": "Bringing harmony into your space",
    "hero_lead": "Traditional Buddhist blessings, consecrated pieces and Feng Shui guidance in Singapore, from a practice of more than 20 years.",
    "hero_alt": "A family altar with gilded Buddha statues and lotus lamps",
    "welcome_h": "Welcome",
    "welcome": [
        "Sometimes life feels stuck: a run of bad luck, a home that no longer feels settled, or simply a wish for a fresh start. For more than 20 years, our Master has helped people through traditional Buddhist practice, consecrating sacred pieces, performing blessings and cleansings, and offering Feng Shui guidance for homes and workplaces.",
        "Our practice is rooted in Buddhism, and our door is open to everyone, whatever your background or beliefs."],
    "what_we_do": "What we do",
    "pillars": [
        ("Consecrated", "Every piece is consecrated by our Master, then placed in your home and consecrated again in its new spot."),
        ("Crafted with care", "Pieces chosen for their craftsmanship and the care of the artisans who made them."),
        ("Based in Singapore", "We meet in person, visit homes locally, and take time to understand each situation.")],
    "band_h": "Every situation is different",
    "band_p": "Tell us yours. We're happy to listen.",
    "services_h1": "Our services",
    "services_intro": "Our services draw on traditional Buddhist practice, carried out with care and respect. Everyone is welcome, whatever their faith or background. Because every person and every space is different, we always start with a conversation.",
    "dl": ["What it is", "Who it suits", "How it's done"],
    "services_end_h": "Not sure which fits?",
    "services_end_p": "Tell us what's happening, and we'll guide you to what suits your situation.",
    "jump_label": "Jump to a service",
    "services": [
        ("consecration", "开", "Consecration",
         "A traditional ritual that invites the presence of the Buddha or deity into a statue, amulet or sacred object, so it can be honoured as more than a decoration.",
         "Anyone bringing a new statue or amulet home, or who has a piece that has never been consecrated.",
         "Our Master first consecrates the piece. We then bring it to your home, help place it in a suitable Feng Shui spot, and consecrate it again in its new place. You can bring your own piece to us, or choose one from our Collection.",
         "Hi, I'd like to find out more about a consecration.",
         "Inviting a sacred presence into a statue or amulet."),
        ("blessings", "福", "Blessings",
         "Prayers and chanting offered for a person, family, home or new beginning: a new house, a new business, a birthday or a difficult season.",
         "Anyone marking a milestone, or wanting support through a hard time.",
         "We first talk about what the blessing is for. It can take place at your home, at your premises, or with us.",
         "Hi, I'd like to find out more about a blessing.",
         "Prayers for a person, family, home or new beginning."),
        ("fengshui", "风", "Feng Shui",
         "A consultation on the layout and energy of your home or workplace, guided by traditional Feng Shui principles.",
         "People moving house, renovating, opening a business, or feeling that their space no longer sits right.",
         "We ask about the space and what you hope for, then arrange a visit. You receive guidance on arrangement and, where it helps, suitable pieces.",
         "Hi, I'd like to find out more about a Feng Shui consultation.",
         "Guidance on the layout and energy of your home or workplace."),
        ("spirit-clearing", "驱", "Spirit Clearing",
         "A traditional ritual to clear unsettled or troubling energy from a person or a space.",
         "People who feel a space or a situation has become heavy or disturbed, and want it addressed through traditional practice.",
         "This always begins with a private, unhurried conversation, so our Master understands the situation before anything is arranged.",
         "Hi, I'd like to speak privately about a spirit clearing.",
         "Clearing unsettled energy from a person or a space."),
        ("cleansing", "净", "Cleansing",
         "A ritual to cleanse stagnant energy (煞气) from a home, office or object and restore a sense of peace (平安).",
         "People moving into a new or pre-owned home, coming out of a difficult period, or simply wanting a fresh start.",
         "Usually performed on-site, with guidance afterwards on keeping the space settled.",
         "Hi, I'd like to find out more about a cleansing.",
         "Cleansing stagnant energy from a home, office or object."),
    ],
    "coll_h1": "Our collection",
    "coll_intro": [
        "Each piece is chosen for its craftsmanship and consecrated with care. When you take one home, our Master consecrates it, brings it to you, helps place it in a suitable Feng Shui spot, and consecrates it again there.",
        "If a piece speaks to you, ask us about it. We'll share its story and help you decide if it suits your space."],
    "coll_filters": [("all", "All pieces"), ("statues", "Buddha statues"), ("amulets", "Amulets"), ("fengshui", "Feng Shui pieces")],
    "coll_filter_label": "Filter pieces",
    "search": "Search by name or code",
    "gal_h1": "Gallery",
    "gal_intro": "Pieces that have found their home, and moments from past work. Shared with our clients' permission.",
    "gal_filters": [("all", "Everything"), ("work", "Our work"), ("homed", "Pieces now in homes")],
    "gal_filter_label": "Filter gallery",
    "close": "Close",
    "contact_h1": "Have a chat with us",
    "contact_p": "Tell us a little about what's on your mind: a piece you saw, a space you'd like us to look at, or simply a situation you're facing. Everything you share stays private.",
    "contact_wa": "Message on WhatsApp", "contact_tg": "Message on Telegram",
    "contact_card": [("Reply hours", None), ("Where we serve", "Singapore, with home and office visits"), ("How it starts", "A short chat, then a meeting in person if it suits you")],
    "faq_h": "Common questions",
    "faq_p": "A few quick answers. For anything else, just message us.",
    "faq": [
        ("Do I need to be Buddhist?", "No. Our practice comes from Buddhist tradition, and we welcome everyone, whatever their faith or background."),
        ("How much does it cost?", "Every situation is different, so we'd like to understand yours first. Message us and we'll talk it through."),
        ("Are the pieces consecrated?", "Yes. Our Master consecrates each piece, brings it to your home, helps place it in a suitable Feng Shui spot, and consecrates it again there."),
        ("Can I collect a piece instead?", "Yes. We'll arrange pick-up or delivery with you after we chat.")],
},
"zh": {
    "html_lang": "zh-Hans",
    "nav": ["首页", "服务", "法物", "作品集", "联系我们"],
    "titles": ["首页", "服务", "法物", "作品集", "联系我们"],
    "other_lang_label": "English", "other_lang_name": "English",
    "chat": "聊一聊",
    "wa_general": "您好，我经朋友介绍认识 Craftsman Artifacts，想进一步了解。",
    "footer_copy": "&copy; 2026 Craftsman Artifacts，新加坡",
    "footer_replies": "回复时间",
    "hours": "上午9点至下午6点",
    "hero_h1": "让您的空间安宁和顺",
    "hero_lead": "传统佛教祈福、开光法物与风水指导，新加坡本地服务，二十余年修持经验。",
    "hero_alt": "供奉着镀金佛像与莲花灯的家中佛坛",
    "welcome_h": "欢迎",
    "welcome": [
        "有时候，生活似乎停滞不前：运势不顺、家中不再安宁，或只是想要一个新的开始。二十多年来，师父以传统佛教修持帮助众人，为法物开光、主持祈福与净化，并为住家与工作场所提供风水指导。",
        "我们的修持源自佛教，大门向所有人敞开，无论您的背景或信仰。"],
    "what_we_do": "我们的服务",
    "pillars": [
        ("开光加持", "每件法物皆由师父开光，送到您府上安放后，在新位置再次开光。"),
        ("匠心独运", "法物因其工艺与匠人的用心而精选。"),
        ("本地服务", "我们亲自会面、上门服务，用心了解每个情况。")],
    "band_h": "每个情况都不一样",
    "band_p": "告诉我们您的情况，我们乐意倾听。",
    "services_h1": "我们的服务",
    "services_intro": "我们的服务源自传统佛教修持，以用心与恭敬进行。无论您的信仰或背景，都欢迎您。因为每个人、每个空间都不同，我们总是从一次谈话开始。",
    "dl": ["是什么", "适合谁", "如何进行"],
    "services_end_h": "不确定哪项适合您？",
    "services_end_p": "告诉我们您的情况，我们会为您建议合适的方式。",
    "jump_label": "跳至服务",
    "services": [
        ("consecration", "开", "开光",
         "传统仪式，为佛像、护身符或圣物迎请佛菩萨的加持，使其不只是摆设，而是值得恭敬供奉的圣物。",
         "请新佛像或护身符回家的人，或家中法物尚未开光者。",
         "师父先为法物开光，再送到您府上，协助安放于合适的风水位置，并在新位置再次开光。您可带来自己的法物，或在我们的法物中挑选。",
         "您好，我想了解开光。",
         "为佛像或护身符迎请加持。"),
        ("blessings", "福", "加持祈福",
         "为个人、家庭、住宅或新的开始诵经祈福：乔迁、开业、生日，或艰难时期。",
         "迎接人生新阶段，或在困难时期需要支持的人。",
         "我们先了解祈福的缘由。可在您府上、您的营业场所或我们这里进行。",
         "您好，我想了解加持祈福。",
         "为个人、家庭、住宅或新的开始祈福。"),
        ("fengshui", "风", "风水",
         "依据传统风水原理，为您的住家或工作场所的格局与气场提供咨询。",
         "搬家、装修、开业，或觉得空间不再安稳的人。",
         "我们先了解空间与您的期望，再安排上门。您将获得布局建议，如有需要，也会推荐合适的法物。",
         "您好，我想了解风水咨询。",
         "为住家或工作场所的格局与气场提供指导。"),
        ("spirit-clearing", "驱", "驱邪",
         "以传统仪式清除人或空间中不安、困扰的能量。",
         "觉得某个空间或处境变得沉重、不安，希望以传统方式处理的人。",
         "一切从私下、从容的谈话开始，让师父在安排任何事之前先了解情况。",
         "您好，我想私下了解驱邪。",
         "清除人或空间中不安的能量。"),
        ("cleansing", "净", "净化",
         "以仪式净化住家、办公室或物品中的煞气，恢复平安。",
         "入住新屋或二手屋、走出困难时期，或只是想重新开始的人。",
         "通常上门进行，之后提供保持空间安稳的建议。",
         "您好，我想了解净化。",
         "净化住家、办公室或物品中的煞气。"),
    ],
    "coll_h1": "我们的法物",
    "coll_intro": [
        "每件法物都因其工艺而精选，并用心开光。请回家时，师父会为其开光、送到您府上、协助安放于合适的风水位置，并在那里再次开光。",
        "若有法物与您有缘，欢迎询问。我们会分享它的故事，帮助您判断是否适合您的空间。"],
    "coll_filters": [("all", "全部"), ("statues", "佛像"), ("amulets", "护身符"), ("fengshui", "风水摆件")],
    "coll_filter_label": "筛选法物",
    "search": "按名称或编号搜索",
    "gal_h1": "作品集",
    "gal_intro": "已请回家中的法物，以及过往服务的点滴。经客户同意后分享。",
    "gal_filters": [("all", "全部"), ("work", "过往服务"), ("homed", "已结缘法物")],
    "gal_filter_label": "筛选作品集",
    "close": "关闭",
    "contact_h1": "与我们聊聊",
    "contact_p": "告诉我们您的想法：您看到的某件法物、希望我们看看的空间，或只是您正面对的处境。您分享的一切都会保密。",
    "contact_wa": "通过 WhatsApp 联系", "contact_tg": "通过 Telegram 联系",
    "contact_card": [("回复时间", None), ("服务范围", "新加坡，可上门至住家与办公室"), ("如何开始", "先简短聊聊，如合适再亲自会面")],
    "faq_h": "常见问题",
    "faq_p": "以下是一些简短解答。其他问题，欢迎直接留言。",
    "faq": [
        ("我需要是佛教徒吗？", "不需要。我们的修持源自佛教传统，欢迎任何信仰或背景的人。"),
        ("费用是多少？", "每个情况都不同，我们希望先了解您的情况。欢迎留言，我们会与您详谈。"),
        ("法物有开光吗？", "有。师父会为每件法物开光，送到您府上，协助安放于合适的风水位置，并在那里再次开光。"),
        ("可以自取吗？", "可以。聊过之后，我们会与您安排自取或送货。")],
},
}

COUPLETS = {"": "平安吉祥", "services/": "佛法护持", "products/": "法物结缘", "gallery/": "缘起缘续"}


def couplet(text, cls="couplet"):
    spans = "".join(f'<span aria-hidden="true">{c}</span>' for c in text)
    return f'<p class="{cls}" lang="zh" aria-label="{text}">{spans}</p>'


def shell(lang, path, body, page, scripts=""):
    t = T[lang]
    in_zh = lang == "zh"
    # prefix from this page up to the site root (where style.css, site.js, images live)
    depth = (1 if in_zh else 0) + (1 if path else 0)
    root = "../" * depth
    # prefix from this page up to this language's home
    lang_home = "../" if path else ""
    nav = "\n".join(
        f'                <a href="{lang_home}{p}"' + (' class="active" aria-current="page"' if p == path else '') + f'>{name}</a>'
        for p, name in zip(PAGES, t["nav"]))
    other = (root + path) if in_zh else (root + "zh/" + path)
    title = t["titles"][PAGES.index(path)]
    return f'''<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="robots" content="noindex, nofollow">
    <title>{title} | Craftsman Artifacts</title>
    <link rel="stylesheet" href="{root}style.css">
</head>
<body data-page="{page}">

    <header class="site-header">
        <nav>
            <a href="{lang_home or './'}" class="logo">Craftsman Artifacts</a>
            <div class="nav-links">
{nav}
            </div>
            <a class="lang" href="{other or './'}" lang="{'en' if in_zh else 'zh-Hans'}" hreflang="{'en' if in_zh else 'zh-Hans'}">{t["other_lang_label"]}</a>
        </nav>
    </header>

    <main>
{body}
    </main>

    <footer>
        <div class="wrap">
            <span>{t["footer_copy"]}</span>
            <span>{t["footer_replies"]} <span data-hours>{t["hours"]}</span> · <a data-wa="{t["wa_general"]}">{t["chat"]}</a></span>
        </div>
    </footer>

    <script src="{root}site.js"></script>
{scripts}</body>
</html>
'''


def build(lang):
    t = T[lang]
    root = "../" if lang == "zh" else ""
    files = {}

    # ---------- Home ----------
    rows = "\n".join(f'''                    <li><a href="services/#{sid}">
                        <span class="seal" aria-hidden="true">{seal}</span>
                        <div><h3>{name}</h3><p>{short}</p></div>
                    </a></li>''' for sid, seal, name, *_r, short in t["services"])
    pillars = "\n".join(f'''                <div>
                    <h3>{h}</h3>
                    <p>{p}</p>
                </div>''' for h, p in t["pillars"])
    welcome = "\n".join(f"                <p>{p}</p>" for p in t["welcome"])
    home = f'''        <section class="hero">
            <div class="wrap">
                <div class="text">
                    <h1>{t["hero_h1"]}</h1>
                    <p class="lead">{t["hero_lead"]}</p>
                    <a class="btn" data-wa="{t["wa_general"]}" data-lead>{t["chat"]}</a>
                </div>
                {couplet(COUPLETS[""])}
                <div class="arch"><img src="{root}images/banners/altar16x9.jpeg" alt="{t["hero_alt"]}"></div>
            </div>
        </section>

        <section class="section section-paper">
            <div class="narrow">
                <h2>{t["welcome_h"]}</h2>
{welcome}
            </div>
        </section>

        <section class="section">
            <div class="narrow">
                <h2 class="section-intro">{t["what_we_do"]}</h2>
                <ul class="service-list">
{rows}
                </ul>
            </div>
        </section>

        <section class="section section-paper">
            <div class="wrap pillars">
{pillars}
            </div>
        </section>

        <section class="chat-band">
            <div class="wrap">
                <div>
                    <h2>{t["band_h"]}</h2>
                    <p>{t["band_p"]}</p>
                </div>
                <a class="btn" data-wa="{t["wa_general"]}">{t["chat"]}</a>
            </div>
        </section>
'''
    files[""] = shell(lang, "", home, "home")

    # ---------- Services ----------
    jumps = "\n".join(f'                <a class="chip" href="#{sid}">{name}</a>' for sid, seal, name, *_ in t["services"])
    blocks = "\n".join(f'''            <section class="service" id="{sid}" data-chat-topic="{wa}">
                <span class="seal" aria-hidden="true">{seal}</span>
                <div>
                    <h2>{name}</h2>
                    <dl>
                        <dt>{t["dl"][0]}</dt><dd>{what}</dd>
                        <dt>{t["dl"][1]}</dt><dd>{who}</dd>
                        <dt>{t["dl"][2]}</dt><dd>{how}</dd>
                    </dl>
                </div>
            </section>''' for sid, seal, name, what, who, how, wa, short in t["services"])
    services = f'''        <section class="page-head">
            <div class="wrap">
                {couplet(COUPLETS["services/"])}
                <div>
                    <h1>{t["services_h1"]}</h1>
                    <p>{t["services_intro"]}</p>
                </div>
            </div>
        </section>

        <div class="wrap">
            <nav class="chips jump" aria-label="{t["jump_label"]}">
{jumps}
            </nav>
{blocks}
        </div>

        <section class="chat-band">
            <div class="wrap">
                <div>
                    <h2>{t["services_end_h"]}</h2>
                    <p>{t["services_end_p"]}</p>
                </div>
                <a class="btn" data-wa="{t["wa_general"]}">{t["chat"]}</a>
            </div>
        </section>
'''
    files["services/"] = shell(lang, "services/", services, "services")

    # ---------- Collection & Gallery ----------
    dialog = f'''        <dialog class="detail" id="detail" aria-labelledby="detail-title">
            <div class="detail-body">
                <img id="detail-img" src="" alt="">
                <div class="detail-text">
                    <button class="close" type="button" aria-label="{t["close"]}">&times;</button>
                    <h2 id="detail-title"></h2>
                    <p class="code" id="detail-code"></p>
                    <dl id="detail-facts"></dl>
                    <p id="detail-desc"></p>
                    <a class="btn" id="detail-btn"></a>
                </div>
            </div>
        </dialog>
'''

    def chips(filters, label, search=False):
        buttons = "\n".join(
            f'                    <button class="chip" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>'
            for k, v in filters)
        s = f'\n                <input class="search" type="search" id="search" placeholder="{t["search"]}" aria-label="{t["search"]}">' if search else ""
        return f'''            <div class="tools">
                <div class="chips" role="group" aria-label="{label}">
{buttons}
                </div>{s}
            </div>'''

    coll_intro = "\n".join(f"                    <p>{p}</p>" for p in t["coll_intro"])
    products = f'''        <section class="page-head">
            <div class="wrap">
                {couplet(COUPLETS["products/"])}
                <div>
                    <h1>{t["coll_h1"]}</h1>
{coll_intro}
                </div>
            </div>
        </section>

        <div class="wrap">
{chips(t["coll_filters"], t["coll_filter_label"], search=True)}
            <div class="grid" id="grid"></div>
        </div>

{dialog}'''
    gallery = f'''        <section class="page-head">
            <div class="wrap">
                {couplet(COUPLETS["gallery/"])}
                <div>
                    <h1>{t["gal_h1"]}</h1>
                    <p>{t["gal_intro"]}</p>
                </div>
            </div>
        </section>

        <div class="wrap">
{chips(t["gal_filters"], t["gal_filter_label"])}
            <div class="grid" id="grid"></div>
        </div>

{dialog}'''
    coll_js = lambda mode: f'    <script src="{"../" * (2 if lang == "zh" else 1)}collection.js"></script>\n    <script>showItems("{mode}");</script>\n'
    files["products/"] = shell(lang, "products/", products, "collection", coll_js("collection"))
    files["gallery/"] = shell(lang, "gallery/", gallery, "gallery", coll_js("gallery"))

    # ---------- Contact ----------
    card = "\n".join(
        f'                        <dt>{k}</dt><dd' + (' data-hours' if v is None else '') + f'>{t["hours"] if v is None else v}</dd>'
        for k, v in t["contact_card"])
    faq = "\n".join(f'                <details><summary>{q}</summary><p>{a}</p></details>' for q, a in t["faq"])
    contact = f'''        <section class="page-head">
            <div class="wrap contact-grid">
                <div>
                    <h1>{t["contact_h1"]}</h1>
                    <p>{t["contact_p"]}</p>
                    <div class="btn-row">
                        <a class="btn" data-wa="{t["wa_general"]}">{t["contact_wa"]}</a>
                        <a class="btn btn-quiet" data-tg>{t["contact_tg"]}</a>
                    </div>
                </div>
                <div class="contact-card">
                    <dl>
{card}
                    </dl>
                </div>
            </div>
        </section>

        <section class="section section-paper">
            <div class="narrow faq">
                <h2>{t["faq_h"]}</h2>
                <p>{t["faq_p"]}</p>
{faq}
            </div>
        </section>
'''
    files["contact/"] = shell(lang, "contact/", contact, "contact")
    return files


for lang in ("en", "zh"):
    base = os.path.join(OUT, "zh") if lang == "zh" else OUT
    for path, html in build(lang).items():
        folder = os.path.join(base, path)
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w") as f:
            f.write(html)
print("ok")
