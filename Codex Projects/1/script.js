const button = document.querySelector(".love-button");
const colors = ["#ff4f8e", "#ff7cad", "#ffd55d", "#ffffff"];

function makeHeart(x, y, index) {
  const heart = document.createElement("span");
  heart.className = "spark";
  heart.style.left = `${x}px`;
  heart.style.top = `${y}px`;
  heart.style.setProperty("--spark-color", colors[index % colors.length]);
  heart.style.setProperty("--spark-x", `${(index - 3) * 26}px`);

  heart.addEventListener("animationend", () => heart.remove());
  document.body.append(heart);
}

button?.addEventListener("click", (event) => {
  const rect = button.getBoundingClientRect();
  const centerX = rect.left + rect.width / 2;
  const centerY = rect.top + rect.height / 2;

  for (let i = 0; i < 7; i += 1) {
    window.setTimeout(() => makeHeart(centerX, centerY, i), i * 45);
  }

  event.currentTarget.animate(
    [
      { transform: "translate(0, 0) scale(1)" },
      { transform: "translate(0, -4px) scale(1.04)" },
      { transform: "translate(0, 0) scale(1)" },
    ],
    {
      duration: 280,
      easing: "ease-out",
    },
  );
});
