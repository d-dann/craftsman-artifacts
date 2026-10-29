/* ==========================================================
   CRAFTSMAN ARTIFACTS — SHARED SITE SETTINGS
   Edit ONLY this block to update contact details everywhere.
   ========================================================== */
const SITE = {
    // WhatsApp number with country code, digits only. e.g. "6598765432"
    whatsapp: "",
    // Telegram username without the @. e.g. "craftsmanartifacts"
    telegram: "",
    hours: "9am – 6pm"
};

/* ---------- Helpers (no need to edit below) ---------- */

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
    document.querySelectorAll("[data-hours]").forEach(el => el.textContent = SITE.hours);
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
    a.setAttribute("data-wa", "Hi, I was referred to Craftsman Artifacts and would like to find out more.");
    a.innerHTML = "Have a chat";
    document.body.appendChild(a);

    // Wait until the page's own first chat button has scrolled away, so two never show at once.
    const first = document.querySelector("main [data-wa]");
    if (first && "IntersectionObserver" in window) {
        a.classList.add("waiting");
        new IntersectionObserver(([entry]) => {
            a.classList.toggle("waiting", entry.isIntersecting || entry.boundingClientRect.top > 0);
        }).observe(first);
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
