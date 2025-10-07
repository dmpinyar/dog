(() => {
    let ans = prompt("what's your favorite food?") || "nothing";

    document.body.insertAdjacentHTML("beforeend", "<p>Hello World!</p>");
    document.body.insertAdjacentHTML("beforeend", "<p>Did tsconfig.json see this?</p>");
    document.body.insertAdjacentHTML("beforeend", "<br><i>What the flip</i>");
    document.body.insertAdjacentHTML("beforeend", `<br><br>I just stole 17 ${ans}s.`);
})();