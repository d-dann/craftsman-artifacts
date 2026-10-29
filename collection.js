/* Collection and Gallery pages: render items from data/items.json.
   Collection = statues / amulets / fengshui pieces that are not sold.
   Gallery    = past work, plus any piece marked "sold". */

const L = (typeof IS_ZH !== "undefined" && IS_ZH) ? {
    categories: { statues: "佛像", amulets: "护身符", fengshui: "风水摆件", work: "过往服务" },
    facts: ["类型", "尺寸", "材质"],
    piece: code => "编号 " + code,
    ourWork: "过往服务", homed: "已结缘",
    reserved: "已预留",
    ask: "询问这件法物",
    askMsg: i => `您好，我对编号 ${i.code}（${i.title}）的法物感兴趣，可以多介绍一下吗？`,
    similar: "询问类似服务",
    similarMsg: i => `您好，我在作品集中看到"${i.title}"，想询问类似的服务。`,
    noMatch: "没有符合的法物。欢迎留言询问现有法物。",
    nothing: "暂无内容。",
    failed: "列表无法加载，请刷新页面。"
} : {
    categories: { statues: "Buddha statue", amulets: "Amulet", fengshui: "Feng Shui piece", work: "Our work" },
    facts: ["Type", "Size", "Material"],
    piece: code => "Piece " + code,
    ourWork: "Our work", homed: "Now in a home",
    reserved: "Reserved",
    ask: "Ask about this piece",
    askMsg: i => `Hi, I'm interested in piece ${i.code} – ${i.title}. Could you tell me more?`,
    similar: "Ask about something similar",
    similarMsg: i => `Hi, I saw "${i.title}" in your gallery and would like to ask about something similar.`,
    noMatch: "No pieces match. Message us to ask what is available.",
    nothing: "Nothing here yet.",
    failed: "The list could not load. Please refresh the page."
};

// Chinese pages use the *_zh fields when an item has them, otherwise the English text.
const pick = (i, field) => ((IS_ZH && i[field + "_zh"]) || i[field]);

function showItems(mode) {
    const grid = document.getElementById("grid");
    const search = document.getElementById("search");
    const dialog = document.getElementById("detail");
    let items = [];
    let filter = "all";

    loadItems().then(data => {
        items = data
            .filter(i => mode === "gallery"
                ? (i.category === "work" || i.status === "sold")
                : (i.category !== "work" && i.status !== "sold"))
            .map(i => ({ ...i, group: i.category === "work" ? "work" : (mode === "gallery" ? "homed" : i.category) }));
        render();
    }).catch(() => {
        grid.innerHTML = `<p class="empty">${L.failed}</p>`;
    });

    document.querySelectorAll(".chip").forEach(chip => chip.addEventListener("click", () => {
        filter = chip.dataset.filter;
        document.querySelectorAll(".chip").forEach(c => c.setAttribute("aria-pressed", c === chip));
        render();
    }));
    if (search) search.addEventListener("input", render);

    function render() {
        const q = search ? search.value.trim().toLowerCase() : "";
        const shown = items.filter(i =>
            (filter === "all" || i.group === filter) &&
            (!q || (i.title + " " + i.code).toLowerCase().includes(q)));

        grid.innerHTML = "";
        if (shown.length === 0) {
            grid.innerHTML = `<p class="empty">${mode === "gallery" ? L.nothing : L.noMatch}</p>`;
            return;
        }
        shown.forEach(i => {
            const card = document.createElement("button");
            card.type = "button";
            card.className = "item";
            const tag = i.status === "reserved" ? `<span class="tag">${L.reserved}</span>` : "";
            card.innerHTML = `
                <div class="frame"><img loading="lazy" alt=""></div>
                <span class="name"></span>
                <span class="meta"></span>${tag}`;
            card.querySelector("img").src = asset(i.image);
            card.querySelector("img").alt = i.title;
            card.querySelector(".name").textContent = i.title;
            card.querySelector(".meta").textContent = mode === "gallery" ? (i.group === "work" ? L.ourWork : L.homed) : i.code;
            card.addEventListener("click", () => open(i));
            grid.appendChild(card);
        });
    }

    function open(i) {
        dialog.querySelector("#detail-img").src = asset(i.image);
        dialog.querySelector("#detail-img").alt = i.title;
        dialog.querySelector("#detail-title").textContent = i.title;
        dialog.querySelector("#detail-code").textContent = mode === "gallery" ? "" : L.piece(i.code);
        const facts = dialog.querySelector("#detail-facts");
        facts.innerHTML = "";
        [[L.facts[0], L.categories[i.category]], [L.facts[1], pick(i, "size")], [L.facts[2], pick(i, "material")]].forEach(([k, v]) => {
            if (!v) return;
            const dt = document.createElement("dt"); dt.textContent = k;
            const dd = document.createElement("dd"); dd.textContent = v;
            facts.append(dt, dd);
        });
        dialog.querySelector("#detail-desc").textContent = pick(i, "desc") || "";
        const btn = dialog.querySelector("#detail-btn");
        if (mode === "gallery") {
            btn.textContent = L.similar;
            btn.setAttribute("data-wa", L.similarMsg(i));
        } else {
            btn.textContent = L.ask;
            btn.setAttribute("data-wa", L.askMsg(i));
        }
        wireChatLinks(dialog);
        dialog.querySelector(".detail-body").scrollTop = 0;
        document.documentElement.style.overflow = "hidden";
        dialog.showModal();
    }

    dialog.addEventListener("close", () => { document.documentElement.style.overflow = ""; });
    dialog.querySelector(".close").addEventListener("click", () => dialog.close());
    dialog.addEventListener("click", e => { if (e.target === dialog) dialog.close(); });
}
