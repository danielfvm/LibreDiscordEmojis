const SERVER_URL = "http://127.0.0.1:8875/";

const getByTagAndClass = (tag, clazz) => {
	return Array.from(document.getElementsByTagName(tag)).filter(x => x.className.includes(clazz))
}

const removeClass = (dom, clazz) => {
	for (const c of dom.classList) {
		if (c.includes(clazz)) {
			dom.classList.remove(c);
		}
	}
}

const hooksEmoji = () => Array.from(getByTagAndClass("button", "emojiItemDisabled")).forEach(x => {
	x.onclick = () => {
		getByTagAndClass("button", "emojiButtonHovered")[0].click();
		setTimeout(() => fetch(SERVER_URL + encodeURIComponent(x.children[0].src)), 0);
	};
	x.onmouseover = () => {
		hooksEmoji();
	}
	removeClass(x, "emojiItemDisabled");
});

const hooksStickers = () => Array.from(getByTagAndClass("div", "stickerUnsendable")).forEach(x => {
	x.onclick = () => {
		getByTagAndClass("div", "stickerButton")[0].click();
		setTimeout(() => fetch(SERVER_URL + encodeURIComponent(x.children[0].children[0].src)), 0);
	};
	removeClass(x, "stickerUnsendable");
});

const interval = setInterval(() => {
	hooksEmoji();
	hooksStickers();
}, 100);
