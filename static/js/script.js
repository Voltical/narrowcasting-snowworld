    const data = {
      living: {
        title: "FURNITURE DESIGNED FOR\nMODERN LIVING",
        text: "Crafted with precision, designed for comfort, and built to elevate everyday spaces."
      },
      bedroom: {
        title: "CALM ESSENTIALS FOR\nBETTER REST",
        text: "Soft textures, warm tones, and minimal silhouettes made for a quieter bedroom."
      },
      workspace: {
        title: "CLEAN LINES FOR\nFOCUSED WORK",
        text: "Functional pieces with a modern edge—built to keep your workspace effortless."
      }
    };

    const titleEl = document.getElementById("heroTitle");
    const textEl = document.getElementById("heroText");
    const tabs = document.querySelectorAll(".tab");

    function setSpace(space){
      const entry = data[space];
      if(!entry) return;

      titleEl.innerHTML = entry.title.replaceAll("\n","<br/>");
      textEl.textContent = entry.text;

      tabs.forEach(btn => {
        const active = btn.dataset.space === space;
        btn.classList.toggle("is-active", active);
        btn.setAttribute("aria-selected", active ? "true" : "false");
      });
    }

    tabs.forEach(btn => btn.addEventListener("click", () => setSpace(btn.dataset.space)));