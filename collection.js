/* Collection and Gallery pages: render items from data/items.json.
   Collection = statues / amulets / fengshui pieces that are not sold.
   Gallery    = past work, plus any piece marked "sold". */

const CATEGORY_NAMES = { statues: "Buddha statue", amulets: "Amulet", fengshui: "Feng Shui piece", work: "Our work" };

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
        grid.innerHTML = '<p class="empty">The list could not load. Please refresh the page.</p>';
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
            grid.innerHTML = mode === "gallery"
                ? '<p class="empty">Nothing here yet.</p>'
                : '<p class="empty">No pieces match. Message us to ask what is available.</p>';
            return;
        }
        shown.forEach(i => {
            const card = document.createElement("button");
            card.type = "button";
            card.className = "item";
            const tag = i.status === "reserved" ? '<span class="tag">Reserved</span>' : "";
            card.innerHTML = `
                <div class="frame"><img loading="lazy" alt=""></div>
                <span class="name"></span>
                <span class="meta"></span>${tag}`;
            card.querySelector("img").src = asset(i.image);
            card.querySelector("img").alt = i.title;
            card.querySelector(".name").textContent = i.title;
            card.querySelector(".meta").textContent = mode === "gallery" ? (i.group === "work" ? "Our work" : "Now in a home") : i.code;
            card.addEventListener("click", () => open(i));
            grid.appendChild(card);
        });
    }

    function open(i) {
        dialog.querySelector("#detail-img").src = asset(i.image);
        dialog.querySelector("#detail-img").alt = i.title;
        dialog.querySelector("#detail-title").textContent = i.title;
        dialog.querySelector("#detail-code").textContent = mode === "gallery" ? "" : "Piece " + i.code;
        const facts = dialog.querySelector("#detail-facts");
        facts.innerHTML = "";
        [["Type", CATEGORY_NAMES[i.category]], ["Size", i.size], ["Material", i.material]].forEach(([k, v]) => {
            if (!v) return;
            const dt = document.createElement("dt"); dt.textContent = k;
            const dd = document.createElement("dd"); dd.textContent = v;
            facts.append(dt, dd);
        });
        dialog.querySelector("#detail-desc").textContent = i.desc || "";
        const btn = dialog.querySelector("#detail-btn");
        if (mode === "gallery") {
            btn.textContent = "Ask about something similar";
            btn.setAttribute("data-wa", `Hi, I saw "${i.title}" in your gallery and would like to ask about something similar.`);
        } else {
            btn.textContent = "Ask about this piece";
            btn.setAttribute("data-wa", `Hi, I'm interested in piece ${i.code} – ${i.title}. Could you tell me more?`);
        }
        wireChatLinks(dialog);
        dialog.showModal();
    }

    dialog.querySelector(".close").addEventListener("click", () => dialog.close());
    dialog.addEventListener("click", e => { if (e.target === dialog) dialog.close(); });
}
