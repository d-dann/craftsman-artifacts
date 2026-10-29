/* ==========================================================
   CRAFTSMAN ARTIFACTS — SHARED SITE SETTINGS
   Edit ONLY this block to update contact details everywhere.
   ========================================================== */
const SITE = {
    // WhatsApp number with country code, digits only. e.g. "6598765432"
    whatsapp: "",
    // Telegram username without the @. e.g. "craftsmanartifacts"
    telegram: "",
    hours: "9am – 6pm",
    hoursZh: "上午9点至下午6点"
};

/* ---------- Helpers (no need to edit below) ---------- */

const IS_ZH = document.documentElement.lang.startsWith("zh");
const WORDS = IS_ZH
    ? { chat: "聊一聊", general: "您好，我经朋友介绍认识 Craftsman Artifacts，想进一步了解。" }
    : { chat: "Have a chat", general: "Hi, I was referred to Craftsman Artifacts and would like to find out more." };

// Path to the site root, so links work from any page depth.
const ROOT = document.currentScript.src.replace(/site\.js.*$/, "");

function waLink(message) {
    if (!SITE.whatsapp) return ROOT + "contact/";
    return "https://wa.me/" + SITE.whatsapp + "?text=" + encodeURIComponent(message);
}

function tgLink() {
    if (!SITE.telegram) return ROOT + "contact/";
    return "https://t.me/" + SITE.telegram;
}

// Any element with data-wa="message" becomes a WhatsApp link with that message pre-filled.
// Any element with data-tg becomes a Telegram link.
function wireChatLinks(scope) {
    (scope || document).querySelectorAll("[data-wa]").forEach(el => {
        el.href = waLink(el.getAttribute("data-wa"));
        if (SITE.whatsapp) { el.target = "_blank"; el.rel = "noopener"; }
    });
    (scope || document).querySelectorAll("[data-tg]").forEach(el => {
        el.href = tgLink();
        if (SITE.telegram) { el.target = "_blank"; el.rel = "noopener"; }
    });
    document.querySelectorAll("[data-hours]").forEach(el => el.textContent = IS_ZH ? SITE.hoursZh : SITE.hours);
}

// Image paths in data/items.json are written from the site root.
function asset(path) {
    return /^https?:\/\//.test(path) ? path : ROOT + path;
}

// Load all collection + gallery items from the one shared data file.
function loadItems() {
    return fetch(ROOT + "data/items.json").then(r => r.json());
}

// Floating "Have a chat" button on every page except Contact (which has its own buttons).
function addFloatingChat() {
    if (document.body.dataset.page === "contact") return;
    document.body.classList.add("has-chat-bar");
    const a = document.createElement("a");
    a.className = "float-chat";
    a.setAttribute("data-wa", WORDS.general);
    a.textContent = WORDS.chat;
    document.body.appendChild(a);
    if (!("IntersectionObserver" in window)) return;

    // Hide the bar while a big chat button is on screen (the home hero, closing bands),
    // and until the hero button has been scrolled past, so two never show at once.
    const lead = document.querySelector("main [data-lead]");
    const bands = [...document.querySelectorAll("main .chat-band")];
    const seen = new Map();
    const update = () => {
        const leadAhead = lead && (seen.get(lead) || lead.getBoundingClientRect().top > 0);
        const bandOnScreen = bands.some(b => seen.get(b));
        a.classList.toggle("waiting", Boolean(leadAhead || bandOnScreen));
    };
    const io = new IntersectionObserver(entries => {
        entries.forEach(e => seen.set(e.target, e.isIntersecting));
        update();
    });
    [lead, ...bands].filter(Boolean).forEach(el => io.observe(el));
    update();

    // On pages with topics (Services), the bar's message follows the section being read.
    const topics = [...document.querySelectorAll("[data-chat-topic]")];
    if (topics.length) {
        const topicIO = new IntersectionObserver(entries => {
            entries.forEach(e => {
                if (!e.isIntersecting) return;
                a.setAttribute("data-wa", e.target.getAttribute("data-chat-topic"));
                a.href = waLink(a.getAttribute("data-wa"));
            });
        }, { rootMargin: "-45% 0px -45% 0px" });
        topics.forEach(t => topicIO.observe(t));
    }
}

// On phones, tuck the header away while scrolling down and bring it back on scroll up.
function tuckHeaderOnScroll() {
    const header = document.querySelector(".site-header");
    if (!header) return;
    const phone = window.matchMedia("(max-width: 860px)");
    let lastY = window.scrollY;
    window.addEventListener("scroll", () => {
        const y = window.scrollY;
        const down = y > lastY && y > 120;
        header.classList.toggle("tucked", phone.matches && down);
        lastY = y;
    }, { passive: true });
}

document.addEventListener("DOMContentLoaded", () => {
    addFloatingChat();
    wireChatLinks();
    tuckHeaderOnScroll();
});
